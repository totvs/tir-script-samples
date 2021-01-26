from tir import Webapp
import unittest
import time


class GTPR019(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '19/11/2020', 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA422')

   
    def test_GTPR019_CT001(self):
        print("test_GTPR019_CT001 - Visualizar")   
        self.oHelper.SetButton('Visualizar')    
        self.oHelper.SetButton("Outras Ações", "Imprimir DAPE")    
        self.oHelper.SetButton('Imprimir')        
        self.oHelper.SetButton('Sair')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()       

   
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
