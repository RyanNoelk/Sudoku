from django.http import Http404, JsonResponse
from django.views.generic.base import TemplateView
import json

from common.generator import Generator
from common.checker import Checker


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
        puzzle = [
            [8, 0, 0, 0, 0, 0, 0, 4, 0],
            [5, 7, 2, 0, 0, 0, 3, 0, 0],
            [3, 0, 4, 8, 6, 5, 0, 0, 7],
            [2, 0, 0, 0, 8, 3, 0, 0, 0],
            [0, 0, 0, 6, 1, 4, 5, 0, 0],
            [4, 0, 0, 5, 0, 0, 0, 7, 1],
            [0, 0, 5, 0, 3, 7, 0, 0, 4],
            [0, 4, 0, 0, 0, 0, 0, 3, 0],
            [0, 0, 7, 1, 4, 8, 6, 0, 2]
        ]
        #puzzle = Generator(9, 9).generate()

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

