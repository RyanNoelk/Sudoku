#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
from django.db import models


class Puzzle(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    total_values = models.IntegerField()

    def get_total_values(self, difficulty):
        if 'Easy' == difficulty:
            return self.filter(total_values__gte=40)
        if 'Medium' == difficulty:
            return self.filter(total_values__gte=30).filter(total_values__lte=40)
        if 'Hard' == difficulty:
            return self.filter(total_values__gte=20).filter(total_values__lte=30)
        if 'Evil' == difficulty:
            return self.filter(total_values__lte=20)
        else:
            return self.all()


class PuzzleValue(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    value = models.IntegerField()
    y_cord = models.IntegerField()
    x_cord = models.IntegerField()
