import unittest

import pandas as pd

from laliga_bot.features import add_target_label, add_team_form_features


class TestFeatures(unittest.TestCase):
    def test_features_and_target(self):
        df = pd.DataFrame(
            [
                {"date": "2026-01-01", "home_team": "A", "away_team": "B", "home_goals": 2, "away_goals": 1},
                {"date": "2026-01-08", "home_team": "A", "away_team": "C", "home_goals": 0, "away_goals": 0},
            ]
        )
        feat = add_team_form_features(df)
        labeled = add_target_label(feat)
        self.assertIn("home_form_points_avg", labeled.columns)
        self.assertEqual(labeled.loc[0, "target"], "H")
        self.assertEqual(labeled.loc[1, "target"], "D")


if __name__ == "__main__":
    unittest.main()
