from GameBuilder.squareBuilder import SquareBuilder
from gameBoard import GameBoard

class Builder:
    def __init__(self, odds):
        self.squareBuilder = SquareBuilder(odds)

    def build(self,m,n):
        output = GameBoard(m,n)
        for i in range(0,m):
            for j in range(0,n):
                output.Squares[i,j] = self.squareBuilder.build()
        output.CountMines()
        return output
