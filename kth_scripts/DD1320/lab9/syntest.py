import unittest
from lab9_v1 import *


class SyntaxTest(unittest.TestCase):

    def test_1(self):
        indata = "Na H2O Si(C3(COOH)2)4(H2O)7 Na332".split(" ")
        utdata = ["Formeln är syntaktiskt korrekt"]*4
        for x in range(len(indata)):
            self.assertEqual(kolla_syntax(indata[x]), utdata[x])
    def test_2(self):
        indata = "C(Xx4)5 C(OH4)C C(OH4C H2O)Fe H0 H1C H02C Nacl a (Cl)2)3 ) 2".split(" ")
        utdata = ["Okänd atom vid radslutet 4)5",
                  "Saknad siffra vid radslutet C",
                  "Saknad högerparentes vid radslutet ",
                  "Felaktig gruppstart vid radslutet )Fe",
                  "För litet tal vid radslutet ",
                  "För litet tal vid radslutet C",
                  "För litet tal vid radslutet 2C",
                  "Saknad stor bokstav vid radslutet cl",
                  "Saknad stor bokstav vid radslutet a",
                  "Felaktig gruppstart vid radslutet )3",
                  "Felaktig gruppstart vid radslutet )",
                  "Felaktig gruppstart vid radslutet 2"]
        for x in range(len(indata)):
            self.assertEqual(kolla_syntax(indata[x]), utdata[x])



if __name__ == '__main__':
    unittest.main()
