from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCIAS = ROOT / "skills" / "social-media-manager" / "references"

# O FONTES.md é a lista de fontes; não se conta a si próprio.
#
# O 05-estado-das-plataformas.md também sai, e não é indulgência: cada registo
# PLAT é obrigado por scripts/validar_estado_plataformas.py a ter URL oficial no
# campo de fonte, mais data de releitura e estado. Esse validador é mais estrito
# do que esta heurística de três linhas, e contar o ficheiro aqui só produzia
# falsos positivos — uma afirmação dentro de um registo está sustentada pelo
# campo de fonte do registo, mesmo que o URL esteja quinze linhas acima.
EXCLUIDOS = {"FONTES.md", "05-estado-das-plataformas.md"}

# Uma fonte da alínea, linha de tabela, título ou parágrafo seguinte não prova
# a afirmação anterior. A continuação pode ocupar até duas linhas, mas não pode
# atravessar uma fronteira estrutural de Markdown.
INICIO_NOVO_BLOCO = re.compile(
    r"^\s*(?:$|#{1,6}\s|[-+*]\s+|\d+[.)]\s+|>\s?|\|)"
)


def tem_fonte_visivel(linhas: list[str], indice: int) -> bool:
    janela = [linhas[indice]]
    for linha in linhas[indice + 1 : indice + 3]:
        if INICIO_NOVO_BLOCO.match(linha):
            break
        janela.append(linha)
    texto = " ".join(janela)
    return "http" in texto or "PLAT-" in texto

def afirmacoes_sem_fonte() -> dict[str, int]:
    """⬤ sem URL/PLAT no mesmo bloco, até duas linhas de continuação.

    A definição de ⬤ no SKILL.md é "fonte primária ... sempre com URL colado ao
    facto". Um ⬤ sem fonte à vista não cumpre a própria definição. A janela de
    três linhas existe porque a fonte aparece muitas vezes na linha seguinte,
    em itálico com a amostra.

    Um ID PLAT conta como sustentação: o registo de estado das plataformas tem
    a fonte, a data de releitura e o estado, que é mais do que um URL solto.
    """
    contagem: dict[str, int] = {}
    for caminho in sorted(REFERENCIAS.glob("*.md")):
        if caminho.name in EXCLUIDOS:
            continue
        linhas = caminho.read_text(encoding="utf-8").split("\n")
        n = 0
        for i, linha in enumerate(linhas):
            if "⬤" not in linha:
                continue
            if not tem_fonte_visivel(linhas, i):
                n += 1
        if n:
            contagem[caminho.name] = n
    return contagem


class SustentacaoCompleta(unittest.TestCase):
    """Impede que reapareça dívida de sustentação depois do fecho a zero."""

    def test_todas_as_afirmacoes_tem_fonte_visivel(self) -> None:
        contagem = afirmacoes_sem_fonte()
        total = sum(contagem.values())
        detalhe = ", ".join(f"{k}={v}" for k, v in sorted(contagem.items()))
        self.assertEqual(
            total,
            0,
            f"há {total} afirmações ⬤ sem fonte à vista: {detalhe}. "
            "Colar a fonte ao lado do facto, ou baixar o nível de confiança.",
        )

    def test_uma_alinea_nao_empresta_a_fonte_a_anterior(self) -> None:
        self.assertFalse(
            tem_fonte_visivel(
                ["⬤ afirmação sem fonte", "- ⬤ outra afirmação — PLAT-999"],
                0,
            )
        )
        self.assertFalse(
            tem_fonte_visivel(
                ["⬤ afirmação sem fonte", "", "https://example.com/outra"],
                0,
            )
        )
        self.assertTrue(
            tem_fonte_visivel(
                ["⬤ afirmação sustentada", "https://example.com/fonte"],
                0,
            )
        )


if __name__ == "__main__":
    unittest.main()
