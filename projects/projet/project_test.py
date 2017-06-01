# coding: utf-8
import unittest
from unittest.mock import patch
from ddt import ddt, data, unpack
import os

import sys
from io import StringIO
from contextlib import contextmanager

@contextmanager
def capture(command, *args, **kwargs):
    out, sys.stdout = sys.stdout, StringIO()
    try:
        command(*args, **kwargs)
        sys.stdout.seek(0)
        yield sys.stdout.read()
    finally:
        sys.stdout = out

@ddt
class ProjectTest(unittest.TestCase):

    def tearDown(self):
        try:
            del sys.modules["algorithme"]
        except KeyError:
            pass
    
    @data("Aidhf", "INnhGNIUnkhkHKIhil,lbKYUGNk,HBK")
    def test_algorithme(self, solution):
        os.environ["SECRET_KEY"] = solution
        with patch('builtins.input', lambda: str(len(solution))):
            import algorithme
            with capture(algorithme.algorithme) as output:
                self.assertEqual("Expected output", solution)
        
