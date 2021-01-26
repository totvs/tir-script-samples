from tir import Webapp
import unittest

class GFEX003(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "28/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEX003")

    def test_GFEX003_CT001(self):   
                
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()      
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
