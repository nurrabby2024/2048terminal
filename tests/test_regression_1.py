import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def test_regression_1():
 """Regression guard for a auth edge case discovered earlier."""
 from 2048terminal.features.feature-auth-1 import run_auth
 result = run_auth("sample-1", timeout=5)
 assert result["ok"] is True
 assert "value" in result