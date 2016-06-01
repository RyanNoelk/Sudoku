from django.http import Http404, JsonResponse
from django.views.generic.base import TemplateView
import json
import random

from common.checker import Checker

from play.models import Puzzle, PuzzleValue


class PlayView(TemplateView):
    """Django class-based view for the new cities browse page."""

    template_name = 'play/play.html'

    def __init__(self, **kwargs):
        """Initialize a new `PlayView` instance."""
        super(PlayView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """Get context data for new puzzles."""

        # Get random Puzzle from the DB
        last = Puzzle.objects.count() - 1
        index = random.randint(0, last)
        db_puzzle = Puzzle.objects.all()[index]

        # Load blank puzzle with replace it with the values of the loaded puzzle
        values = PuzzleValue.objects.filter(puzzle__id=db_puzzle.id)
        puzzle = []
        for y in range(db_puzzle.height):
            row = []
            for x in range(db_puzzle.width):
                row.append(0)
            puzzle.append(row)
        for value in values:
            puzzle[value.y_cord][value.x_cord] = value.value

        context = {
          'puzzle': puzzle,
        }

        return context


#@cbv_decorator(require_http_methods(['GET']))
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
        puzzle = json.loads(request.GET.get('puzzle', None))
        if puzzle:
            checked = Checker(puzzle).validate()
            if not checked:
                checked = Checker(puzzle, True).validate()
        else:
            checked = 'error'

        context = {
            'result': checked,
        }

        return context

