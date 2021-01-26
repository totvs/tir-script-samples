from tir import Webapp
import unittest

class GFEC065(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "22/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC065")

    def test_GFEC065_CT001(self):

        self.oHelper.SearchBrowse("D MG 01 ICMS 300           1    300003          ")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("GW3_NRDF", "300003          ")   

        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Conferencia")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
