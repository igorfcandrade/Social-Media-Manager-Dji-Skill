from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SMM = ROOT / "skills" / "social-media-manager"


class ProductionPlanContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.skill = (SMM / "SKILL.md").read_text(encoding="utf-8")
        self.reference = (
            SMM / "references" / "13-plano-de-producao.md"
        ).read_text(encoding="utf-8")
        self.template = (
            SMM / "assets" / "plano-de-producao-modelo.md"
        ).read_text(encoding="utf-8")

    def test_mode_is_routed_without_embedding_or_requiring_pjm(self) -> None:
        for marker in (
            "### Plano de produção",
            "references/13-plano-de-producao.md",
            "assets/plano-de-producao-modelo.md",
            "smm-production-handoff/v1",
            "capacidade independente",
            "Se não estiver",
            "não alterar quadros",
        ):
            self.assertIn(marker, self.skill)
        self.assertNotIn("../adaptive-project-manager/SKILL.md", self.skill)

    def test_eight_required_sections_exist_in_order(self) -> None:
        headings = (
            "## 1. Totais consolidados de ativos",
            "## 2. Lista de fotografias",
            "## 3. Lista de vídeos e planos",
            "## 4. Formatos, rácios e durações-alvo",
            "## 5. Pessoas, produtos, locais, adereços e autorizações",
            "## 6. Mapa de reutilização entre peças",
            "## 7. Dependências e aprovações",
            "## 8. Handoff normalizado para a PJM",
        )
        positions = [self.template.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))

    def test_source_assets_and_exports_are_counted_separately(self) -> None:
        for marker in (
            "matéria-prima única",
            "entregas finais",
            "FOTO-###",
            "PLANO-###",
            "VID-###",
            "EXP-###",
            "POR_CONFIRMAR",
            "Nunca somar uma adaptação",
        ):
            self.assertIn(marker, self.reference)

    def test_handoff_has_pjm_control_and_return_contract(self) -> None:
        for marker in (
            "schema: smm-production-handoff/v1",
            "handoff_id:",
            "canonical_work_item:",
            "production_plan_id:",
            "assignment_state: proposed",
            "unresolved_conflicts:",
            "hard:",
            "soft:",
            "mutation_authorization: propose-only",
            "acceptance:",
            "failure_signals:",
            "prohibited_actions:",
            "stop_conditions:",
            "ticket_candidates:",
            "return_contract:",
            "completed, partial, blocked, needs-decision, failed",
            "recommended_next_state",
        ):
            self.assertIn(marker, self.template)

    def test_integration_guidance_stays_out_of_the_repository(self) -> None:
        # O repositório é agnóstico quanto ao modelo: o formato de um assistente
        # concreto produz-se fora daqui. Ver INTEGRAR.md.
        self.assertFalse((ROOT / "_gpt").exists(), "pacote específico de um assistente no repositório")
        self.assertTrue((ROOT / "INTEGRAR.md").is_file())
