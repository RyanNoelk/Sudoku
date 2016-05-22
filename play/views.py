from django.http import Http404, JsonResponse
from django.views.generic.base import TemplateView

from common.generator import Generator


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
        puzzle = Generator(9, 9).generate()

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
        context = self.get_context_data(**kwargs)
        return JsonResponse(context)

    def get_context_data(self, **kwargs):
        """Get context function for the api."""

        context = {
            'puzzle': '123',
        }

        return context

