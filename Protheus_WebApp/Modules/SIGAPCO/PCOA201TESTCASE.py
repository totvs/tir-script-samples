from tir import Webapp
import unittest

class PCOA201(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAPCO", "01/01/2019", "T1", "M SP 01", "57")
        inst.oHelper.Program("PCOA201")

    def test_PCOA201_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01")
        self.oHelper.SetValue("AKR_ORCAME", "PCO0000010002")
        self.oHelper.SetValue("AKR_VERBAS", "0001")
        self.oHelper.SetValue("AKR_REVISA", "0002")
        self.oHelper.SetValue("AKR_DESCRI", "SIMULACAO INCLUSAO CONTROL")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_PCOA201_002(self):
        COD = "PCO0000010002  0005"
        self.oHelper.SearchBrowse(f"M SP 01 {COD}", "Filial+planilha Orc + Versao Sim")
        self.oHelper.SetButton("Outras Ações", "Simular")
        self.oHelper.ClickLabel("PCO000001000-SQUAD CONTROL PCOA201")
        self.oHelper.ClickLabel("057-SQUAD CONTROL SINT C.O")
        self.oHelper.ClickLabel("057000000002-SQUAD CONTROL C.O ANALITICA")
        self.oHelper.SetButton("Gerar Gráfico")
        self.oHelper.SetButton("Salvar", position=2)
        self.oHelper.AssertTrue()

    def test_PCOA201_003(self):
        COD = "PCO0000010002  0005"
        self.oHelper.SearchBrowse(f"M SP 01 {COD}", "Filial+planilha Orc + Versao Sim")
        self.oHelper.SetButton("Outras Ações", "Simular")
        self.oHelper.ClickTree("PCO000001000-SQUAD CONTROL PCOA201")
        self.oHelper.ClickTree("057-SQUAD CONTROL SINT C.O")
        self.oHelper.ClickLabel("057000000002-SQUAD CONTROL C.O ANALITICA")
        self.oHelper.SetButton("Gerar Gráfico")
        self.oHelper.SetButton("Outras Ações", "Pl.Compar.")
        self.oHelper.SetValue("MV_PAR01", "PCO000001")
        self.oHelper.SetValue("MV_PAR02", "0001")
        self.oHelper.SetButton("Ok")
        self.oHelper.ClickTree("057000000002-SQUAD CONTROL C.O ANALITICA")
        self.oHelper.ClickTree("057-SQUAD CONTROL SINT C.O")
        self.oHelper.ClickLabel("057-SQUAD CONTROL SINT C.O")
        self.oHelper.ClickTree("057000000002-SQUAD CONTROL C.O ANALITICA")
        self.oHelper.ClickLabel("057000000002-SQUAD CONTROL C.O ANALITICA")
        self.oHelper.SetButton("Gerar Gráfico")
        self.oHelper.SetButton("Salvar", position=2)
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
