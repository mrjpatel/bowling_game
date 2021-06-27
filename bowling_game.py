from frame_scorer import FrameScorer


class BowlingGame:

    def __init__(self):
        self.frame_scorer = FrameScorer()
        self.rolls = []
        self.first_roll_in_frame = True
        self.current_frame_number = 0

    def score(self):
        player_score = self.frame_scorer.score_for_frame(self.current_frame_number, self.rolls)
        return player_score

    def roll(self, pins):
        self.rolls.append(pins)
        self.adjust_frame_if_a_strike(pins)

    def adjust_frame_if_a_strike(self, pins):
        if self.first_roll_in_frame:
            if pins == self.frame_scorer.MAX_PINS:
                self.current_frame_number = min(self.current_frame_number + 1, self.frame_scorer.MAX_PINS)
            else:
                self.first_roll_in_frame = False
        else:
            self.first_roll_in_frame = True
            self.current_frame_number = min(self.current_frame_number + 1, self.frame_scorer.MAX_PINS)

    def print_scores(self):
        player_score = self.score()
        print(f"Player rolled {self.rolls}")
        print(f"Player score is {player_score}")
