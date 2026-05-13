import unittest

from laliga_bot.polymarket import build_edge_decision, implied_prob_from_price


class TestPolymarket(unittest.TestCase):
    def test_implied_prob(self):
        self.assertEqual(implied_prob_from_price(0.61), 0.61)

    def test_decision_take(self):
        d = build_edge_decision("HOME", model_prob=0.6, market_prob=0.5, min_edge=0.05)
        self.assertTrue(d.take)


if __name__ == "__main__":
    unittest.main()
