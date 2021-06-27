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

    def test_gutter_game(self):
        self.roll(0, 20)

    def test_for_a_strike(self):
        self.bg.roll(10)
        self.bg.roll(5)
        self.bg.roll(4)
        self.assertEqual(28, self.bg.score())

    def test_for_a_spare(self):
        self.bg.roll(4)
        self.bg.roll(6)
        self.bg.roll(5)
        self.bg.roll(0)
        self.assertEqual(20, self.bg.score())

    def test_for_11_frames(self):
        self.roll(1, 23)
        self.assertEqual(20, self.bg.score())

    def test_error_on_missing_rolls_in_frame(self):
        self.bg.roll(10)
        with self.assertRaises(IndexError):
            self.bg.score()

    def test_all_strikes(self):
        self.roll(10, 12)
        self.assertEqual(300, self.bg.score())

    def test_all_spares(self):
        self.roll(5, 21)
        self.assertEqual(150, self.bg.score())
