from frame_scorer import FrameScorer


class BowlingGame:
    """
    Bowling Game Class, Tracks all the rolls and frames
    """

    def __init__(self):
        self.frame_scorer = FrameScorer()
        self.rolls = []
        self.first_roll_in_frame = True
        self.current_frame_number = 0

    def score(self):
        """
        Calculates the player's score for the game
        :return: player's score
        :rtype: int
        :raises IndexError: if not enough rolls are provided in a frame
        """
        player_score = self.frame_scorer.score_for_frame(self.current_frame_number, self.rolls)
        return player_score

    def roll(self, pins):
        """
        Adds the pins from the roll to the list
        :param pins: pins in the roll
        :type pins: int
        """
        self.rolls.append(pins)
        self.adjust_frame_if_a_strike(pins)

    def adjust_frame_if_a_strike(self, pins):
        """
        Tracks the rolls in a frame and adjusts the frame after roll is completed
        :param pins: pins in the roll
        :type pins: int
        """
        if self.first_roll_in_frame:
            if pins == self.frame_scorer.MAX_PINS:
                self.update_current_frame()
            else:
                self.first_roll_in_frame = False
        else:
            self.first_roll_in_frame = True
            self.update_current_frame()

    def update_current_frame(self):
        """
        Update current frame until max frame has reached
        """
        self.current_frame_number = min(self.current_frame_number + 1, self.frame_scorer.MAX_PINS)

    def print_scores(self):
        """
        prints score for game
        """
        player_score = self.score()
        print(f"Player rolled {self.rolls}")
        print(f"Player score is {player_score}")
