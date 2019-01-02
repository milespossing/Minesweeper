from __future__ import division
import ConsoleBoardView as view

class Solver:
    def __init__(self, gameBoard):
        self.gameBoard = gameBoard

    def Print(self):
        view.Print(self.gameBoard)

    @property
    def openSquares(self):
        return self.gameBoard.openSquares

    def solve(self):
        self.firstMove()
        if self.gameBoard.loseCondition:
            print("You lose!")
            return
        self.Print()
        found = True
        self.Print()
        while not self.gameBoard.winCondition and not self.gameBoard.loseCondition and found:
            found = self.iterate()
            self.Print()
        print("Result: ")
        if self.gameBoard.loseCondition: print("I lose!")
        elif self.gameBoard.winCondition: print("I win!")
        else: print("I give up!")
        self.Print()

    def firstMove(self):
        i = self.gameBoard.m - 1
        j = self.gameBoard.n - 1
        self.gameBoard.openSquare(i,j)

    def iterate(self):
        found = False
        for square in self.openSquares:
            if square.mineCount == len(square.closedNeighbors):
                [s.flag() for s in square.closedNeighbors]
                found = True
            elif square.neighborFlagCount == square.mineCount:
                [s.open() for s in square.closedNeighbors]
                found = True
        if not found:
            found = self.tryGuess()
        return found

    def tryGuess(self):
        neighbors = []
        for square in self.openSquares:
            neighbors.append([square.closedNeighbors, square.mineCount/len(square.closedNeighbors)])
        lst = sorted(neighbors, key=lambda x: x[1])
        lst[0][0][0].open()
        return True

    def checkSquare(self):
        return