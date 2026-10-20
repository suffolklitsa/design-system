import json
import tempfile
import unittest
from pathlib import Path

from scripts import build_tokens as bt


def write(tmp, data):
    p = Path(tmp) / "tokens.json"
    p.write_text(json.dumps(data))
    return p


class Tokens(unittest.TestCase):
    def test_real_tokens_load(self):
        groups = bt.load()
        self.assertIn("ink", groups["color"])
        self.assertEqual(bt.flat(groups)["blue"], "#1769E0")

    def test_css_has_every_token(self):
        groups = bt.load()
        text = bt.css(groups)
        for name in bt.flat(groups):
            self.assertIn(f"--{name}:", text)

    def test_python_module_runs(self):
        ns = {}
        exec(bt.python(bt.load()), ns)
        self.assertEqual(ns["BLUE_DEEP"], "#0F4FAB")
        self.assertEqual(ns["TOKENS"]["s4"], "16px")

    def test_duplicate_names_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = write(d, {"color": {"ink": {"value": "#000"}}, "size": {"ink": {"value": "1px"}}})
            with self.assertRaises(ValueError):
                bt.load(p)

    def test_bad_names_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = write(d, {"color": {"Ink Blue": {"value": "#000"}}})
            with self.assertRaises(ValueError):
                bt.load(p)

    def test_outputs_are_current(self):
        stale = [p for p, text in bt.outputs(bt.load()).items() if not p.exists() or p.read_text() != text]
        self.assertEqual(stale, [], "run python3 scripts/build_tokens.py and commit the results")


if __name__ == "__main__":
    unittest.main()
