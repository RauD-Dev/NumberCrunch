from itertools import product
from game.models

standard_moves = {
    1: '+1',
    -1: '-1',
    20: 'x2',
    -20: '/2',
    100: 'x10',
    -100: '/10',
    2000: '**2',
    -2000: 'root2'
}

extra_moves = [1, 2, 3, 4, 5, 20, 30, 40, 50, 100, 2000, 3000]
wild_moves = []
for x in extra_moves:
    wild_moves.append(x)
    wild_moves.append(-1*x)

class PuzzleCreator():

    def __init__(self, moves: int, up_to: int, standard: bool):
        self.moves = moves
        self.up_to = up_to
        self.standard = standard