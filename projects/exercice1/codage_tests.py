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
class ChromosomeTest(unittest.TestCase):
        
    def tearDown(self):
        try:
            del sys.modules["codage"]
        except KeyError:
            pass
            
    @data(38, 42, 72)
    def test_type_chromosome(self, value):
        with patch('builtins.input', lambda: str(value)):
            import codage
            self.assertTrue(type(codage.creer_chromosome()) == bytearray)
            
    @data(38, 42, 72)
    def test_size_chromosome(self, value):
        with patch('builtins.input', lambda: str(value)):
            import codage
            self.assertEqual(value, len(codage.creer_chromosome()))
            
_ = lambda x: bytearray(x,"ascii")

@ddt
class ToolsTest(unittest.TestCase):
    
    def test_selection(self):
        os.environ["SECRET_KEY"] = "blop"
        
        blob = [_("truc"), _("plop"), _("caca"), _("chei"), _("tric"), _("fuck")]
        
        import tools
        import secret
        
        selection = tools.selection(blob)
        is_sublist = all(x in blob for x in selection)
        
        self.assertTrue(len(selection) >= 2, "pas assez de chromosomes selectionnés")
        self.assertTrue(is_sublist, "création de nouveaux chromosomes interdite")
        self.assertTrue(len(selection) < len(blob), "trop de chromosomes selectionnés")
        self.assertTrue(secret.get_mean_rang(selection) >= secret.get_mean_rang(blob), "la selection n'est pas assez bonne")
        
    
    @data((_("abcd"), _("efgh"), _("abgh")),(_("abcde"), _("fghij"), _("abhij")))
    @unpack
    def test_croisement(self, chrom1, chrom2, chrom3):
        import tools
        self.assertEqual(tools.croisement(chrom1, chrom2), chrom3)
    
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
        
        
    
