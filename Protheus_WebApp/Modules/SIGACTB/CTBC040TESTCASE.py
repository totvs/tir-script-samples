# coding: UTF-8
from tir import Webapp
import unittest

class CTBC040(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "13/07/2015", "T1", "D MG 01 ", "34")
        
        inst.oHelper.Program("CTBC040")

    def test_CTBC040_001(self):

        self.oHelper.SetValue("Data Inicial ?"              ,"01/01/2015")
        self.oHelper.SetValue("Data Final ?"                ,"31/12/2015")
        self.oHelper.SetValue("Qual a moeda ?"              ,"01")
        self.oHelper.SetValue("Qual Tipo Saldo ?"           ,"1")
        self.oHelper.SetValue("Seleciona Filiais ?"         ,"Nao")
        
        self.oHelper.SetButton("OK")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

