from tir import Webapp 
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class FATA240(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "D MG 01 ", "05")
        self.oHelper.Program("FATA240") 

    def test_FATA240_CT001(self):
        cPortal = "FTC001"
        cDesc = "CT001 - INCLUSAO"
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.WaitShow("Menu dos Portais - INCLUIR")
        self.oHelper.SetValue("AI9_PORTAL", cPortal)
        self.oHelper.SetValue("AI9_DESCRI", cDesc)
        self.oHelper.SetValue("AI9_DESC_S", cDesc)
        self.oHelper.SetValue("AI9_DESC_E", cDesc)        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SearchBrowse(f"D MG    {cPortal}", "Filial+portal")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("AI9_PORTAL", cPortal)
        self.oHelper.CheckResult("AI9_DESCRI", cDesc)
        self.oHelper.CheckResult("AI9_DESC_S", cDesc)
        self.oHelper.CheckResult("AI9_DESC_E", cDesc)
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()