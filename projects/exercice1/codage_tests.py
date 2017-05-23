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
        
def test_is_chromosome(cls, chrom, size):
    cls.assertIsInstance(chrom, bytearray)
    cls.assertEqual(len(chrom), size)
    
@ddt
class ChromosomeTest(unittest.TestCase):
        
    def tearDown(self):
        try:
            del sys.modules["codage"]
        except KeyError:
            pass
            
    @data(38, 42, 72)
    def test_chromosome(self, value):
        with patch('builtins.input', lambda: str(value)):
            import codage
            test_is_chromosome(self, codage.creer_chromosome(), value)
            