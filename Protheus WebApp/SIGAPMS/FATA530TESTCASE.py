from tir import Webapp 
import unittest
from datetime import datetime
import time  
DateSystem = datetime.today().strftime("%d/%m/%Y")

class FATA530(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        SETUP
        Test Case Initial Setup
        '''
        #Endereço do webapp e o nome do Browser 
        self.oHelper = Webapp()

        #Parametros de inicializaçao
        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "D MG 01 ", "05")

        #Nome da rotina do Caso de Teste
        self.oHelper.Program("FATA300") 

    def test_FATA530_CT001(self):
        '''
        Test Case CT001 - Inclusão de EDT's na Proposta de Serviços (PMS)
        '''
        Opportunity = '000287'
        Proposal = '000285'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=2, grid_number=1)
        self.oHelper.ClickBox("Versão", "002")
        self.oHelper.WaitShow('Proposta de servicos')
        self.oHelper.ClickTree("Proposta de servicos Id: TIR000099B002 > EDT 01 - FATA530", right_click = True)        
        self.oHelper.ClickMenuPopUpItem("Incluir EDT")        
        self.oHelper.ClickFolder("Edt")
        self.oHelper.SetValue("AF5_EDT","01.01")
        self.oHelper.SetValue("AF5_DESCRI","EDT 01.01")
        self.oHelper.SetValue("AF5_UM","UN")
        self.oHelper.SetValue("AF5_QUANT","1,0000")
        self.oHelper.SetValue("AF5_ORDEM","001")        
        self.oHelper.ClickFolder("Observacoes")
        self.oHelper.SetValue("AF5_OBS","01.01")        
        self.oHelper.ClickFolder("Vendas/remessa")
        self.oHelper.SetValue("AF5_FATURA","1")        
        self.oHelper.SetButton("Salvar")        
        self.oHelper.ClickTree("Proposta de servicos Id: TIR000099B002", right_click = True)
        self.oHelper.ClickMenuPopUpItem("Procurar...")
        self.oHelper.SetValue("Procurar por:","EDT 01 -")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetButton("Procurar")        
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")   
        self.oHelper.AssertTrue()

    def test_FATA530_CT002(self):
        '''
        Test Case CT002 - Alteração de EDT na Proposta de Serviços (PMS)
        '''
        Opportunity = '000287'
        Proposal = '000285'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')
        self.oHelper.ClickGridCell("No.Projeto", row=2, grid_number=1)
        self.oHelper.ClickBox("Versão", "002")
        self.oHelper.ClickTree("EDT 02 - FATA530", right_click = True)
        self.oHelper.ClickMenuPopUpItem("Alterar")
        self.oHelper.ClickFolder("Edt")
        self.oHelper.SetValue("AF5_DESCRI","EDT 02 - FATA530 - ALTERADO")
        self.oHelper.SetButton("Salvar")
        self.oHelper.ClickTree("EDT 02 - FATA530 - ALTERADO", right_click = True)
        self.oHelper.ClickMenuPopUpItem("Visualizar")        
        self.oHelper.ClickFolder("Edt")
        self.oHelper.CheckResult("AF5_DESCRI","EDT 02 - FATA530 - ALTERADO")        
        self.oHelper.SetButton("Cancelar")        
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página") 
        self.oHelper.AssertTrue()

    def test_FATA530_CT003(self):
        '''
        Test Case CT003 - Visualizar EDT na Proposta de Serviços (PMS)
        '''
        Opportunity = '000287'
        Proposal = '000285'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=2, grid_number=1)
        self.oHelper.ClickBox("Versão", "002")
        self.oHelper.ClickTree("EDT 02 - FATA530 - ALTERADO", right_click = True)
        self.oHelper.ClickMenuPopUpItem("Visualizar")
        self.oHelper.ClickFolder("Edt")
        self.oHelper.CheckResult("AF5_DESCRI","EDT 02 - FATA530 - ALTERADO")        
        self.oHelper.SetButton("Confirmar")        
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.AssertTrue()

    def test_FATA530_CT004(self):
        '''
        Test Case CT004 - Inclusão de Tarefa na Proposta de Serviços (PMS) - Falha ao preencher grid
        '''
        Opportunity = '000287'
        Proposal = '000285'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')
        self.oHelper.ClickGridCell("No.Projeto", row=2, grid_number=1)
        self.oHelper.ClickBox("Versão", "002")        
        self.oHelper.ClickTree("EDT 02 - FATA530 - ALTERADO", right_click = True)
        self.oHelper.ClickMenuPopUpItem("Incluir Tarefa")
        self.oHelper.SetValue("AF2_STATUS","1")
        self.oHelper.SetValue("AF2_TPTARE","FTSRV2")
        self.oHelper.SetValue("AF2_DESCRI","Tarefa 02.01")        
        self.oHelper.SetValue("AF2_UM","UN")
        self.oHelper.SetValue("AF2_QUANT","1,0000")
        self.oHelper.SetValue("AF2_GRPCOM","FTSV1")
        self.oHelper.SetValue("AF2_HDURAC","40,00")
        self.oHelper.SetValue("AF2_CALEND","001")
        self.oHelper.SetValue("AF2_ORDEM","001")
        self.oHelper.SetValue("AF2_FATURA","1")
        self.oHelper.SetValue("AF2_OBS","Tarefa 02.01")
        self.oHelper.ClickFolder("Produtos")        
        self.oHelper.SetValue("Produto","FATSERVICOPMS1", grid=True, grid_number=1,row=1)
        self.oHelper.ClickGridCell("Quantidade", row=1, grid_number=1)
        self.oHelper.SetValue("Quantidade","1,0000", grid=True, grid_number=1,row=1)   
        self.oHelper.LoadGrid()
        self.oHelper.ClickFolder("Componentes")        
        self.oHelper.SetValue("ADX_CODCMP","FTSRV2", grid=True, grid_number=3,row=1)
        self.oHelper.SetValue("ADX_ITCOMP","01", grid=True, grid_number=3,row=1)
        self.oHelper.SetValue("ADX_QUANT","1,0000", grid=True, grid_number=3,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")     
        self.oHelper.AssertTrue()

    def test_FATA530_CT005(self):
        '''
        CT005 - Alteração da Tarefa na Proposta de Serviços (PMS)
        '''
        Opportunity = '000287'
        Proposal = '000285'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')        
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=1, grid_number=1)
        self.oHelper.ClickBox("Versão", "001")        
        self.oHelper.ClickTree("Proposta de servicos Id: TIR000099B001 > EDT 03 - FATA530 > Tarefa 03.01", right_click = True)
        self.oHelper.ClickMenuPopUpItem("Alterar")        
        self.oHelper.WaitShow("Tarefas do Orcamento")
        self.oHelper.SetValue("Duracao Hrs.","30,00")
        self.oHelper.SetButton("Salvar")        
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.AssertTrue()

    def test_FATA530_CT006(self):
        '''
        CT006 - Cópia Projeto com EDT e Tarefa para a Proposta de Serviços (PMS)
        '''
        Opportunity = '000286'
        Proposal = '000284'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")
        self.oHelper.SetButton("Alterar")        
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')
        self.oHelper.WaitHide("Projetos(s) gerado para proposta: TIR000099A")
        self.oHelper.ClickGridCell("No.Projeto", row=1, grid_number=1)
        self.oHelper.ClickBox("Versão", "001")
        self.oHelper.WaitShow('Proposta de servicos')
        self.oHelper.SetButton('Outras Ações','Copiar Projeto')
        self.oHelper.WaitHide("Selecione o projeto a ser copiado")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse(f"FATSERV001", "Orcamento")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")    
        self.oHelper.AssertTrue()

    def test_FATA530_CT008(self):
        '''
        CT008 - Trocar EDT Pai do Orçamento de Serviço (PMS)
        '''
        Opportunity = '000286'
        Proposal = '000284'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')
        
        self.oHelper.ClickGridCell("No.Projeto", row=2, grid_number=1)
        self.oHelper.ClickBox("Versão", "002")
        self.oHelper.WaitShow('Proposta de servicos')        
        self.oHelper.ClickTree("Proposta de servicos Id: TIR000099A002 > ORCAMENTO DE SERVICO PMS - FATSERV001 - FATA530 > EDT 02 - FATA530 - STATUS NAO UTILIZADO", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Trocar EDT Pai")        
        self.oHelper.WaitHide('Seleção de EDT')       
        self.oHelper.ClickTree("Proposta de servicos Id: TIR000099A002 > ORCAMENTO DE SERVICO PMS - FATSERV001 - FATA530 > EDT 03 - FATA530 - STATUS PREEXISTENTE")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.AssertTrue()
    
    def test_FATA530_CT009(self):
        '''
        CT009 - Importar Composição no Orçamento de Serviço (PMS)
        '''
        Opportunity = '000286'
        Proposal = '000284'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=2, grid_number=1)
        self.oHelper.ClickBox("Versão", "002")
        self.oHelper.WaitShow('Proposta de servicos')
        self.oHelper.ClickTree("Proposta de servicos Id: TIR000099A002", right_click = True)
        self.oHelper.ClickMenuPopUpItem("Importar Composicao")
        self.oHelper.SetValue("Cod. Composicao","FATSERV001")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetValue("Quantidade","2,0000")
        self.oHelper.SetButton("Confirma")
        self.oHelper.ClickTree("Proposta de servicos Id: TIR000099A002 > COMPOSICAO SERVICO PMS - FATA530", right_click = True)        
        '''        
        self.oHelper.ClickMenuPopUpItem("Visualizar")
        self.oHelper.WaitShow("Tarefas do Orcamento")
        self.oHelper.CheckResult("AF2_DESCRI","COMPOSICAO SERVICO PMS - FATA530")
        self.oHelper.SetButton("Cancelar")
        '''
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.AssertTrue()

    def test_FATA530_CT012(self):
        '''
        CT012 - Legenda no Orçamento de Serviço PMS
        '''
        Opportunity = '000286'
        Proposal = '000284'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=2, grid_number=1)
        self.oHelper.ClickBox("Versão", "002")
        self.oHelper.WaitShow('Proposta de servicos')
        self.oHelper.SetButton('Outras Ações','Legenda')
        self.oHelper.WaitHide('Legenda/Status')   
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.AssertTrue()

    def test_FATA530_CT013(self):
        '''
        CT013 - Selecionar Modelos de Projetos (Manual) na Proposta de Serviços (PMS)
        '''
        Opportunity = '000286'
        Proposal = '000284'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=3, grid_number=1)
        self.oHelper.ClickBox("Versão", "003")
        self.oHelper.WaitShow('Proposta de servicos')
        self.oHelper.SetButton('Outras Ações','Selecionar Modelos')
        self.oHelper.WaitHide('Seleção de modelos')       
        self.oHelper.ClickBox("Codigo", "FATSRVPMS1", grid_number=1 )
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Manual")
        self.oHelper.ClickGridCell("Descricao", row=2, grid_number=2)
        self.oHelper.ClickBox("Descricao", "Edt 01 - Fata530 - Status Utilizado", grid_number=2 )
        self.oHelper.ClickGridCell("Descricao", row=3, grid_number=2)
        self.oHelper.ClickBox("Descricao", "Edt 02 - Fata530 - Status Nao Utilizado", grid_number=2 )
        self.oHelper.ClickGridCell("Descricao", row=4, grid_number=2)
        self.oHelper.ClickBox("Descricao", "Edt 03 - Fata530 - Status Preexistente", grid_number=2 )
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.AssertTrue()

    def test_FATA530_CT014(self):
        '''
        CT014 - Selecionar Modelos de Projetos (Completo) na Proposta de Serviços (PMS)
        '''
        Opportunity = '000286'
        Proposal = '000284'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=4, grid_number=1)
        self.oHelper.ClickBox("Versão", "004")
        self.oHelper.WaitShow('Proposta de servicos')
        self.oHelper.SetButton('Outras Ações','Selecionar Modelos')
        self.oHelper.WaitHide('Seleção de modelos')   
        self.oHelper.ClickBox("Codigo", "FATSRVPMS1", grid_number=1 )
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Completo")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.AssertTrue()

    def test_FATA530_CT015(self):
        '''
        CT015 - Selecionar Modelos de Projetos (Cancelar) na Proposta de Serviços (PMS)
        '''
        Opportunity = '000286'
        Proposal = '000284'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=4, grid_number=1)
        self.oHelper.ClickBox("Versão", "004")
        self.oHelper.WaitShow('Proposta de servicos')
        self.oHelper.SetButton('Outras Ações','Selecionar Modelos')
        self.oHelper.WaitHide('Seleção de modelos')   
        self.oHelper.ClickBox("Codigo", "FATSRVPMS1", grid_number=1 )
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.AssertTrue()

    def test_FATA530_CT017(self):
        '''
        CT017 - Definir Projeto na Proposta de Serviços (PMS)
        '''
        Opportunity = '000286'
        Proposal = '000284'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=2, grid_number=1)
        self.oHelper.ClickBox("Versão", "002")
        self.oHelper.WaitShow('Proposta de servicos')
        self.oHelper.SetButton('Outras Ações','Definições')
        self.oHelper.WaitHide('Definições do projeto')         
        self.oHelper.SetValue("AF3_FATOR","1,0000", row=1,grid=True, grid_number=1)
        self.oHelper.SetValue("AF3_FATOR","1,0000", row=2,grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Fechar")        
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.AssertTrue()

    def test_FATA530_CT018(self):
        '''
        CT018 - Componentes duplicados na Proposta de Serviços (PMS)
        '''
        Opportunity = '000286'
        Proposal = '000284'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=5, grid_number=1)
        self.oHelper.ClickBox("Versão", "005")
        self.oHelper.WaitShow('Proposta de servicos')
        self.oHelper.SetButton('Outras Ações','Componentes duplicados')
        self.oHelper.WaitHide('Itens em duplicidade')       
        self.oHelper.ClickBox("Código", "02.01")
        self.oHelper.ClickBox("Código", "02.02")
        self.oHelper.ClickBox("Código", "02.03")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.AssertTrue()

    def test_FATA530_CT019(self):
        '''
        CT019 - Configuração de atalhos na Proposta de Serviços (PMS)
        '''
        Opportunity = '000286'
        Proposal = '000284'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')        
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")        
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')        
        self.oHelper.ClickGridCell("No.Projeto", row=2, grid_number=1)
        self.oHelper.ClickBox("Versão", "002")
        self.oHelper.WaitShow('Proposta de servicos')
        self.oHelper.SetButton('Outras Ações','Atalhos')        
        self.oHelper.SetValue("Acesso Directo","CTRL+A", row=1,grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetFocus("AF1_ORCAME")
        self.oHelper.SetKey(key="CTRL", additional_key="A")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.AssertTrue()

    def test_FATA530_CT020(self):
        '''
        CT020 - Cancelamento da Criação de Orçamento de Projeto via Proposta de Serviços (PMS)
        '''
        Opportunity = '000286'
        
        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial') 
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetValue("ADY_CONDPG","001")
        self.oHelper.SetValue("ADY_TES","501")
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')
        self.oHelper.ClickLabel('Proposta de servicos')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case. 
        """
        self.oHelper.TearDown()  


if __name__ == "__main__":
    unittest.main()