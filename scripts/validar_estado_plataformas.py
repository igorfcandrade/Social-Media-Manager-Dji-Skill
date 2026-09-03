#!/usr/bin/env python3
"""Valida o registo de atualidade das plataformas e os seus consumidores."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
STATE = (
    SKILLS
    / "social-media-manager"
    / "references"
    / "05-estado-das-plataformas.md"
)
REQUIRED_FIELDS = (
    "Plataforma / superfície",
    "Tipo de afirmação",
    "Afirmação atual",
    "Volatilidade",
    "Âmbito",
    "Publicado em",
    "Efetivo em",
    "Rollout",
    "Fonte relida em",
    "Rever quando",
    "Confiança",
    "Estado",
    "Implicação",
)

EXPECTED_CONSUMERS = {
    "PLAT-001": (
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-002": (
        "skills/social-media-manager/references/03-planeamento-e-calendario.md",
        "skills/social-media-manager/references/05-plataformas.md",
        "skills/guiao-video-curto/SKILL.md",
    ),
    "PLAT-003": (
        "skills/social-media-manager/references/05-plataformas.md",
        "skills/escrever-post/SKILL.md",
        "skills/formatar-post/SKILL.md",
        "skills/guiao-video-curto/SKILL.md",
    ),
    "PLAT-004": (
        "skills/social-media-manager/references/00-a-conta.md",
        "skills/social-media-manager/references/05-plataformas.md",
        "skills/otimizar-perfil/SKILL.md",
    ),
    "PLAT-005": (
        "skills/social-media-manager/references/03-planeamento-e-calendario.md",
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-006": (
        "skills/social-media-manager/references/03-planeamento-e-calendario.md",
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-007": (
        "skills/avaliar-post/SKILL.md",
        "skills/carrossel/SKILL.md",
        "skills/comentario-fixado/SKILL.md",
        "skills/design-grafico/SKILL.md",
        "skills/escrever-post/SKILL.md",
        "skills/formatar-post/SKILL.md",
        "skills/gerar-ganchos/SKILL.md",
        "skills/guiao-video-curto/SKILL.md",
        "skills/infografico/SKILL.md",
        "skills/matriz-de-conteudo/SKILL.md",
        "skills/painel-metricas/SKILL.md",
        "skills/pesquisa-de-nicho/SKILL.md",
        "skills/post-de-citacao/SKILL.md",
        "skills/social-media-manager/references/06-comunidade-e-dm.md",
        "skills/social-media-manager/references/10-risco-crise-e-conformidade.md",
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-008": (
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-009": (
        "skills/social-media-manager/SKILL.md",
    ),
    "PLAT-010": (
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-011": (
        "skills/capa-de-video/SKILL.md",
        "skills/escrever-post/SKILL.md",
        "skills/formatar-post/SKILL.md",
        "skills/guiao-video-curto/SKILL.md",
        "skills/social-media-manager/SKILL.md",
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-012": (
        "skills/otimizar-perfil/SKILL.md",
        "skills/painel-metricas/SKILL.md",
        "skills/social-media-manager/references/00-a-conta.md",
        "skills/social-media-manager/references/03-planeamento-e-calendario.md",
        "skills/social-media-manager/references/05-plataformas.md",
        "skills/social-media-manager/references/07-analise-e-relatorio.md",
        "skills/social-media-manager/references/12-contextos-de-negocio.md",
    ),
    "PLAT-013": (
        "skills/otimizar-perfil/SKILL.md",
        "skills/painel-metricas/SKILL.md",
        "skills/social-media-manager/references/00-a-conta.md",
        "skills/social-media-manager/references/03-planeamento-e-calendario.md",
        "skills/social-media-manager/references/05-plataformas.md",
        "skills/social-media-manager/references/07-analise-e-relatorio.md",
        "skills/social-media-manager/references/12-contextos-de-negocio.md",
    ),
    "PLAT-014": (
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-015": (
        "skills/comentario-fixado/SKILL.md",
        "skills/social-media-manager/references/06-comunidade-e-dm.md",
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-016": (
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-017": (
        "skills/capa-de-video/SKILL.md",
        "skills/escrever-post/SKILL.md",
        "skills/formatar-post/SKILL.md",
        "skills/guiao-video-curto/SKILL.md",
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-018": (
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-019": (
        "skills/design-grafico/SKILL.md",
        "skills/infografico/SKILL.md",
        "skills/otimizar-perfil/SKILL.md",
        "skills/post-de-citacao/SKILL.md",
        "skills/social-media-manager/references/05-plataformas.md",
    ),
    "PLAT-020": (
        "skills/social-media-manager/references/08-promocao-paga.md",
        "skills/social-media-manager/references/11-numeros-de-referencia.md",
    ),
    "PLAT-021": (
        "skills/social-media-manager/references/08-promocao-paga.md",
    ),
    "PLAT-022": (
        "skills/social-media-manager/references/08-promocao-paga.md",
    ),
    "PLAT-023": (
        "skills/social-media-manager/references/08-promocao-paga.md",
    ),
    "PLAT-024": (
        "skills/social-media-manager/references/08-promocao-paga.md",
        "skills/social-media-manager/references/12-contextos-de-negocio.md",
    ),
    "PLAT-025": (
        "skills/social-media-manager/references/08-promocao-paga.md",
    ),
    "PLAT-026": (
        "skills/social-media-manager/references/08-promocao-paga.md",
    ),
}

UNSAFE_PATTERNS = {
    "limiar antigo apresentado como atual": r"limiar indicado:\s*10\+",
    "abril de 2026 tratado como data efetiva global": (
        r"Desde abril de 2026, o Instagram deixa"
    ),
    "cinco hashtags tratados como limite global fixo": (
        r"Instagram.{0,180}(?:limite|limitad[oa]).{0,50}(?:cinco|5)"
        r".{0,180}(?:desde|impost[oa].{0,40}(?:aplica|app))"
    ),
    "mapa de Pesquisa de 2021 apresentado como peso atual": (
        r"texto.{0,60}barra de pesquisa.{0,80}de longe.{0,60}sinal"
    ),
    "campo de Pesquisa histórico apresentado no presente": (
        r"(?:Nome de utilizador e nome de exibição|Nome de exibição)"
        r".{0,100}(?:é|estão).{0,30}campos? indexad"
    ),
    "observação de 50% convertida em proibição de agendar": (
        r"Isto não invalida a produção em lote\s*[—-]\s*invalida"
    ),
    "Trial Reels com alegação causal sem fonte": (
        r"Trial Reels têm quase sempre menos alcance"
    ),
    "despromoção por marca de água apresentada como regra universal": (
        r"(?:várias plataformas.{0,100}despromov.{0,100}marca de água|"
        r"marca de água.{0,100}perda de alcance.{0,100}declarad)"
    ),
    "penalização do Facebook extrapolada para Instagram": (
        r"(?:Facebook.{0,20}Instagram|Facebook e pelo Instagram)"
        r".{0,120}(?:desde 2017|reincidência penaliza)"
    ),
    "YouTube tags declaradas ausentes": r"YouTube.{0,180}já nem (?:as )?menciona",
    "Pinterest vídeo orgânico limitado a 15 minutos": (
        r"(?:vídeo|video)\s+de\s+4s\s+a\s+15\s*(?:min|minutos)"
    ),
    "categoria principal do Google tratada como peso máximo": (
        r"Google Business Profile.{0,180}(?:categoria acima de tudo|"
        r"o que decide é a categoria|categoria principal.{0,60}número um)"
    ),
    "Perguntas e Respostas do Google declaradas removidas": (
        r"(?:Perguntas e Respostas|Q&A).{0,80}removid"
    ),
    "WhatsApp declarado sem descoberta": (
        r"(?:Não tem feed nem sistema de recomendação|"
        r"canal de conversa e retenção, não de aquisição)"
    ),
    "vídeo curto imposto universalmente a 9:16": (
        r"(?:Vídeo é sempre vertical|Vídeo sempre vertical 9:16|"
        r"todas estas colunas se produzem.{0,40}vertical 9:16|"
        r"Vídeo:\s*9:16)"
    ),
    "janela da WhatsApp Business Platform aplicada a toda a app": (
        r"(?:janela (?:do )?WhatsApp.{0,60}(?:é|de)\s*24 horas|"
        r"WhatsApp.{0,80}janela de\s*24 horas|"
        r"conversa morta no WhatsApp.{0,30}está mesmo morta|"
        r"deixar uma janela do WhatsApp fechar-se)"
    ),
    "nome do Google Business Profile tratado como top-5 de keywords": (
        r"palavras-chave no nome do negócio.{0,160}(?:cinco fatores|top.?5)"
    ),
    "remoção das exclusões detalhadas atribuída a março de 2025": (
        r"(?:(?:março(?:\s+de)?\s+2025|03[./-]2025|2025[./-]03)"
        r".{0,240}(?:exclusões\s+de\s+segmentação\s+detalhada|"
        r"detailed targeting exclusions).{0,80}(?:retirad|removid)|"
        r"(?:exclusões\s+de\s+segmentação\s+detalhada|"
        r"detailed targeting exclusions).{0,80}(?:retirad|removid)"
        r".{0,240}(?:março(?:\s+de)?\s+2025|03[./-]2025|2025[./-]03))"
    ),
    "Advantage+ audience atribuída a uma mudança universal de fevereiro de 2026": (
        r"(?:(?:fevereiro(?:\s+de)?\s+2026|02[./-]2026|2026[./-]02)"
        r".{0,240}(?:interesses|Advantage\+\s+audience)"
        r".{0,100}(?:passar|tornar|começar).{0,80}sugest|"
        r"(?:interesses|Advantage\+\s+audience)"
        r".{0,100}(?:passar|tornar|começar).{0,80}sugest"
        r".{0,240}(?:fevereiro(?:\s+de)?\s+2026|02[./-]2026|2026[./-]02))"
    ),
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    if not STATE.exists():
        print(f"ERRO: falta {STATE.relative_to(ROOT)}", file=sys.stderr)
        return 1

    state_text = STATE.read_text(encoding="utf-8")
    if "## Calendário" not in state_text:
        fail(errors, "o estado não tem bloco Calendário")

    recap_match = re.search(
        r"^- \*\*Último recap:\*\*\s*`?([^`\n]+\.md)`?\s*$",
        state_text,
        flags=re.MULTILINE,
    )
    recap = STATE.parent / recap_match.group(1) if recap_match else None
    if recap is None:
        fail(errors, "o calendário não declara Último recap")

    heading_matches = list(
        re.finditer(r"^### (PLAT-\d{3})\b.*$", state_text, flags=re.MULTILINE)
    )
    record_ids = [match.group(1) for match in heading_matches]
    if not record_ids:
        fail(errors, "não foram encontrados registos PLAT")
    if len(record_ids) != len(set(record_ids)):
        fail(errors, "há IDs PLAT repetidos nos registos")

    index_ids = set(
        re.findall(r"^\| (PLAT-\d{3}) \|", state_text, flags=re.MULTILINE)
    )
    if index_ids != set(record_ids):
        fail(
            errors,
            "o índice e os registos divergem: "
            f"só no índice={sorted(index_ids - set(record_ids))}; "
            f"só nos registos={sorted(set(record_ids) - index_ids)}",
        )

    record_blocks: dict[str, str] = {}
    for number, match in enumerate(heading_matches):
        record_id = match.group(1)
        end = (
            heading_matches[number + 1].start()
            if number + 1 < len(heading_matches)
            else state_text.find("\n## Como acrescentar", match.end())
        )
        if end == -1:
            end = len(state_text)
        block = state_text[match.end() : end]
        record_blocks[record_id] = block

        for field in REQUIRED_FIELDS:
            if not re.search(
                rf"^- \*\*{re.escape(field)}:\*\*\s*\S",
                block,
                flags=re.MULTILINE,
            ):
                fail(errors, f"{record_id}: falta o campo {field}")

        source_line = re.search(
            r"^- \*\*Fontes? primárias?:\*\*.*$",
            block,
            flags=re.MULTILINE,
        )
        if not source_line or "https://" not in source_line.group(0):
            fail(errors, f"{record_id}: falta URL oficial no campo de fonte")

        if "**Fonte relida em:** não concluída" in block:
            if "**Acesso tentado em:**" not in block:
                fail(
                    errors,
                    f"{record_id}: releitura não concluída sem tentativa de acesso",
                )
            confidence_line = re.search(
                r"^- \*\*Confiança:\*\*\s*(.+)$",
                block,
                flags=re.MULTILINE,
            )
            if confidence_line and "◐" not in confidence_line.group(1):
                fail(
                    errors,
                    f"{record_id}: fonte não relida não pode manter confiança plena",
                )

    index_statuses = {
        match.group(1): match.group(2).strip()
        for match in re.finditer(
            r"^\| (PLAT-\d{3}) \|[^\n]*\| ([^|]+) \|$",
            state_text,
            flags=re.MULTILINE,
        )
    }
    for record_id, block in record_blocks.items():
        state_match = re.search(
            r"^- \*\*Estado:\*\*\s*(.+)$", block, flags=re.MULTILINE
        )
        if not state_match or record_id not in index_statuses:
            continue
        record_prefix = state_match.group(1).split()[0].lower().rstrip(".;,")
        index_prefix = index_statuses[record_id].split()[0].lower().rstrip(".;,")
        if record_prefix != index_prefix:
            fail(
                errors,
                f"{record_id}: estado do índice começa por "
                f"'{index_prefix}' e o registo por '{record_prefix}'",
            )

    if recap is None or not recap.exists():
        fail(errors, "falta o recap de linha de base")
    else:
        recap_ids = set(
            re.findall(
                r"^\| (PLAT-\d{3}) \|",
                recap.read_text(encoding="utf-8"),
                flags=re.MULTILINE,
            )
        )
        if recap_ids != set(record_ids):
            fail(
                errors,
                "o recap e os registos divergem: "
                f"só no recap={sorted(recap_ids - set(record_ids))}; "
                f"só nos registos={sorted(set(record_ids) - recap_ids)}",
            )

    if re.search(r"rollout global", record_blocks.get("PLAT-002", ""), re.I):
        fail(errors, "PLAT-002: rollout global não é suportado pela fonte")
    if re.search(
        r"^- \*\*(?:Âmbito|Rollout):\*\*\s*global\b",
        record_blocks.get("PLAT-007", ""),
        flags=re.MULTILINE | re.IGNORECASE,
    ):
        fail(errors, "PLAT-007: rollout global sobredeclara a fonte")
    if re.search(
        r"^- \*\*Âmbito:\*\*\s*global\b",
        record_blocks.get("PLAT-001", ""),
        flags=re.MULTILINE | re.IGNORECASE,
    ):
        fail(errors, "PLAT-001: âmbito global não é declarado pela fonte")
    if "**Verificado em:**" in state_text:
        fail(errors, "usar Fonte relida em; tentativa de acesso não é verificação")

    all_defined = set(record_ids)
    mapped_ids = set(EXPECTED_CONSUMERS)
    if mapped_ids != all_defined:
        fail(
            errors,
            "mapa de consumidores não cobre exatamente os registos: "
            f"sem consumidor={sorted(all_defined - mapped_ids)}; "
            f"sem registo={sorted(mapped_ids - all_defined)}",
        )
    for path in SKILLS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for referenced in set(re.findall(r"\bPLAT-\d{3}\b", text)):
            if referenced not in all_defined:
                fail(
                    errors,
                    f"{path.relative_to(ROOT)} referencia ID inexistente {referenced}",
                )

    for record_id, consumers in EXPECTED_CONSUMERS.items():
        if record_id not in all_defined:
            fail(errors, f"mapa de consumidores usa ID inexistente {record_id}")
            continue
        for relative in consumers:
            consumer = ROOT / relative
            if not consumer.exists():
                fail(errors, f"{record_id}: consumidor inexistente {relative}")
                continue
            if record_id not in consumer.read_text(encoding="utf-8"):
                fail(errors, f"{record_id}: falta propagação para {relative}")

            confidence_match = re.search(
                r"^- \*\*Confiança:\*\*\s*(.+)$",
                record_blocks[record_id],
                flags=re.MULTILINE,
            )
            if confidence_match and "◐" in confidence_match.group(1):
                for line_number, line in enumerate(
                    consumer.read_text(encoding="utf-8").splitlines(),
                    start=1,
                ):
                    if record_id in line and "⬤" in line:
                        fail(
                            errors,
                            f"{relative}:{line_number}: {record_id} tem confiança "
                            "condicionada no registo, mas o consumidor usa ⬤",
                        )

    module = (
        SKILLS
        / "social-media-manager"
        / "references"
        / "05-plataformas.md"
    )
    module_text = module.read_text(encoding="utf-8")
    for start, end, label in (
        ("## TikTok", "## YouTube", "TikTok"),
        ("## Threads e X", "## Google Business Profile", "Threads e X"),
    ):
        section_match = re.search(
            rf"^{re.escape(start)}\n(.*?)^{re.escape(end)}\n",
            module_text,
            flags=re.MULTILINE | re.DOTALL,
        )
        if not section_match:
            fail(errors, f"módulo 05: falta secção controlada de {label}")
            continue
        section = section_match.group(1)
        if "LOOK INTO" not in section or re.search(r"[⬤◑◐]|https://", section):
            fail(errors, f"módulo 05: {label} deve conter apenas LOOK INTO")

    for line_number, line in enumerate(
        module_text.splitlines(), start=1
    ):
        if "PLAT-" in line and "⬤" in line and "http" not in line:
            fail(
                errors,
                f"{module.relative_to(ROOT)}:{line_number}: "
                "facto ⬤ com ID PLAT sem URL na mesma linha",
            )

    ignored = {STATE}
    if recap is not None:
        ignored.add(recap)
    runtime_paths = [
        path
        for path in SKILLS.rglob("*.md")
        if path not in ignored
        and not any(part.startswith("recaps-") for part in path.parts)
        and not path.name.startswith("HISTORICO-")
    ]
    consumer_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in runtime_paths
    )
    for label, pattern in UNSAFE_PATTERNS.items():
        if re.search(
            pattern,
            consumer_text,
            flags=re.IGNORECASE | re.DOTALL,
        ):
            fail(errors, label)

    for path in runtime_paths:
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_number, line in enumerate(lines, start=1):
            lowered = line.casefold()
            if "tiktok" in lowered and "look into" not in lowered:
                if re.match(r"^#{2,}\s+TikTok\s*$", line, flags=re.IGNORECASE):
                    continue
                fail(
                    errors,
                    f"{path.relative_to(ROOT)}:{line_number}: "
                    "TikTok só pode aparecer como LOOK INTO",
                )
            if "threads" in lowered and "look into" not in lowered:
                if re.match(r"^#{2,}\s+Threads(?:\s+e\s+X)?\s*$", line, flags=re.IGNORECASE):
                    continue
                if "threads.com" in lowered and "instagram" in lowered:
                    continue
                fail(
                    errors,
                    f"{path.relative_to(ROOT)}:{line_number}: "
                    "Threads só pode aparecer como LOOK INTO",
                )
            if re.match(r"^\|\s*X\s*\|", line, flags=re.IGNORECASE):
                if "look into" not in lowered:
                    fail(
                        errors,
                        f"{path.relative_to(ROOT)}:{line_number}: "
                        "X só pode aparecer como LOOK INTO",
                    )

    if errors:
        print("Validação do estado das plataformas: FALHOU", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Validação do estado das plataformas: OK "
        f"({len(record_ids)} registos, {len(index_ids)} entradas no índice, "
        f"{sum(len(paths) for paths in EXPECTED_CONSUMERS.values())} "
        "ligações a consumidores)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
