# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("updater", Path(__file__).resolve().parents[1] / "DaylightUpdater.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

class UpdaterTests(unittest.TestCase):
    def test_preview_plan(self):
        self.assertEqual(app.plan("upgrade"), ("apt-get", "--simulate", "upgrade"))
        self.assertEqual(app.plan("update"), ("apt-get", "--version"))
    def test_invalid_action(self):
        with self.assertRaises(ValueError):
            app.plan("invalid")
    def test_preview_uses_injected_runner(self):
        calls = []
        class Result:
            returncode = 0
        def runner(args, check):
            calls.append((args, check))
            return Result()
        self.assertEqual(app.execute("upgrade", runner=runner), 0)
        self.assertEqual(calls[0][0], ("apt-get", "--simulate", "upgrade"))
    def test_apply_requires_root(self):
        with patch.object(app.os, "geteuid", return_value=1000):
            with self.assertRaises(PermissionError):
                app.execute("upgrade", apply=True)

if __name__ == "__main__":
    unittest.main()
