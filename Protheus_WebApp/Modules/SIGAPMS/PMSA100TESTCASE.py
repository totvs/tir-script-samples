from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest
import time


class PMSA100(unittest.TestCase):
    Contr = ""

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAPMS", DataSystem,"T1","D MG 01 ","44")
        

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("PMSA100")

    def test_PMSA100_CT001(self):
        '''
        Test Case 001 - GTSER-T42255
        '''

        NumOrc = "TIR0000001"

        self.oHelper.SetButton("Outras Ações","Legenda")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("AF1_ORCAME", NumOrc)
        self.oHelper.SetValue("AF1_DESCRI",'INCLUSAO TIR')
        self.oHelper.SetValue("AF1_VALID", DataSystem)
        self.oHelper.SetValue("AF1_CLIENT","FAT001")
        self.oHelper.SetValue("AF1_LOJA","01")
        self.oHelper.SetValue("AF1_TPORC","0001")
     
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {NumOrc}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AF1_ORCAME", NumOrc)
        self.oHelper.CheckResult("AF1_DESCRI",'INCLUSAO TIR')
        self.oHelper.CheckResult("AF1_VALID", DataSystem)
        self.oHelper.CheckResult("AF1_CLIENT","FAT001")
        self.oHelper.CheckResult("AF1_LOJA","01")
        self.oHelper.CheckResult("AF1_TPORC","0001")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_PMSA100_CT002(self):
        '''
        Test Case 002 - GTSER-T42256
        '''

        NumOrc = "TIR0000999"

        self.oHelper.SearchBrowse(f"D MG 01 {NumOrc}")

        self.oHelper.SetButton("Alt.Cadastro")
        
        self.oHelper.SetValue("AF1_DESCRI",'ALTERACAO ORCAMENTO TIR')
        self.oHelper.SetValue("AF1_VALID", DataSystem)

        self.oHelper.SetButton("Salvar")

        self.oHelper.SearchBrowse(f"D MG 01 {NumOrc}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AF1_DESCRI",'ALTERACAO ORCAMENTO TIR')

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()        

    def test_PMSA100_CT003(self):
        '''
        Test Case 003 - GTSER-T42257
        '''

        NumOrc = "TIR0000999"

        self.oHelper.SearchBrowse(f"D MG 01 {NumOrc}")

        self.oHelper.SetButton("Outras Ações", "Usuarios")
        
        self.oHelper.SetButton("Outras Ações","Informacoes do Orcamento")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()  

    def test_PMSA100_CT004(self):
        '''
        Test Case 004 - GTSER-T42258
        '''

        NumOrc = "TIR0000999"

        self.oHelper.SearchBrowse(f"D MG 01 {NumOrc}")

        self.oHelper.SetButton("Outras Ações", "Alt.estRutura")
        self.AjustaAtalho()
        self.oHelper.SetKey(key="CTRL", additional_key="M") #Procurar CTRL+M
        self.oHelper.SetValue("Procurar por:", NumOrc)
        self.oHelper.SetButton("Procurar")
        self.oHelper.SetFocus("AF5_DESCRI")
        self.oHelper.SetFocus("AF5_DESCRI")
        self.oHelper.SetKey(key="CTRL", additional_key="Y") #Incluir EDT CTRL+Y
        self.oHelper.WaitShow("EDT do Orcamento")
        self.oHelper.SetValue("AF5_DESCRI", "INCLUSAO EDT TIR")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetKey(key="CTRL", additional_key="M") #Procurar CTRL+M        
        self.oHelper.SetValue("Procurar por:", 'INCLUSAO EDT TIR')
        self.oHelper.SetButton("Procurar")        
        self.oHelper.ClickFolder("Edt")
        self.oHelper.ClickFolder("Edt")
        self.oHelper.SetKey(key="CTRL", additional_key="H") #Incluir Tarefa CTRL+H        
        self.oHelper.SetValue("AF2_DESCRI", "INCLUSAO TAREFA TIR")

        self.oHelper.ClickFolder("Produtos")
        self.oHelper.SetValue("Produto", "FAT001" , grid=True)
        self.oHelper.SetValue("Quantidade"  , "1,0000"          , grid=True)
        self.oHelper.LoadGrid()        

        self.oHelper.ClickFolder("Despesas")
        self.oHelper.SetValue("Tipo Despesa", "0001" , grid=True)
        self.oHelper.SetValue("Descricao"  , "TESTE" , grid=True)
        self.oHelper.SetValue("Valor"  , "10,00" , grid=True)
        self.oHelper.LoadGrid()                

        self.oHelper.ClickFolder("Recursos")
        self.oHelper.SetValue("Cod. Recurso", "PMS000000000001" , grid=True)
        self.oHelper.SetValue("Quantidade"  , "1,0000" , grid=True)
        self.oHelper.LoadGrid()         

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    def test_PMSA100_CT005(self):
        '''
        Test Case 005 - GTSER-T42261
        '''

        NumOrc = "TIR0000999"

        self.oHelper.SearchBrowse(f"D MG 01 {NumOrc}")

        self.oHelper.SetButton("Outras Ações", "Alt.estRutura")
        self.AjustaAtalho()
        time.sleep(15)
        self.oHelper.ClickFolder("Orcamento")
        self.oHelper.ClickFolder("Orcamento")
        self.oHelper.SetKey(key="CTRL", additional_key="J") #Procurar CTRL+M
        self.oHelper.SetValue("Produto De ?", 'FAT001')
        self.oHelper.SetValue("Produto Ate ?", 'FAT001')
        self.oHelper.SetButton("Ok")        
        time.sleep(5)

        self.oHelper.ClickFolder("Orcamento")
        self.oHelper.ClickFolder("Orcamento")
        self.oHelper.SetKey(key="CTRL", additional_key="J") #Procurar CTRL+J
        self.oHelper.ClickLabel('Aplicar Percentual')
        self.oHelper.SetValue("Produto De ?", 'FAT001')
        self.oHelper.SetValue("Produto Ate ?", 'FAT001')
        self.oHelper.SetButton("Ok")        
        #self.oHelper.SetValue("Percentual Reajuste ?", '10,00') 
        self.oHelper.SetButton("Cancelar")        
        time.sleep(5)

        self.oHelper.SetKey(key="CTRL", additional_key="K") #Procurar CTRL+K
        time.sleep(5)
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()  

    def test_PMSA100_CT006(self):
        '''
        Test Case 006 - GTSER-T42263
        '''

        NumOrc = "TIR0000002"

        self.oHelper.SearchBrowse(f"D MG 01 {NumOrc}")

        self.oHelper.SetButton("Outras Ações", "Excluir")
        
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()  

    def test_PMSA100_CT007(self):
        '''
        Test Case 007 - GTSER-T42264
        '''

        NumOrc = "TIR000003"

        self.oHelper.SearchBrowse(f"D MG 01 {NumOrc}")

        self.oHelper.SetButton("Outras Ações", "Alt.estRutura")
        self.AjustaAtalho()
        self.oHelper.SetKey(key="CTRL", additional_key="U") #Procurar CTRL+U
        self.oHelper.ClickLabel('Substituir Produtos')
        self.oHelper.SetValue("Produto Atual:", 'FAT001')
        self.oHelper.SetValue("Novo Produto:", 'FAT000000000000000000000000001')
        self.oHelper.ClickLabel('Substituir Recursos')
        self.oHelper.SetValue("Recurso Atual:", 'PMS000000000001')
        self.oHelper.SetValue("Novo Recurso:", 'PMS000000000002')

        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    def AjustaAtalho(self):
        time.sleep(10)
        self.oHelper.SetButton("Outras Ações", "Atalhos")
        self.oHelper.SetValue("Acesso Directo",'CTRL+U', grid=True, row=5)
        self.oHelper.SetValue("Acesso Directo",'CTRL+Y', grid=True, row=7)
        self.oHelper.SetValue("Acesso Directo",'CTRL+H', grid=True, row=8)
        self.oHelper.SetValue("Acesso Directo",'CTRL+M', grid=True, row=17)
        self.oHelper.SetValue("Acesso Directo",'CTRL+B', grid=True, row=18)
        self.oHelper.SetValue("Acesso Directo",'CTRL+J', grid=True, row=2)
        self.oHelper.SetValue("Acesso Directo",'CTRL+K', grid=True, row=3)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
