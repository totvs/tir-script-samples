from tir import Webapp 
import unittest

class PCOXDIV(unittest.TestCase):

    @classmethod
    def setUpClass(inst): 
        inst.oHelper = Webapp()
        inst.oHelper.SetTIRConfig(config_name="User",value="PCO1")
        inst.oHelper.SetTIRConfig(config_name="Password",value="a")
        inst.oHelper.Setup('SIGAPCO', '19/08/2020', 'T1', 'M SP 01 ')
        inst.oHelper.Program('PCOA100')

    def test_PCOXDIV_CT001(self): 

        self.oHelper.WaitShow("Planilha Orcamentaria")

        self.oHelper.WaitShow("Planilha Orcamentaria")
        self.oHelper.SetKey( key = "F12", wait_show="Tipo Exibição ? ?", step = 3)
        self.oHelper.SetValue("Tipo Exibição ? ? ","1 - Completa")
        self.oHelper.SetButton("Ok")

        codigoCT005 = 'TIRPCOA100     '
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}0001')

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}0001')

        self.oHelper.SetButton('Alterar')
        self.oHelper.SetButton('Fechar')

        codigoCT005 = 'TIRPCO1002     '
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}0001')
                        
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetFocus("Descricao", grid_cell=True, row_number=2)
        self.oHelper.ClickGridCell("Descricao", row=4,grid_number=1)

        self.oHelper.SetButton("Editar",position=1)

        self.oHelper.ClickGridCell("Item Contab.", row=1, grid_number=2)
        self.oHelper.SetKey("F3",grid=True, grid_number=2)
        self.oHelper.SetButton('Cancelar')

        self.oHelper.ClickGridCell("Classe Valor", row=1, grid_number=2)
        self.oHelper.SetKey("F3",grid=True, grid_number=2)
        self.oHelper.SetButton('Cancelar')

        self.oHelper.ClickGridCell("Classe Orc.", row=1, grid_number=2)
        self.oHelper.SetKey("F3",grid=True, grid_number=2)
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Cancelar') 

        self.oHelper.SetButton('Sim') 

        self.oHelper.AssertTrue()
    
    def test_PCOXDIV_CT002(self): 

        codigoCT005 = 'TIRPCO1003     '

        self.oHelper.WaitShow("Planilha Orcamentaria")


        self.oHelper.SetKey( key = "F12", wait_show="Tipo Exibição ? ?", step = 3)
        self.oHelper.SetValue("Tipo Exibição ? ? ","4 - Espec.Campos")
        self.oHelper.SetButton("Ok")

        #POSICIONA NO REGISTRO
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}0001')

        self.oHelper.SetButton("Alterar")

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Nao")

        self.oHelper.ClickGridCell("Classe Orc.", row=1, grid_number=1)
        self.oHelper.SetKey("F3",grid=True, grid_number=1)
        self.oHelper.SearchBrowse(f'PCO3')
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton(">")

        # self.oHelper.SetButton("Ok")  ###Intermitencia hora aparece hora nao

        self.oHelper.WaitShow("Planilha Orcamentaria - ALTERAR")
        
        self.oHelper.SetButton("Editar")

        self.oHelper.ClickGridCell("Centro Custo", row=1, grid_number=2)
        self.oHelper.ClickGridCell("Classe Valor", row=1, grid_number=2)

        self.oHelper.SetButton('Salvar') 

        self.oHelper.SetButton('Sim') 

        self.oHelper.SetButton('Sim') 

        self.oHelper.SetButton('Cancelar') 

        self.oHelper.AssertTrue()

    def test_PCOXDIV_CT003(self): 

        self.oHelper.WaitShow("Planilha Orcamentaria")

        #POSICIONA NO REGISTRO
        codigoCT005 = 'TIRPCO1003     '
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}0001')

        self.oHelper.WaitShow("Planilha Orcamentaria")

        #REPOSICIONA NO REGISTRO
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}0001')
                        
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetFocus("Descricao", grid_cell=True, row_number=2)
        self.oHelper.SetFocus("Descricao", grid_cell=True, row_number=4)

        #Por percentual embutido Somar
        self.oHelper.SetButton('Outras Ações', 'Ferram.') 
        self.oHelper.ClickMenuPopUpItem("Reajustar Valores Orcados")
        self.oHelper.SetValue("Por Percentual Embutido", True)
        self.oHelper.SetValue("Somar", True)
        self.oHelper.SetButton("Ok")

        self.oHelper.WaitShow("Planilha Orcamentaria - ALTERAR")

        #Por percentual embutido Diminuir
        self.oHelper.SetButton('Outras Ações', 'Ferram.') 
        self.oHelper.ClickMenuPopUpItem("Reajustar Valores Orcados")
        self.oHelper.SetValue("Por Percentual Embutido", True)
        self.oHelper.SetValue("Diminuir", True)
        self.oHelper.SetButton("Ok")

        self.oHelper.WaitShow("Planilha Orcamentaria - ALTERAR")

        #Por Valor Somar
        self.oHelper.SetButton('Outras Ações', 'Ferram.') 
        self.oHelper.ClickMenuPopUpItem("Reajustar Valores Orcados")
        self.oHelper.SetValue("Por Valor", True)
        self.oHelper.SetValue("Somar", True)
        self.oHelper.SetButton("Ok")

        self.oHelper.WaitShow("Planilha Orcamentaria - ALTERAR")

        #Por Valor Diminuir
        self.oHelper.SetButton('Outras Ações', 'Ferram.') 
        self.oHelper.ClickMenuPopUpItem("Reajustar Valores Orcados")
        self.oHelper.SetValue("Por Valor", True)
        self.oHelper.SetValue("Diminuir", True)
        self.oHelper.SetButton("Ok")

        self.oHelper.WaitShow("Planilha Orcamentaria - ALTERAR")

        #Por Valor Substituir Valor
        self.oHelper.SetButton('Outras Ações', 'Ferram.') 
        self.oHelper.ClickMenuPopUpItem("Reajustar Valores Orcados")
        self.oHelper.SetValue("Por Valor", True)
        self.oHelper.SetValue("Substituir Valor", True)
        self.oHelper.SetButton("Ok")

        self.oHelper.WaitShow("Planilha Orcamentaria - ALTERAR")

        self.oHelper.SetButton('Cancelar') 

        self.oHelper.AssertTrue()
    
    def test_PCOXDIV_CT004(self): 

        self.oHelper.WaitShow("Planilha Orcamentaria")

        self.oHelper.SetKey( key = "F12", wait_show="Tipo Exibição ? ?", step = 3)
        self.oHelper.SetValue("Tipo Exibição ? ?","4 - Espec.Campos")
        self.oHelper.SetButton("Ok")

        #POSICIONA NO REGISTRO
        codigoCT005 = 'TIRPCO1003     '
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}0001')
                        
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Nao")

        self.oHelper.SetFocus("C.O.", grid_cell=True, row_number=1)
        self.oHelper.SearchBrowse(f'TIRANALI')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton(">")

        self.oHelper.WaitShow("Planilha Orcamentaria - ALTERAR")

        self.oHelper.ClickGridCell("Centro Custo", row=1, grid_number=2)
        self.oHelper.SetKey('F3',grid=True, grid_number=2)
        self.oHelper.SetButton("Ok")

        self.oHelper.ClickGridCell("Classe Valor", row=1, grid_number=2)
        self.oHelper.SetKey('F3',grid=True, grid_number=2)
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton('Sim') 

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton('Não') 

        self.oHelper.AssertTrue()


    def test_PCOXDIV_CT005(self):

        self.oHelper.WaitShow("Planilha Orcamentaria")

        #POSICIONA NO REGISTRO
        codigoCT005 = 'PCOA110'
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}')

        self.oHelper.SetButton("Alterar")

        self.oHelper.SetFocus("Descricao", grid_cell=True, row_number=1)
        # self.oHelper.SetFocus("Descricao", grid_cell=True, row_number=2)
        self.oHelper.SetKey( key = "UP",grid=True)
        self.oHelper.ClickGridCell("Descricao", row=2, grid_number=1)
        self.oHelper.SetButton('Confirmar') 

        self.oHelper.AssertTrue()

    def test_PCOXDIV_CT006(self):

        self.oHelper.WaitShow("Planilha Orcamentaria")

        self.oHelper.SetButton('X')
        self.oHelper.Program('PCOA200')

        self.oHelper.SearchBrowse("M SP 01 PCOA200USPCO1")
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetFocus("Descricao",grid_cell=True,row_number=2)
        self.oHelper.ClickGridCell("Descricao", row=3,grid_number=1)

        self.oHelper.SetButton('Editar')
        self.oHelper.SetValue("Item Contab.", "PCOA200",grid=True,grid_number=2,row=1)
        self.oHelper.SetValue("Classe Orc.", "FORMT4",grid=True,grid_number=2,row=1)

        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Gravar')

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton('X')
        self.oHelper.Program('PCOA100')

        self.oHelper.AssertTrue()

    def test_PCOXDIV_CT007(self):

        self.oHelper.WaitShow("Planilha Orcamentaria")

        #POSICIONA NO REGISTRO
        codigoCT005 = 'PCOA110'
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}')

        self.oHelper.SetKey( key = "F12", wait_show="Tipo Exibição ? ?", step = 3)
        self.oHelper.SetValue("Tipo Exibição ? ?","4 - Espec.Campos")
        self.oHelper.SetButton("Ok")

        #botao de alterar
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Nao")

        #Executando filtro vazio
        self.oHelper.SetButton(">")

        #Não digitado nenhum campo para seleção - entrar em modo  de ?
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Cancelar")

        #Abandonar edição dos itens orçamentarios na grid ?
        self.oHelper.SetButton("Sim")
        
        self.oHelper.SetButton("Salvar")

        #Edição em modo completo da planilha
        self.oHelper.SetButton("Não")

        self.oHelper.AssertTrue()

    def test_PCOXDIV_CT008(self): 

        self.oHelper.WaitShow("Planilha Orcamentaria")

        self.oHelper.SetKey( key = "F12", wait_show="Tipo Exibição ? ?", step = 3)
        self.oHelper.SetValue("Tipo Exibição ? ?","4 - Espec.Campos")
        self.oHelper.SetButton("Ok")

        #POSICIONA NO REGISTRO
        codigoCT005 = 'TIROPC4DELETARL'
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}0001')
                        
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Nao")

        self.oHelper.SetFocus("C.O.", grid_cell=True, row_number=1)
        self.oHelper.SearchBrowse(f'CONTAORPCO1')
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton(">")

        self.oHelper.WaitShow("Planilha Orcamentaria - ALTERAR")

        self.oHelper.SetButton("Editar")

        self.oHelper.ClickGridCell("Classe Valor", row=2, grid_number=2)
        self.oHelper.SetKey('Delete',grid=True, grid_number=2)
        self.oHelper.SetButton("Gravar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  


if __name__ == "__main__":
    unittest.main()