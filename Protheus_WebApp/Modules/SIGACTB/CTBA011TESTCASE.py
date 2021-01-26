from tir import Webapp
import unittest


class CTBA011(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "01/04/2016", "T1", "D MG 01 ", "34")
        inst.oHelper.Program("CTBA011")

        # Para que o Tipo de Saldo seja considerado nas pesquisas e validações relacionados

        #inst.oHelper.AddParameter("MV_CTBCTG ","", ".T.")
        # inst.oHelper.SetParameters()

# ==================================================================
#                 Cadastrando moeda somente.
# ==================================================================
    def test_CTBA011_001(self):

        # Clicar no pai da arvore Moeda
        self.oHelper.ClickTree("Moeda", right_click=True)
        # Clicar incluir
        self.oHelper.ClickMenuPopUpItem("Incluir")

        # Cod =
        #self.oHelper.GetValue("CTO_MOEDA", "06")
        #self.oHelper.CheckResult("CTO_MOEDA", Cod)
        self.oHelper.SetValue("CTO_MOEDA", "06")
        #self.oHelper.SetValue("CTO_DESC", "06")
        self.oHelper.SetValue("CTO_DESC", "CONTROL")
        self.oHelper.SetValue("CTO_SIMB", "C$")
        self.oHelper.SetValue("CTO_BLOQ", "2 - Nao")
        self.oHelper.SetValue("CTO_TXPRJ", "1,00")
        self.oHelper.SetValue("CTO_METPRJ", "2 - Inflacao Projetada")
        self.oHelper.SetValue("CTO_DECIM", "2")
        self.oHelper.SetValue("CTO_CRITER", "2 - Mensal")
        # self.oHelper.SetValue("CTO_TXINF","0,00")

        txtinf = self.oHelper.GetValue("CTO_TXINF")
        self.oHelper.CheckResult("CTO_TXINF", txtinf)

        self.oHelper.SetValue("CTO_DTINIC", "01/08/2019")
        self.oHelper.SetValue("CTO_DTFINA", "31/08/2019")
        self.oHelper.SetValue("CTO_CLSMOE", "")
        self.oHelper.SetValue("CTO_CODISO", "")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow("TOTVS")
        self.oHelper.CheckHelp(
            "Apos a inclusao de uma nova moeda,cadastrar a amarracao da moeda com um calendario contabil.", "Fechar")
        #self.oHelper.CheckHelp("O codigo da moeda deve ser igual a quantidade de moedas existente no cadastro.","Fechar")

        self.oHelper.CheckView("Amarrações")
        #self.oHelper.CheckView("06 - CONTROL")

        self.oHelper.AssertTrue()

# AGUARDANDO AUTOMAÇÃO
   # def test_CTBA011_002(self):
#
   #     self.oHelper.ClickIcon("Add")

    # def test_CTBA011_003(self):
#
    #    self.oHelper.WaitShow("Amarrações")
    #    self.oHelper.CheckView("05 - IENE      ")
    #    self.oHelper.ClickTree("05 - IENE      ")
#
    #    self.oHelper.CheckView("001")
    #    self.oHelper.ClickTree("001")
#
    #    self.oHelper.CheckView("01 - 01/01/2012 a 31/12/2049")
    #    self.oHelper.ClickLabel("01 - 01/01/2012 a 31/12/2049")

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
