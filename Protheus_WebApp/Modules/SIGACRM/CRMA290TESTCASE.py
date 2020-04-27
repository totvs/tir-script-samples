from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest

class CRMA290(unittest.TestCase):
    Contr = ""

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.SetTIRConfig(config_name="User", value="APICRM")
        inst.oHelper.SetTIRConfig(config_name="Password", value="1")
        inst.oHelper.Setup("SIGACRM", DataSystem,"T1","D MG 01 ","73")
        inst.oHelper.Program("CRMA290")

    def test_CRMA290_CT001(self):
        self.oHelper.ClickLabel("+ Criar Oportunidade")
        NumOpt = self.oHelper.GetValue("AD1_NROPOR")
        self.oHelper.SetValue("AD1_DESCRI", "INCLUSAO TIR AT")
        self.oHelper.SetValue("AD1_DTINI",DataSystem)
        self.oHelper.SetValue("AD1_CODCLI","FATT01")
        self.oHelper.SetValue("AD1_LOJCLI","01")
        self.oHelper.SetValue("AD1_PROVEN","FAT001")
        self.oHelper.SetValue("AD1_STAGE","000002")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Minhas Oportunidades")      
        self.oHelper.ClickLabel("Minhas Oportunidades")   
        self.oHelper.WaitHide("Minhas Oportunidades")
        self.oHelper.SearchBrowse(f"D MG 01 {NumOpt}")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("AD1_NROPOR", NumOpt)
        self.oHelper.CheckResult("AD1_DESCRI", "INCLUSAO TIR AT")
        self.oHelper.CheckResult("AD1_CODCLI","FATT01")
        self.oHelper.CheckResult("AD1_LOJCLI","01")
        self.oHelper.CheckResult("AD1_PROVEN","FAT001")
        self.oHelper.CheckResult("AD1_STAGE","000002")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()