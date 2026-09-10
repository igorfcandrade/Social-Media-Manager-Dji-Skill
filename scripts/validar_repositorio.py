#!/usr/bin/env python3
"""Valida a estrutura portátil e os contratos de distribuição das skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NOTICE = "Skill necessita de revisão"

FORBIDDEN_SKILL_MARKERS = (
    "AskUserQuestion",
    "CLAUDE.md",
    "MEMORY.md",
    "APIFY_API_TOKEN",
    "GOOGLE_AI_API_KEY",
    "Claude para Chrome",
    "Doces " + "Mimi" + "nhos",
    "Marisa",
)

NOTICE_EXEMPT_SKILLS = {"sistema-contexto-conteudo"}
SKILL_NOTICE_CONSUMERS = tuple(
    str(path.relative_to(ROOT))
    for path in sorted(SKILLS.glob("*/SKILL.md"))
    if path.parent.name not in NOTICE_EXEMPT_SKILLS
)
NOTICE_CONSUMERS = SKILL_NOTICE_CONSUMERS

REQUIRED_EXECUTABLES = (
    "testar.sh",
    "instalar.sh",
    "skills/social-media-manager/scripts/verificar_revisao.py",
    "scripts/validar_estado_plataformas.py",
    "scripts/validar_repositorio.py",
    "scripts/validar_instalacoes.py",
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


def field(block: str, name: str) -> str | None:
    match = re.search(rf"^{re.escape(name)}:\s*(.+)$", block, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip().strip('"\'')


def validar_executoras(texto: str, raiz: Path) -> list[str]:
    """Cada executora do encaminhador tem de acompanhar a distribuição."""
    nomes = re.findall(r"^\| `([a-z0-9-]+)` \|", texto, re.M)
    return [
        f"encaminhamento para {nome}: falta skills/{nome}/SKILL.md"
        for nome in nomes
        if not (raiz / nome / "SKILL.md").is_file()
    ]


def main() -> int:
    errors: list[str] = []
    skill_paths = sorted(SKILLS.glob("*/SKILL.md"))

    for path in sorted(SKILLS.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".py", ".csv"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        relative = path.relative_to(ROOT)
        for marker in FORBIDDEN_SKILL_MARKERS:
            if marker in text:
                fail(
                    errors,
                    f"{relative}: dependência de caso ou ambiente não permitida: {marker}",
                )

    for path in skill_paths:
        text = path.read_text(encoding="utf-8")
        block = frontmatter(text)
        relative = path.relative_to(ROOT)
        if block is None:
            fail(errors, f"{relative}: frontmatter ausente ou inválido")
            continue

        name = field(block, "name")
        description = field(block, "description")
        if name != path.parent.name:
            fail(
                errors,
                f"{relative}: name '{name}' não coincide com a pasta",
            )
        if not name or not re.fullmatch(r"[a-z0-9-]{1,63}", name):
            fail(errors, f"{relative}: name inválido")
        if not description:
            fail(errors, f"{relative}: description ausente")

        if path.parent.name not in {"social-media-manager", "sistema-contexto-conteudo"}:
            if "references/contexto-do-caso.md" not in text:
                fail(errors, f"{relative}: falta o contrato de contexto agnóstico")

    router = (SKILLS / "social-media-manager/SKILL.md").read_text(encoding="utf-8")
    errors.extend(validar_executoras(router, SKILLS))

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    count_match = re.search(r"Conjunto de \*\*(\d+) skills\*\*", readme)
    if not count_match:
        fail(errors, "README.md: contagem de skills ausente")
    elif int(count_match.group(1)) != len(skill_paths):
        fail(
            errors,
            "README.md: contagem de skills diverge das pastas "
            f"({count_match.group(1)} != {len(skill_paths)})",
        )

    context_contract = (
        ROOT
        / "skills"
        / "social-media-manager"
        / "references"
        / "contexto-do-caso.md"
    )
    if not context_contract.exists():
        fail(errors, "falta o contrato universal de contexto do caso")
    else:
        contract_text = context_contract.read_text(encoding="utf-8")
        for marker in (
            "qualquer organização",
            "com ou sem website",
            "Não exigir um nome de ficheiro",
            "Não tratar a ausência de website",
            "Não exigir o nome de uma ferramenta",
        ):
            if marker not in contract_text:
                fail(errors, f"contrato de contexto: falta '{marker}'")

    for relative in NOTICE_CONSUMERS:
        path = ROOT / relative
        if not path.exists() or NOTICE not in path.read_text(encoding="utf-8"):
            fail(errors, f"{relative}: falta o aviso obrigatório '{NOTICE}'")

    for relative in SKILL_NOTICE_CONSUMERS:
        text = (ROOT / relative).read_text(encoding="utf-8")
        for marker in (
            "## Gate de revisão",
            "verificar_revisao.py",
            "Calendário",
            "primeira linha",
            "O aviso não autoriza",
        ):
            if marker not in text:
                fail(errors, f"{relative}: gate incompleto; falta '{marker}'")

    state = (
        ROOT
        / "skills"
        / "social-media-manager"
        / "references"
        / "05-estado-das-plataformas.md"
    ).read_text(encoding="utf-8")
    for platform in ("TikTok", "Threads", "X"):
        if not re.search(
            rf"^\| {re.escape(platform)} \| LOOK INTO \|",
            state,
            flags=re.MULTILINE,
        ):
            fail(errors, f"estado das plataformas: {platform} não está LOOK INTO")

    for relative in REQUIRED_EXECUTABLES:
        path = ROOT / relative
        if not path.exists():
            fail(errors, f"falta o executável {relative}")
        elif not path.stat().st_mode & 0o111:
            fail(errors, f"{relative}: falta permissão de execução")

    workflow = ROOT / ".github" / "workflows" / "validar-skills.yml"
    if not workflow.exists():
        fail(errors, "falta .github/workflows/validar-skills.yml")
    else:
        workflow_text = workflow.read_text(encoding="utf-8")
        for marker in ("push:", "pull_request:", "workflow_dispatch:", "schedule:", "./testar.sh"):
            if marker not in workflow_text:
                fail(errors, f"workflow: falta {marker}")

    checker = (
        ROOT
        / "skills"
        / "social-media-manager"
        / "scripts"
        / "verificar_revisao.py"
    ).read_text(encoding="utf-8")
    if "print(NOTICE)" not in checker:
        fail(errors, "checker: o aviso não é emitido como primeira linha isolada")

    if errors:
        print("Validação do repositório: FALHOU", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Validação do repositório: OK "
        f"({len(skill_paths)} skills, aviso de revisão em "
        f"{len(NOTICE_CONSUMERS)} consumidores)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
