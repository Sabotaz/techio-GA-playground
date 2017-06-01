# coding: utf-8
import unittest
from ddt import ddt, data, unpack

def test_is_chromosome(cls, chrom, size):
    cls.assertIsInstance(chrom, bytearray, "le chromosome n'a pas le bon type")
    cls.assertEqual(len(chrom), size, "le chromosome n'a pas la bonne taille")
    
@ddt
class ChromosomeTest(unittest.TestCase):
            
    @data(38, 42, 72)
    def test_chromosome(self, value):
        import codage
        test_is_chromosome(self, codage.creer_chromosome(value), value)
        