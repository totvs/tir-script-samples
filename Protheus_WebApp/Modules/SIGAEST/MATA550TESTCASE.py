from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA550 - Inclusão e Visualização de Produto
#TABELA SB4
#
#@author Jefferson silva de sousa 
#@since 20/09/2010
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATA550(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()
      
        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAEST","20/09/2019","T1","D MG 01 ","04")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA550")

    def test_MATA550_001(self):
        
        #Incluir
        cod     =  'ESTSEGRADE01'
        desc    =  'MATA550TIR'
        tipo    =  'PA'
        unidade =  'UN'
        armazem =  '01'
        linha   =  '12'
        coluna  =  '13'

        self.oHelper.SetButton("Incluir")
        time.sleep(1)

        self.oHelper.SetButton("OK")

        self.oHelper.SetValue("Codigo", cod)
        self.oHelper.SetValue("Descricao", desc)
        self.oHelper.SetValue("Tipo", tipo)
        self.oHelper.SetValue("Unidade", unidade)
        self.oHelper.SetValue("Armazem Pad.", armazem)
        self.oHelper.SetValue("Tabela Linha", linha)
        self.oHelper.SetValue("Tabela Colun", coluna)

        self.oHelper.ClickFolder("E-Commerce")

        self.oHelper.SetValue("Título ", desc)
           
        
        self.oHelper.SetButton("Salvar")
        time.sleep(2)
        self.oHelper.SetKey("RIGHT", grid=True)        
        self.oHelper.SetValue("[01] PRETO", "X", grid=True,row=1)
        self.oHelper.LoadGrid() 

        self.oHelper.SetButton("Salvar")
        time.sleep(2)
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_MATA550_002(self):
        
        #VISUALIZAR
        cod     =  'ESTSEGRADE01'
        filial   = 'D MG    '
        desc    =  'MATA550TIR'

        self.oHelper.SearchBrowse(f"{filial}{cod}", "Filial+Codigo")       

        self.oHelper.SetButton("Visualizar")
        time.sleep(1)
        self.oHelper.SetFocus("B4_DESC")
        time.sleep(1)
        self.oHelper.CheckResult("B4_DESC", desc)
        self.oHelper.CheckResult("[01] PRETO","X",grid=True,line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_MATA550_003(self):
        
        #Alterar
        cod     =  'ESTSEGRADE01'        
        desc    =  'mata550 tir alt'        
        filial   = 'D MG    '

        self.oHelper.SearchBrowse(f"{filial}{cod}", "Filial+Codigo")       

        self.oHelper.SetButton("Alterar")
        time.sleep(1)

        self.oHelper.CheckResult("B4_COD", cod)

        self.oHelper.SetValue("Descricao", desc)
        self.oHelper.SetButton("Salvar")
        time.sleep(1)
        self.oHelper.SetButton("Salvar")
        self.oHelper.AssertTrue()                

    def test_MATA550_004(self):
        
        #Excluir
        cod     =  'ESTSEGRADE01'        
        filial   = 'D MG    '

        self.oHelper.SearchBrowse(f"{filial}{cod}", "Filial+Codigo")       

        self.oHelper.SetButton('Outras Ações','Excluir')
        time.sleep(1)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()                

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()