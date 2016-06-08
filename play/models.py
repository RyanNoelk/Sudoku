#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
from django.db import models


class Puzzle(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()


class PuzzleValue(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    value = models.IntegerField()
    y_cord = models.IntegerField()
    x_cord = models.IntegerField()
