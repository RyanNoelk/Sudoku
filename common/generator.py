#!/usr/bin/env python
# encoding: utf-8

from math import sqrt
from random import random, randrange, choice

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
        empty = self._generate_blank_puzzle_tuples()
        max_size = len(empty)
        print empty

        while True:
            rand = choice(empty)
            rand_y = rand[0]
            rand_x = rand[1]
            if puzzle[rand_y][rand_x] != 0:
                continue
            puzzle[rand_y][rand_x] = randrange(1, self.max_value)

            if Checker(puzzle, True).validate():
                ss = Solver(puzzle, True)
                ss.solve_puzzle()
                print len(ss.solutions)
                print len(ss.solutions)
                print len(ss.solutions)
                if 0 == len(ss.solutions):
                    puzzle[rand_y][rand_x] = 0
                elif 1 == len(ss.solutions):
                    return puzzle
                else:
                    empty.remove(rand)
            else:
                puzzle[rand_y][rand_x] = 0

            print puzzle
        return puzzle

    def _generate_blank_puzzle(self):
        puzzle = []
        for y in self._range_height:
            row = []
            for x in self._range_width:
                row.append(0)
            puzzle.append(row)
        return puzzle

    def _generate_blank_puzzle_tuples(self):
        puzzle = []
        for y in self._range_height:
            for x in self._range_width:
                puzzle.append((y, x))
        return puzzle
