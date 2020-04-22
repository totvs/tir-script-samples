from tir import Webapp
import unittest


class PCOA160(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAPCO", "06/04/2020", "T1", "D MG 01 ")
        inst.oHelper.Program("PCOA160")

     
    def test_PCOA160_001(self):
        #protege os testes para serem rodados apens no release 12.1.30
        if self.oHelper.GetRelease() > '12.1.027':

            self.oHelper.SearchBrowse("D MG 01 001") #filtra o processo de sistema

            self.oHelper.SetButton("Alterar")

            self.oHelper.CheckHelp(text='Registro de Configuracao de Sistema Nao deve ser alterado ou excluido', button='Fechar')

            self.oHelper.AssertTrue()

    def test_PCOA160_002(self):
        #protege os testes para serem rodados apens no release 12.1.30
        if self.oHelper.GetRelease() > '12.1.027':

            self.oHelper.SetButton("Incluir")

            self.oHelper.SetButton("Ok")

            self.oHelper.SetValue("Configuracao","099")

            self.oHelper.SetValue("Descricao","FILTRO POR CUBO")

            self.oHelper.SetValue("Codigo Cubo","02")

            self.oHelper.SetValue("AKL_UTILIZ","3 - Visoes por Cubo",name_attr=True)

            self.oHelper.SetButton("Outras Ações", "Cpo/Cubo")
        
            self.oHelper.SetFocus("Campo Ref.",grid_cell=True,row_number=1)

            self.oHelper.SetKey("F3",grid=True)

            self.oHelper.SetButton("Cancelar")

            self.oHelper.SetFocus("Campo Filtro",grid_cell=True,row_number=1)

            self.oHelper.SetKey("F3",grid=True)

            self.oHelper.SetButton("Cancelar")

            self.oHelper.ClickGridCell("Tipo", 1)

            self.oHelper.SetButton("Outras Ações", "Cons.Padrao")

            self.oHelper.CheckHelp(text='NO_CONPAD', button='Fechar')
            
            self.oHelper.ClickGridCell("Valor Inicio", 1)

            self.oHelper.SetButton("Outras Ações", "Cons.Padrao")

            self.oHelper.SearchBrowse("01")

            self.oHelper.SetButton("Visualizar")

            self.oHelper.SetButton("Fechar")

            self.oHelper.SetButton("Ok")

            self.oHelper.ClickGridCell("Valor Final", 1)

            self.oHelper.SetButton("Outras Ações", "Cons.Padrao")

            self.oHelper.SearchBrowse("01")

            self.oHelper.SetButton("Ok")

            self.oHelper.SetButton("Salvar")

            self.oHelper.WaitShow("Cadastro de Configuracoes de Visao Gerencial - PCO - INCLUIR")

            self.oHelper.SetButton("Cancelar")

            self.oHelper.SearchBrowse("D MG 01 099")

            self.oHelper.SetButton("Visualizar")

            self.oHelper.CheckResult('AKL_CONFIG','099',name_attr=True)
            self.oHelper.CheckResult('AKL_DESCRI','FILTRO POR CUBO',name_attr=True)
            self.oHelper.CheckResult('AKL_CUBE', '02',name_attr=True)

            self.oHelper.CheckResult('Titulo','CO',grid=True,line=1,grid_number=1,name_attr=False)
            self.oHelper.CheckResult('Titulo','Centro de Custo',grid=True,line=2,grid_number=1,name_attr=False)
            self.oHelper.CheckResult('Titulo','TP.SALDO',grid=True,line=3,grid_number=1,name_attr=False)
            self.oHelper.LoadGrid() #para verificação de valor de grid se faz necessario usar função LoadGrid

            self.oHelper.SetButton("Cancelar")
            
            self.oHelper.AssertTrue()

    def test_PCOA160_003(self):
        #protege os testes para serem rodados apens no release 12.1.30
        if self.oHelper.GetRelease() > '12.1.027':

            self.oHelper.SearchBrowse("D MG 01 098")

            self.oHelper.SetButton("Outras Ações", "Excluir")

            self.oHelper.SetButton("Confirmar")

            self.oHelper.SearchBrowse("D MG 01 098")

            self.oHelper.SetButton("Visualizar")

            self.oHelper.CheckResult('AKL_CONFIG','098',name_attr=True)
            self.oHelper.CheckResult('AKL_DESCRI','FILTRO POR CUBO',name_attr=True)
            self.oHelper.CheckResult('AKL_CUBE', '02',name_attr=True)

            self.oHelper.CheckResult('Titulo','CO',grid=True,line=1,grid_number=1,name_attr=False)
            self.oHelper.CheckResult('Titulo','Centro de Custo',grid=True,line=2,grid_number=1,name_attr=False)
            self.oHelper.CheckResult('Titulo','TP.SALDO',grid=True,line=3,grid_number=1,name_attr=False)
            self.oHelper.LoadGrid() #para verificação de valor de grid se faz necessario usar função LoadGrid

            

            self.oHelper.SetButton("Cancelar")
            
            self.oHelper.AssertFalse()

    def test_PCOA160_004(self):
        #protege os testes para serem rodados apens no release 12.1.30
        if self.oHelper.GetRelease() > '12.1.027':

            self.oHelper.SearchBrowse("D MG 01 097")

            self.oHelper.SetButton("Alterar")

            self.oHelper.SetValue("Descricao","FILTRO POR CUBO ALTERADO")

            self.oHelper.SetValue("Codigo Cubo","50")

            self.oHelper.CheckHelp(text='REGNOIS',text_problem='Não existe registro relacionado a este código.', button='Fechar')

            self.oHelper.SetValue("Codigo Cubo","C1")

            self.oHelper.SetButton("Salvar")

            self.oHelper.SearchBrowse("D MG 01 097")

            self.oHelper.SetButton("Visualizar")

            self.oHelper.CheckResult('AKL_CONFIG','097',name_attr=True)
            self.oHelper.CheckResult('AKL_DESCRI','FILTRO POR CUBO ALTERADO',name_attr=True)
            self.oHelper.CheckResult('AKL_CUBE', 'C1',name_attr=True)

            self.oHelper.CheckResult('Titulo','CO',grid=True,line=1,grid_number=1,name_attr=False)
            self.oHelper.CheckResult('Titulo','Centro de Custo',grid=True,line=2,grid_number=1,name_attr=False)
            self.oHelper.CheckResult('Titulo','TP.SALDO',grid=True,line=3,grid_number=1,name_attr=False)
            self.oHelper.LoadGrid() #para verificação de valor de grid se faz necessario usar função LoadGrid

            self.oHelper.SetButton("Cancelar")
            
            self.oHelper.AssertTrue()

    def test_PCOA160_005(self):
        #protege os testes para serem rodados apens no release 12.1.30
        if self.oHelper.GetRelease() > '12.1.027':

            self.oHelper.SearchBrowse("D MG 01 001") #filtra o processo de sistema

            self.oHelper.SetButton("Outras Ações","Copiar")

            self.oHelper.SetValue("MV_PAR01","")

            self.oHelper.SetButton("Ok")

            self.oHelper.CheckHelp(text='OBRIGAT',text_problem='Um ou mais campos obrigatórios não foram preenchidos. xxxxxxxxxxxxxxxxxx -> xxxxxxxxxx Campo : Copiar Cfg.: 001 >> Nova Config.Parametros Visão', button='Fechar')

            self.oHelper.SetValue("MV_PAR01","096")

            self.oHelper.SetButton("Ok")

            self.oHelper.SetButton("Fechar")

            self.oHelper.SearchBrowse("D MG 01 096")

            self.oHelper.SetButton("Visualizar")

            self.oHelper.CheckResult('AKL_CONFIG','096',name_attr=True)
            self.oHelper.CheckResult('AKL_DESCRI','VISAO ORCAMENTARIA',name_attr=True)
            self.oHelper.CheckResult('AKL_CUBE', '',name_attr=True)

            self.oHelper.CheckResult('Titulo','Planilha Orct.',grid=True,line=1,grid_number=1,name_attr=False)
            self.oHelper.CheckResult('Titulo','Versao',grid=True,line=2,grid_number=1,name_attr=False)
            self.oHelper.CheckResult('Titulo','Conta Orcamentaria',grid=True,line=3,grid_number=1,name_attr=False)
            self.oHelper.CheckResult('Titulo','Classe Orcamentaria',grid=True,line=4,grid_number=1,name_attr=False)
            self.oHelper.LoadGrid() #para verificação de valor de grid se faz necessario usar função LoadGrid

            self.oHelper.SetButton("Cancelar")
            
            self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
