import ConsoleBoardView as view

class Solver:
    def __init__(self, gameBoard):
        self.gameBoard = gameBoard

    def solve(self):
        self.firstMove()
        view.Print(self.gameBoard)
        s = self.gameBoard.openSquares
        while not self.gameBoard.winCondition and not self.gameBoard.loseCondition:
            self.iterate()
        print("Result: ")
        if self.gameBoard.loseCondition: print("You lose!")
        else: print("You win!")
        view.Print(self.gameBoard)

    def firstMove(self):
        i = self.gameBoard.m - 1
        j = self.gameBoard.n - 1
        self.gameBoard.openSquare(i,j)

    def iterate(self):

        return

    def checkSquare(self):
        return