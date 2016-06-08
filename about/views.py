#!/usr/bin/env python
# encoding: utf-8

from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    """Django class-based view for the new cities browse page."""

    template_name = 'about/about.html'

    def __init__(self, **kwargs):
        """Initialize a new `PlayView` instance."""
        super(AboutView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})
