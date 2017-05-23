import unittest

class StringTests(unittest.TestCase):
    def test_to_upper(self):
        import codage
        self.assertEqual(codage.to_upper('foo'), 'FOO', "Wrong uppercase value for foo")
        self.assertEqual(codage.to_upper('Bar'), 'BAR')
		