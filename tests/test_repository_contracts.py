from __future__ import annotations

import re
import unittest
from pathlib import Path

from scripts.validar_estado_plataformas import UNSAFE_PATTERNS


ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_platform_recap_is_discovered_from_calendar(self) -> None:
        source = (ROOT / "scripts" / "validar_estado_plataformas.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("Último recap", source)
        self.assertNotIn("recaps-plataformas/2026-09-01.md", source)

    def test_workflow_runs_same_public_command(self) -> None:
        workflow = (
            ROOT / ".github" / "workflows" / "validar-skills.yml"
        ).read_text(encoding="utf-8")
        for marker in (
            "push:",
            "pull_request:",
            "workflow_dispatch:",
            "schedule:",
            "./testar.sh",
        ):
            self.assertIn(marker, workflow)

    def test_governing_skill_uses_real_revision_checker_path(self) -> None:
        skill = (
            ROOT / "skills" / "social-media-manager" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "python3 skills/social-media-manager/scripts/verificar_revisao.py",
            skill,
        )
        self.assertNotIn("executar `python3 scripts/verificar_revisao.py`", skill)

    def test_public_command_runs_revision_gate_first(self) -> None:
        source = (ROOT / "testar.sh").read_text(encoding="utf-8")
        gate = "executar python3 skills/social-media-manager/scripts/verificar_revisao.py"
        structure = "executar python3 scripts/validar_repositorio.py"
        self.assertLess(source.index(gate), source.index(structure))

    def test_false_meta_dates_are_blocked_in_both_word_orders(self) -> None:
        cases = {
            "remoção das exclusões detalhadas atribuída a março de 2025": (
                "Desde março de 2025, as exclusões de segmentação detalhada foram removidas.",
                "As detailed targeting exclusions foram removidas em 03/2025.",
            ),
            "Advantage+ audience atribuída a uma mudança universal de fevereiro de 2026": (
                "Desde fevereiro de 2026, os interesses passaram a ser sugestões.",
                "No Advantage+ audience, os interesses passaram a ser sugestões em 2026-02.",
            ),
        }
        for label, examples in cases.items():
            pattern = UNSAFE_PATTERNS[label]
            for example in examples:
                with self.subTest(label=label, example=example):
                    self.assertRegex(example, re.compile(pattern, re.I | re.S))


if __name__ == "__main__":
    unittest.main()
