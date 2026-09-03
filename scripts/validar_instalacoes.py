#!/usr/bin/env python3
"""Compara as skills do repositório com as cópias instaladas nos ambientes locais.

Uma correção que fique só no repositório não está a ser usada por skill nenhuma, e
falhar em correr o instalador não produz erro visível: as skills antigas continuam
a responder. Já aconteceu duas vezes — no Claude, onde 14 de 18 skills estavam
atrasadas, e no Codex, onde uma cópia meio-instalada ainda continha o nome de um
cliente dentro da skill genérica.

Ambientes que não existam nesta máquina são ignorados, não são falha: a CI corre
num runner sem nenhum deles, e criar a pasta de um ambiente que não está instalado
seria inventar um destino.
"""

from __future__ import annotations

import filecmp
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

AMBIENTES = (
    ("Claude", Path.home() / ".claude" / "skills"),
    ("Codex", Path.home() / ".codex" / "skills"),
)


def diferencas(origem: Path, destino: Path) -> list[str]:
    """Caminhos relativos que diferem, faltam ou sobram entre duas árvores."""
    comparacao = filecmp.dircmp(origem, destino)
    encontradas: list[str] = []

    def percorrer(dc: filecmp.dircmp, prefixo: str) -> None:
        for nome in dc.left_only:
            encontradas.append(f"{prefixo}{nome} (falta no destino)")
        for nome in dc.right_only:
            encontradas.append(f"{prefixo}{nome} (a mais no destino)")
        for nome in dc.diff_files:
            encontradas.append(f"{prefixo}{nome} (difere)")
        for nome in dc.funny_files:
            encontradas.append(f"{prefixo}{nome} (ilegível)")
        for nome, sub in dc.subdirs.items():
            percorrer(sub, f"{prefixo}{nome}/")

    percorrer(comparacao, "")
    return encontradas


def main() -> int:
    skills = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    if not skills:
        print("Validação das instalações: FALHOU", file=sys.stderr)
        print("- não há skills em skills/", file=sys.stderr)
        return 1

    erros: list[str] = []
    verificados: list[str] = []

    for nome_ambiente, destino in AMBIENTES:
        # A raiz do ambiente é o sinal de que ele existe nesta máquina; a pasta
        # skills/ pode ainda não ter sido criada por nunca se ter instalado.
        if not destino.parent.is_dir():
            continue

        em_falta = [s for s in skills if not (destino / s).is_dir()]
        if em_falta:
            erros.append(
                f"{nome_ambiente}: por instalar — {', '.join(em_falta)}. Correr ./instalar.sh"
            )
            continue

        for skill in skills:
            for caminho in diferencas(SKILLS / skill, destino / skill):
                erros.append(f"{nome_ambiente}: {skill}/{caminho}")

        verificados.append(f"{nome_ambiente} ({len(skills)})")

    if erros:
        print("Validação das instalações: FALHOU", file=sys.stderr)
        for erro in erros[:25]:
            print(f"- {erro}", file=sys.stderr)
        if len(erros) > 25:
            print(f"- (e mais {len(erros) - 25})", file=sys.stderr)
        print("  Uma correção que fique só no repositório não está a ser usada.", file=sys.stderr)
        return 1

    if not verificados:
        print("Validação das instalações: OK (nenhum ambiente local detetado)")
        return 0

    print(f"Validação das instalações: OK — {', '.join(verificados)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
