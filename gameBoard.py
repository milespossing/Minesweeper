from square import Square
from numpy import ndarray

class GameBoard:
    def __init__(self, m, n):
        self.Squares = ndarray(shape=(m,n), dtype=Square)
        self.m = m
        self.n = n
        self.winCondition = False
        self.loseCondition = False

    def openSquare(self,i,j):
        square = self.Squares[i,j]
        mine = square.open()
        if mine: self.loseCondition = True

    @property
    def openSquares(self):
        output = []
        for row in self.Squares:
            for square in row:
                if square.opened and len(square.closedNeighbors) > 0:
                    output.append(square)
        return output

    def CountMines(self):
        for i in range(0,self.m):
            for j in range(0,self.n):
                self.Squares[i,j].NeighborCount = self.AddNeighbors(i,j)

    def AddNeighbors(self,i,j):
        square = self.Squares[i,j]
        if i > 0:
            square.neighbors.append(self.Squares[i-1,j])
            if j > 0:
                square.neighbors.append(self.Squares[i-1,j-1]) # top left
            if j < self.n - 1:
                square.neighbors.append(self.Squares[i-1,j+1]) # top right
        if j > 0:
            square.neighbors.append(self.Squares[i,j-1]) # left
        if j < self.n - 1:
            square.neighbors.append(self.Squares[i,j+1]) # right
        if i < self.m - 1:
            square.neighbors.append(self.Squares[i+1,j]) # bottom
            if j > 0:
                square.neighbors.append(self.Squares[i+1,j-1]) # bottom left
            if j < self.n - 1:
                square.neighbors.append(self.Squares[i+1,j+1]) # bottom right
