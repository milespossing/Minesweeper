from GameBuilder.gameBuilder import Builder
import ConsoleBoardView
from Solver.MineSolver import Solver

if __name__ == '__main__':
    builder = Builder(.8)
    output = builder.build(10,10)
    ConsoleBoardView.Print(output)
    s = Solver(output)
    s.solve()
