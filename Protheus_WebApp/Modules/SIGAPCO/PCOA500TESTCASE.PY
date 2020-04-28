from tir import Webapp
import unittest

class PCOA500(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAPCO", "10/05/2016", "T1", "D MG 01 ", "57")
        inst.oHelper.Program("PCOA500")
        inst.oHelper.AddParameter("MV_PCOINTE", "", "1")
        inst.oHelper.AddParameter("MV_PCOSINC", "", "1")
        inst.oHelper.AddParameter("MV_PCOSDCT", "", ".T.")
        inst.oHelper.AddParameter("MV_PCOVENC", "", "1")
        inst.oHelper.SetParameters()

    def test_PCOA500_001(self):
        self.oHelper.SetValue("Mostrar ?", "Todos")
        self.oHelper.SetButton("Ok")
        self.oHelper.SearchBrowse("D MG 01 00002")
        self.oHelper.SetButton("Liberar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SearchBrowse("D MG 01 00002")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("ALI_CDCNTG", "00002")
        self.oHelper.CheckResult("ALI_USER", "000000")
        self.oHelper.CheckResult("ALI_CODBLQ", "BL2")
        self.oHelper.CheckResult("ALI_STATUS", "03 - Liberado")
        self.oHelper.CheckResult("ALI_PROCES", "000154")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()