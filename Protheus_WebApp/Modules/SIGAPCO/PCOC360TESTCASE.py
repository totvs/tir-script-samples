from tir import Webapp
import unittest

class PCOC360(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAPCO", "01/01/2019", "T1", "M SP 01", "57")
        inst.oHelper.Program("PCOC360")

    def test_PCOC360_001(self):
        self.oHelper.AddParameter("MV_PCOCNIV", "", "F")
        self.oHelper.SetParameters()
        COD = "VS"
        self.oHelper.SearchBrowse(f"M SP 01 {COD}", "Filial+codigo")
        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01012019")
        self.oHelper.SetValue("MV_PAR02", "31122019")
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        self.oHelper.SetValue("MV_PAR05", "4 - Barra")
        self.oHelper.SetValue("MV_PAR06", "1")
        self.oHelper.SetValue("MV_PAR07", "2 - Nao")
        self.oHelper.ClickLabel("Unidade")
        self.oHelper.SetValue("MV_PAR09", "@E 999,999,999,999.99")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetValue("MV_PAR01", "OR")
        self.oHelper.ClickLabel("Sim")
        self.oHelper.SetValue("MV_PAR03", "ORCADO")
        self.oHelper.ClickLabel("Movimento do periodo")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetValue("MV_PAR01", "")
        self.oHelper.SetValue("MV_PAR02", "zzzzzzzzz")
        self.oHelper.SetValue("MV_PAR04", "")
        self.oHelper.SetValue("MV_PAR05", "zzzzzzzzz")
        self.oHelper.SetValue("MV_PAR07", "")
        self.oHelper.SetValue("MV_PAR08", "zz")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
