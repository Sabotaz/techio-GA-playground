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
            
_ = lambda x: bytearray(x,"ascii")

@ddt
class SelectionTest(unittest.TestCase):
    
    def test_selection(self):
        os.environ["SECRET_KEY"] = "blop"
        
        blob = [_("truc"), _("plop"), _("caca"), _("chei"), _("tric"), _("fuck")]
        
        import tools
        import secret
        
        selection = tools.selection(blob)
        for x in selection:
            self.assertIn(x, blob, "création de nouveaux chromosomes interdite")
        
        self.assertTrue(len(selection) >= 2, "pas assez de chromosomes selectionnés")
        self.assertTrue(len(selection) < len(blob), "trop de chromosomes selectionnés")
        self.assertTrue(secret.get_mean_rang(selection) >= secret.get_mean_rang(blob), "la selection n'est pas assez bonne")
        
@ddt
class CroisementTest(unittest.TestCase):
    @data((_("abcd"), _("efgh")),(_("abcde"), _("fghij")))
    @unpack
    def test_croisement(self, chrom1, chrom2):
        import tools
        chrom3 = tools.croisement(chrom1, chrom2)
        
        self.assertEqual(len(chrom1), len(chrom3))
        
        from1 = 0
        from2 = 0
        for x, a, b in zip(chrom3, chrom1, chrom2):
            self.assertTrue(x == a or x == b)
            if x == a:
                from1 += 1
            if x == b:
                from2 += 1
        self.assertTrue(from1 + from2 >= len(chrom3))
        self.assertNotEqual(chrom1, chrom3)
        self.assertNotEqual(chrom2, chrom3)
        
@ddt
class MutationTest(unittest.TestCase):
    @data(_("jkdjsfo"), _("jinailnfoe"))
    def test_mutation(self, chrom2):
    
        import copy
        import tools
        
        chrom1 = copy.copy(chrom2)
        tools.mutation(chrom2)
        
        self.assertTrue(type(chrom2) == bytearray)
        self.assertEqual(len(chrom1), len(chrom2))
        
        score = 0
        for a, b in zip(chrom1, chrom2):
            if a != b:
                score += 1
                
        self.assertEqual(score, 1)
        