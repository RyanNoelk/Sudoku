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
            return self.filter(total_values=<40)
        if 'Medium' == difficulty:
            return self.filter(total_values=<30)
        if 'Hard' == difficulty:
            return self.filter(total_values=<20)
        if 'Evil' == difficulty:
            return self.filter(total_values=<10)
        else:
            return self.all()


class PuzzleValue(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    value = models.IntegerField()
    y_cord = models.IntegerField()
    x_cord = models.IntegerField()
