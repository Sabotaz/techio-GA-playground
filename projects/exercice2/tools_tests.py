# coding: utf-8
import unittest
from unittest.mock import patch
from ddt import ddt, data, unpack
import os

        
def test_is_chromosome(cls, chrom, size):
    cls.assertIsInstance(chrom, bytearray, "le chromosome n'a pas le bon type")
    cls.assertEqual(len(chrom), size, "le chromosome n'a pas la bonne taille")
            
_ = lambda x: bytearray(x,"ascii")

class FittingTest(unittest.TestCase):

    @patch('solution.get_solution')
    def test_fitting(self, mock_function):
        import fitting
        key = "QweJWLgWLIhdvkwyHouO"
        mock_function.return_value = key
        self.assertTrue(0 <= fitting.get_score(_("wedfyIXpkKdZJoGYKYaF")) <= 1, "Le score doit être compris entre 0 et 1")
        self.assertTrue(fitting.get_score(_("QweJWLgWLIhdvkwyHouO")) == 1, "Le score d'une solution doit être de 1")
        self.assertTrue(fitting.get_score(_("aaaaaaaaaaaaaaaaaaaa")) < 0.05, "Le score d'un chromosome totalement différent doit être proche de 0")
        self.assertTrue(fitting.get_score(_("QweaaaaaaaaaaaaaaouO")) < fitting.get_score(_("aaeJWLgWLIhdvkwyaaaa")), "Plus un chromosome ressemble à la solution, plus son score doit être élevé")

@ddt
class SelectionTest(unittest.TestCase):
    
    def test_selection(self):
        os.environ["SECRET_KEY"] = "grqFWIhIDmOmyDsPkbBY"
        
        blob = [
            _("nRLTPNabIglNSDsPkbBY"),
            _("KVlwiRFaZdAYgWrSQGcM"),
            _("grqFWbJtJpBEfbEZavSt"),
            _("gVqyFBNMFrxJVYKhrcoa"),
            _("SMQusibGODXYTteMkxPF"),
            _("zlIMmIhIDmOmyDqrJwYs"),
            _("vZqhviNbCEuzJEtswvqV"),
            _("LDTnPNuaVdnSyrMpllIe"),
            _("rhvNDnUIKHbfpUFntAtX"),
            _("jmmqRZgmfcszPtXxusSG")]
        
        import selection
        import solution
        
        select = selection.selection(blob)
        for x in select:
            self.assertIn(x, blob, "création de nouveaux chromosomes interdite")
        
        self.assertTrue(len(select) >= 2, "pas assez de chromosomes selectionnés")
        self.assertTrue(len(select) < len(blob), "trop de chromosomes selectionnés")
        self.assertTrue(solution.get_mean_rang(select) >= solution.get_mean_rang(blob), "la selection n'est pas assez bonne")
        
@ddt
class CroisementTest(unittest.TestCase):
    @data(
        (_("AAAAAAAA"), _("BBBBBBBB")),
        (_("VHFyYNasyaBVeFEdFPWy"), _("zNxISamKololUBZkMdBz")),
        (_("xadgHOQkUvnYnBoJMNQgFieoTxpttzOVEFSaNpGx"), _("cmZpPCJSifHsQzJDSYYJzXaZFrRzZxlxmmyxWgvr")))
    @unpack
    def test_croisement(self, chrom1, chrom2):
        import croisement
        chrom3 = croisement.croisement(chrom1, chrom2)
        
        test_is_chromosome(self, chrom3, len(chrom1))
        
        from1 = 0
        from2 = 0
        for x, a, b in zip(chrom3, chrom1, chrom2):
            self.assertTrue(x == a or x == b, "création de nouveaux gènes interdite")
            if x == a:
                from1 += 1
            if x == b:
                from2 += 1
        self.assertTrue(from1 + from2 >= len(chrom3), "création de nouveaux gènes interdite")
        self.assertNotEqual(chrom1, chrom3, "le chromosome est identique à l'un des parents")
        self.assertNotEqual(chrom2, chrom3, "le chromosome est identique à l'un des parents")
        
@ddt
class MutationTest(unittest.TestCase):
    @data(_("VfsyfRNouNpNcXKDmuAF"), _("VGZuMPHnadKPtdVNeBUz"))
    def test_mutation(self, chrom2):
    
        import copy
        import mutation
        
        chrom1 = copy.copy(chrom2)
        mutation.mutation(chrom2)
        
        test_is_chromosome(self, chrom2, len(chrom1))
        
        score = 0
        for a, b in zip(chrom1, chrom2):
            if a != b:
                score += 1
                
        self.assertFalse(score > 1, "trop de mutations effectuées")
        self.assertFalse(score == 0, "le chromosome n'a pas subi de mutations")
        