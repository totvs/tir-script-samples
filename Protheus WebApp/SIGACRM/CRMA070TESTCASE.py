from tir import Webapp
import unittest
import time
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class CRMA070(unittest.TestCase):    
    
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()

        inst.oHelper.SetTIRConfig(config_name="user", value="aline.toyoda")
        inst.oHelper.SetTIRConfig(config_name="password", value="1")

        inst.oHelper.Setup('SIGACRM',DateSystem,'T1','D MG 01 ','73')
        inst.oHelper.Program('CRMA070')
 
    def test_CRMA070_001(self):
        '''
        Caso de Teste 001
        '''
        clienteCodigo = "CLI029"
        clienteNome = "CLIENTE AUTOMACAO"

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitShow("Clientes - INCLUIR")
        self.oHelper.SetValue("Codigo",clienteCodigo)
        self.oHelper.SetValue("Loja","01")
        self.oHelper.SetValue("Nome",clienteNome)
        self.oHelper.SetValue("N Fantasia","FANTASIA CLIENTE")
        self.oHelper.SetValue("Endereco","ENDERECO CLIENTE")
        self.oHelper.SetValue("Tipo","F")
        self.oHelper.SetValue("Estado","SP")
        self.oHelper.SetValue("Cd.Municipio","50308")
        self.oHelper.SetValue("Municipio","SAO PAULO")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Cancelar")
        
        self.oHelper.AssertTrue()

    #CT021 - TIR - Incluir uma Atividade do tipo E-mail vinculada à uma Entidade (Clientes)
    def test_CRMA070_CT021(self):
        self.oHelper.SearchBrowse("D MG    CRM180")
        self.oHelper.SetButton("Outras Ações", "Relacionadas, Atividades, Nova Atividade")
        time.sleep(5)

        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.ClickLabel('E-mail')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetValue("AOF_PARTIC", "teste@hotmail.com")
		#Se o campo de destinatário estiver vazio, sem carregar o A1_EMAIL, não passa
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()