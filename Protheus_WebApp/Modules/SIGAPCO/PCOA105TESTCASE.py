from tir import Webapp
import unittest

class PCOA105(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAPCO", "01/06/2017", "T1", "M PR 01 ", "57")
        inst.oHelper.Program("PCOA105")
    
    def test_PCOA105_001(self):
        self.oHelper.SetValue("Totais da Planilha Orçamentária", True)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M PR 01 ")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Classe Orçamentária", True)
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Total Por  ? ", "Total por Classe")
        self.oHelper.SetValue("Acumulado Por  ? ", "Acumulado por Classe")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Entidade Origem  ? ", "AK6")
        self.oHelper.SetButton("Finalizar")
        self.oHelper.SearchBrowse("M PR 01 001")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("AKK_COD", "001")
        self.oHelper.CheckResult("AKK_DESCRI", "Total por Classe")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SearchBrowse("M PR 01 002")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("AKK_COD", "002")
        self.oHelper.CheckResult("AKK_DESCRI", "Acumulado por Classe")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
