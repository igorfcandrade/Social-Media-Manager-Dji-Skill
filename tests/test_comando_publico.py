"""Executa o comando público num ambiente isolado para testar o contrato de saídas."""
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicCommandExitTests(unittest.TestCase):
    def run_command(self, revision, structural=0):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            shutil.copyfile(ROOT / 'testar.sh', base / 'testar.sh')
            (base / 'instalar.sh').write_text('#!/bin/sh\nexit 0\n')
            (base / 'bin').mkdir()
            python = base / 'bin/python3'
            python.write_text('#!/bin/sh\ncase "$1" in\n'
                '*verificar_revisao.py) echo "Skill necessita de revisão"; exit ' + str(revision) + ';;\n'
                '*validar_repositorio.py) echo "ESTRUTURA EXECUTADA"; exit ' + str(structural) + ';;\n'
                '*) exit 0;;\nesac\n')
            git = base / 'bin/git'
            git.write_text('#!/bin/sh\nexit 0\n')
            python.chmod(0o755); git.chmod(0o755)
            return subprocess.run(['bash', 'testar.sh'], cwd=base, capture_output=True,
                text=True, env=dict(os.environ, PATH=str(base / 'bin') + os.pathsep + os.environ['PATH']))

    def test_overdue_warns_and_still_validates(self):
        result = self.run_command(2)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual('Skill necessita de revisão', result.stdout.splitlines()[0])
        self.assertIn('ESTRUTURA EXECUTADA', result.stdout)

    def test_invalid_calendar_fails_but_still_validates(self):
        result = self.run_command(1)
        self.assertEqual(1, result.returncode)
        self.assertIn('ESTRUTURA EXECUTADA', result.stdout)

    def test_warning_does_not_hide_structural_failure(self):
        result = self.run_command(2, 1)
        self.assertEqual(1, result.returncode)


if __name__ == '__main__':
    unittest.main()
