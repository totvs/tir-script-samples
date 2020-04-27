from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')
import unittest

class TMSA440(unittest.TestCase):
    
    cDUE_CODSOL = ''
    
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGATMS",DateSystem,"T1","M SP 01 ","43")
        inst.oHelper.Program("TMSA440")

    def test_TMSA440_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01 ")
        self.oHelper.SetValue("DUE_CODCLI","TMS001")
        self.oHelper.SetValue("DUE_LOJCLI","01")
        self.oHelper.ClickFolder("Coleta")
        self.oHelper.SetValue("DUE_TIPTRA","1")
        self.oHelper.SetValue("DVJ_CODPRO", "TMS-DIVERSOS000000000000000000", grid=True)
        self.oHelper.SetValue("DVJ_CODEMB", "CX", grid=True)
       
        global cDUE_CODSOL
        cDUE_CODSOL = self.oHelper.GetValue("DUE_CODSOL")
        print(self.cDUE_CODSOL)

        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()