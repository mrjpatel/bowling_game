class FrameScorer:
    """
    Frame Scorer Class, houses core logic for the game
    """
    MAX_PINS = 10

    def __init__(self):
        self.ball = 0

    def score_for_frame(self, frame, rolls):
        """
        Returns score for given frame, Houses core logic for the game
        :param frame: frame number for which to return score
        :type frame: int
        :param rolls: list of rolls for the game
        :type: rolls: list
        :return: score for a frame
        :rtype: int
        :raises IndexError: if not enough rolls are provided in a frame
        """
        score = 0
        try:
            for _ in range(frame):
                if self.is_strike(rolls):
                    score += self.score_for_strike(rolls)
                elif self.is_spare(rolls):
                    score += self.score_for_spare(rolls)
                else:
                    score += self.score_for_normal(rolls)
        except IndexError:
            raise IndexError("Not enough rolls provided in frame, cannot calculate score")
        return score

    def is_strike(self, rolls):
        """
        Returns true if the rolls in frame is a strike
        :param rolls: list of rolls for the game
        :type: rolls: list
        :return: boolean
        """
        return rolls[self.ball] == self.MAX_PINS

    def score_for_strike(self, rolls):
        """
        Calculates score for a strike
        :param rolls:
        :param rolls: list of rolls for the game
        :type: rolls: list
        :return: int
        """
        self.ball += 1
        return self.MAX_PINS + rolls[self.ball] + rolls[self.ball + 1]

    def score_for_normal(self, rolls):
        """
        Calculates score for a normal frame
        :param rolls:
        :param rolls: list of rolls for the game
        :type: rolls: list
        :return: int
        """
        score_for_normal = rolls[self.ball] + rolls[self.ball + 1]
        self.ball += 2
        return score_for_normal

    def is_spare(self, rolls):
        """
        Returns true if the rolls in frame is a spare
        :param rolls: list of rolls for the game
        :type: rolls: list
        :return: boolean
        """
        return rolls[self.ball] + rolls[self.ball + 1] == self.MAX_PINS

    def score_for_spare(self, rolls):
        """
        Calculates score for a spare
        :param rolls:
        :param rolls: list of rolls for the game
        :type: rolls: list
        :return: int
        """
        self.ball += 2
        return self.MAX_PINS + rolls[self.ball]
