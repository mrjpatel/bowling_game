class FrameScorer:
    MAX_PINS = 10

    def __init__(self):
        self.ball = 0

    def score_for_frame(self, frame, rolls):
        score = 0
        for _ in range(frame):
            if self.is_strike(rolls):
                score += self.score_for_strike(rolls)
            elif self.is_spare(rolls):
                score += self.score_for_spare(rolls)
            else:
                score += self.score_for_normal(rolls)
        return score

    def is_strike(self, rolls):
        return rolls[self.ball] == self.MAX_PINS

    def score_for_strike(self, rolls):
        self.ball += 1
        return self.MAX_PINS + rolls[self.ball] + rolls[self.ball + 1]

    def score_for_normal(self, rolls):
        score_for_normal = rolls[self.ball] + rolls[self.ball + 1]
        self.ball += 2
        return score_for_normal

    def is_spare(self, rolls):
        return rolls[self.ball] + rolls[self.ball + 1] == self.MAX_PINS

    def score_for_spare(self, rolls):
        self.ball += 2
        return self.MAX_PINS + rolls[self.ball]
