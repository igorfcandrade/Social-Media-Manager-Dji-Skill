#!/usr/bin/env python3
"""Verifica os calendários da skill sem pesquisar nem alterar ficheiros."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
NOTICE = "Skill necessita de revisão"
LIMITATION = (
    "O aviso não autoriza pesquisa externa, acesso a contas "
    "nem atualização automática."
)


class RevisionArgumentParser(argparse.ArgumentParser):
    """Mantém o contrato público 0=ok, 1=erro, 2=revisão devida."""

    def error(self, message: str) -> None:
        print(NOTICE)
        print(f"- argumentos: {message}")
        print(LIMITATION)
        raise SystemExit(1)


@dataclass(frozen=True)
class Calendar:
    label: str
    last_field: str
    next_field: str


CALENDARS = (
    Calendar(
        "plataformas",
        "Última revisão concluída",
        "Próxima revisão programada",
    ),
    Calendar(
        "tendências",
        "Último recap concluído",
        "Próximo recap devido",
    ),
)


def read_date(text: str, field: str) -> date:
    match = re.search(
        rf"^- \*\*{re.escape(field)}:\*\*\s*(\d{{4}}-\d{{2}}-\d{{2}})\b",
        text,
        flags=re.MULTILINE,
    )
    if not match:
        raise ValueError(f"falta o campo '{field}'")
    return date.fromisoformat(match.group(1))


def parse_today(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("usar AAAA-MM-DD") from error


def main() -> int:
    parser = RevisionArgumentParser(
        description="Verifica se a revisão da skill está vencida."
    )
    parser.add_argument(
        "--hoje",
        type=parse_today,
        default=date.today(),
        help="data de referência para testes, em AAAA-MM-DD",
    )
    parser.add_argument(
        "--plataformas",
        type=Path,
        default=SKILL_DIR / "references" / "05-estado-das-plataformas.md",
        help="caminho alternativo para o estado das plataformas",
    )
    parser.add_argument(
        "--tendencias",
        type=Path,
        default=SKILL_DIR / "references" / "09-estado-da-vigilancia.md",
        help="caminho alternativo para o estado das tendências",
    )
    args = parser.parse_args()

    paths = {
        "plataformas": args.plataformas,
        "tendências": args.tendencias,
    }

    due: list[str] = []
    future: list[str] = []
    errors: list[str] = []

    for calendar in CALENDARS:
        path = paths[calendar.label]
        try:
            text = path.read_text(encoding="utf-8")
            last = read_date(text, calendar.last_field)
            next_due = read_date(text, calendar.next_field)
            if next_due <= last:
                raise ValueError(
                    "a próxima revisão não é posterior à última conclusão"
                )
        except (OSError, ValueError) as error:
            errors.append(f"{calendar.label}: {error}")
            continue

        detail = (
            f"{calendar.label}: última conclusão {last.isoformat()}; "
            f"revisão prevista {next_due.isoformat()}"
        )
        if args.hoje >= next_due:
            due.append(detail)
        else:
            future.append(detail)

    if errors or due:
        print(NOTICE)
        for detail in errors + due:
            print(f"- {detail}")
        print(LIMITATION)
        return 1 if errors else 2

    print(f"Revisão da skill: OK — {' | '.join(future)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
