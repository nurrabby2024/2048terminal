import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def test_regression_0():
 """Regression guard for a validation edge case discovered earlier."""
 from 2048terminal.features.feature-validation-0 import run_validation
 result = run_validation("sample-0", timeout=5)
 assert result["ok"] is True
 assert "value" in result