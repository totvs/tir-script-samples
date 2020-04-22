from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')
import unittest
import time


class TMSA440(unittest.TestCase):
    
    cDUE_CODSOL = ''
    
    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGATMS",DateSystem,"T1","M SP 01 ","43")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("TMSA440")

    def test_TMSA440_001(self):
        '''
        Test Case 001
        '''

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01 ")

        self.oHelper.SetValue("DUE_CODCLI","TMS001")
        self.oHelper.SetValue("DUE_LOJCLI","01")
        
        self.oHelper.ClickFolder("Coleta")
        self.oHelper.SetValue("DUE_TIPTRA","1")

        self.oHelper.SetValue("DVJ_CODPRO", "TMS-DIVERSOS000000000000000000", grid=True)
        self.oHelper.SetValue("DVJ_CODEMB", "CX", grid=True)

        global cDUE_CODSOL

        cDUE_CODSOL = self.oHelper.GetValue("DUE_CODSOL")

        print(self.cDUE_CODSOL)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_TMSA440_002(self):

        order = '000000007'

        self.oHelper.SearchBrowse(f"M SP    {order}", "Filial+cod. Solicit")
        
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("DUE_END","RUA DAS FLORES, 1000")
        self.oHelper.SetValue("DUE_BAIRRO","MONTE ALTO ALEGRE")

        self.oHelper.SetValue("DVJ_CODPRO", "TMS-DIVERSOS000000000000000000", grid=True)
        self.oHelper.SetValue("DVJ_CODEMB", "CX", grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_TMSA440_003(self):

        global cDUE_CODSOL

        self.oHelper.SearchBrowse(f"M SP    {cDUE_CODSOL}", "Filial+cod. Solicit")

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()