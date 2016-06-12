#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
from django.db import models


class PuzzleFilter(models.Manager):
    def get_total_values(self, difficulty=None):
        if isinstance(difficulty, basestring):
            difficulty = difficulty.lower()
        if 'easy' == difficulty:
            return self.filter(total_values__gte=40)
        if 'medium' == difficulty:
            return self.filter(total_values__gte=30).filter(total_values__lte=40)
        if 'hard' == difficulty:
            return self.filter(total_values__gte=20).filter(total_values__lte=30)
        if 'evil' == difficulty:
            return self.filter(total_values__lte=20)
        return self.all()


class Puzzle(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    total_values = models.IntegerField(default=0)
    objects = PuzzleFilter()


class PuzzleValue(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    value = models.IntegerField()
    y_cord = models.IntegerField()
    x_cord = models.IntegerField()
