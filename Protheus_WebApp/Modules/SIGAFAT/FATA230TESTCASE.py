from tir import Webapp 
import unittest
from datetime import datetime 
DateSystem = datetime.today().strftime("%d/%m/%Y")

class FATA230(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "D RJ 01 ", "05")
        self.oHelper.Program("FATA230") 

    def test_FATA230_CT001(self):
        cWs = "FTC001"
        cDesc = "CT001 - INCLUSAO"
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D RJ 01 ")
        self.oHelper.WaitShow("Web Services - INCLUIR")
        self.oHelper.SetValue("AI7_WEBSRV", cWs)
        self.oHelper.SetValue("AI7_DESCRI", cDesc)     
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SearchBrowse(f"D RJ    {cWs}", "Filial+codigo WS")        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("AI7_WEBSRV", cWs)
        self.oHelper.CheckResult("AI7_DESCRI", cDesc)
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()