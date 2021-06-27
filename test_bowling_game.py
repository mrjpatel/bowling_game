import unittest

from bowling_game import BowlingGame


class BowlingGameTest(unittest.TestCase):

    def test_score_at_game_start(self):
        bg = BowlingGame()
        self.assertEqual(0, bg.score())

