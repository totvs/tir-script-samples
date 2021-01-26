from tir import Webapp
import time
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class CRMA110(unittest.TestCase):

    @classmethod
    def setUpClass(self):   
        self.oHelper = Webapp()        
        self.oHelper.Setup('SIGACRM', DateSystem, 'T1', 'D MG 01 ', '73')
        self.oHelper.Program('CRMA110')

    def test_CRMA110_CT001(self):
        '''
        Test Case CT001 - Oportunidade de Venda - Acessar a opção Privilégios (CRM)
        '''

        self.oHelper.SearchBrowse(f"D MG 01 000299", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton('Outras Ações','Relacionadas, Privilégios')
        self.oHelper.WaitShow('Privilégios do Registro - Alterar')
        self.oHelper.CheckResult('Entidade', 'AD1')
        self.oHelper.CheckResult('Nome', 'OPORTUNIDADES DE VENDA')
        self.oHelper.CheckResult('Descrição', '000299 | TIR - CRMA110 - CT001')
        self.oHelper.ClickFolder('Usuários do CRM')
        self.oHelper.CheckResult('Usuário', '000000', grid=True, line=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case. 
        """
        self.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main() 