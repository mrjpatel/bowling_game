import unittest

from bowling_game import BowlingGame


class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.bg = BowlingGame()

    def roll(self, pins, times):
        for _ in range(times):
            self.bg.roll(pins)

    def test_score_at_game_start(self):
        self.assertEqual(0, self.bg.score())

    def test_two_fours(self):
        self.roll(4, 2)
        self.assertEqual(8, self.bg.score())
