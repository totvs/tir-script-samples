from tir import Webapp
import unittest
import time
#//-------------------------------------------------------------------
#@author Squad Entradas
#@since 16/11/2020
#@version 1.0
#/*/
#//-------------------------------------------------------------------
class TECA470(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGATEC","16/11/2020","T1","D MG 01")
        inst.oHelper.Program("TECA470")

    def test_TECA470_001(self):
        #Definição dos perguntes iniciais
        self.oHelper.SetButton("Visualizar")

        time.sleep(2)
        self.oHelper.ClickGridCell("Quantidade", 1)
        self.oHelper.SetKey("F4")

        self.oHelper.SetButton('X')
        time.sleep(1)
        self.oHelper.SetKey("F4")
        time.sleep(1)
        self.oHelper.SetButton("OK")
        time.sleep(1)
        self.oHelper.SetButton("OK")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()