from tir import Webapp
import unittest
import time


class GTPA802(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '07/10/2020', 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA802')

    def test_GTPA802_CT001(self):
        print("test_GTPA802_CT001 - Visualizar")        
        self.oHelper.SetButton('Vizualização')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA802_CT002(self):
        print("test_GTPA802_CT001 - Alteração")        
        self.oHelper.SetButton('Alteração')
        self.oHelper.SetValue('Status', '1')
        self.oHelper.SetButton('Confirmar')        
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
