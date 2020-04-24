from tir import Webapp
import unittest


class CTBA355(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "01/02/2016", "T1", "D MG 01 ", "34")
        inst.oHelper.Program("CTBA355")

    def test_CTBA355_001(self):
        self.oHelper.SetButton("Conferir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Conferir ?",             "Nao conferidos")
        self.oHelper.SetValue("Da Data ?",              "01/02/2016")
        self.oHelper.SetValue("Ate a Data ?",           "01/02/2016")
        self.oHelper.SetValue("Valor minimo ?",               "0,00")
        self.oHelper.SetValue("Valor maximo ?",     "999.999.999.999,99")
        self.oHelper.SetValue("Do Lote ?",                      "")
        self.oHelper.SetValue("Ate o Lote ?",               "ZZZZZZ")
        self.oHelper.SetValue("Do SubLote ?",                   "")
        self.oHelper.SetValue("Ate o Sublote ?",            "ZZZ")
        self.oHelper.SetValue("Do Documento ?",                "")
        self.oHelper.SetValue("Ate o Documento ?",       "ZZZZZZ")
        self.oHelper.SetValue("Moeda ?",                     "01")
        self.oHelper.SetValue("Tipo de saldo ?",                 "1")
        self.oHelper.SetValue("Conta ?",                    "101020")
        self.oHelper.SetValue("Centro de custo ?",              "")
        self.oHelper.SetValue("Item contabil ?",                "")
        self.oHelper.SetValue("Classe de valor ?",              "")
        self.oHelper.SetValue("Acao do clique ?",       "Conferir")
        self.oHelper.SetButton("OK")
        self.oHelper.WaitShow("Conferencia de lancamentos - CONFERIR")
        self.oHelper.ClickBox("Data Lcto","01/02/2016" ,grid_number=1)
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
