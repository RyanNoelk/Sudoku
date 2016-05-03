#!/usr/bin/env python
# encoding: utf-8

from math import sqrt


class Checker:
    """Given a user solved puzzle, this class will check if the puzzle is correctly solved.

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
        checked = Checker(puzzle)
        pprint(checked._compare_list()) -> True

        puzzle = [
            [2, 1, 4, 3],
            [4, 3, 2, 1],
            [3, 2, 1, 4],
            [1, 1, 1, 1]
        ]
        checked = Checker(puzzle)
        pprint(checked.check_puzzle()) -> False
    """
    def __init__(self, puzzle):
        # The unsolved raw puzzle
        self.puzzle = puzzle

        # TODO: We are assuming that we have a square puzzle, make this work for rectangles
        # The total box height and width
        self.height = self.width = len(self.puzzle)
        # The inner box height and width
        self.box_height = self.box_width = int(sqrt(self.height))
        # The maximum int value of the number that can be used in the puzzle
        self.max_value = self.height if self.height > self.width else self.width

        # Predefined ranges
        self._range_box_height = range(self.box_height)
        self._range_box_width = range(self.box_width)
        self._range_max_value = range(1, self.max_value + 1)

    def _is_complete(self):
        """:return: False if there is still an empty space left in the puzzle, True otherwise."""
        for y in range(self.height):
            for x in range(self.width):
                if 0 == self.puzzle[y][x]:
                    return False
        return True

    def _compare_list(self, my_list):
        """Compare a list to self._range_max_value to see if they have the same contains
            :return: True if they are the same, False otherwise."""
        for val in self._range_max_value:
            if val not in my_list:
                return False
        return True

    def _invert_puzzle(self):
        """:return: An inverted puzzle"""
        inverted_puzzle = []
        for x in range(self.width):
            inverted_row = []
            for y in range(self.height):
                inverted_row.append(self.puzzle[y][x])
            inverted_puzzle.append(inverted_row)
        return inverted_puzzle

    def validate(self):
        """:return: True if the puzzle is solve correctly, False otherwise."""

        # check if the puzzle is complete
        if not self._is_complete():
            return False

        # check the row
        for my_list in self.puzzle:
            if self._compare_list(my_list) is False:
                return False

        # check the column
        for my_list in self._invert_puzzle():
            if self._compare_list(my_list) is False:
                return False

        # build the box
        for box_num in range(self.max_value):
            box_list = []
            y_offset = (int(box_num / self.box_height) * self.box_height)
            x_offset = (int(box_num % self.box_width) * self.box_width)
            for y in self._range_box_height:
                for x in self._range_box_width:
                    try:
                        box_list.append(self.puzzle[y + y_offset][x + x_offset])
                    except:
                        return False
            # check the box
            if self._compare_list(box_list) is False:
                return False

        return True
