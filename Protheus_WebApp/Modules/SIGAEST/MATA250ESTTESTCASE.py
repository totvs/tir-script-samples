#//-------------------------------------------------------------------
#@author Squad Entradas 
#@since 20/11/2020
#@version 1.00
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA250(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAEST','20/11/2020','T1','D MG 01')
        inst.oHelper.Program('MATA250')		

    def test_MATA250EST_CT001(self):

        self.oHelper.AddParameter("MV_DIGIPER", "", "S", "S", "S")
        self.oHelper.SetParameters()

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
		
        self.oHelper.SetValue('TP Movimento','011')
        self.oHelper.SetFocus("Ord Producao")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse("pcpA79")
        self.oHelper.SetButton("Ok")
        time.sleep(3)
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetValue('Quantidade',"5,00")
        self.oHelper.SetValue('Perda',"1,00")
        time.sleep(3)

        #Grid
        self.oHelper.SetButton("X")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()