from tir import Webapp
import unittest

class CNTA121(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGCT','09/12/2020','T1','D MG 02 ','69')
        inst.oHelper.Program('CNTA121')
    
    #==========================================================================
    # CT001 - Inclusão de contrato com cronograma financeiro, físico e contábil
    #==========================================================================
    def test_CNTA121_001(self):
        data = '09/12/2020'
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 02')
                
        #Cabecalho da medicao (Aba cadastrais)
        self.oHelper.SetValue('CND_CONTRA', 'CNTA121TIRCT001')
        
        #Selecionar planilha 000001
        self.oHelper.ClickFolder('Planilhas')
        self.oHelper.SetValue('CXN_CHECK', True, grid=True)
        self.oHelper.LoadGrid()

        #Gravacaoo do registro
        self.oHelper.SetButton('Confirmar')
       
        #Fechamento da mensagem "registro incluído com sucesso"
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('Outras Ações', sub_item='Visualizar')
        
        self.oHelper.SetButton('Fechar')

    #=======================================================================================
    # CT002 - Encerra, Alterar, Visualizar, Estornar e excluir medição inclusao pelo CNTA121
    #=======================================================================================
        # Pesquisar contrato
        self.oHelper.SearchBrowse("D MG 02", key=2, index=True)
        self.oHelper.SearchBrowse("D MG 02 CNTA121TIRCT002")

        # Alterar. Inclusão rateio
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetButton('Outras Ações', sub_item='Rateio')
        self.oHelper.SetValue("CNZ_PERC",'100,00',grid=True,grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetValue('CNZ_CC', 'CCHONDA1',grid=True,grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Salvar')
        
        # Encerrar
        self.oHelper.SetButton('Outras Ações', sub_item='Encerrar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Ok')

        # Visualizar
        self.oHelper.SetButton('Outras Ações', sub_item='Visualizar')
        self.oHelper.SetButton('Confirmar')

        # Estornar
        self.oHelper.SetButton('Outras Ações', sub_item='Estornar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Ok')

        # Excluir
        self.oHelper.SetButton('Outras Ações', sub_item='Excluir')
        self.oHelper.SetButton('Confirmar')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()