import unittest

from bowling_game import BowlingGame


class BowlingGameTest(unittest.TestCase):
    """
    Bowling Game Tests
    """

    def setUp(self):
        """
        Setup for bowling game tests
        :return: bowling game object
        :rtype: BowlingGame
        """
        self.bg = BowlingGame()

    def roll(self, pins, times):
        """
        Rolls pins for number of times
        :param pins: pins to roll
        :type pins: int
        :param times:
        :type times: int
        """
        for _ in range(times):
            self.bg.roll(pins)

    def test_score_at_game_start(self):
        """ Test score at the start of game """
        self.assertEqual(0, self.bg.score())

    def test_two_fours(self):
        """ Test score for normal frame """
        self.roll(4, 2)
        self.assertEqual(8, self.bg.score())

    def test_gutter_game(self):
        """ Test score for a full game with no score """
        self.roll(0, 20)

    def test_for_a_strike(self):
        """ Test score for a strike """
        self.bg.roll(10)
        self.bg.roll(5)
        self.bg.roll(4)
        self.assertEqual(28, self.bg.score())

    def test_for_a_spare(self):
        """ Test score for a spare """
        self.bg.roll(4)
        self.bg.roll(6)
        self.bg.roll(5)
        self.bg.roll(0)
        self.assertEqual(20, self.bg.score())

    def test_for_11_frames(self):
        """ Test score for max 10 frames """
        self.roll(1, 23)
        self.assertEqual(20, self.bg.score())

    def test_error_on_missing_rolls_in_frame(self):
        """ Test for raised exception for insufficient rolls provided for frame """
        self.bg.roll(10)
        with self.assertRaises(IndexError):
            self.bg.score()

    def test_all_strikes(self):
        """ Test score for a full game of strikes """
        self.roll(10, 12)
        self.assertEqual(300, self.bg.score())

    def test_all_spares(self):
        """ Test score for a full game of spares """
        self.roll(5, 21)
        self.assertEqual(150, self.bg.score())
