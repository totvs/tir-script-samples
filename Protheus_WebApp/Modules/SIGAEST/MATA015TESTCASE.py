from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA015 - Endereço Fisico
#TABELA SBE
#
#@author JEFFERSON SILVA DE SOUSA
#@since 13/09/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATA015(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAEST","13/09/2019","T1","D MG 01 ","04")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA015")

         #Visualizar grafico de ocupaçao de endereço
    def test_MATA015_001(self):       
        
        self.oHelper.SetButton('Outras Ações','ocupacao')        

        self.oHelper.SetValue("Armazem De ?", '')
        self.oHelper.SetValue("Armazem Ate ?",'ZZ')
        self.oHelper.SetValue("Zona de Armaz. De ?",'')
        self.oHelper.SetValue("Zona de Armaz. Ate ?",'ZZZZ')
        self.oHelper.SetValue("Estrut. Fisica De ?",'')
        self.oHelper.SetValue("mv_par06",'ZZZZZ')
        self.oHelper.SetValue("Endereco De ?",'')
        self.oHelper.SetValue("Endereco Ate",'ZZZZZ')        

        self.oHelper.SetButton("OK")
        time.sleep(5)
        self.oHelper.SetButton("OK")       

        self.oHelper.AssertTrue()

    #VISUALIZAÇAO DE PRODUTO 
    def test_MATA015_002(self):
         filial   = "D MG 01 "
         endereco = "ESTSE002"

         self.oHelper.SearchBrowse(f"{filial}{endereco}", "Filial+endereco")

         self.oHelper.SetButton('Visualizar')
         time.sleep(3)
         self.oHelper.SetButton('Fechar')
         
         self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()