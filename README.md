# DiUs Bowling Game
Bowling game for dius coding test

## User Guide
Download the repository and inside the project directory run the command
```shell
python main.py
```
Alternatively you can use the logic of the code by calling the bowling_game module
```python
from bowling_game import BowlingGame

bg = BowlingGame()
bg.roll(4)
bg.roll(4)
bg.score()
```

## Tests
To run tests, download the repository and inside the project directory run the command
```shell
python -m unittest bowling_game_tests.py
```

## Code Design
- The code was written based on TDD approach so minim code is written to pass the tests with some OOP design principals in mind.
- The original approach to solution is bellow in approach section regarding the basic thinking
- SOme considerations were made, which are listed below

## Approach
- TDD approach to write failing test with enough code to pass it. Using built-in python unittest module
- Using oop to give code a structure and make it more readable and modular
- Rough design thinking
    - Keep a list all the rolls for entire game to make the frame calculations easy when its strike or spare
    - When a ball is being rolled, add to list of rolls, track frames and maybe adjust frame depending on if its a strike or not
    - When player wants to know score, go frame by frame and calculate score based on logic of spare, strike and normal score
    - Have a print score to print scores
    - Include some exception handling when there are not enough rolls throwing and player requests for score

## Consideration
- Assuming that player will add correct number of rolls in a given frame
- Assuming that the player will need score for partial game and any given frame

## License
[MIT](https://choosealicense.com/licenses/mit/)
