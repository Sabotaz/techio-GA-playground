# coding: utf-8
import unittest
from unittest.mock import patch
from ddt import ddt, data, unpack
import os

        
def test_is_chromosome(cls, chrom, size):
    cls.assertIsInstance(chrom, str, "The chromosome's type is incorrect")
    cls.assertEqual(len(chrom), size, "The chromosome's size is incorrect")

class FittingTest(unittest.TestCase):

    @patch('answer.get_answer')
    def test_fitting(self, mock_function):
        import fitting
        key = "QweJWLgWLIhdvkwyHouO"
        mock_function.return_value = key
        self.assertTrue(0 <= fitting.get_score("wedfyIXpkKdZJoGYKYaF") <= 1, "The score must fit between 0 and 1")
        self.assertTrue(fitting.get_score("QweJWLgWLIhdvkwyHouO") == 1, "A solution to the problem should have a score of 1")
        self.assertTrue(fitting.get_score("aaaaaaaaaaaaaaaaaaaa") < 0.05, "A chromosome really different from the solution should have a near 0 score")
        self.assertTrue(fitting.get_score("QweaaaaaaaaaaaaaaouO") < fitting.get_score("aaeJWLgWLIhdvkwyaaaa"), "The more a chromosome fits the solution, the higher its score")

@ddt
class SelectionTest(unittest.TestCase):
    
    def test_selection(self):
        os.environ["SECRET_KEY"] = "grqFWIhIDmOmyDsPkbBY"
        
        blob = [
            "nRLTPNabIglNSDsPkbBY",
            "KVlwiRFaZdAYgWrSQGcM",
            "grqFWbJtJpBEfbEZavSt",
            "gVqyFBNMFrxJVYKhrcoa",
            "SMQusibGODXYTteMkxPF",
            "zlIMmIhIDmOmyDqrJwYs",
            "vZqhviNbCEuzJEtswvqV",
            "LDTnPNuaVdnSyrMpllIe",
            "rhvNDnUIKHbfpUFntAtX",
            "jmmqRZgmfcszPtXxusSG"]
        
        import selection
        import answer
        
        select = selection.selection(blob)
        for x in select:
            self.assertIn(x, blob, "Creation of new chromosoms is forbidden")
        
        self.assertTrue(len(select) >= 2, "Not enough selected chromosoms")
        self.assertTrue(len(select) < len(blob), "Too many selected chromosoms")
        self.assertTrue(answer.get_mean_score(select) >= answer.get_mean_score(blob), "The selection is not good enough")
        
@ddt
class CrossoverTest(unittest.TestCase):
    @data(
        ("AAAAAAAA", "BBBBBBBB"),
        ("VHFyYNasyaBVeFEdFPWy", "zNxISamKololUBZkMdBz"),
        ("xadgHOQkUvnYnBoJMNQgFieoTxpttzOVEFSaNpGx", "cmZpPCJSifHsQzJDSYYJzXaZFrRzZxlxmmyxWgvr"))
    @unpack
    def test_croisement(self, chrom1, chrom2):
        import crossover
        chrom3 = crossover.crossover(chrom1, chrom2)
        
        test_is_chromosome(self, chrom3, len(chrom1))
        
        from1 = 0
        from2 = 0
        for x, a, b in zip(chrom3, chrom1, chrom2):
            self.assertTrue(x == a or x == b, "Gene generation is forbidden")
            if x == a:
                from1 += 1
            if x == b:
                from2 += 1
        self.assertTrue(from1 + from2 >= len(chrom3), "Gene generation is forbidden")
        self.assertNotEqual(chrom1, chrom3, "The chromosome is identical to one of its parents")
        self.assertNotEqual(chrom2, chrom3, "The chromosome is identical to one of its parents")
        
@ddt
class MutationTest(unittest.TestCase):
    @data("VfsyfRNouNpNcXKDmuAF", "VGZuMPHnadKPtdVNeBUz")
    def test_mutation(self, chrom1):
    
        import mutation
        
        chrom2 = mutation.mutation(chrom1)
        
        test_is_chromosome(self, chrom2, len(chrom1))
        
        score = 0
        for a, b in zip(chrom1, chrom2):
            if a != b:
                score += 1
                
        self.assertFalse(score > 1, "Too many mutations")
        self.assertFalse(score == 0, "The chromosome has not been mutated")
        