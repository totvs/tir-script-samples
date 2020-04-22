from tir import Webapp
import unittest
from datetime import datetime
import string
import random

class PCOA170(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper =  Webapp()
        inst.oHelper.Setup('SIGAPCO', '08/04/2020', 'T1', 'D MG 02 ')
        inst.oHelper.Program('PCOA170')
        
    # Inclusao
    
    def test_PCOA170_CT001(self):

        codigoAKN01 = 'TIR'
        memoAKN01   = 'TESTE TIR - INCLUSAO'
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 02 ')

        self.oHelper.SetValue('AKN_CODIGO', codigoAKN01)
        self.oHelper.SetValue('AKN_DESCRI', memoAKN01)
        self.oHelper.SetValue('AKN_NMAX', '1'             )
        self.oHelper.SetValue('AKN_CONFIG', '001'    )
        self.oHelper.SetValue('AKN_MEMO', memoAKN01         )

        self.oHelper.SetButton('Salvar')    
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'D MG 02 {codigoAKN01}')
        self.oHelper.AssertTrue()

    # Alteracao
    
    def test_PCOA170_CT002(self):

        codigoAKN01 = '001'
        contaOrc    = '01'
        descricItem = 'VISAO GERENCIAL ORCAMENTARIA 001'

        self.oHelper.SearchBrowse(f'D MG 02 {codigoAKN01}')
        self.oHelper.SetButton('Alterar')
        
        # Abertura de Arvore e posicionando no segundo item 
        self.oHelper.ClickGridCell('Descricao', 2)
        
        # Clicar no Botao 'outras acoes'
        self.oHelper.SetButton('Outras ações', 'Estrut.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Incluir C.O.G.")

        self.oHelper.SetValue('AKO_CO', contaOrc )
        self.oHelper.SetValue('AKO_DESCRI', descricItem )
        self.oHelper.SetButton('Salvar')  
        
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SearchBrowse(f'D MG 02 {codigoAKN01}')
        self.oHelper.AssertTrue()

    # Alteracao com edicao de item de configuracao

    def test_PCOA170_CT003(self):

        codigoAKN01 = '002'
        memoAKN01   = 'VISAO GERENCIAL 002'
        codigoPlan  = 'PCO000001'
        versao      = '0001'
        contaOrcDe  = '01001'
        contaOrcAte = '01002'
        operacaoDe  = '0000000001'
        operacaoAte = '0000000002'

        self.oHelper.SearchBrowse(f'D MG 02 {codigoAKN01}')
        self.oHelper.SetButton('Alterar')

        # Abertura de Arvore e posicionando no segundo item 
        self.oHelper.WaitShow('Visao Gerencial Orcamentaria - ALTERAR')
        self.oHelper.ClickGridCell("Descricao", 2)

        # Expande Arvore
        self.oHelper.GridTree('Descricao', memoAKN01, right_click=True)

        # Abertura de Arvore e posicionando no terceiro item 
        self.oHelper.ClickGridCell('Descricao', 3)

        # Clicar na aba "itens"
        self.oHelper.ClickFolder('Itens')
        self.oHelper.SetButton('Editar')

        self.oHelper.SetValue('Planilha Orct.', codigoPlan, grid=True, grid_number=2)
        self.oHelper.SetValue('Versao', versao, grid=True, grid_number=2)
        self.oHelper.SetValue('Conta Orcamentaria De', contaOrcDe, grid=True, grid_number=2)
        self.oHelper.SetValue('Conta Orcamentaria Ate', contaOrcAte, grid=True, grid_number=2)
        self.oHelper.SetValue('Operacao De', operacaoDe, grid=True, grid_number=2)
        self.oHelper.SetValue('Operacao Ate', operacaoAte, grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Gravar')

        self.oHelper.CheckResult('Planilha Orct.', codigoPlan, grid=True, grid_number=2)
        self.oHelper.CheckResult('Versao', versao, grid=True, grid_number=2)
        self.oHelper.CheckResult('Conta Orcamentaria De', contaOrcDe, grid=True, grid_number=2)
        self.oHelper.CheckResult('Conta Orcamentaria Ate', contaOrcAte, grid=True, grid_number=2)
        self.oHelper.CheckResult('Operacao De', operacaoDe, grid=True, grid_number=2)
        self.oHelper.CheckResult('Operacao Ate', operacaoAte, grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SearchBrowse(f'D MG 02 {codigoAKN01}')

        self.oHelper.AssertTrue()

    # Exclusao
    
    def test_PCOA170_CT004(self):
        
        codigoAKN01 = '003'

        self.oHelper.SearchBrowse(f'D MG 02 {codigoAKN01}')
        self.oHelper.SetButton('Outras ações', 'Excluir')
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.SearchBrowse(f'D MG 02 {codigoAKN01}')

        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult('AKN_CODIGO', codigoAKN01)
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.AssertFalse()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()    