from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest
import time


class CRMA290(unittest.TestCase):
    Contr = ""

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()
        inst.oHelper.SetTIRConfig(config_name="User", value="APICRM")
        inst.oHelper.SetTIRConfig(config_name="Password", value="1")

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGACRM", DataSystem,"T1","D MG 01 ","73")
        

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("CRMA290")

    def test_CRMA290_CT001(self):
        '''
        Test Case 001
        '''
        #self.oHelper.SetButton("Não")

        time.sleep(15)

        self.oHelper.ClickLabel("+ Criar Oportunidade")

        NumOpt = self.oHelper.GetValue("AD1_NROPOR")
        self.oHelper.SetValue("AD1_DESCRI", "INCLUSAO TIR AT")
        self.oHelper.SetValue("AD1_DTINI",DataSystem)
        self.oHelper.SetValue("AD1_CODCLI","FATT01")
        self.oHelper.SetValue("AD1_LOJCLI","01")
        self.oHelper.SetValue("AD1_PROVEN","FAT001")
        self.oHelper.SetValue("AD1_STAGE","000002")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow("Minhas Oportunidades")
        
        self.oHelper.ClickLabel("Minhas Oportunidades")
       
        self.oHelper.WaitHide("Minhas Oportunidades")
        self.oHelper.SearchBrowse(f"D MG 01 {NumOpt}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AD1_NROPOR", NumOpt)
        self.oHelper.CheckResult("AD1_DESCRI", "INCLUSAO TIR AT")
        self.oHelper.CheckResult("AD1_CODCLI","FATT01")
        self.oHelper.CheckResult("AD1_LOJCLI","01")
        self.oHelper.CheckResult("AD1_PROVEN","FAT001")
        self.oHelper.CheckResult("AD1_STAGE","000002")

        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")

        self.oHelper.AssertTrue()

    def test_CRMA290_CT002(self):
        '''
        Test Case 002
        '''
        self.oHelper.WaitShow("Minhas Oportunidades")

        self.oHelper.ClickLabel("Minhas Oportunidades")

        NumOpt = '000273'

        self.oHelper.SearchBrowse(f"D MG 01 {NumOpt}")
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("AD1_DESCRI", "ALTERACAO TIR AT")
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SearchBrowse(f"D MG 01 {NumOpt}")
        self.oHelper.SetButton("Alterar")

        self.oHelper.ClickFolder('Produtos')

        self.oHelper.SetValue("ADJ_PROD", "FAT004", grid=True, row=1)
        self.oHelper.SetValue("ADJ_PRUNIT", "1,00", grid=True, row=1)

        self.oHelper.LoadGrid()

        self.oHelper.SetValue("AD1_DESCRI", "ALTERACAO 2 TIR AT")
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")    

        self.oHelper.SearchBrowse(f"D MG 01 {NumOpt}")
        self.oHelper.SetButton("Visualizar")            
        
        self.oHelper.CheckResult("AD1_NROPOR",NumOpt)
        self.oHelper.CheckResult("AD1_REVISA","02")

        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")

        self.oHelper.AssertTrue()          

    def test_CRMA290_CT003(self):
        '''
        Test Case 003
        '''
        self.oHelper.WaitShow("Oportunidade Rápida")

        self.oHelper.ClickLabel("Oportunidade Rápida")

        NumOpt = self.oHelper.GetValue("AD1_NROPOR")
        self.oHelper.SetValue("AD1_DESCRI", "INCLUSAO TIR AT")
        self.oHelper.SetValue("AD1_DTINI",DataSystem)
        self.oHelper.SetValue("AD1_CODCLI","FATT01")
        self.oHelper.SetValue("AD1_LOJCLI","01")
        self.oHelper.SetValue("AD1_PROVEN","FAT001")
        self.oHelper.SetValue("AD1_STAGE","000002")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow("Minhas Oportunidades")
        
        self.oHelper.ClickLabel("Minhas Oportunidades")
       
        self.oHelper.WaitHide("Minhas Oportunidades")
        self.oHelper.SearchBrowse(f"D MG 01 {NumOpt}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AD1_NROPOR", NumOpt)
        self.oHelper.CheckResult("AD1_DESCRI", "INCLUSAO TIR AT")
        self.oHelper.CheckResult("AD1_CODCLI","FATT01")
        self.oHelper.CheckResult("AD1_LOJCLI","01")
        self.oHelper.CheckResult("AD1_PROVEN","FAT001")
        self.oHelper.CheckResult("AD1_STAGE","000002")

        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")

        self.oHelper.AssertTrue()

    def test_CRMA290_CT004(self):
        '''
        Test Case 004
        '''
        time.sleep(15)
        self.oHelper.WaitShow("Minhas Oportunidades")

        self.oHelper.ClickLabel("Minhas Oportunidades")

        NumOpt = '000277'

        self.oHelper.SearchBrowse(f"D MG 01 {NumOpt}")
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetButton("Outras Ações","Proposta Comercial")
        self.oHelper.SetButton("Incluir")

        self.oHelper.SetValue("ADY_TABELA","API")
        self.oHelper.SetValue("ADY_CONDPG","000")
        self.oHelper.SetValue("ADY_TES","501")

        self.oHelper.SetValue("ADZ_PRODUT", "FAT001", grid=True)
        self.oHelper.SetValue("ADZ_PRCVEN", "100,00", grid=True)
        self.oHelper.LoadGrid()        
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("X")

        self.oHelper.SetValue("AD1_FCS", "000003")
        self.oHelper.SetValue("AD1_STATUS", "9 - Ganha")

        self.oHelper.ClickFolder("Aceite da proposta")
        self.oHelper.SetValue("AD1_DTASSI", DataSystem)
        self.oHelper.SetFocus("AD1_CNTPRO")
        self.oHelper.SetKey("F3")

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetValue("U5_CODCONT", "TIR001")
        self.oHelper.SetValue("U5_CONTAT", "Contato OP TIR")
        
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")

        time.sleep(15)
        self.oHelper.AssertTrue()        

    def test_CRMA290_CT005(self):
        '''
        Test Case 005 - Teste
        '''
        time.sleep(15)
        self.oHelper.WaitShow("Minhas Oportunidades")

        self.oHelper.ClickLabel("Minhas Oportunidades")

        NumOpt = '000275'

        #Alterar a tela de legenda para acrescentar o botão fechar.
        #self.oHelper.SetButton("Outras Ações","Legenda")
        #self.oHelper.SetButton("x")

        self.oHelper.SearchBrowse(f"D MG 01 {NumOpt}")
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetButton("Outras Ações","Legenda Evolução da Venda")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Outras Ações","Histórico da Oportunidade")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("ADC_NROPOR", '000275')
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")

        self.oHelper.SetButton("Outras Ações","Pendência Financeira")
        self.oHelper.SetButton("Ok")        

        self.oHelper.SetButton("Outras Ações","Avaliação Financeira")
        self.oHelper.SetButton("Ok")        

        self.oHelper.SetButton("Outras Ações","Análise do Custo")
        self.oHelper.SetButton("Parâmetro")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")
        self.oHelper.SetButton("X")        

        time.sleep(15)
        self.oHelper.AssertTrue()        

    def test_CRMA290_CT006(self):
        '''
        Test Case 006 - Teste
        '''
        time.sleep(15)
        self.oHelper.WaitShow("Minhas Oportunidades")

        self.oHelper.ClickLabel("Minhas Oportunidades")
        
        time.sleep(15)
        self.oHelper.WaitShow("Oportunidade de Venda:")

        NumOpt = '000275'

        #Alterar a tela de legenda para acrescentar o botão fechar.
        #self.oHelper.SetButton("Outras Ações","Legenda")
        #self.oHelper.SetButton("x")

        self.oHelper.SearchBrowse(f"D MG 01 {NumOpt}")

        self.oHelper.SetButton("Outras Ações","Comparar")
        self.oHelper.ClickGridCell("Revisao",row=1)
        self.oHelper.ClickBox("Revisao", "01")
        self.oHelper.ClickGridCell("Revisao",row=2)
        self.oHelper.ClickBox("Revisao", "02")
        self.oHelper.SetButton("Ok")

        self.oHelper.WaitShow("COMPARAR")

        self.oHelper.SetButton("Outras Ações","Legenda")
        time.sleep(15)
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Outras Ações","Próx.Dif") 
        self.oHelper.SetButton("Outras Ações","Dif.Ant.")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("X")

        time.sleep(15)
        self.oHelper.AssertTrue()        

    def test_CRMA290_CT007(self):
        '''
        Test Case 007 - Teste
        '''
        time.sleep(15)
        self.oHelper.WaitShow("Criar Painel")

        self.oHelper.ClickLabel("Criar Painel")
        self.oHelper.SetButton("Sim")

        self.oHelper.WaitShow("Configuração")

        self.oHelper.SetButton("Avançar >>")

        self.oHelper.SetValue("Digite o nome do Painel:","TIR001")        
        self.oHelper.SetButton("Avançar >>")

        self.oHelper.SetValue("cCbxOpcs1","Tabela",name_attr = True)
        self.oHelper.SetValue("cCbxAlias1","SA1 - Clientes", name_attr = True)

        self.oHelper.SetValue("cCbxOpcs2","Gráfico", name_attr = True)
        self.oHelper.SetValue("cCbxAlias2","SA1 - Clientes", name_attr = True)
        
        self.oHelper.SetButton("Avançar >>")

        self.oHelper.SetButton("Avançar >>")

        self.oHelper.SetButton("Finalizar")

        self.oHelper.SetButton("Sim")
        
        time.sleep(15)
        self.oHelper.AssertTrue()     

    def test_CRMA290_CT008(self):
        '''
        Test Case 008 - Meus Pedidos
        '''
        self.oHelper.WaitShow("Minhas Oportunidades")

        self.oHelper.ClickLabel("Meus Pedidos")

        self.oHelper.SetButton("X")

        self.oHelper.AssertTrue()              
        
    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
