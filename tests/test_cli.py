import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_python(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        check=False,
    )


class CliTests(unittest.TestCase):
    def test_sys_direct_run(self) -> None:
        result = run_python("src/sys_tool.py")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "командна строка")

    def test_sys_import_is_silent(self) -> None:
        result = run_python("-c", "import src.sys_tool")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_sys_help(self) -> None:
        result = run_python("src/sys_tool.py", "--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Використання", result.stdout)

    def test_click_allowed_name(self) -> None:
        result = run_python("src/click_tool.py", "say", "--name", "Alice")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Alice")

    def test_click_rejected_name(self) -> None:
        result = run_python("src/click_tool.py", "say", "--name", "peter")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Ім’я не підходить")

    def test_click_rejected_uppercase_p(self) -> None:
        result = run_python("src/click_tool.py", "say", "--name", "Paul")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Ім’я не підходить")

    def test_click_help(self) -> None:
        result = run_python("src/click_tool.py", "--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("say", result.stdout)

    def test_fire_greet(self) -> None:
        result = run_python("src/fire_expose.py", "greet", "Alice")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertEqual(result.stdout.strip(), "Привіт, Alice!")

    def test_fire_goodbye(self) -> None:
        result = run_python("src/fire_expose.py", "goodbye", "Bob")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertEqual(result.stdout.strip(), "До побачення, Bob!")

    def test_fire_help(self) -> None:
        result = run_python("src/fire_expose.py", "--help")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("greet", result.stdout + result.stderr)
        self.assertIn("goodbye", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
