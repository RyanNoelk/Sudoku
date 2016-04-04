#!/usr/bin/env python
# encoding: utf-8


from generator import Generator
from solver import Solver
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
pprint(Solver(raw_puzzle).solve_puzzle())

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
pprint(Solver(raw_puzzle).solve_puzzle())
