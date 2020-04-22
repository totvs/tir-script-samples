from tir import Webapp
import unittest
from datetime import datetime
import time
DateSystem = datetime.today().strftime("%d/%m/%Y")

class PMSA200(unittest.TestCase):

    @classmethod
    def setUpClass(self): 
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAPMS", DateSystem, "T1", "D MG 01 ", "44")
        self.oHelper.Program("PMSA200") 

    def test_PMSA200_CT059(self):
        """
        Test Case CT059 - Inclusão de um projeto com troca de código 
        """
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("Projeto*", "TIRINC0001")
        self.oHelper.SetValue("Descricao*", "PROJETO TIR")
        self.oHelper.SetValue("Tipo Proj*", "0002")
        self.oHelper.ClickFolder("Cronograma")
        self.oHelper.SetValue("Calendario*", "001")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar") 
        self.oHelper.WaitShow("Gerenciamento de Projetos - Incluir")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Gerenciamento de Projetos") 
        self.oHelper.SearchBrowse("D MG 01 TIRINC0001", "Filial+projeto")
        self.oHelper.SetButton("Outras Ações", "Trocar Codigo")
        self.oHelper.SetValue("Novo Projeto:", "TIRALT0001")
        self.oHelper.SetButton("OK")
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 TIRALT0001", "Filial+projeto")
        self.oHelper.AssertTrue()

    def test_PMSA200_CT060(self):
        """
        Test Case CT060 - Alterar a estrutura do projeto incluindo uma nova tarefa / recursos
        """
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSRTIR001", "Filial+projeto")
        self.oHelper.SetButton("Outras Ações", "Alt.Estrutura")
        self.AjustaAtalho()
       
        self.oHelper.SetFocus("AF8_PROJET")
        time.sleep(5)
        self.oHelper.SetKey(key="CTRL", additional_key="M") #Procurar CTRL+M
        self.oHelper.SetValue("Procurar por:", "ALTERACAO DO PROJETO POR TIR")
        self.oHelper.SetButton("Procurar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetFocus("AF8_PROJET")
        time.sleep(5)
        self.oHelper.SetKey(key="CTRL", additional_key="B") #Procurar proxima CTRL+B
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetFocus("AF8_PROJET")
        time.sleep(5)
        self.oHelper.SetKey(key="CTRL", additional_key="Y") #Incluir      CTRL+Y
        self.oHelper.WaitShow("Tarefas do Projeto")
        self.oHelper.SetValue("Descricao*", "Tarefa TIR")
        self.oHelper.ClickFolder("Cronograma") 
        self.oHelper.SetValue("Dt.Ini. Prv.*", DateSystem)
        self.oHelper.SetValue("Dt.Fin. Prv.*", DateSystem)
        self.oHelper.SetButton("Data Inicial")
        self.oHelper.WaitShow("Tarefas do Projeto")
        
        self.oHelper.ClickFolder("Produtos")
        self.oHelper.SetValue("Cod.Produto" , "PMS000000000000000000000000001"  , grid=True)
        self.oHelper.SetValue("Quantidade"  , "1,0000"                          , grid=True)
        self.oHelper.SetValue("Dt. Necess." , DateSystem                        , grid=True)
        self.oHelper.LoadGrid()
       
        '''
        self.oHelper.ClickFolder("Despesas")
        self.oHelper.SetValue("Tipo Despesa" , "0004"                           , grid=True)
        self.oHelper.SetValue("Descricao"  , "DESPESAS TIR"                     , grid=True)
        self.oHelper.SetValue("Valor"  , "50,00"                                , grid=True)
        self.oHelper.LoadGrid()
        

        self.oHelper.ClickFolder("Relac.Tarefas")
        self.oHelper.SetValue("Predecessora"    , "01"                          , grid=True)
        self.oHelper.SetValue("Tipo"            , "1"                           , grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Recalcular")
        
        self.oHelper.ClickFolder("Eventos")
        self.oHelper.SetValue("Uso"             , "0005"                        , grid=True)
        self.oHelper.SetValue("Descricao"       , "EVENTOS TIR"                 , grid=True)
        self.oHelper.SetValue("Dt.Prevista"     , DateSystem                    , grid=True)
        self.oHelper.SetValue("%Perc. Exec."    , "50,00"                       , grid=True)
        self.oHelper.LoadGrid()
        
        self.oHelper.ClickFolder("Aloc. Recursos")
        self.oHelper.SetValue("Cod. Recurso", "PMS000000000001" , grid=True)
        self.oHelper.SetValue("Quantidade"  , "1,0000"          , grid=True)
        self.oHelper.SetValue("Dt. Necess." , DateSystem        , grid=True)
        self.oHelper.LoadGrid()
        '''
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitShow("Gerenciamento de Projetos - Alterar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.AssertTrue()

    def test_PMSA200_CT061(self):
        """
        Test Case CT061 - Excluir o projeto
        """
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSDTIR001", "Filial+projeto")
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.WaitShow("Gerenciamento de Projetos - Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Gerenciamento de Projetos") 
        self.oHelper.AssertTrue()

    def test_PMSA200_CT062(self):
        """
        Test Case CT062 - Alterar a fase do projeto
        """
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSRTIR002", "Filial+projeto")
        self.oHelper.SetButton("Outras Ações", "Alt.Fase")
        self.oHelper.SetValue("Nova fase:", "03")
        self.oHelper.SetButton("Salvar") 
        self.oHelper.AssertTrue()
    
    def AjustaAtalho(self): 
        time.sleep(10)
        self.oHelper.SetButton("Outras Ações", "Atalhos")
        self.oHelper.ScrollGrid(column="Opcoes", match_value="Incluir Tarefa")
        self.oHelper.SetValue("Acesso Directo",'CTRL+Y', grid=True) #Incluir Tarefa CTRL+Y
        self.oHelper.LoadGrid()
        self.oHelper.ScrollGrid("Opcoes", "Procurar...")
        self.oHelper.SetValue("Acesso Directo",'CTRL+M', grid=True) #Procurar CTRL+M
        self.oHelper.LoadGrid()
        self.oHelper.ScrollGrid("Opcoes", "Procurar proxima")
        self.oHelper.SetValue("Acesso Directo",'CTRL+B', grid=True) #Procurar proxima CTRL+B
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")


    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case. 
        """
        self.oHelper.TearDown() 


if __name__ == "__main__":
    unittest.main()