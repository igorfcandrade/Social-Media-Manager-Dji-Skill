from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "skills"
    / "social-media-manager"
    / "scripts"
    / "verificar_revisao.py"
)
NOTICE = "Skill necessita de revisão"


class RevisionWarningTests(unittest.TestCase):
    def run_check(
        self,
        today: str,
        platforms: Path | None = None,
        trends: Path | None = None,
    ) -> subprocess.CompletedProcess[str]:
        command = [sys.executable, str(SCRIPT), "--hoje", today]
        if platforms is not None:
            command.extend(["--plataformas", str(platforms)])
        if trends is not None:
            command.extend(["--tendencias", str(trends)])
        return subprocess.run(
            command,
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_before_both_deadlines_is_current(self) -> None:
        result = self.run_check("2026-09-29")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn(NOTICE, result.stdout)

    def test_trends_deadline_emits_exact_notice(self) -> None:
        result = self.run_check("2026-09-30")
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout.splitlines()[0], NOTICE, result.stdout)
        self.assertIn("tendências", result.stdout)

    def test_platform_deadline_emits_exact_notice(self) -> None:
        result = self.run_check("2026-10-01")
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout.splitlines()[0], NOTICE, result.stdout)
        self.assertIn("plataformas", result.stdout)

    def test_both_deadlines_emit_notice_once(self) -> None:
        result = self.run_check("2027-01-01")
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout.count(NOTICE), 1, result.stdout)
        self.assertIn("plataformas", result.stdout)
        self.assertIn("tendências", result.stdout)

    def test_state_text_cannot_override_due_date(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "plataformas.md"
            path.write_text(
                "# Estado\n\n- **Estado:** em dia\n"
                "- **Última revisão concluída:** 2026-09-01\n"
                "- **Próxima revisão programada:** 2026-09-10\n",
                encoding="utf-8",
            )
            result = self.run_check("2026-09-10", platforms=path)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout.splitlines()[0], NOTICE, result.stdout)

    def test_missing_date_fails_safe(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "plataformas.md"
            path.write_text(
                "- **Última revisão concluída:** 2026-09-01\n",
                encoding="utf-8",
            )
            result = self.run_check("2026-09-02", platforms=path)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(result.stdout.splitlines()[0], NOTICE, result.stdout)
        self.assertIn("falta o campo", result.stdout)

    def test_invalid_date_fails_safe(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "plataformas.md"
            path.write_text(
                "- **Última revisão concluída:** 2026-09-01\n"
                "- **Próxima revisão programada:** 2026-13-40\n",
                encoding="utf-8",
            )
            result = self.run_check("2026-09-02", platforms=path)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(result.stdout.splitlines()[0], NOTICE, result.stdout)

    def test_invalid_cli_date_is_structural_error(self) -> None:
        result = self.run_check("invalida")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(result.stdout.splitlines()[0], NOTICE, result.stdout)
        self.assertNotIn("usage:", result.stdout + result.stderr)

    def test_contradictory_dates_fail_safe(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "plataformas.md"
            path.write_text(
                "- **Última revisão concluída:** 2026-09-10\n"
                "- **Próxima revisão programada:** 2026-09-09\n",
                encoding="utf-8",
            )
            result = self.run_check("2026-09-02", platforms=path)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(result.stdout.splitlines()[0], NOTICE, result.stdout)
        self.assertIn("não é posterior", result.stdout)


if __name__ == "__main__":
    unittest.main()
