# coding: utf-8
import unittest
from ddt import ddt, data, unpack

def test_is_chromosome(cls, chrom, size):
    cls.assertIsInstance(chrom, str, "The chromosom's type is incorrect")
    cls.assertEqual(len(chrom), size, "The chromosom's size is incorrect")
    
@ddt
class ChromosomeTest(unittest.TestCase):
            
    @data(38, 42, 72)
    def test_chromosome(self, value):
        import codage
        test_is_chromosome(self, codage.create_chromosom(value), value)
        