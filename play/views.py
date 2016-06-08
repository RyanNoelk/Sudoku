from django.http import JsonResponse, Http404
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.template.loader import render_to_string

import json
import random
from math import sqrt

from common.checker import Checker

from play.models import Puzzle, PuzzleValue


class PlayView(TemplateView):
    """Django class-based view for the new cities browse page."""

    template_name = 'play/play.html'
    puzzle_id = None

    def __init__(self, **kwargs):
        """Initialize a new `PlayView` instance."""
        super(PlayView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """Get context data for new puzzles."""
        puzzle_id = self.kwargs.get('puzzle_id', None)

        if puzzle_id is None:
            # Get random Puzzle id from the DB
            puzzle_id = self._get_random_puzzle_id()

        context = self._build_puzzle(puzzle_id)

        return context

    def _get_random_puzzle_id(self):
        # Get random Puzzle id from the DB
        last = Puzzle.objects.count() - 1
        return random.randint(0, last)

    def _build_puzzle(self, puzzle_id):
        try:
            db_puzzle = Puzzle.objects.all()[int(puzzle_id)]
        except IndexError:
            raise Http404("Sorry, that puzzle doesn't exist.")

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

        try:
            width_border = [x*int(sqrt(len(puzzle[0]))) for x in range(int(sqrt(len(puzzle[0]))))]
            height_border = [x*int(sqrt(len(puzzle))) for x in range(int(sqrt(len(puzzle))))]
        except IndexError:
            raise Http404("Sorry, the puzzle u request isn't valid.")

        return {
            'puzzle': puzzle,
            'width_border': width_border,
            'height_border': height_border,
            'puzzle_id': puzzle_id,
        }


class APIView(PlayView):
    """Django class-based view for the ajax api."""

    def __init__(self, **kwargs):
        """Initialize a new `APIView` instance."""
        super(APIView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        return JsonResponse(context)

    def get_context_data(self, request, **kwargs):
        """Get context function for the api."""
        action = request.GET.get('action', None)

        board_html = ''
        checked = ''

        if action == 'new':
            puzzle_data = self._build_puzzle(self._get_random_puzzle_id())
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
        if puzzle:
            checked = Checker(puzzle).validate()
            if not checked:
                checked = Checker(puzzle, True).validate()
                if checked:
                    checked = 'ok'
                else:
                    checked = 'problem'
            else:
                checked = 'complete'
        else:
            checked = 'error'

        return checked

