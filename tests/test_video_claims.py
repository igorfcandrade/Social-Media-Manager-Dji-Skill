from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class VideoClaimsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.paths = (
            ROOT / "skills" / "social-media-manager" / "references" / "04-criacao-de-conteudo.md",
            ROOT / "skills" / "guiao-video-curto" / "SKILL.md",
            ROOT / "skills" / "capa-de-video" / "SKILL.md",
            ROOT / "skills" / "formatar-post" / "SKILL.md",
            ROOT / "skills" / "avaliar-post" / "SKILL.md",
        )
        self.text = "\n".join(path.read_text(encoding="utf-8") for path in self.paths)

    def test_rejected_absolutes_do_not_return(self) -> None:
        for claim in (
            "o ficheiro nunca serve",
            "Um destino, uma exportação",
            "3 a 5 palavras.** Seis é o limite absoluto",
            "o único segundo que decide tudo",
            "o sinal que mais pesa",
            "20 a 40 segundos, dois pontos no máximo, nunca três",
        ):
            self.assertNotIn(claim, self.text)

    def test_cover_can_be_text_free_and_export_can_be_reused(self) -> None:
        cover = (ROOT / "skills" / "capa-de-video" / "SKILL.md").read_text(encoding="utf-8")
        script = (ROOT / "skills" / "guiao-video-curto" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Uma capa sem texto pode ser a escolha certa", cover)
        self.assertIn("mesmo ficheiro limpo pode servir várias superfícies", script)


if __name__ == "__main__":
    unittest.main()
