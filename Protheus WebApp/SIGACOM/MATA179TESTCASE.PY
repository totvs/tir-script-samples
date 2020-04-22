from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA179 - Centrao de Compras
#TABELA SF1. SD1
#
#@author LEANDRO NISHIHATA
#@since 18/12/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATA179(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGACOM","18/12/2019","T1","D MG 01 ","02")

       
        inst.oHelper.Program("MATA179")
    # Gera sugestão de compra
    def test_MATA179_001(self):

        self.oHelper.SetButton('Gerar Sugestão')
        self.oHelper.SetValue("DBJ_FILDIS", "D MG 01")
        self.oHelper.SetValue("DBJ_DTDE","01/01/2019")
        self.oHelper.SetValue("DBJ_DTATE","30/12/2019")
        self.oHelper.SetValue("DBJ_DIASCO","30")
        self.oHelper.SetButton("Confirmar")
        time.sleep(2)
        self.oHelper.SetButton("Sim")
        time.sleep(2)
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton('Outras Ações','efetivar')
        time.sleep(2)
        self.oHelper.SetButton("Sim")
        time.sleep(5)
        self.oHelper.AssertTrue()
    
    
    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

    # efetiva sugestão de compra
    #def test_MATA179_001(self):


        
    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()