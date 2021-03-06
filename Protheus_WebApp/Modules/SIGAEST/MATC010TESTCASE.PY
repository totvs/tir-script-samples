from tir import Webapp
import unittest

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATC010 - Consulta Geral ao Produto
#TABELA SB1
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 09/03/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATC010(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAEST","04/07/2019","T1","D MG 01 ","04")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATC010")

    def test_MATC010_001(self):
        self.oHelper.AddParameter("MV_REVPLAN", "", "T", "T", "T")
	
        self.oHelper.SetParameters()

        self.oHelper.WaitShow("Formacao de Precos")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue('Mostra ?', 'Estrutura')
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse('D MG 01 ESTSE0000000000000000000000145')

        self.oHelper.SetButton("Forma Precos")
 
        self.oHelper.ClickGridCell("Niv", 2)

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetValue('Codigo','ESTSE0000000001')
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Recalculo")
        self.oHelper.SetButton("Custo")
        self.oHelper.SetButton("Ok")

        self.oHelper.ClickGridCell("Niv", 2)
        self.oHelper.SetButton("Excluir")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Editar")

        self.oHelper.SetValue('Quantidade','11,000000')
        self.oHelper.SetButton("Ok")

        self.oHelper.ClickGridCell("Niv", 2)

        self.oHelper.SetButton("Editar")

        self.oHelper.SetValue('Quantidade','11,000000')
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Planilha")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetValue('Codigo do Produto:','ESTSE0000000000000000000000145')
        self.oHelper.SetButton("Pesquisar")

        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_MATC010_002(self):
        
        self.oHelper.WaitShow("Formacao de Precos")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue('Mostra ?', 'Pre-Estrutura')
        self.oHelper.SetValue('Selec. Opcionais do Produto ?', 'Sim')
        self.oHelper.SetButton("Ok")
        self.oHelper.SearchBrowse('D MG 01 ESTSE0000000000000000000000941')
        self.oHelper.SetButton("Forma Precos")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
       
    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()