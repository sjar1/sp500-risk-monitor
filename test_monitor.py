import json
import unittest
from pathlib import Path

class SnapshotTests(unittest.TestCase):
    def test_report_schema(self):
        data=json.loads(Path("report.json").read_text(encoding="utf-8"))
        self.assertIsInstance(data.get("companies"),list)
        self.assertGreaterEqual(data.get("companies_scanned",0),450)
        self.assertEqual(data.get("forecast_status"),"not_calibrated")
    def test_dashboard_references_report(self):
        html=Path("index.html").read_text(encoding="utf-8")
        self.assertIn("report.json",html)
        self.assertIn("escapeHTML",html)
    def test_scanner_syntax(self):
        compile(Path("scanner.py").read_text(encoding="utf-8"),"scanner.py","exec")

if __name__=="__main__":
    unittest.main()
