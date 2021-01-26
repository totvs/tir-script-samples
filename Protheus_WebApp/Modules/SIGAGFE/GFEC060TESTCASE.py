from tir import Webapp
import unittest

class GFEC060(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "22/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC060")

    def test_GFEC060_CT001(self):

        self.oHelper.SearchBrowse("CTRC                ")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("GV2_CDCOMP", "CTRC                ")
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
