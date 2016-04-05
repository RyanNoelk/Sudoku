#!/usr/bin/env python
# encoding: utf-8


from generator import Generator
from solver import Solver
from checker import Checker

from pprint import pprint

# Generate a puzzle and solve it
puzzle = None


# Example puzzles being passed to the solve
raw_puzzle = [
    [0, 1, 0, 0],
    [0, 0, 2, 0],
    [0, 2, 0, 0],
    [0, 0, 3, 0]
]
#pprint(Solver(raw_puzzle).solve_puzzle())

raw_puzzle = [
    [0, 7, 8, 5, 6, 0, 1, 0, 0],
    [0, 2, 3, 0, 0, 0, 5, 7, 0],
    [0, 0, 0, 0, 0, 2, 6, 0, 0],
    [7, 0, 0, 0, 9, 1, 0, 5, 3],
    [0, 8, 0, 0, 4, 0, 0, 6, 0],
    [4, 3, 0, 6, 2, 0, 0, 0, 1],
    [0, 0, 6, 2, 0, 0, 0, 0, 0],
    [0, 4, 7, 0, 0, 0, 3, 8, 0],
    [0, 0, 1, 0, 3, 6, 7, 2, 0]
]
#pprint(Solver(raw_puzzle).solve_puzzle())


# Example puzzles for checking the puzzle
puzzle = [
    [9, 7, 8, 5, 6, 3, 1, 4, 2],
    [6, 2, 3, 9, 1, 4, 5, 7, 8],
    [5, 1, 4, 7, 8, 2, 6, 3, 9],
    [7, 6, 2, 8, 9, 1, 4, 5, 3],
    [1, 8, 9, 3, 4, 5, 2, 6, 7],
    [4, 3, 5, 6, 2, 7, 8, 9, 1],
    [3, 5, 6, 2, 7, 8, 9, 1, 4],
    [2, 4, 7, 1, 5, 9, 3, 8, 6],
    [8, 9, 1, 4, 3, 6, 7, 2, 5]
]
pprint (puzzle)
print
print
print

checked = Checker(puzzle)
pprint(checked.validate())