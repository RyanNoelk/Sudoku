#!/usr/bin/env python
# encoding: utf-8

# This program solves a sudoku pullze

from math import sqrt
from pprint import pprint

class Solver:

    def __init__(self, **kwargs):
        self.puzzle = kwargs.get('puzzle', None)

        # We are assuming that we have a square puzzle
        # TODO make this work for rectangles
        self.height = self.width = len(self.puzzle)
        self.box_height = self.box_width = int(sqrt(self.height))
        self.max_value = self.height if self.height > self.width else self.width

        # Predefined ranges
        self._range_box_height = range(self.box_height)
        self._range_box_width = range(self.box_width)
        self._range_max_value = range(1, self.max_value + 1)

    def solve_puzzle(self):
        """:return: the solved puzzle"""
        return self._solve(self.puzzle)

    def _solve(self, puzzle, current_y=0, current_x=0):
        """Recursive function that solves the a sudoku puzzle using backtracking
            :param current_x: current position of the x-axis
            :param current_y: current position of the y-axis
            :param puzzle: the current puzzle
            :return: a valid puzzle or None
        """
        y, x = self._next_empty(puzzle, current_y, current_x)
        if x is None or y is None:
            return puzzle
        for write_val in self._range_max_value:
            if self._validate(puzzle, y, x, write_val):
                puzzle[y][x] = write_val
                if self._solve(puzzle, y, x) is not None:
                    return puzzle
                puzzle[y][x] = 0
        return None

    def _next_empty(self, puzzle, y_start, x_start):
        """ Returns the position of the next empty value, none if there aren't any.
            Then sets moves the pointer to the next number.
            :param x_start: starting position of the x-axis
            :param y_start: starting position of the y-axis
            :param puzzle: the current puzzle
            :return: the y, x coordinates of the next empty square
        """
        for y in range(y_start, self.height):
            for x in range(x_start, self.width):
                if 0 == puzzle[y][x]:
                    return y, x
            x_start = 0

        return None, None

    def _validate(self, puzzle, y, x, num):
        """ Checks the puzzle if its valid
            :param x: x-axis location
            :param y: y-axis location
            :param num: The number to be tried
            :return: If the puzzle is valid
        """
        # check the row
        for val in puzzle[y]:
            if num == val:
                return False
        # check the column
        for val in puzzle:
            if num == val[x]:
                return False
        # check the box
        start_y = int(y / self.box_height) * self.box_height
        start_x = int(x / self.box_width) * self.box_width
        for val_y in self._range_box_height:
            for val_x in self._range_box_width:
                if num == puzzle[val_y+start_y][val_x+start_x]:
                    return False

        return True

raw_puzzle = [
    [0,7,8,5,6,0,1,0,0],
    [0,2,3,0,0,0,5,7,0],
    [0,0,0,0,0,2,6,0,0],
    [7,0,0,0,9,1,0,5,3],
    [0,8,0,0,4,0,0,6,0],
    [4,3,0,6,2,0,0,0,1],
    [0,0,6,2,0,0,0,0,0],
    [0,4,7,0,0,0,3,8,0],
    [0,0,1,0,3,6,7,2,0]
]

'''raw_puzzle = [
    [0,1,0,0],
    [0,0,2,0],
    [0,2,0,0],
    [0,0,3,0]
]'''

pprint(Solver(puzzle=raw_puzzle).solve_puzzle())
