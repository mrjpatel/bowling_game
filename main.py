from bowling_game import BowlingGame


def main():
    """
    Driver Class
    """
    bg = BowlingGame()
    bg.roll(4)
    bg.roll(4)
    bg.print_scores()

    bg = BowlingGame()
    bg.roll(4)
    bg.roll(6)  # spare
    bg.roll(5)
    bg.roll(0)
    bg.print_scores()

    bg = BowlingGame()
    bg.roll(10)  # strike
    bg.roll(5)
    bg.roll(4)
    bg.roll(0)
    bg.print_scores()


if __name__ == "__main__":
    main()
