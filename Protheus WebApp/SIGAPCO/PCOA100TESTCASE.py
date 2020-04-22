from tir import Webapp
import unittest
from datetime import datetime
import string
import random

class PCOA100(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper =  Webapp()
        inst.oHelper.Setup('SIGAPCO', '26/02/2019', 'T1', 'D MG 01 ')
        inst.oHelper.Program('PCOA100')
        #inst.oHelper.SetKey("ESC")#Inserir nova l inha
        #DateSystem = datetime.today().strftime('%d/%m/%Y')
        
    
    #Inclusao
    
    def test_PCOA100_CT001(self):

        codigoCT001 = 'PLANILHA0000001'
        memoCT001   = 'PLANILHA SEMANAL'
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', codigoCT001)
        self.oHelper.SetValue('AK1_TPPERI', '1'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('AK1_MEMO', memoCT001         )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )

        self.oHelper.SetButton('Salvar')    
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()
        
        
    
    #Alteração
    
    def test_PCOA100_CT002(self):

        codigoCT001 = 'PLANILHA0000002'
        descriCT001 = 'QUINZENAL'
        descri2     = 'DESC PER ALTER'
        memoCT001   = 'PLANILHA SEMANAL'

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', codigoCT001)
        self.oHelper.SetValue('AK1_TPPERI', '2'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('AK1_MEMO', memoCT001         )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )

        self.oHelper.SetButton('Salvar')    
        self.oHelper.SetButton('Cancelar')

        ##

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.SetButton('Outras ações', 'Alt.Cadastro')
        self.oHelper.SetValue('AK1_DESCRI', descri2      )
        self.oHelper.SetButton('Salvar')

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.SetButton('Visualizar')

        self.oHelper.CheckResult('AK1_CODIGO', codigoCT001 )
        self.oHelper.CheckResult('AK1_DESCRI', descri2 )
        
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()

    #Exclusao
    
    def test_PCOA100_CT003(self):
        
        codigoCT001 = 'PLANILHA0000003'
        descriCT001 = 'BIMESTRAL'
        memoCT001   = 'BIMESTRAL'
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', codigoCT001)
        self.oHelper.SetValue('AK1_TPPERI', '4'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('AK1_MEMO', memoCT001         )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )

        self.oHelper.SetButton('Salvar')    
        self.oHelper.SetButton('Cancelar')
        
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')

        self.oHelper.SetButton('Outras ações', 'Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Excluir')
        
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertFalse()

    #Inclusao com controle de usuário desabilitado precondição CT005
    
    def test_PCOA100_CT004(self):

        codigoCT004 = 'PLANILHA0000004'
        memoCT004   = 'PLANILHA SEMESTRAL'

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT004)
        self.oHelper.SetValue('AK1_DESCRI', memoCT004)
        self.oHelper.SetValue('AK1_TPPERI', '5'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('AK1_MEMO', memoCT004         )
        self.oHelper.SetValue('AK1_CTRUSR', '2'             )

        self.oHelper.SetButton('Salvar')    
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT004}0001')

        self.oHelper.AssertTrue()
    
    #Alteração fase orçamentária
    
    def test_PCOA100_CT005(self):

        codigoCT005 = 'PLANILHA0000004'
        cFase = '003'
        
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT005}0001')

        self.oHelper.SetButton('Outras ações', 'Altera Fase')
        self.oHelper.SetValue('Pesquisar', cFase)
        self.oHelper.SetButton('Salvar')
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT005}0001')
        self.oHelper.AssertTrue()

    #Legenda 
    
    def test_PCOA100_CT006(self):

        codigoCT006 = 'PLANILHA0000004'
        
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT006}0001')

        self.oHelper.SetButton('Outras ações', 'Legenda')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    #Inclusao com controle de usuário desabilitado precondição CT008
    
    def test_PCOA100_CT007(self):

        codigoCT007 = 'PLANILHA0000005'
        memoCT007   = 'PLANILHA ANUAL'

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT007)
        self.oHelper.SetValue('AK1_DESCRI', memoCT007)
        self.oHelper.SetValue('AK1_TPPERI', '6'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('AK1_MEMO', memoCT007         )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )

        self.oHelper.SetButton('Salvar')    
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT007}0001')

        self.oHelper.AssertTrue()

    #Copiar Planilha 
    
    def test_PCOA100_CT008(self):

        codigoCT008 = 'PLANILHA0000005'
        cPlanilha = '001PCO'
        
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT008}0001')
        self.oHelper.SetButton('Outras ações', 'Copiar Planilha')
        self.oHelper.SetValue('Copiar Planilha', cPlanilha)
        self.oHelper.SetButton('Ok')
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT008}0001')
        self.oHelper.AssertTrue()

    #Consultar C.O. de uma planilha
    
    def test_PCOA100_CT009(self):

        codigoCT009 = 'PLANILHA0000005'
        
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT009}0001')

        self.oHelper.SetButton('Alterar')
        self.oHelper.SetButton('Outras Ações','Estrut.')
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Visualizar C.O.")
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    #Incluir cadastro da planilha e conta orçamentária
    
    def test_PCOA100_CT010(self):

        codigoCT001 = 'ZZZZZZ000000001'
        sDescri     = 'ZZZZZZ000000001'
        memoCT001   = 'PLANILHA MENSAL'
        cContaOrc   = 'PCOR1003'
        cPlanilha   = 'PCORJ00001'
        cVersao     = '0001'

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', sDescri)
        self.oHelper.SetValue('AK1_TPPERI', '6'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('Memo', memoCT001     )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar') 
        

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        # Clicar no Botão 'outras ações'
        self.oHelper.SetButton('Outras Ações', 'Estrut.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Incluir C.O.")

        # TELA DE INCLUSÃO CONTA ORÇAMENTÁRIA   
        #self.oHelper.WaitShow('Planilha Orcamentaria - Contas Orcamenta...')   
        self.oHelper.SetValue('AK3_CO', cContaOrc) 
        self.oHelper.SetButton('Salvar')
        # FINALIZAÇÃO DA TELA DE INCLUSÃO DE CONTA ORÇAMENTÁRIA

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') #CTRL+Z
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
            
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') #CTRL+Z

        #Abrir item pesquisar, cancelar, confirmar, expandir
        self.oHelper.SetButton('Outras Ações', 'Pesquisar')
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') #CTRL+Z
        self.oHelper.SetButton('Cancelar')
        self.oHelper.WaitShow("Atencao")
        self.oHelper.SetButton('Ok')

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') #CTRL+Z

        #Abrir item pesquisar conta orçamentária
        self.oHelper.SetButton('Outras Ações', 'Pesquisar')
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        self.oHelper.SetValue("MV_PAR01",cContaOrc    )
        self.oHelper.ClickCheckBox("Utilizar Pesquisa Exata",1)
        self.oHelper.ClickCheckBox("Pesquisar Proxima Ocorrencia",1)
        self.oHelper.SetButton('Ok')
        
                        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        
        #Abrir item Filtro
        self.oHelper.SetButton('Outras Ações', 'Filtro')
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        self.oHelper.SetValue("Campos:", "C.O.")
        self.oHelper.SetValue("cExpr",cContaOrc, name_attr=True)
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 

        #Confirmar Cadastro 
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()


    #Cadastrar planilha e conta orçamentária por cópia de uma planilha existente
    
    def test_PCOA100_CT011(self):

        codigoCT001 = 'ZZOJ00000000002'
        sDescri     = 'ZZOJ00000000002'
        memoCT001   = 'Planilha Mensal'
        cContaOrc   = 'PCOR1002'
        cPlanilha   = 'PCORJ00002'
        cVersao     = '0001'
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', sDescri)
        self.oHelper.SetValue('AK1_TPPERI', '3'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('Memo', memoCT001     )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar') 
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        # Botão 'outras ações'
        self.oHelper.SetButton('Outras Ações', 'Ferram.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Copiar Planilha/Contas")
      

        #Abertura do Wizzard de Copia de Orçamentos
        self.oHelper.WaitShow('Cópiar Orçamento')
                
        #PAGINA 1 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 2 DO WIZZARD
        self.oHelper.SetValue("MV_PAR01",cPlanilha    )
        self.oHelper.SetValue("MV_PAR02",cVersao      )
        self.oHelper.SetValue("Considera valores dos periodos da planilha a ser copiada", True)
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 3 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 4 DO WIZZARD 
                
        self.oHelper.SetValue("Planilha ", True, position=0)
        #browser.find_elements_by_css_selector("input[type='radio'][value='Planilha']")[0].click()
        self.oHelper.SetButton('Finalizar')

        #TELA DE CONFIRMAÇÃO
        self.oHelper.WaitShow("Copia da planilha ")
        self.oHelper.SetButton('Sim')       
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        self.oHelper.SetButton('Cancelar')
        #self.oHelper.WaitShow('Planilha Orcamentaria')
        
        # Na tela principal a planilha aparecerá posicionada no topo
        self.oHelper.SetButton("Visualizar")

        # Na tela da estrutura, Pesquisar a conta orçamentária para que o cursor se posicione nela
        # Abrir item pesquisar conta orçamentária
        self.oHelper.WaitShow('Planilha Orcamentaria - VISUALIZAR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        #Abrir item Filtro
        
        self.oHelper.SetButton('Outras Ações', 'Filtro')        
        self.oHelper.SetValue("cCampo","C.O.",name_attr=True)
        self.oHelper.SetValue("cExpr",cContaOrc,name_attr=True)
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        
       
        #Clicar na aba "Total por Classe"
        self.oHelper.ClickFolder("Total por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        #Clicar na aba "Acumulado por Classe"
        self.oHelper.ClickFolder("Acumulado por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        #Para sair da tela clique no botão "Confirmar"
        self.oHelper.WaitShow('Planilha Orcamentaria - VISUALIZAR')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()
        
    
    
    # Cadastro de planilha orçamentária, com cópia de estrutura de 
    # períodos vazia e posterior preenchiemnto dos períodos por rateio
    def test_PCOA100_CT012(self):

        codigoCT001 = 'ZZOJ00000000003'
        sDescri     = 'ZZOJ00000000003'
        memoCT001   = 'Planilha Mensal'
        cContaOrc   = 'PCOR1001'
        cPlanilha   = 'PCORJ00001'
        cVersao     = '0001'
        cVlrRat     = '120.000,00'
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', sDescri)
        self.oHelper.SetValue('AK1_TPPERI', '3'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('Memo', memoCT001     )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar') 
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        # Botão 'outras ações'
        self.oHelper.SetButton('Outras Ações', 'Ferram.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Copiar Planilha/Contas")
      
        #Abertura do Wizzard de Copia de Orçamentos
        self.oHelper.WaitShow('Cópiar Orçamento')
                
        #PAGINA 1 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 2 DO WIZZARD
        self.oHelper.SetValue("MV_PAR01",cPlanilha  )
        self.oHelper.SetValue("MV_PAR02",cVersao    )
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 3 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 4 DO WIZZARD 
                
        self.oHelper.SetValue("Planilha ", True, position=0)
        #browser.find_elements_by_css_selector("input[type='radio'][value='Planilha']")[0].click()
        self.oHelper.SetButton('Finalizar')

        #TELA DE CONFIRMAÇÃO
        self.oHelper.WaitShow("Copia da planilha ")
        self.oHelper.SetButton('Sim')       
        
        #Após a confirmação da cópia, é aberta uma nova tela de inclusão, 
        # se procede a fechar esta tela e abrir o registro posicionado que corresponde à inclusão 
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Alterar')

        
        # Na tela da estrutura, Pesquisar a conta orçamentária para que o cursor se posicione nela
        # Abrir item pesquisar conta orçamentária
        self.oHelper.WaitShow('Planilha Orcamentaria - ALTERAR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        #Abrir item Filtro
        self.oHelper.SetButton('Outras Ações', 'Filtro')        
        self.oHelper.SetValue("cCampo","C.O.",name_attr=True)
        self.oHelper.SetValue("cExpr",cContaOrc,name_attr=True)
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        
        #Abrir menu outras ações>Ferram.
        self.oHelper.SetButton('Outras Ações', 'Ferram.') 
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Rateio de Valores nos Periodos")
      
        #Abertura do Wizzard de Copia de Orçamentos
        self.oHelper.WaitShow('Rateio de Valores para o Orçamento')
                
        #PAGINA 1 DO WIZZARD DE RATEIO DE VALORES
        self.oHelper.SetButton('Avançar')
        
        #TELA 2 DO WIZZARD - RADIO BUTTONS DEFAULT
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 3 DO WIZZARD - VALOR A SER RATEADO
        self.oHelper.SetValue("MV_PAR03", cVlrRat )
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 4 DO WIZZARD  - PERCENTUAIS APRESENTADOS
        self.oHelper.SetButton('Avançar')

        #PAGINA 5 DO WIZZARD  - VALORES APRESENTADOS
        self.oHelper.SetButton('Finalizar')

        #Clicar na aba "Itens"
        self.oHelper.ClickFolder("Itens")
        self.oHelper.SetButton('Gravar')

        self.oHelper.WaitShow('Planilha Orcamentaria - ALTERAR')

        #Clicar na aba "Total por Classe"
        self.oHelper.ClickFolder("Total por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        #Clicar na aba "Acumulado por Classe"
        self.oHelper.ClickFolder("Acumulado por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        self.oHelper.SetButton("Confirmar")

        #A TELA DE ALTERAÇÃO SERÁ REABERTA
        self.oHelper.WaitShow('Planilha Orcamentaria - ALTERAR')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()
    


    #Inclusão de planilha com reajuste de valores, por percentual
    
    def test_PCOA100_CT013(self):

        codigoCT001 = 'ZZZJ00000000004'
        sDescri     = 'ZZOJ00000000004'
        memoCT001   = 'Reajuste de valor por %'
        cContaOrc   = 'PCOR1002'
        cPlanilha   = 'PCORJ00002'
        cVersao     = '0001'
        cPercent    = '10,00'
        
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', sDescri)
        self.oHelper.SetValue('AK1_TPPERI', '3'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('Memo', memoCT001     )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar') 
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        # Botão 'outras ações'
        self.oHelper.SetButton('Outras Ações', 'Ferram.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Copiar Planilha/Contas")
      
        #Abertura do Wizzard de Copia de Orçamentos
        self.oHelper.WaitShow('Cópiar Orçamento')
                
        #PAGINA 1 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 2 DO WIZZARD
        self.oHelper.SetValue("MV_PAR01",cPlanilha  )
        self.oHelper.SetValue("MV_PAR02",cVersao    )
        self.oHelper.SetValue("Considera valores dos periodos da planilha a ser copiada", True)
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 3 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 4 DO WIZZARD 
                
        self.oHelper.SetValue("Planilha ", True, position=0)
        #browser.find_elements_by_css_selector("input[type='radio'][value='Planilha']")[0].click()
        self.oHelper.SetButton('Finalizar')

        #TELA DE CONFIRMAÇÃO
        self.oHelper.WaitShow("Copia da planilha ")
        self.oHelper.SetButton('Sim')       
        
        #Após a confirmação da cópia, é aberta uma nova tela de inclusão, 
        # se procede a fechar esta tela e abrir o registro posicionado que corresponde à inclusão 
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Alterar')

        
        # Na tela da estrutura, Pesquisar a conta orçamentária para que o cursor se posicione nela
        # Abrir item pesquisar conta orçamentária
        self.oHelper.WaitShow('Planilha Orcamentaria - ALTERAR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        #Abrir item Filtro
        self.oHelper.SetButton('Outras Ações', 'Filtro')        
        self.oHelper.SetValue("cCampo","C.O.",name_attr=True)
        self.oHelper.SetValue("cExpr",cContaOrc,name_attr=True)
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        
        #Abrir menu outras ações>Ferram.
        self.oHelper.SetButton('Outras Ações', 'Ferram.') 
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Reajustar Valores Orcados")
      
        #Abertura do Wizzard de Copia de Orçamentos
        
        #self.oHelper.CheckView('Planilha Orcamentaria - ALTERAR - Parametros')
        self.oHelper.SetValue("MV_PAR07",cPercent)
        self.oHelper.SetButton('Ok')
        
        self.oHelper.WaitShow('Planilha Orcamentaria - ALTERAR')

        #Clicar na aba "Total por Classe"
        self.oHelper.ClickFolder("Total por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        #Clicar na aba "Acumulado por Classe"
        self.oHelper.ClickFolder("Acumulado por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        self.oHelper.SetButton("Confirmar")

        #A TELA DE ALTERAÇÃO SERÁ REABERTA
        self.oHelper.WaitShow('Planilha Orcamentaria - ALTERAR')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()

    #Inclusão de planilha com reajuste de valores, por percentual
    
    def test_PCOA100_CT014(self):

        codigoCT001 = 'ZZZJ00000000005'
        sDescri     = 'ZZOJ00000000005'
        memoCT001   = 'Importar dados'
        cContaOrc   = 'PCOR1002'
        cPlanilha   = 'PCORJ00002'
        cVersao     = '0001'
        cProces     = '900004'
        cItemPr     = '01'
        
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', sDescri)
        self.oHelper.SetValue('AK1_TPPERI', '3'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('Memo', memoCT001     )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar') 
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        # Botão 'outras ações'
        self.oHelper.SetButton('Outras Ações', 'Ferram.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Copiar Planilha/Contas")
      
        #Abertura do Wizzard de Copia de Orçamentos
        self.oHelper.WaitShow('Cópiar Orçamento')
                
        #PAGINA 1 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 2 DO WIZZARD
        self.oHelper.SetValue("MV_PAR01",cPlanilha  )
        self.oHelper.SetValue("MV_PAR02",cVersao    )
        self.oHelper.SetValue("Considera valores dos periodos da planilha a ser copiada", True)
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 3 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 4 DO WIZZARD 
                
        self.oHelper.SetValue("Planilha ", True, position=0)
        #browser.find_elements_by_css_selector("input[type='radio'][value='Planilha']")[0].click()
        self.oHelper.SetButton('Finalizar')

        #TELA DE CONFIRMAÇÃO
        self.oHelper.WaitShow("Copia da planilha ")
        self.oHelper.SetButton('Sim')       
        
        #Após a confirmação da cópia, é aberta uma nova tela de inclusão, 
        # se procede a fechar esta tela e abrir o registro posicionado que corresponde à inclusão 
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Alterar')

        
        # Na tela da estrutura, Pesquisar a conta orçamentária para que o cursor se posicione nela
        # Abrir item pesquisar conta orçamentária
        self.oHelper.WaitShow('Planilha Orcamentaria - ALTERAR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        #Abrir item Filtro para posicionar na conta orçamentária
        self.oHelper.SetButton('Outras Ações', 'Filtro')        
        self.oHelper.SetValue("cCampo","C.O.",name_attr=True)
        self.oHelper.SetValue("cExpr",cContaOrc,name_attr=True)
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        
        #Abrir menu outras ações>Ferram.
        self.oHelper.SetButton('Outras Ações', 'Ferram.') 
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Importar dados Integração")
      
        #Abertura do Wizzard de Copia de Orçamentos
        self.oHelper.WaitShow('Importar Dados da Área de Integração')
                
        #PAGINA 1 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 2 DO WIZZARD
        self.oHelper.SetValue("MV_PAR01", cProces )
        self.oHelper.SetValue("MV_PAR02", cItemPr )
        self.oHelper.SetButton('Avançar')

        #PAGINA 3 DO WIZZARD
        self.oHelper.SetButton('Avançar')

        #PAGINA 4 DO WIZZARD
        self.oHelper.SetButton('Avançar')

        #PAGINA 3 DO WIZZARD
        self.oHelper.SetButton('Avançar')

        #PAGINA 4 DO WIZZARD
        self.oHelper.SetButton('Finalizar')    


        #Clicar na aba "Total por Classe"
        self.oHelper.ClickFolder("Total por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()

    #Distribuição de valores - Replicar
    def test_PCOA100_CT015(self):

        codigoCT001 = 'ZZZJ00000000017'
        sDescri     = 'ZZOJ00000000017'
        memoCT001   = 'Distrib. Vlrs'
        cContaOrc   = 'PCOR1001'
        cPlanilha   = 'PCORJ00002'
        cVersao     = '0001'
        cRegra      = '000001'
        cValor      = '10.000,00'
        
        
        self. oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', sDescri)
        self.oHelper.SetValue('AK1_TPPERI', '3'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('Memo', memoCT001     )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar') 
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        # Clicar no Botão 'outras ações'
        self.oHelper.SetButton('Outras Ações', 'Estrut.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Incluir C.O.")
      
        # TELA DE INCLUSÃO CONTA ORÇAMENTÁRIA   
        #self.oHelper.WaitShow('Planilha Orcamentaria - Contas Orc...')   
        self.oHelper.SetValue('AK3_CO', cContaOrc) 
        self.oHelper.SetButton('Salvar')
        # FINALIZAÇÃO DA TELA DE INCLUSÃO DE CONTA ORÇAMENTÁRIA

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
            
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        #Abrir item Filtro
        self.oHelper.SetButton('Outras Ações', 'Filtro')        
        self.oHelper.SetValue("cCampo","C.O.",name_attr=True)
        self.oHelper.SetValue("cExpr",cContaOrc,name_attr=True)
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        # Botão 'outras ações' > Incluir C.O.
        self.oHelper.SetButton('Outras Ações', 'Ferram.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Distribuição Valores")

        #Abertura do Wizzard: 'Distribuição de valores por entidade'
        self.oHelper.WaitShow('Distribuição de valores por entidade')
                
        #PAGINA 1 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 2 DO WIZZARD
        self.oHelper.SetValue("MV_PAR01",cRegra  )
        self.oHelper.SetValue("MV_PAR02",cValor  )
        #percentual padrão 100.00%
        #posicição radio button padrão
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 3 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 4 DO WIZZARD 
        self.oHelper.SetButton('Avançar')

        #PAGINA 5 DO WIZZARD
        self.oHelper.SetButton('Finalizar')

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
       
        #Clicar na aba "Total por Classe"
        self.oHelper.ClickFolder("Itens")
        self.oHelper.SetButton("Gravar")

        self.oHelper.ClickFolder("Total por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        #Clicar na aba "Acumulado por Classe"
        self.oHelper.ClickFolder("Acumulado por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()


    #Distribuição de valores - Dividir
    def test_PCOA100_CT016(self):

        codigoCT001 = 'ZZZJ00000000018'
        sDescri     = 'ZZZJ00000000018'
        memoCT001   = 'Distrib. Vlrs'
        cContaOrc   = 'PCOR1001'
        cPlanilha   = 'PCORJ00002'
        cVersao     = '0001'
        cRegra      = '000001'
        cValor      = '5.000,00'
        
        self. oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', sDescri)
        self.oHelper.SetValue('AK1_TPPERI', '3'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('Memo', memoCT001     )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar') 
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        # Clicar no Botão 'outras ações'
        self.oHelper.SetButton('Outras Ações', 'Estrut.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Incluir C.O.")
      
        # TELA DE INCLUSÃO CONTA ORÇAMENTÁRIA   
        #self.oHelper.WaitShow('Planilha Orcamentaria - Contas Orc...')   
        self.oHelper.SetValue('AK3_CO', cContaOrc) 
        self.oHelper.SetButton('Salvar')
        # FINALIZAÇÃO DA TELA DE INCLUSÃO DE CONTA ORÇAMENTÁRIA

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
            
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        #Abrir item Filtro
        self.oHelper.SetButton('Outras Ações', 'Filtro')        
        self.oHelper.SetValue("cCampo","C.O.",name_attr=True)
        self.oHelper.SetValue("cExpr",cContaOrc,name_attr=True)
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        # Botão 'outras ações' > Incluir C.O.
        self.oHelper.SetButton('Outras Ações', 'Ferram.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Distribuição Valores")

        #Abertura do Wizzard: 'Distribuição de valores por entidade'
        self.oHelper.WaitShow('Distribuição de valores por entidade')
                
        #PAGINA 1 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 2 DO WIZZARD
        self.oHelper.SetValue("MV_PAR01",cRegra  )
        self.oHelper.SetValue("MV_PAR02",cValor  )
        #percentual padrão 100.00%
        #posicição radio button padrão
        self.oHelper.SetValue("Dividir", True)#, position=0)
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 3 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 4 DO WIZZARD 
        self.oHelper.SetButton('Avançar')

        #PAGINA 5 DO WIZZARD
        self.oHelper.SetButton('Finalizar')

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
       
        #Clicar na aba "Total por Classe"
        self.oHelper.ClickFolder("Itens")
        self.oHelper.SetButton("Gravar")

        self.oHelper.ClickFolder("Total por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        #Clicar na aba "Acumulado por Classe"
        self.oHelper.ClickFolder("Acumulado por Classe")
        self.oHelper.CheckView("Classenbsp;Orçamentária")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()


    #Distribuição de valores - Dividir
    def test_PCOA100_CT017(self):

        codigoCT001 = 'ZZZJ00000000079'
        sDescri     = 'ZZZJ00000000079'
        memoCT001   = 'Fórmulas'
        cContaOrc   = 'PCOR1002'
        cPlanilha   = 'PCORJ00002'
        cVersao     = '0001'
        
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', sDescri)
        self.oHelper.SetValue('AK1_TPPERI', '3'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('Memo', memoCT001     )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar') 
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        # Botão 'outras ações'
        self.oHelper.SetButton('Outras Ações', 'Ferram.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Copiar Planilha/Contas")
      
        #Abertura do Wizzard de Copia de Orçamentos
        self.oHelper.WaitShow('Cópiar Orçamento')
                
        #PAGINA 1 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 2 DO WIZZARD
        self.oHelper.SetValue("MV_PAR01",cPlanilha  )
        self.oHelper.SetValue("MV_PAR02",cVersao    )
        self.oHelper.SetValue("Considera valores dos periodos da planilha a ser copiada", True)
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 3 DO WIZZARD
        self.oHelper.SetButton('Avançar')
        
        #PAGINA 4 DO WIZZARD 
                
        self.oHelper.SetValue("Planilha ", True, position=0)
        #browser.find_elements_by_css_selector("input[type='radio'][value='Planilha']")[0].click()
        self.oHelper.SetButton('Finalizar')

        #TELA DE CONFIRMAÇÃO
        self.oHelper.WaitShow("Copia da planilha ")
        self.oHelper.SetButton('Sim')       
        
        #Após a confirmação da cópia, é aberta uma nova tela de inclusão, 
        # se procede a fechar esta tela e abrir o registro posicionado que corresponde à inclusão 
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Alterar')

        
        # Na tela da estrutura, Pesquisar a conta orçamentária para que o cursor se posicione nela
        # Abrir item pesquisar conta orçamentária
        self.oHelper.WaitShow('Planilha Orcamentaria - ALTERAR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        #Abrir item Filtro para posicionar na conta orçamentária
        self.oHelper.SetButton('Outras Ações', 'Filtro')        
        self.oHelper.SetValue("cCampo","C.O.",name_attr=True)
        self.oHelper.SetValue("cExpr",cContaOrc,name_attr=True)
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        
        #Abrir menu outras ações>Ferram.
        self.oHelper.SetButton('Outras Ações', 'Ferram.') 
              
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Recalculo de Formulas")

        #Tela: 'Planilha Orcamentaria - INCLUIR - Recalculo das Formulas'
        #self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR - Recalculo das Formulas')
        self.oHelper.SetButton("Ok")        
        self.oHelper.WaitShow('Planilha Orcamentaria - ALTERAR')        
      
        #Clicar na aba "Total por Classe"
        self.oHelper.ClickFolder("Itens")
        self.oHelper.SetButton("Gravar")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow('Planilha Orcamentaria - ALTERAR')
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()   

#Exclusão de conta orçamentária
    def test_PCOA100_CT018(self):

        codigoCT001 = 'ZZZJ00000000211'
        sDescri     = 'PCZJ00000000211'
        memoCT001   = 'Excluir C.O.'
        cContaOrc   = 'PCOR1001'
        cPlanilha   = 'PCORJ00002'
        cVersao     = '0001'
        
        
        self. oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', sDescri)
        self.oHelper.SetValue('AK1_TPPERI', '3'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('Memo', memoCT001     )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar') 
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        # Clicar no Botão 'outras ações'
        self.oHelper.SetButton('Outras Ações', 'Estrut.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Incluir C.O.")
      
        # TELA DE INCLUSÃO CONTA ORÇAMENTÁRIA   
        #self.oHelper.WaitShow('Planilha Orcamentaria - Contas Orc...')   
        self.oHelper.SetValue('AK3_CO', cContaOrc) 
        self.oHelper.SetButton('Salvar')
        # FINALIZAÇÃO DA TELA DE INCLUSÃO DE CONTA ORÇAMENTÁRIA

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
            
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        #Abrir item Filtro
        self.oHelper.SetButton('Outras Ações', 'Filtro')        
        self.oHelper.SetValue("cCampo","C.O.",name_attr=True)
        self.oHelper.SetValue("cExpr",cContaOrc,name_attr=True)
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        # Botão 'outras ações' > Estrut.
        self.oHelper.SetButton('Outras Ações', 'Estrut.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Excluir C.O.")
        #self.oHelper.WaitShow('Planilha Orcamentaria - Contas Or...')
        self.oHelper.SetButton("Confirmar")                        
        
        self.oHelper.WaitShow('Atencao')
        self.oHelper.SetButton("Excluir")                        

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Cancelar")
                
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()


    #Alterar conta orçamentária 
    def test_PCOA100_CT019(self):

        codigoCT001 = 'ZZZJ00000000X11'
        sDescri     = 'ZZZJ00000000811'
        memoCT001   = 'Alterar C.O.'
        cContaOrc   = 'PCOR1001'
        cContaOrc2  = 'ALTERAÇÃO DESC'
        cPlanilha   = 'PCORJ00002'
        cVersao     = '0001'
        
        
        self. oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')

        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', sDescri)
        self.oHelper.SetValue('AK1_TPPERI', '3'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('Memo', memoCT001     )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar') 
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
        
        # Clicar no Botão 'outras ações'
        self.oHelper.SetButton('Outras Ações', 'Estrut.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Incluir C.O.")
      
        # TELA DE INCLUSÃO CONTA ORÇAMENTÁRIA   
        #self.oHelper.WaitShow('Planilha Orcamentaria - Contas Orc...')   
        self.oHelper.SetValue('AK3_CO', cContaOrc) 
        self.oHelper.SetButton('Salvar')
        # FINALIZAÇÃO DA TELA DE INCLUSÃO DE CONTA ORÇAMENTÁRIA

        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        #Abertura de árvore e posicionando no segundo item 
        self.oHelper.ClickGridCell("Descricao", 2)
            
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        #Abrir item Filtro
        self.oHelper.SetButton('Outras Ações', 'Filtro')        
        self.oHelper.SetValue("cCampo","C.O.",name_attr=True)
        self.oHelper.SetValue("cExpr",cContaOrc,name_attr=True)
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR') 
        # Botão 'outras ações' > Estrut.
        self.oHelper.SetButton('Outras Ações', 'Estrut.')
        
        # MENU FLUTUANTE(menupopup)
        self.oHelper.ClickMenuPopUpItem("Alterar C.O.")
        #self.oHelper.WaitShow('Planilha Orcamentaria - Contas Orc...')
        # TELA DE INCLUSÃO CONTA ORÇAMENTÁRIA   
        self.oHelper.SetButton('Salvar')
        # FINALIZAÇÃO DA TELA DE INCLUSÃO DE CONTA ORÇAMENTÁRIA
        
        self.oHelper.WaitShow('Planilha Orcamentaria - INCLUIR')
        self.oHelper.SetButton("Confirmar")
                
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()    

    def test_PCOA100_CT020(self):

        codigoCT005 = 'PLANILHA0000004'
        
        
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT005}0001')

        self.oHelper.SetButton('Outras ações', 'Altera Fase')
        self.oHelper.SetButton('Outras ações', 'Legenda')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT005}0001')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()    