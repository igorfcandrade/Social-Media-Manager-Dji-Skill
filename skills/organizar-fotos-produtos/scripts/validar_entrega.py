#!/usr/bin/env python3
"""Valida um pacote fotográfico e, opcionalmente, cria o respetivo ZIP."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import tempfile
import zipfile
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

from PIL import Image, ImageOps, UnidentifiedImageError

FORMATS = {'1x1': (1080, 1080), '3x4': (1080, 1440), '9x16': (1080, 1920)}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(chunk)
    return result.hexdigest()


def local_file(root, relative):
    rel = PurePosixPath(relative)
    require(not rel.is_absolute() and '..' not in rel.parts, f'Caminho não relativo: {relative}')
    p = (root / relative).resolve()
    require(p.is_relative_to(root), f'Caminho fora do pacote: {relative}')
    require(p.is_file(), f'Ficheiro ausente: {relative}')
    return p


class GalleryLinks(HTMLParser):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.paths = set()

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key not in ('src', 'href') or not value:
                continue
            parsed = urlsplit(value)
            if parsed.scheme == 'data' and value.startswith(('data:image/jpeg;base64,', 'data:image/png;base64,', 'data:image/webp;base64,')):
                continue  # Preview incorporada acompanha o HTML offline.
            if parsed.scheme or parsed.netloc:
                require(key != 'src' and parsed.scheme in ('http', 'https', 'mailto'), 'Recurso de galeria não portátil')
                continue
            if parsed.path:
                local_file(self.root, unquote(parsed.path))
                self.paths.add(unquote(parsed.path))


def validate_csv(root, catalog):
    with (root / 'catalogo.csv').open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream, delimiter=';'))
    expected = {e['ficheiro']: e for e in catalog['derivados']}
    require(len(rows) == len(expected), 'Contagem CSV divergente do JSON')
    require({r.get('ficheiro') for r in rows} == set(expected), 'Ficheiros CSV divergentes do JSON')
    for row in rows:
        item = expected[row['ficheiro']]
        require(row.get('ordem') == str(item['ordem']) and row.get('formato') == item['formato'], 'Ordem/formato CSV divergente')
        require(row.get('original') == item['fonte'], 'Original CSV divergente')
        dims = [int(n) for n in re.findall(r'\d+', row.get('dimensoes', ''))]
        require(dims == item['dimensoes_entrega'], 'Dimensões CSV divergentes')


def validate(root, incoming=None):
    root = root.resolve()
    catalog = json.loads((root / 'catalogo.json').read_text(encoding='utf-8'))
    formats = catalog.get('formatos', FORMATS)
    require(isinstance(formats, dict) and formats, 'Formatos inválidos')
    for fmt, dimensions in formats.items():
        require(re.fullmatch(r'[1-9]\d*x[1-9]\d*', fmt) is not None, 'Nome de formato inválido')
        require(len(dimensions) == 2 and all(isinstance(n, int) and n > 0 for n in dimensions), 'Dimensões preferenciais inválidas')
        rw, rh = map(int, fmt.split('x'))
        require(dimensions[0] * rh == dimensions[1] * rw, 'Formato e proporção preferencial divergem')
    for folder in ['originais', *formats]:
        require((root / folder).is_dir(), f'Falta pasta {folder}')
    sources = {}
    warnings = []
    for original in catalog['originais']:
        relative = original['ficheiro']
        require(PurePosixPath(relative).parts[0] == 'originais', f'Original fora de originais: {relative}')
        require(relative not in sources, f'Original duplicado no catálogo: {relative}')
        copied = local_file(root, relative)
        checksum = digest(copied)
        require(checksum == original['sha256'], f'Hash do original alterado: {relative}')
        require(original['id'] == 'sha256:' + checksum, f'ID do original inconsistente: {relative}')
        received = original.get('origem_recebida')
        if received:
            source_path = Path(received).expanduser()
            require(source_path.name == copied.name, f'Nome do original alterado: {relative}')
            if source_path.is_file():
                require(checksum == digest(source_path), f'Cópia diferente da origem recebida: {relative}')
            else:
                warnings.append(f'Origem recebida indisponível; comparado apenas com o hash registado: {relative}')
        sources[relative] = original
    require(sources, 'Não existem originais catalogados')
    if incoming is not None:
        entries = [p for entry in incoming for p in (entry.rglob('*') if entry.is_dir() else [entry])
                   if p.is_file() and not p.name.startswith('.')]
        require(entries, 'Inventário de entrada vazio')
        expected = Counter((p.name, digest(p)) for p in entries)
        copied_inventory = Counter((Path(rel).name, item['sha256']) for rel, item in sources.items())
        require(expected == copied_inventory, 'Inventário recebido diverge dos originais preservados')
    else:
        warnings.append('Completude do lote recebido não conferida: fornecer --received com as entradas exatas')
    actual_originals = {str(p.relative_to(root)) for p in (root / 'originais').rglob('*') if p.is_file() and not p.name.startswith('.')}
    require(actual_originals == set(sources), 'O catálogo não corresponde a todos os originais na pasta')
    rows, seen, counts = defaultdict(set), set(), defaultdict(int)
    all_orders, exceptions = set(), []
    for item in catalog['derivados']:
        fmt, number = item['formato'], item['ordem']
        require(fmt in formats, f'Formato desconhecido: {fmt}')
        require(isinstance(number, int) and not isinstance(number, bool) and number >= 1, 'Ordem inválida')
        require((fmt, number) not in seen, f'Número repetido: {fmt}/{number}')
        seen.add((fmt, number)); counts[fmt] += 1; all_orders.add(number)
        relative = item['ficheiro']
        require(PurePosixPath(relative).parent == PurePosixPath(fmt), f'Pasta de corte incorreta: {relative}')
        require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*_' + fmt + '_' + str(number) + r'\.jpg', Path(relative).name), f'Nome inválido: {relative}')
        file = local_file(root, relative)
        require(digest(file) == item['sha256'], f'Hash do corte não atualizado: {relative}')
        require(item['fonte'] in sources, f'Fonte não catalogada: {relative}')
        original = sources[item['fonte']]
        require(item.get('fonte_id') == original['id'], f'Ligação ao original inconsistente: {relative}')
        rows[number].add(original['id'])
        box = item['corte_xyxy']
        require(len(box) == 4 and all(isinstance(v, int) for v in box), f'Caixa inválida: {relative}')
        x1, y1, x2, y2 = box
        require(0 <= x1 < x2 and 0 <= y1 < y2, f'Caixa fora dos limites: {relative}')
        bounds = item.get('dimensoes_fonte_orientada')
        if not bounds and original.get('largura_ficheiro') and original.get('altura_ficheiro'):
            bounds = [original['largura_ficheiro'], original['altura_ficheiro']]
            if original.get('orientacao_exif') in (5, 6, 7, 8):
                bounds.reverse()
        require(bounds and len(bounds) == 2, f'Faltam dimensões da fonte orientada: {relative}')
        # JPEG/PNG: conferir a fonte real, não confiar só em dimensões declaradas.
        # RAW não descodificável aqui: a verificação da renderização continua explícita.
        try:
            with Image.open(local_file(root, item['fonte'])) as source_image:
                actual_bounds = list(ImageOps.exif_transpose(source_image).size)
            require(list(bounds) == actual_bounds, f'Dimensões declaradas não correspondem à fonte: {relative}')
        except UnidentifiedImageError:
            warnings.append(f'Renderização da fonte requer verificação separada: {relative}')
        require(x2 <= bounds[0] and y2 <= bounds[1], f'Corte excede a fonte: {relative}')
        crop_w, crop_h = x2 - x1, y2 - y1
        require(item['dimensoes_corte'] == [crop_w, crop_h], f'Dimensões do corte incorretas: {relative}')
        with Image.open(file) as im:
            im.load()
            width, height = im.size
            require(im.format == 'JPEG', f'Não é JPEG: {relative}')
            require(im.getexif().get(274, 1) == 1, f'Orientação não aplicada: {relative}')
        require([width, height] == item['dimensoes_entrega'], f'Dimensões de entrega incorretas: {relative}')
        target_w, target_h = formats[fmt]
        require(width * target_h == height * target_w, f'Proporção de entrega incorreta: {relative}')
        require(crop_w * target_h == crop_h * target_w, f'Proporção do corte incorreta: {relative}')
        require(width <= crop_w and height <= crop_h and item.get('ampliacao') is False, f'Ampliação detetada: {relative}')
        if (width, height) != (target_w, target_h):
            exceptions.append(f'{relative}: {width} × {height}, fora da dimensão preferencial')
    require(seen, 'Não existem cortes catalogados')
    require(all_orders == set(range(1, max(all_orders) + 1)), 'A sequência global não começa em 1 ou contém lacunas')
    require(all(len(source_ids) == 1 for source_ids in rows.values()), 'O mesmo número aponta para originais diferentes entre formatos')
    for fmt in formats:
        actual = {str(p.relative_to(root)) for p in (root / fmt).rglob('*') if p.is_file() and not p.name.startswith('.')}
        expected = {e['ficheiro'] for e in catalog['derivados'] if e['formato'] == fmt}
        require(actual == expected, f'Ficheiros extra ou ausentes em {fmt}')
        if counts[fmt] > catalog.get('maximo_por_formato', 6) or {n for f, n in seen if f == fmt} != all_orders:
            exceptions.append(f'{fmt}: {counts[fmt]} cortes; conferir quantidade/lacunas com a limitação declarada')
    require(not exceptions or bool(catalog.get('limitacoes')), 'Há exceções de resolução/quantidade sem limitações documentadas')
    parser = GalleryLinks(root)
    parser.feed((root / 'galeria-comparacao.html').read_text(encoding='utf-8'))
    require(set(sources).issubset(parser.paths), 'Galeria omite links para originais')
    require({e['ficheiro'] for e in catalog['derivados']}.issubset(parser.paths), 'Galeria omite cortes')
    validate_csv(root, catalog)
    return catalog, warnings + exceptions


def validate_zip(root, destination, prefix):
    root = root.resolve()
    files = {str(PurePosixPath(prefix) / p.relative_to(root)): p for p in root.rglob('*')
             if p.is_file() and not any(part.startswith('.') for part in p.relative_to(root).parts)}
    with zipfile.ZipFile(destination) as archive:
        names = archive.namelist()
        require(len(names) == len(set(names)) and set(names) == set(files), 'Conteúdo ZIP divergente da pasta')
        for name, path in files.items():
            checksum = hashlib.sha256()
            with archive.open(name) as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b''):
                    checksum.update(block)
            require(checksum.hexdigest() == digest(path), f'Ficheiro ZIP divergente: {name}')


def make_zip(root, destination, prefix, replace=False):
    root, destination = root.resolve(), destination.resolve()
    require(not destination.is_relative_to(root), 'Guardar ZIP fora do pacote para não o incluir em si próprio')
    require(not destination.exists() or replace, 'ZIP já existe; use --replace-zip só para uma revisão pedida')
    arc = PurePosixPath(prefix)
    require(bool(arc.parts) and not arc.is_absolute() and '..' not in arc.parts, 'Prefixo ZIP inválido')
    files = sorted(p for p in root.rglob('*') if p.is_file() and not any(part.startswith('.') for part in p.relative_to(root).parts))
    require(all(p.resolve().is_relative_to(root) for p in files), 'O pacote contém ligações para ficheiros externos')
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=destination.parent, suffix='.zip.tmp', delete=False) as f:
            temporary = Path(f.name)
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=4) as archive:
            for file in files:
                archive.write(file, str(arc / file.relative_to(root)))
        validate_zip(root, temporary, prefix)
        temporary.replace(destination)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pacote', type=Path)
    parser.add_argument('--zip', type=Path, dest='zip_path')
    parser.add_argument('--prefix', help='Caminho relativo preservado dentro do ZIP')
    parser.add_argument('--replace-zip', action='store_true')
    parser.add_argument('--check-zip', type=Path, help='Verificar ZIP existente sem o alterar')
    parser.add_argument('--received', type=Path, nargs='+', help='Ficheiros ou pastas exatos recebidos; confere completude')
    args = parser.parse_args()
    try:
        catalog, warnings = validate(args.pacote, args.received)
        if args.zip_path:
            make_zip(args.pacote, args.zip_path, args.prefix or args.pacote.name, args.replace_zip)
        if args.check_zip:
            validate_zip(args.pacote, args.check_zip, args.prefix or args.pacote.name)
        print(f"Verificação estrutural OK: {len(catalog['originais'])} originais, {len(catalog['derivados'])} cortes.")
        for warning in warnings:
            print('NOTA:', warning)
        if args.zip_path:
            print('ZIP criado e verificado:', args.zip_path)
        print('A composição e a fidelidade visual exigem revisão humana/visual separada.')
        return 0
    except (ValueError, KeyError, OSError, TypeError, zipfile.BadZipFile) as error:
        print('FALHA:', error)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
