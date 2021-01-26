from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA120 - Pedido de Compra
#@author Leandro Nishihata
#@since 01/05/2020
#@version P12
#//-------------------------------------------------------------------

class MATA120(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACOM","01/01/2020","T1","D MG 01 ","02")
        inst.oHelper.Program("MATA121")

    # CRUD PEDIDO DE COMPRA
    def test_MATA120_001(self):

        pc1 = 'COMTI1'
        loj1 = '01'
                       
        #Inclusão de PC com rateio vinculado a uma SC        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.WaitShow("Pedido de Compra - INCLUIR")
        self.oHelper.SetValue("Numero", pc1)
        self.oHelper.F3(field='Fornecedor', name_attr=False,send_key=True)
        self.oHelper.SearchBrowse(f'000003', 'Código')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetValue("Loja", loj1) 
        self.oHelper.F3(field='Cond. Pagto', name_attr=False,send_key=True)
        self.oHelper.SearchBrowse(f'000', 'Código')
        self.oHelper.SetButton("Ok")        
        self.oHelper.SetFocus("Produto", grid_cell = True)
        self.oHelper.SetKey("F3",grid=True)
        self.oHelper.SearchBrowse(f'COMTIR1', 'Código')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton('Outras Ações','Solicit.')
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton('Outras Ações','Sol./Item')
        self.oHelper.WaitShow("Pedido de Compra - INCLUIR")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetValue("C7_PRECO",'10,00',grid=True,grid_number=1) 
        self.oHelper.LoadGrid()

        #Adiciona o rateio
        self.oHelper.SetButton('Outras Ações','Rateio')
        self.oHelper.WaitShow("Pedido de Compra - INCLUIR")
        #Linha 1
        self.oHelper.SetFocus("C. de Custo", grid_cell = True)
        self.oHelper.SetKey("F3",grid=True)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetValue("CH_PERC",'100,00',grid=True,grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitShow("Pedido de Compra - INCLUIR")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

        #Excluir PC com rateio 
        self.oHelper.SearchBrowse(f"D MG 01 {pc1}", "Filial+numero Pc")       
        self.oHelper.SetButton('Outras Ações','Excluir')        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
    
    #-------------------------------------------------------------------
    #/*/{Protheus.doc} test_MATA120_002
    #Caso de Teste CT002WEB - Alterar pedido de compra, importar SC para pedido que já possui uma SC de mesmo número importada.

    #@author juan.felipe
    #@since 17/11/2020
    #@version 1.0
    #@kanoah: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/214513
    #/*/
    #-------------------------------------------------------------------
    def test_MATA120_002(self):

        pc1 = 'COMTI2'
        self.oHelper.SearchBrowse(f"D MG 01 {pc1}", "Filial+numero Pc")       
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetButton('Outras Ações','Solicit.')
        self.oHelper.WaitShow("Pedido de Compra - ALTERAR")

        #Pesquisa SC
        self.oHelper.SetButton('Outras Ações','Pesquisar')
        self.oHelper.SetButton('Parâmetro')
        self.oHelper.SetValue('Filial', 'D MG 01')
        self.oHelper.SetValue('Numero da SC', pc1)
        self.oHelper.SetButton('Ok')

        #Seleciona SC
        self.oHelper.ClickLabel(' ') #Marca e desmarca todas as SCs apenas para dar foco no Grid
        self.oHelper.ClickLabel(' ')
        self.oHelper.SetKey("ENTER", grid=True)
        self.oHelper.SetButton("Salvar")

        #Confirma importação de SC já importada para o PC
        self.oHelper.SetButton("Sim")

        #Veifica C7_ITEM linha 1
        self.oHelper.CheckResult("C7_ITEM", '0001', grid=True, line=1, grid_number=1)	
        self.oHelper.LoadGrid()
        
        #Preenche C7_PRECO linha 2
        self.oHelper.ClickGridCell("C7_PRECO", row=2, grid_number=1)
        self.oHelper.SetValue("C7_PRECO",'100,00', grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        #Verifica C7_ITEM linha 2
        self.oHelper.CheckResult("C7_ITEM", '0002', grid=True, line=2, grid_number=1)
        self.oHelper.LoadGrid()

        #Salva PC
        self.oHelper.SetButton("Salvar")

        self.oHelper.AssertTrue()

    #-------------------------------------------------------------------
    #/*/{Protheus.doc} test_MATA120_002
    #Caso de Teste CT003WEB - Copia de pedido com condição de pagamento bloqueado

    #@author Leandro Nishihata
    #@since 27/11/2020
    #@version 1.0
    #@kanoah: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/214513
    #/*/
    #-------------------------------------------------------------------
    def test_MATA120_003(self):

        pc1 = 'PMSACA'
        #Excluir PC com rateio 
        self.oHelper.SearchBrowse(f"D MG 01 {pc1}", "Filial+numero Pc")       
        self.oHelper.SetButton('Outras Ações','Copia')        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.CheckHelp(text_help="REGBLOQ", button="Fechar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()
        
if __name__ == '__main__':
	unittest.main()