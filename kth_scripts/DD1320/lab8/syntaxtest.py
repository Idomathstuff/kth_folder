import unittest
from syntax import *


class SyntaxTest(unittest.TestCase):

    def test_storsaknas(self):
        self.assertEqual(kolla_syntax("aa"), "Saknad stor bokstav vid radslutet aa")
        
    def test_litensaknas(self):
        self.assertEqual(kolla_syntax("AA"), "Litenbokstav saknas A")

    def test_num(self):
        self.assertEqual(kolla_syntax("Aa0"), "För litet tal vid radslutet ")

    def test_nonum(self):
        self.assertEqual(kolla_syntax("Aaa"), "Radslutet borde vara ett tal")

    def test_korrekt(self):
        self.assertEqual(kolla_syntax("Aa2"), "Formeln är syntaktiskt korrekt")

if __name__ == '__main__':
    unittest.main()