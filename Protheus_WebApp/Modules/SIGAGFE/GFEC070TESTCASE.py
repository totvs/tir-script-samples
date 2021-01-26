from tir import Webapp
import unittest

class GFEC070(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "22/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC070")

    def test_GFEC070_CT001(self):

        self.oHelper.SetButton("Visualizar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Detalhe Conf.")
        
        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
