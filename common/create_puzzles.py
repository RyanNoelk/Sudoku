#!/usr/bin/env python
# encoding: utf-8

from common.generator import Generator
from play.models import Puzzle, PuzzleValue

"""
This file will generate sudoku puzzles and save them to the DB.
"""


def create_puzzles(height=9, width=9):
    puzzle = Generator(height, width).generate()
    db_puzzle = Puzzle(height=height, width=width)
    db_puzzle.save()
    for y in range(height):
        for x in range(width):
            tmp = PuzzleValue(db_puzzle, puzzle[y][x], y, x)
            tmp.save()


if __name__ == '__main__':
    for i in range(50):
        create_puzzles()
