"""Ensaios com ficheiros sintéticos; não comprovam enquadramento ou direitos."""
import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / 'skills/organizar-fotos-produtos/scripts/validar_entrega.py'
if Image:
    spec = importlib.util.spec_from_file_location('photo_delivery', MODULE)
    delivery = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(delivery)


@unittest.skipUnless(Image, 'Pillow ausente: testes de ficheiros fotográficos não executados')
class PhotoDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.root = self.base / 'pacote'
        self.root.mkdir()
        (self.root / 'originais').mkdir()
        source = self.root / 'originais/IMG_1.jpg'
        Image.new('RGB', (1200, 1800), 'tan').save(source)
        self.source = source
        checksum = delivery.digest(source)
        self.catalog = {'schema': 1, 'originais': [
            {'id': 'sha256:' + checksum, 'ficheiro': 'originais/IMG_1.jpg',
             'sha256': checksum, 'largura_ficheiro': 1200, 'altura_ficheiro': 1800}
        ], 'derivados': [], 'limitacoes': ['9x16 menor: fonte insuficiente para 1080x1920']}
        for fmt, crop, size in (
            ('1x1', (0, 0, 1200, 1200), (1080, 1080)),
            ('3x4', (0, 0, 1200, 1600), (1080, 1440)),
            ('9x16', (0, 0, 1008, 1792), (1008, 1792)),
        ):
            (self.root / fmt).mkdir()
            rel = fmt + '/produto_' + fmt + '_1.jpg'
            with Image.open(source) as im:
                im.crop(crop).resize(size).save(self.root / rel)
            self.catalog['derivados'].append({
                'ordem': 1, 'titulo': 'Vista frontal', 'formato': fmt, 'ficheiro': rel,
                'fonte': 'originais/IMG_1.jpg', 'fonte_id': 'sha256:' + checksum,
                'corte_xyxy': list(crop), 'dimensoes_corte': [crop[2], crop[3]],
                'dimensoes_entrega': list(size), 'ampliacao': False,
                'sha256': delivery.digest(self.root / rel)})
        self.write_catalog()
        self.write_csv()
        (self.root / 'galeria-comparacao.html').write_text(
            '<a href="originais/IMG_1.jpg">Original</a>' +
            ''.join('<img src="' + i['ficheiro'] + '">' for i in self.catalog['derivados']))

    def write_catalog(self):
        (self.root / 'catalogo.json').write_text(json.dumps(self.catalog))

    def write_csv(self):
        with (self.root / 'catalogo.csv').open('w', newline='') as f:
            w = csv.writer(f, delimiter=';')
            w.writerow(['ordem', 'formato', 'ficheiro', 'original', 'dimensoes'])
            for i in self.catalog['derivados']:
                w.writerow([i['ordem'], i['formato'], i['ficheiro'], i['fonte'],
                            ' x '.join(map(str, i['dimensoes_entrega']))])

    def test_smaller_crop_and_fewer_than_six_are_valid(self):
        catalog, notes = delivery.validate(self.root, [self.source])
        self.assertEqual(3, len(catalog['derivados']))
        self.assertFalse(any('quantidade' in n for n in notes))

    def test_original_tampering_is_rejected(self):
        self.source.write_bytes(b'alterado')
        with self.assertRaisesRegex(ValueError, 'Hash do original'):
            delivery.validate(self.root)

    def test_missing_received_input_is_rejected(self):
        extra = self.base / 'IMG_2.jpg'
        Image.new('RGB', (50, 50)).save(extra)
        with self.assertRaisesRegex(ValueError, 'Inventário recebido'):
            delivery.validate(self.root, [self.source, extra])

    def test_upscale_is_rejected_even_with_updated_export_hash(self):
        item = self.catalog['derivados'][-1]
        path = self.root / item['ficheiro']
        with Image.open(path) as im:
            im.resize((1080, 1920)).save(path)
        item.update(dimensoes_entrega=[1080, 1920], sha256=delivery.digest(path))
        self.write_catalog()
        with self.assertRaisesRegex(ValueError, 'Ampliação'):
            delivery.validate(self.root)

    def test_invented_source_dimensions_are_rejected(self):
        self.catalog['derivados'][0]['dimensoes_fonte_orientada'] = [5000, 5000]
        self.write_catalog()
        with self.assertRaisesRegex(ValueError, 'não correspondem'):
            delivery.validate(self.root)

    def test_csv_stale_data_is_rejected(self):
        csv_path = self.root / 'catalogo.csv'
        csv_path.write_text(csv_path.read_text().replace('1080 x 1080', '100 x 100'))
        with self.assertRaisesRegex(ValueError, 'Dimensões CSV'):
            delivery.validate(self.root)

    def test_gallery_omission_is_rejected(self):
        (self.root / 'galeria-comparacao.html').write_text('<p>Galeria vazia</p>')
        with self.assertRaisesRegex(ValueError, 'Galeria omite'):
            delivery.validate(self.root)

    def test_external_image_dependency_is_rejected(self):
        with (self.root / 'galeria-comparacao.html').open('a') as f:
            f.write('<img src="https://example.invalid/a.jpg">')
        with self.assertRaisesRegex(ValueError, 'não portátil'):
            delivery.validate(self.root)

    def test_zip_exact_content_and_refusal_to_overwrite(self):
        archive = self.base / 'entrega.zip'
        delivery.make_zip(self.root, archive, 'sessao/artigo')
        delivery.validate_zip(self.root, archive, 'sessao/artigo')
        with self.assertRaisesRegex(ValueError, 'já existe'):
            delivery.make_zip(self.root, archive, 'sessao/artigo')
        (self.root / 'catalogo.csv').write_text('revisão posterior')
        with self.assertRaisesRegex(ValueError, 'ZIP divergente'):
            delivery.validate_zip(self.root, archive, 'sessao/artigo')

    def test_zip_extraction_keeps_relative_gallery_valid(self):
        import zipfile
        archive = self.base / 'entrega.zip'
        delivery.make_zip(self.root, archive, 'sessao/artigo')
        with zipfile.ZipFile(archive) as z:
            z.extractall(self.base / 'extraido')
        delivery.validate(self.base / 'extraido/sessao/artigo')

    def test_configurable_export_size(self):
        self.catalog['formatos'] = {'1x1': [1080, 1080], '3x4': [1080, 1440], '9x16': [1008, 1792]}
        self.catalog['limitacoes'] = []
        self.write_catalog()
        _, warnings = delivery.validate(self.root, [self.source])
        self.assertEqual([], warnings)


if __name__ == '__main__':
    unittest.main()
