from tir import Webapp
import unittest

class GFEC032(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "22/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC032")

    def test_GFEC032_CT001(self):

        self.oHelper.SearchBrowse("D MG 01 00000002")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("GWD_NROCO", "00000002")
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
