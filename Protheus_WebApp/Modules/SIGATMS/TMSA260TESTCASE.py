from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')
import unittest
import time


class TMSA260(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGATMS",DateSystem,"T1","M SP 03 ","43")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("TMSA260")

    def test_TMSA260_001(self):
        '''
        Test Case 001
        '''

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 03 ")

        self.oHelper.SetValue("DTZ_CODROD","TMS001")
        self.oHelper.SetValue("DTZ_NOMROD","CASTELO BRANCO")
        
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_TMSA260_002(self):

        order = 'TMS001'

        self.oHelper.SearchBrowse(f"M SP    {order}", "Filial+cod. Rodovia")
        
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("DTZ_NOMROD","RAPOSO TAVARES")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_TMSA260_003(self):

        order = 'TMS001'

        self.oHelper.SearchBrowse(f"M SP    {order}", "Filial+cod. Rodovia")

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