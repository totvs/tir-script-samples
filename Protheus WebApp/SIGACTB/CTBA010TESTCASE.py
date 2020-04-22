from tir import Webapp
import unittest


class CTBA010(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "01/04/2016", "T1", "D MG 01 ", "34")
        inst.oHelper.Program("CTBA010")

     
    def test_CTBA010_001(self):

        self.oHelper.WaitShow("Cadastro Calendário Contábil")

        self.oHelper.SetKey("F12") #abri o wizard de parâmetro

        self.oHelper.SetValue("Tipo da Interface ?","Assistente") #Seleciona o modo assistente para inclusão 

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Avançar")

        self.oHelper.SetValue("Data Inicial ?","01/01/2098") 

        self.oHelper.SetValue("Data Final ?","31/12/2098")

        self.oHelper.SetButton("Avançar")

        self.oHelper.SetButton("Avançar")

        self.oHelper.SetButton("Avançar")

        self.oHelper.SetValue("Calendario ?","298")

        self.oHelper.SetValue("Exercicio Contabil ?","2098")

        self.oHelper.ClickCheckBox("Amarrar Calendario com Moedas",1)

        self.oHelper.SetButton("Avançar")

        self.oHelper.SetButton("Finalizar")

        self.oHelper.SetButton("Avançar")   #wizard de amarração da moeda

        self.oHelper.SetButton("Finalizar")

        self.oHelper.SetButton("Sim")

        self.oHelper.SearchBrowse("D MG 01 298") #filtra o calendário criado na tela
        
        self.oHelper.SetButton("Visualizar") 
        
        #na opcao de visualizar clica nos itens da arvore para expandir o conteudo
        self.oHelper.ClickTree("298 - Exercicio : 2098 > Periodo 01 de : 01/01/2098 ate : 31/01/2098", right_click=True)

        #checando os valores do resultado esperado
        self.oHelper.CheckResult('CTG_CALEND','298',name_attr=True)
        self.oHelper.CheckResult('CTG_EXERC','2098',name_attr=True)
        self.oHelper.CheckResult('CTG_PERIOD','01',name_attr=True)
        self.oHelper.CheckResult('CTG_DTINI','01/01/2098',name_attr=True)
        self.oHelper.CheckResult('CTG_DTFIM','31/01/2098',name_attr=True)
        self.oHelper.CheckResult('CTG_STATUS','1 - Aberto',name_attr=True)

        self.oHelper.SetButton("x")

        self.oHelper.SetButton("x") #volta para a tela principal para inicio automatico de novo caso de teste

        self.oHelper.AssertTrue()

    def test_CTBA010_002(self):

        self.oHelper.SearchBrowse("D MG 01 297") #seleciona registro criado na base congelada
        
        self.oHelper.SetButton("Outras Ações","Excluir") #clica no botao excluir

        self.oHelper.SetButton("Ok")

        self.oHelper.SearchBrowse("D MG 01 297") #faz a pesquisa pelo registro que foi excluido

        self.oHelper.SetButton("Alterar") #com o registro filtrado seleciona a opcao alterar para validacao dos valores

        #verificando se o registro encontrado é igual ao excluido
        self.oHelper.CheckResult('cCalendCTB','297',name_attr=True)
        self.oHelper.CheckResult('cExerc','2097',name_attr=True)

        self.oHelper.SetButton("x") # voltando para a tela principal para inicio de novos casos de teste

        self.oHelper.AssertFalse() #como os dados encontrados não devem ser iguais ao do registro excluido usado assertfalse

    def test_CTBA010_003(self):
       
        self.oHelper.SearchBrowse("D MG 01 296")    #seleciona registro criado na base congelada

        self.oHelper.SetButton("Outras Ações","Bloqueio de Processo") 

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse("D MG 01 296")

        self.oHelper.SetButton("Outras Ações","Bloqueio Automático")

        self.oHelper.SetValue("Data Inicial ?","01/01/2096") #setando os valores para o bloqueio automatico

        self.oHelper.SetValue("Data Final ?","28/02/2096")

        self.oHelper.SetValue("Processo Inicial ?","ATF001")

        self.oHelper.SetValue("Processo Final ?","ATF001")

        self.oHelper.SetValue("Status ?","Bloqueado")

        self.oHelper.SetValue("Seleciona Filial ?","Não")

        self.oHelper.SetButton("Ok")

        self.oHelper.SearchBrowse("D MG 01 296")

        self.oHelper.SetButton("Outras Ações","Visualizar Bloqueio") #entra na tela de visualização de bloqueio para validar os valores

        self.oHelper.WaitShow("Bloqueio de Processo - Visualização - Bloqueio de Processo") #força o robo esperar o conteudo da tela carregar

        #checando valor esperado 
        self.oHelper.CheckResult('Status bloq.','Bloqueado',grid=True,line=1,grid_number=2,name_attr=False)
        self.oHelper.LoadGrid() #para verificação de valor de grid se faz necessario usar função LoadGrid

        self.oHelper.SetButton("Fechar") #Volta para a tela inicial

        self.oHelper.AssertTrue()



    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
