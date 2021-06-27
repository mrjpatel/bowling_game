class BowlingGame:

    rolls = []

    def score(self):
        player_score = 0
        for roll in self.rolls:
            player_score += roll
        return player_score

    def roll(self, pins):
        self.rolls.append(pins)
