#!/usr/bin/env python
# encoding: utf-8

from math import sqrt


class Generator:
    """Create and y by x Sudoku puzzle"""

    def __init__(self, y, x, diffuculty):
        self.width = y
        self.height = x

        # The inner box height and width
        self.box_height = self.box_width = int(sqrt(self.height))
        # The maximum int value of the number that can be used in the puzzle
        self.max_value = self.height if self.height > self.width else self.width

        # Predefined ranges
        self._range_box_height = range(self.box_height)
        self._range_box_width = range(self.box_width)
        self._range_max_value = range(1, self.max_value + 1)

    def generate(self):
        puzzle = []

        return puzzle