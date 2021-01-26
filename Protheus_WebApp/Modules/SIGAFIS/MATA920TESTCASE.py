from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')


class MATA920(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()
        DateSystem = datetime.today()
        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAADV", DateSystem.strftime('%d/%m/%Y'), "T1", "X FIS01", "09")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA920")

    def test_MATA920_001(self):
        '''
        Test Case 001
        '''

        self.oHelper.SearchBrowse("X FIS01 000776", 3, index=True)
        self.oHelper.SetButton('Outras Ações', 'Complementos')
        self.oHelper.ClickTree('Armas de fogo')
        self.oHelper.ClickTree('Combustível')
        self.oHelper.ClickTree('Comunicação e telecomunicação')
        self.oHelper.ClickTree('Energia elétrica')
        self.oHelper.ClickTree('Gás canalizado')
        self.oHelper.ClickTree('Importação')
        self.oHelper.ClickTree('Medicamentos')
        self.oHelper.ClickTree('Veículos automotores')
        self.oHelper.ClickTree('Exportação')
        self.oHelper.ClickTree('Anfavea (Cabeçalho)')
        self.oHelper.ClickTree('Anfavea (Itens)')
        self.oHelper.ClickTree('Compl. Ressarc')
        self.oHelper.ClickTree('Rastreabilidade')

        self.oHelper.ClickTree('Processos referenciados')
        self.oHelper.ClickTree('Guias de recolhimento')
        self.oHelper.ClickTree('Documentos fiscais')
        self.oHelper.ClickTree('Cupons fiscais')
        self.oHelper.ClickTree('Locais de coleta e entrega')
        self.oHelper.ClickTree('Informações Complementares')
        self.oHelper.ClickTree('Crédito Acumulado de ICMS')

        self.oHelper.SetButton('Salvar')
        
        self.oHelper.AssertFalse()

    def test_MATA920_002(self):
        '''
        Test Case 002
        '''

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('X FIS01')

        self.oHelper.SetValue('c920Nota', '999999999', name_attr=True)   
        self.oHelper.SetValue('c920Serie', '999', name_attr=True)
        self.oHelper.SetValue('d920Emis', '12/03/2019', name_attr=True)
        self.oHelper.SetValue('c920Client', '000001', name_attr=True)
        self.oHelper.SetValue('c920Loja', '01', name_attr=True)        
        self.oHelper.SetValue('c920Especi', 'SPED', name_attr=True)

        self.oHelper.SetValue('Produto', 'FIS000000000000000000000000001', grid=True)
        self.oHelper.SetValue('Quantidade', '1,00', grid=True)
        self.oHelper.SetValue('Vlr.Unitario', '100,00', grid=True)
        self.oHelper.SetValue('Vlr.Total', '100,00', grid=True)
        self.oHelper.SetValue('Tipo Saida', '501', grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetKey("DELETE", grid=True)

        self.oHelper.LoadGrid()        

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()        
if __name__ == '__main__':
    unittest.main()