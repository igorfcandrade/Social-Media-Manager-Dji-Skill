from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

# Cabeçalhos de pergunta que significam "para onde vai isto".
# Uma pergunta com um destes e multiSelect deixa escolher várias superfícies de
# uma vez, e é aí que nasce a peça única atirada para todo o lado.
CABECALHOS_DE_DESTINO = {"plataforma", "plataformas", "destino", "destinos", "canal", "canais", "onde"}

CONTRATO = "### Vários destinos ao mesmo tempo"
TRAVAO_DO_PERFIL = "secção 4 do perfil"

BLOCO_JSON = re.compile(r"```json\s*(\[.*?\])\s*```", re.S)


def skills_com_destino_multiplo() -> list[tuple[str, Path, str]]:
    """As skills que deixam escolher mais do que um destino numa só pergunta."""
    encontradas = []
    for caminho in sorted(SKILLS.glob("*/SKILL.md")):
        texto = caminho.read_text(encoding="utf-8")
        for bruto in BLOCO_JSON.findall(texto):
            try:
                perguntas = json.loads(bruto)
            except json.JSONDecodeError:
                # Um bloco JSON inválido é outro defeito, apanhado noutro teste.
                continue
            if not isinstance(perguntas, list):
                continue
            for pergunta in perguntas:
                if not isinstance(pergunta, dict) or not pergunta.get("multiSelect"):
                    continue
                if str(pergunta.get("header", "")).strip().lower() in CABECALHOS_DE_DESTINO:
                    encontradas.append((caminho.parent.name, caminho, texto))
                    break
            else:
                continue
            break
    return encontradas


class ContratoMulticanal(unittest.TestCase):
    """Se uma skill deixa escolher vários destinos, tem de dizer o que isso custa.

    Decisão registada no ESTADO.md: manter o multiSelect e tornar o custo
    explícito — uma peça por destino, e destinos fora da secção 4 do perfil
    não se produzem. Este teste existe para a decisão não voltar a ficar
    escrita sem estar aplicada.
    """

    def setUp(self) -> None:
        self.alvos = skills_com_destino_multiplo()

    def test_ha_skills_a_verificar(self) -> None:
        # Guarda contra o teste passar por deixar de encontrar seja o que for
        # (uma mudança de formato das perguntas silenciaria tudo o resto).
        self.assertGreaterEqual(len(self.alvos), 9, "esperava pelo menos 9 skills com destino múltiplo")

    def test_toda_a_skill_com_destino_multiplo_declara_o_contrato(self) -> None:
        em_falta = [nome for nome, _, texto in self.alvos if CONTRATO not in texto]
        self.assertEqual(
            [], em_falta,
            "deixam escolher vários destinos e não dizem o que fazer com isso: "
            + ", ".join(em_falta),
        )

    def test_toda_a_skill_com_destino_multiplo_trava_pelo_perfil(self) -> None:
        em_falta = [nome for nome, _, texto in self.alvos if TRAVAO_DO_PERFIL not in texto]
        self.assertEqual(
            [], em_falta,
            "não travam destinos que a marca não escolheu (secção 4 do perfil): "
            + ", ".join(em_falta),
        )

    def test_a_entrega_produz_uma_peca_por_destino(self) -> None:
        # O defeito concreto que originou este teste: o escrever-post mandava
        # readaptar por plataforma e entregava um bloco de código só.
        formulas = (
            "por destino",
            "por plataforma",
        )
        em_falta = [
            nome for nome, _, texto in self.alvos
            if not any(f in texto for f in formulas)
        ]
        self.assertEqual(
            [], em_falta,
            "declaram o contrato e não dizem como entregar: " + ", ".join(em_falta),
        )


if __name__ == "__main__":
    unittest.main()
