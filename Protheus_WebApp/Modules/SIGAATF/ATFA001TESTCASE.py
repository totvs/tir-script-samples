from tir import Webapp
import unittest


class ATFA001(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAATF", "30/06/2020", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA001")

# ==================================================================================
#  Teste Exploratório abertura de tela
# ==================================================================================
    def test_ATFA001_001(self):
        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
        # self.oHelper.SetButton("X")
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
