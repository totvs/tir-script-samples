from tir import Webapp
import unittest

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATC050 - Consulta Geral ao Produto
#TABELA SB1
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 09/03/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATC050(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereco do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializacao
        inst.oHelper.Setup("SIGAEST","04/07/2019","T1","D MG 01 ","04")

       #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATC050")

    def test_MATC050_001(self):
        #Consulta
        cod = 'ESTSE0000000000000000000000327'
        self.oHelper.SetButton("Ok")
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton("Consulta")

        self.oHelper.ClickTree('Dados Cadastrais')
        self.oHelper.ClickTree('Dados Complementares ')
        self.oHelper.ClickTree('Amarracoes ')
        self.oHelper.ClickTree('Amarracoes > Produto X Fornecedor > EST001 / 01 - FORNECEDOR SQUAD ENTRADAS ')

        self.oHelper.ClickTree('Solicitacoes de Compra ')
        #self.oHelper.SetButton('Outras Ações', 'Expande')
        #self.oHelper.ClickTree('Solicitacoes de Compra > SOL125 / 0001')

        self.oHelper.ClickTree('Pedidos de Compra ')
        #self.oHelper.SetButton('Outras Ações', 'Expande')
        #self.oHelper.ClickTree('Pedidos de Compra > PMS540 / 0001 - EST001 / 01')

        self.oHelper.ClickTree('Empenhos ')

        self.oHelper.ClickTree('Ordens de Producao ')
        #self.oHelper.SetButton('Outras Ações', 'Expande')
        #self.oHelper.ClickTree('Ordens de Producao > pcpA1M01001')

        self.oHelper.ClickTree('Previsoes de Venda ')
        self.oHelper.SetButton('Outras Ações', 'Expande')
        self.oHelper.ClickTree('Previsoes de Venda > - 06/09/2019')

        self.oHelper.ClickTree('Pedidos de Venda ')
        self.oHelper.SetButton('Outras Ações', 'Expande')
        self.oHelper.ClickTree('Pedidos de Venda > pcpA11 / 01 - EST001 / 01')

        self.oHelper.ClickTree('Plano Mestre de Producao ')
        self.oHelper.SetButton('Outras Ações', 'Expande')
        self.oHelper.ClickTree('Plano Mestre de Producao > 06/09/2019')

        self.oHelper.ClickTree('Solicitacao ao Armazem ')
        self.oHelper.SetButton('Outras Ações', 'Expande')
        self.oHelper.ClickTree('Solicitacao ao Armazem > PMS040 / 01')


        self.oHelper.ClickTree('Pre-requisicao ')
        self.oHelper.SetButton('Outras Ações', 'Expande')
        self.oHelper.ClickTree('Pre-requisicao > PMS039 / 01')

        self.oHelper.ClickTree('Reserva para projetos ')
        self.oHelper.ClickTree('Tabela de Precos ')

        self.oHelper.ClickTree('Tabela de Precos dos Fornecedores ')
        self.oHelper.SetButton('Outras Ações', 'Expande')
        #self.oHelper.ClickTree('Tabela de Precos dos Fornecedores > Tabela - 1 Fornecedor - EST001 / 01 > 1 / 001')

        self.oHelper.ClickTree('Orcamento SIGALOJA ')
        self.oHelper.ClickTree('Orçamento de Venda ')
        self.oHelper.ClickTree('Solicitação de Transferência ')
        self.oHelper.ClickTree('MRP ')
        

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