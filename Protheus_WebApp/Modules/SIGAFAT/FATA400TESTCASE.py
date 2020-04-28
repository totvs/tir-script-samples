from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest

class FATA400(unittest.TestCase):
    Contr = ""

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAFAT", DataSystem,"T1","D MG 01 ","05")
        inst.oHelper.Program("FATA400")

    def test_FATA400_CT001(self):
        global Contr

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")

        Contr = self.oHelper.GetValue("ADA_NUMCTR")
        self.oHelper.SetValue("ADA_NUMCTR", Contr)
        self.oHelper.SetValue("ADA_EMISSA","04/07/2019")
        self.oHelper.SetValue("ADA_CODCLI","000001")
        self.oHelper.SetValue("ADA_LOJCLI","01")
        self.oHelper.SetValue("ADA_CONDPG","000")
        self.oHelper.SetValue("ADB_CODPRO", "FAT000000000000000000000000001", grid=True)
        self.oHelper.SetValue("ADB_QUANT", "1,00", grid=True)
        self.oHelper.SetValue("ADB_PRCVEN", "1,00", grid=True)
        self.oHelper.SetValue("ADB_TES", "501", grid=True)
        self.oHelper.SetValue("ADB_TESCOB", "503", grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")   
        self.oHelper.SearchBrowse(f"D MG 01 {Contr}", "Filial+contrato N.")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("ADA_NUMCTR", Contr)
        self.oHelper.CheckResult("ADA_CODCLI","000001")
        self.oHelper.CheckResult("ADA_LOJCLI","01")
        self.oHelper.CheckResult("ADA_CONDPG","000")
        self.oHelper.CheckResult("ADB_CODPRO", " FAT000000000000000000000000001", grid=True, line=1)
        self.oHelper.CheckResult("ADB_QUANT", "1,00", grid=True, line=1)
        self.oHelper.CheckResult("ADB_PRCVEN", "1,00", grid=True, line=1)
        self.oHelper.CheckResult("ADB_TES", "501", grid=True, line=1)
        self.oHelper.CheckResult("ADB_TESCOB", "503", grid=True, line=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
