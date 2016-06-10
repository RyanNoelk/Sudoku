#!/usr/bin/env python
# encoding: utf-8

import json
import random
from math import sqrt

from django.http import JsonResponse, Http404
from django.views.generic.base import TemplateView
from django.template.loader import render_to_string

from common.checker import Checker
from play.models import Puzzle, PuzzleValue


class PlayView(TemplateView):
    """Django class-based view for playing Sudoku."""

    template_name = 'play/play.html'
    puzzle_id = None

    def __init__(self, **kwargs):
        """Initialize a new `PlayView` instance."""
        super(PlayView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        """Render `PlayView` instance."""
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """Get context data for new puzzles."""

        # If we have an ID from the get request, use that.
        # Otherwise get a random puzzle.
        puzzle_id = self.kwargs.get('puzzle_id', None)
        if puzzle_id is None:
            # Get a random Puzzle id from the DB
            puzzle_id = self._get_random_puzzle()

        # return the puzzle once we get and format its context from the DB.
        return self._build_puzzle(puzzle_id)

    def _get_random_puzzle(self, difficulty='Easy'):
        """Get a random Puzzle id from the DB"""
        available_puzzles = Puzzle.objects.get_total_values()
        last = available_puzzles.count() - 1
        puzzle_id = random.randint(0, last)
        try:
            return available_puzzles[int(puzzle_id)]
        except IndexError:
            raise Http404("Sorry, that puzzle doesn't exist.")

    def _build_puzzle(self, db_puzzle):
        """
        Fetch a puzzle from the DB based on ID.
        Then format the output so the template can understand it.
        """

        # Load blank puzzle then replace it with the values of the loaded puzzle
        values = PuzzleValue.objects.filter(puzzle__id=db_puzzle.id)
        puzzle = []
        for y in range(db_puzzle.height):
            row = []
            for x in range(db_puzzle.width):
                row.append(0)
            puzzle.append(row)
        for value in values:
            puzzle[value.y_cord][value.x_cord] = value.value

        # Try to get locations of where to draw thick borders, 404 otherwise.
        try:
            width_border = [x*int(sqrt(len(puzzle[0]))) for x in range(int(sqrt(len(puzzle[0]))))]
            height_border = [x*int(sqrt(len(puzzle))) for x in range(int(sqrt(len(puzzle))))]
        except IndexError:
            raise Http404("Sorry, the puzzle u request isn't valid.")

        return {
            'puzzle': puzzle,
            'puzzle_id': db_puzzle.pk,
            'width_border': width_border,
            'height_border': height_border,
        }


class APIView(PlayView):
    """Django class-based view for the ajax api."""

    def __init__(self, **kwargs):
        """Initialize a new `APIView` instance."""
        super(APIView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        """Return `APIView` json."""
        context = self.get_context_data(request, **kwargs)
        return JsonResponse(context)

    def get_context_data(self, request, **kwargs):
        """Get context function for the api."""
        action = request.GET.get('action', None)

        board_html = ''
        checked = ''

        # if the action is new, return a new Sudoku puzzle.
        # Otherwise, check the current puzzle and return the result of the check.
        if action == 'new':
            puzzle_data = self._build_puzzle(self._get_random_puzzle())
            board_html = render_to_string('play/board.html', puzzle_data)
        else:
            puzzle = json.loads(request.GET.get('puzzle', None))
            checked = self._check_puzzle(puzzle)

        context = {
            'result': checked,
            'board_html': board_html,
        }

        return context

    def _check_puzzle(self, puzzle):
        """Check the puzzle and return its status"""
        if puzzle:
            # First, check if the puzzle is complete and correct.
            checked = Checker(puzzle).validate()
            if not checked:
                # If the puzzle is not complete or not correct,
                # Check to see if it's correct while being incomplete.
                checked = Checker(puzzle, True).validate()
                if checked:
                    # return problem, if the puzzle is not complete but correct.
                    checked = 'ok'
                else:
                    # return problem, if the puzzle is not correct.
                    checked = 'problem'
            else:
                # return complete, if the puzzle is complete and correct.
                checked = 'complete'
        else:
            # return error, if the function got None for the puzzle
            checked = 'error'

        return checked

