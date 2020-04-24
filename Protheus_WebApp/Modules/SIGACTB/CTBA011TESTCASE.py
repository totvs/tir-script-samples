from tir import Webapp
import unittest

class CTBA011(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "01/04/2016", "T1", "D MG 01 ", "34")
        inst.oHelper.Program("CTBA011")

    def test_CTBA011_001(self):
        self.oHelper.ClickTree("Moeda", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Incluir")
        self.oHelper.SetValue("CTO_MOEDA", "06")
        self.oHelper.SetValue("CTO_DESC", "CONTROL")
        self.oHelper.SetValue("CTO_SIMB", "C$")
        self.oHelper.SetValue("CTO_BLOQ", "2 - Nao")
        self.oHelper.SetValue("CTO_TXPRJ", "1,00")
        self.oHelper.SetValue("CTO_METPRJ", "2 - Inflacao Projetada")
        self.oHelper.SetValue("CTO_DECIM", "2")
        self.oHelper.SetValue("CTO_CRITER", "2 - Mensal")
        
        txtinf = self.oHelper.GetValue("CTO_TXINF")
        self.oHelper.CheckResult("CTO_TXINF", txtinf)
        self.oHelper.SetValue("CTO_DTINIC", "01/08/2019")
        self.oHelper.SetValue("CTO_DTFINA", "31/08/2019")
        self.oHelper.SetValue("CTO_CLSMOE", "")
        self.oHelper.SetValue("CTO_CODISO", "")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("TOTVS")
        self.oHelper.CheckHelp("Apos a inclusao de uma nova moeda,cadastrar a amarracao da moeda com um calendario contabil.", "Fechar")
        self.oHelper.CheckView("Amarrações")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
