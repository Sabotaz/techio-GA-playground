import unittest
from unittest.mock import patch
from ddt import ddt, data

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
class StringTests(unittest.TestCase):
        
    def tearDown(self):
        try:
            del sys.modules["codage"]
        except KeyError:
            pass
            
    @data(38, 42, 72)
    def test_creer_chromosome(self, value):
        with patch('builtins.input', lambda: str(value)):
            import codage
            
            self.assertEqual(value, len(codage.creer_chromosome()))
            self.assertTrue(type(codage.creer_chromosome()) == str)
            
