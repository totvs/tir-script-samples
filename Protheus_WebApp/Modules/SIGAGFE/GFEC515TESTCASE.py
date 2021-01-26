from tir import Webapp
import unittest

class GFEC515(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "25/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC515")

    def test_GFEC515_CT001(self):   
                        
        self.oHelper.SetButton('X')
                  
        self.oHelper.AssertTrue()      
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
