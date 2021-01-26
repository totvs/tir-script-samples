# coding: UTF-8
from tir import Webapp
import unittest

class CTBC030(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "13/07/2015", "T1", "D MG 01 ", "34")
        
        inst.oHelper.Program("CTBC030")

    def test_CTBC030_001(self):

        self.oHelper.SetValue("Data Inicial ?"              ,"01/01/2015")
        self.oHelper.SetValue("Data Final ?"                ,"31/12/2015")
        self.oHelper.SetValue("Qual a moeda ?"              ,"01")
        self.oHelper.SetValue("Qual Tipo Saldo ?"           ,"1")
        self.oHelper.SetValue("Saldo p/ Comparacao ?"       ,"1")

        self.oHelper.SetValue("Conta Inicial ?"             ,"1010101001")
        self.oHelper.SetValue("Conta Final ?"               ,"1010101001")
        self.oHelper.SetValue("C.Custo Inicial ?"           ,"000000001")
        self.oHelper.SetValue("C.Custo Final ?"             ,"000000001")
        self.oHelper.SetValue("Item Contabil Inicial ?"     ,"000000001")
        self.oHelper.SetValue("Item Contabil Final ?"       ,"000000001")
        self.oHelper.SetValue("Classe de Valor Inicial ?"   ,"000000100")
        self.oHelper.SetValue("Classe de Valor Final ?"     ,"000000100")

        self.oHelper.SetValue("Seleciona Filiais ?"         ,"Nao")
        
        self.oHelper.SetButton("OK")

        self.oHelper.ClickTree("1 - ATIVO")
        
        self.oHelper.ClickLabel("1.0.1.01.01001 - CAIXA")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()