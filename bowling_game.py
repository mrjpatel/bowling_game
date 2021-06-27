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
        self.adjust_frame_if_strike(pins)

    def adjust_frame_if_strike(self, pins):
        if self.first_roll_in_frame:
            if pins == 10:  # frame is finished so adjust current to new frame
                self.current_frame_number = self.current_frame_number + 1
            else:  # adjust roll in frame since its not a strike
                self.first_roll_in_frame = False
        else:
            self.first_roll_in_frame = True
            self.current_frame_number = self.current_frame_number + 1
