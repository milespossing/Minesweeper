from random import Random
from square import Square

class SquareBuilder:
    def __init__(self, odds):
        self.odds = odds
        self.rnd = Random()

    def build(self):
        val = self.rnd.random()
        output = Square()
        if val > self.odds:
            output.HasMine = True
        else:
            output.HasMine = False
        return output
