from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest

class PMSA100(unittest.TestCase):
    Contr = ""

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAPMS", DataSystem,"T1","D MG 01 ","44")
        inst.oHelper.Program("PMSA100")

    def test_PMSA100_CT001(self):
        NumOrc = "TIR0000001"

        self.oHelper.SetButton("Outras Ações","Legenda")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("AF1_ORCAME", NumOrc)
        self.oHelper.SetValue("AF1_DESCRI",'INCLUSAO TIR')
        self.oHelper.SetValue("AF1_VALID", DataSystem)
        self.oHelper.SetValue("AF1_CLIENT","FAT001")
        self.oHelper.SetValue("AF1_LOJA","01")
        self.oHelper.SetValue("AF1_TPORC","0001")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SearchBrowse(f"D MG 01 {NumOrc}")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("AF1_ORCAME", NumOrc)
        self.oHelper.CheckResult("AF1_DESCRI",'INCLUSAO TIR')
        self.oHelper.CheckResult("AF1_VALID", DataSystem)
        self.oHelper.CheckResult("AF1_CLIENT","FAT001")
        self.oHelper.CheckResult("AF1_LOJA","01")
        self.oHelper.CheckResult("AF1_TPORC","0001")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
