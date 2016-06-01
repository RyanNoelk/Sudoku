#!/usr/bin/env python
# encoding: utf-8

from django.core.management import BaseCommand
from optparse import make_option

from common.generator import Generator
from play.models import Puzzle, PuzzleValue


class Command(BaseCommand):
    """Management command to create puzzles."""

    help = "python manage.py save_puzzle --help"

    option_list = BaseCommand.option_list + (
        make_option('--num',
                    action='store',
                    type='int',
                    default="",
                    help='Number of puzzles to create'),
        make_option('--height',
                    action='store',
                    type='int',
                    default="",
                    help='Height of the puzzle'),
        make_option('--width',
                    action='store',
                    type='int',
                    default="",
                    help='Width of the puzzle'),)

    def handle(self, *args, **options):
        """Create puzzles."""
        num = options.get('num', 50)
        height = options.get('height', 9)
        width = options.get('width', 9)
        for i in range(num):
            puzzle = Generator(height, width).generate()
            db_puzzle = Puzzle(height=height, width=width)
            db_puzzle.save()
            for y in range(height):
                for x in range(width):
                    tmp = PuzzleValue(db_puzzle, puzzle[y][x], y, x)
                    tmp.save()
