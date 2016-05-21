#!/usr/bin/env python
# encoding: utf-8

from math import sqrt
from random import random, randrange

from common.solver import Solver
from common.checker import Checker


class Generator:
    """Create and y by x Sudoku puzzle"""

    def __init__(self, y, x, diffuculty=None):
        self.width = y
        self.height = x

        # The inner box height and width
        self.box_height = self.box_width = int(sqrt(self.height))
        # The maximum int value of the number that can be used in the puzzle
        self.max_value = self.height if self.height > self.width else self.width

        # Predefined ranges
        self._range_height = range(self.height)
        self._range_width = range(self.width)
        self._range_max_value = range(1, self.max_value + 1)

    def generate(self):
        puzzle = self._generate_blank_puzzle()

        while True:
            rand_y = randrange(0, self.height)
            rand_x = randrange(0, self.width)
            if puzzle[rand_y][rand_x] != 0:
                continue
            puzzle[rand_y][rand_x] = randrange(1, self.max_value)

            print
            print puzzle

            if Checker(puzzle, True).validate():
                ss = Solver(puzzle)
                ss.solve_puzzle()
                print len(ss.solutions)
                if 0 == len(ss.solutions):
                    puzzle[rand_y][rand_x] = 0
                elif 1 == len(ss.solutions):
                    return ss.solutions[0]
                for row in puzzle:
                    print row
            else:
                puzzle[rand_y][rand_x] = 0
        return puzzle

    def _has_empty_cells(self, puzzle):
        for tmp in puzzle:
            if 0 in tmp:
                return True
        return False

    def _generate_blank_puzzle(self):
        puzzle = []
        for y in self._range_height:
            tmp = []
            for x in self._range_width:
                tmp.append(0)
            puzzle.append(tmp)
        return puzzle
