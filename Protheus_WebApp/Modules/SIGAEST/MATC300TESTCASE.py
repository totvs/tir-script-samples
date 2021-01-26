from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc}  MATC300 - DIAGNOSTICO BLOCO K
#
#@author ADRIANO VIEIRA
#@since 16/09/2019
#@version 1.0
#/*/
#//-------------------------------------------------------------------
class MATC300(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAEST","01/04/2018","T1","D MG 01 ","04")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATC300")

    def test_MATC300_001(self):
        
        #Contempla os CT001 e CT002
        #MATC300 - CT001: Amarração de Produto - TIR
        #MATC300 - CT002: Estoque Negativo - TIR

        self.oHelper.SetValue("MV_PAR01", "Mar")
        self.oHelper.SetValue("MV_PAR02","2018")

        self.oHelper.SetButton("Processar")
        time.sleep(38)

        self.oHelper.ClickLabel("Sair")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()