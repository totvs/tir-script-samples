from tir import Webapp
import unittest

class CTBA161(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "01/01/2019", "T1", "D MG 01", "34")
        inst.oHelper.Program("CTBA161")

    def test_CTBA161_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("CTS_CODPLA", "T01")
        
        OrdemAut = self.oHelper.GetValue("CTS_ORDEM")
        EntiGerenAut = self.oHelper.GetValue("CTS_CONTAG")
        self.oHelper.CheckResult("CTS_ORDEM", OrdemAut)
        self.oHelper.CheckResult("CTS_CONTAG", EntiGerenAut)
        self.oHelper.SetValue("CTS_CTASUP", "")
        self.oHelper.SetValue("CTS_DESCCG", "ENTIDADE TIR 01 INCLUIR")
        self.oHelper.SetValue("CTS_DETHCG", "TIR")
        self.oHelper.SetValue("CTS_NORMAL", "2 - Credito")
        self.oHelper.SetValue("CTS_COLUNA", "0")
        self.oHelper.SetValue("CTS_CLASSE", "1 - Sintetica")
        self.oHelper.SetValue("CTS_NOME", "TIR INCS")
        self.oHelper.SetValue("CTS_VISENT", "1 - Sim")
        self.oHelper.SetValue("CTS_FATSLD", "1 - Mantem")
        self.oHelper.SetValue("CTS_TOTVIS", "1 - Sim")
        self.oHelper.CheckView("Identificadores")
        self.oHelper.ClickCheckBox("Total Geral")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        
        chave = "T010000000001001"
        self.oHelper.SearchBrowse(f"D MG 01 {chave}", key=1, index=True)
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("CTS_CODPLA", "T01")
        self.oHelper.CheckResult("CTS_ORDEM", OrdemAut)
        self.oHelper.CheckResult("CTS_CONTAG", EntiGerenAut)
        self.oHelper.CheckResult("CTS_CTASUP", "")
        self.oHelper.CheckResult("CTS_DESCCG", "ENTIDADE TIR 01 INCLUIR")
        self.oHelper.CheckResult("CTS_DETHCG", "TIR")
        self.oHelper.CheckResult("CTS_NORMAL", "2 - Credito")
        self.oHelper.CheckResult("CTS_COLUNA", "0")
        self.oHelper.CheckResult("CTS_CLASSE", "1 - Sintetica")
        self.oHelper.CheckResult("CTS_NOME", "TIR INCS")
        self.oHelper.CheckResult("CTS_VISENT", "1 - Sim")
        self.oHelper.CheckResult("CTS_FATSLD", "1 - Mantem")
        self.oHelper.CheckResult("CTS_TOTVIS", "1 - Sim")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
