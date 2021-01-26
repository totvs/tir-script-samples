from tir import Webapp
import unittest

class GFEC061(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "23/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC061")

    def test_GFEC061_CT001(self):
        
        self.oHelper.SetButton('Cancelar')

        self.oHelper.ClickTree('Tabelas')

        self.oHelper.SetButton('Sair')
       
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
