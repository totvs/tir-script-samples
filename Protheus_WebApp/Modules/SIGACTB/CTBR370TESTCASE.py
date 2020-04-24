from tir import Webapp
import unittest

class CTBR370(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "09/09/2019", "T1", "D RJ 01 ", "34")
        inst.oHelper.Program("CTBR370")

    def test_CTBR370_001(self):
        self.oHelper.SetValue("Moeda ?", "01")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Imprimir")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()