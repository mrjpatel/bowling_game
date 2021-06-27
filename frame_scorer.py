class FrameScorer:
    MAX_PINS = 10

    def __init__(self):
        self.ball = 0

    def score_for_frame(self, frame, rolls):
        score = 0
        for _ in range(frame):
            if rolls[self.ball] == 10:
                self.ball += 1
                score += 10 + rolls[self.ball] + rolls[self.ball + 1]
            else:
                score += rolls[self.ball] + rolls[self.ball + 1]
                self.ball += 2
        return score
