from django.views.generic.base import TemplateView


class ContactView(TemplateView):
    """Django class-based view for the new cities browse page."""

    template_name = 'about/contact.html'

    def __init__(self, **kwargs):
        """Initialize a new `PlayView` instance."""
        super(ContactView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """Get context data for new puzzles."""

        return {}


class AboutView(TemplateView):
    """Django class-based view for the new cities browse page."""

    template_name = 'about/about.html'

    def __init__(self, **kwargs):
        """Initialize a new `PlayView` instance."""
        super(AboutView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})
