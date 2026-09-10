import tempfile
import unittest
from pathlib import Path

from scripts.validar_repositorio import validar_executoras


class ExecutorLinksTests(unittest.TestCase):
    def test_encaminhamento_sem_skill_instalavel_falha(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(validar_executoras("| `fotografia` | Direção visual | 04 |", Path(tmp)))

    def test_encaminhamento_com_skill_distribuida_passa(self):
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            (raiz / "fotografia").mkdir()
            (raiz / "fotografia/SKILL.md").write_text("---\nname: fotografia\n---\n")
            self.assertEqual(validar_executoras("| `fotografia` | Direção visual | 04 |", raiz), [])


if __name__ == "__main__":
    unittest.main()
