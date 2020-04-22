from tir import Webapp
import unittest
import time
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class PMSA410(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAPMS",DateSystem,"T1","D MG 01 ","44")
        self.oHelper.Program("PMSA410")
    def test_PMSA410_065(self):

        '''
        Test Case 065 - Inclusao de um Projeto com troca de código
        '''
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("Projeto","PMSC000001")
        self.oHelper.SetValue("Descricao","PROJETO TIR")
        self.oHelper.SetValue("Tipo Proj","0002")
        self.oHelper.ClickFolder("Cronograma")  
        self.oHelper.SetValue("Calendario","004")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse("D MG 01 PMSC000001", "Filial+projeto")
        time.sleep(20)
        self.oHelper.SetButton("Outras Ações","Trocar Codigo")
        self.oHelper.SetValue("Novo Projeto:","PMSU000002")
        self.oHelper.SetButton("OK")
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSU000002", "Filial+projeto")
        
        '''Teste case de visualização'''
        self.oHelper.SetButton("Alt.Cadastro") #Mudar para Visualizar!
        self.oHelper.WaitShow("Gerenciamento de Projetos - Gerenciamento de Projetos")
        self.oHelper.CheckResult("Projeto","PMSU000002")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_PMSA410_066(self):

        '''Teste case 066 de Alteração'''
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSU000001", "Filial+projeto")
        self.oHelper.SetButton("Alt.Cadastro")
        self.oHelper.WaitShow("Gerenciamento de Projetos - Gerenciamento de Projetos")
        self.oHelper.SetValue("Tipo Proj","0001")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        '''Teste case de visualização'''
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSU000001", "Filial+projeto")
        self.oHelper.SetButton("Alt.Cadastro")#Mudar para Visualizar!
        self.oHelper.WaitShow("Gerenciamento de Projetos - Gerenciamento de Projetos")
        self.oHelper.CheckResult("Tipo Proj","0001")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SetButton("Outras Ações","Legenda")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_PMSA410_067(self):

        '''Teste case 067 de Exclusão '''
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSD000001", "Filial+projeto")
        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSD000001", "Filial+projeto")
        self.oHelper.AssertFalse()


    #def test_PMSA410_068(self):

        
        #'''Test Case 068 - Revisão de um Projeto'''
        
        #projeto = "PMSU000001"
        #self.oHelper.WaitShow("Gerenciamento de Projetos")
        #self.oHelper.SearchBrowse(f'D MG 01 {projeto}', 'Filial+projeto')
        #self.oHelper.SetButton("Outras Ações","Revisoes")
        #self.oHelper.SetButton("Salvar")
        #self.oHelper.SetButton("Visualizar")
        #self.oHelper.WaitShow("Gerenciamento de Projetos - Visualizar")
        #self.oHelper.CheckResult("Projeto","PMSU000001")
        #self.oHelper.SetButton("Fechar")
        #self.oHelper.AssertTrue()

    def test_PMSA410_069(self):

        '''Teste case 069 de atalho'''
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSU000001", "Filial+projeto")
        self.oHelper.SetButton("Outras Ações","Alt.Estrutura")
        self.oHelper.WaitShow("Gerenciamento de Projetos - Alterar")
     #   self.oHelper.SetFocus("AF8_PROJET")
     #   self.oHelper.SetKey(key="CTRL", additional_key="M") #Procurar CTRL+M
     #   self.oHelper.SetValue("Procurar por:", "ALTERACAO DO PROJETO POR TIR")
     #   self.oHelper.SetButton("Procurar")
     #   self.oHelper.SetButton("Fechar")
     #   self.oHelper.SetButton("Fechar")
     #   self.oHelper.SetFocus("AF8_PROJET")
     #   self.oHelper.SetKey(key="CTRL", additional_key="B") #Procurar proxima CTRL+B
     #   self.oHelper.SetButton("Fechar")
     #   self.oHelper.SetButton("Fechar")
     #   self.oHelper.SetFocus("AF8_PROJET")
        self.oHelper.SetButton("Outras Ações","Atalhos")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        '''
        Method that finishes the test case.
        '''
        self.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
