from tir import Webapp
import unittest

class CTBR510(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "15/04/2015", "T1", "D RJ 02 ", "34")
        inst.oHelper.Program("CTBR510")

    @classmethod
    def test_CTBR510_001(self):
        self.oHelper.AddParameter("MV_TREPORT", "", "1")
        self.oHelper.SetParameters()
        self.oHelper.SetValue("Exercicio Contabil ?", "215")
        self.oHelper.SetValue("Cod. Config. Livros ?", "060")
        self.oHelper.SetValue("Moeda ?", "01")
        self.oHelper.SetValue("Posicao Anterior L/P ?", "Nao")
        self.oHelper.SetValue("Data Lucros/Perdas ?", "")
        self.oHelper.SetValue("Dem. Periodo Anterior ?", "Nao")
        self.oHelper.SetValue("Folha Inicial ? ", "2")
        self.oHelper.SetValue("Data de Referencia ?", "31/12/2015")
        self.oHelper.SetValue("Periodo ?", "Periodo")
        self.oHelper.SetValue("Imprime Termo Auxiliar ?", "Sim")
        self.oHelper.SetValue("Termo Auxil. a ser impresso ?", "")
        self.oHelper.SetValue("Saldos Zerados ?", "Nao")
        self.oHelper.SetValue("Considerar ?", "Mov. Periodo")
        self.oHelper.SetValue("Descrição na Moeda ?", "01")
        self.oHelper.SetValue("Tipo de saldo ?", "1")
        self.oHelper.SetValue("Titulo com nome da visao ?", "Sim")
        self.oHelper.SetValue("Consolidar Saldo ?", "Nao")
        self.oHelper.SetValue("Saldo a Consolidar ?", "")
        self.oHelper.SetValue("Seleciona Filiais ?", "Nao")
        self.oHelper.SetValue("Data Periodo Anterior ?", "")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Imprimir")
        self.oHelper.WaitShow("Ediçäo dos Termos de Abertura/Encerramento")
        self.oHelper.SetButton("x",)
        self.oHelper.SetButton("Sair")
        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
