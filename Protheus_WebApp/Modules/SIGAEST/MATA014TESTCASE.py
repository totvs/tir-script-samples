from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA014 - Endereço Fisico
#TABELA SBE
#
#@author hebert.santos
#@since 14/11/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------


class MATA014(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAEST", "", "T1", "D MG 01 ", "04")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA014")

    def test_MATA014_001(self):

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton("OK")        
       
        self.oHelper.SetValue('Produto', 'ESTSE0000000000000000000000366')
        self.oHelper.ClickGridCell("Usuário",1 )
        self.oHelper.SetValue('Usuário', '000000', grid=True)
        self.oHelper.SetValue('Documento', 'MTA103', grid=True)
        self.oHelper.SetValue('Inclui', True, grid=True)
        self.oHelper.SetValue('Exclui', True, grid=True)
        self.oHelper.SetValue('Altera', True, grid=True)
        self.oHelper.LoadGrid()
    
        self.oHelper.SetButton("Outras Ações","Cad. Produto")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Outras Ações","Pesquisar")
        self.oHelper.SetButton("Cancela")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
