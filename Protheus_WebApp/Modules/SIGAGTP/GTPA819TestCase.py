from tir import Webapp
import unittest
import time


class GTPA819(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '19/11/2020', 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA819')

   
    def test_GTPA819_CT001(self):
        print("test_GTPA819_CT001 - Incluir")   
        self.oHelper.SetButton('Incluir')      
        self.oHelper.SetButton('OK') 
        self.oHelper.SetButton("Outras Ações", "Pesquisar")        
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()       

   
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
