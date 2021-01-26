from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA552
#
#@author hebert.santos
#@since 11/12/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------

class MATA552(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAEST", "12/12/2019", "T1", "D MG 01 ", "04")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA552")

    def test_MATA552_001(self):

        self.oHelper.AddParameter("MV_GRADE", "", "T", "T", "T")
        self.oHelper.SetParameters()

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetButton("OK")

        self.oHelper.SetValue("Prod. Refer.", "ESTSE00000000000000000003")
        self.oHelper.SetValue("Cod. Curva", "0001")
        self.oHelper.SetValue("Cod. Curva", "0001")

        self.oHelper.SetValue("Quantidade", "1,00", grid=True, grid_number=0)
        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        time.sleep(5)

        self.oHelper.AssertTrue()
    
    def test_MATA552_002(self):

        self.oHelper.SearchBrowse("D MG 01 ESTSE00000000000000000004 0001")
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("Descricao", "ALTERADO")

        self.oHelper.SetValue("Quantidade", "2,00", grid=True, grid_number=0)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")
        time.sleep(5)

        self.oHelper.AssertTrue()


    def test_MATA552_003(self):

        self.oHelper.SearchBrowse("D MG 01 ESTSE00000000000000000004 0001")
        self.oHelper.SetButton("Outras Ações", "Excluir")

        self.oHelper.SetButton("Confirmar")
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
