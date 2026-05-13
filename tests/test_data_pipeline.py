import tempfile
import unittest
from pathlib import Path

from laliga_bot.data_pipeline import load_matches


class TestDataPipeline(unittest.TestCase):
    def test_load_matches_success(self):
        csv = "date,home_team,away_team,home_goals,away_goals\n2026-01-01,A,B,1,0\n"
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "ok.csv"
            p.write_text(csv)
            df = load_matches(str(p))
            self.assertEqual(len(df), 1)

    def test_load_matches_missing_column(self):
        csv = "date,home_team,away_team,home_goals\n2026-01-01,A,B,1\n"
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "bad.csv"
            p.write_text(csv)
            with self.assertRaises(ValueError):
                load_matches(str(p))


if __name__ == "__main__":
    unittest.main()
