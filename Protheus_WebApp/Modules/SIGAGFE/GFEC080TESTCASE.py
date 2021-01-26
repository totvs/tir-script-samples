from tir import Webapp
import unittest

class GFEC080(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "30/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC080")
           
    def test_GFEC080_CT001(self):
               
        self.oHelper.SetButton('Visualizar')

        self.oHelper.SetButton('Fechar')        
       
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()