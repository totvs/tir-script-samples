from cawebhelper import CAWebHelper
import unittest

class TAFA500(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = CAWebHelper()
		#inst.oHelper.Setup('SIGATAF','10/08/2017','99','01','05')
		inst.oHelper.Setup('SIGATAF','08/05/2018','T1','D MG 01 ','05')
		inst.oHelper.SetLateralMenu("Miscelanea > Integração > Importação de Arquivos")

	def test_TAFA500_CT001(self):
		#Deve-se entrar no sistema com a data de 07/05/2018
		self.oHelper.SetButton('Avançar >>')
		self.oHelper.SetButton('...')
		#self.oHelper.SetFilePath("SERVIDOR\\xml\\")
		self.oHelper.SetFilePath("C:\\tmp")
		#self.oHelper.SetFilePath("C:")
		self.oHelper.UTSetValue('aCab','Método de Importação ?','3-Importa XML - Layout eSocial')

		self.oHelper.SetButton('Finalizar') 
		
		self.oHelper.SetButton('Sim') # Confirma processamento de arquivos?

		self.oHelper.SetButton('Fechar') # Processo finalizado.
		
		self.oHelper.SetButton('Sim') # Deseja realiza o processo de validação?
		
		self.oHelper.SetButton('Sim') # Integração Finalizada, Deseja visualizar o monitor de integração?
		
		self.oHelper.UTSetValue('aCab','Data De','01/05/2018')
		self.oHelper.UTSetValue('aCab','Data Até','08/05/2018')
		self.oHelper.UTSetValue('aCab','Monitor de Integração',True)
		self.oHelper.UTSetValue('aCab','Monitor de Validação',True)
		self.oHelper.UTSetValue('aCab','Escolha abaixo a visão à ser aplicada no monitor de integração', 'Visão por status de integração')

		self.oHelper.SetButton('Confirmar')
		self.oHelper.ClickFolder('Visão por lote')
		self.oHelper.SearchBrowse('DTOS(TAFDATA)+TAFHORA','08/05/2018',True)
		self.oHelper.SetButton('Expandir')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Alterar')
		self.oHelper.UTSetValue('aCab','C9V_NOMMAE','MAE ALTERADO')
		self.oHelper.UTSetValue('aCab','C9V_NOMPAI','PAI ALTERADO')
		
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar') #Registro alterado com sucesso

		self.oHelper.SetButton("x")
		self.oHelper.ClickFolder('Visão individualizada')
		self.oHelper.ClickFolder('Monitor de Validação')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetLateralMenu("Atualizações > Eventos Esocial > Trabalhador > Cadastro Trabalhador")

		self.oHelper.SearchBrowse('Filial+cpf + Reg. Ativo?','D MG 01 087.862.077-09',True)
		self.oHelper.SetButton('Visualizar')
		self.oHelper.UTSetValue('aCab','S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador.',True)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.ClickFolder('Trabalhador')
		self.oHelper.ClickFolder('Informações do Trabalhador')
		
		self.oHelper.UTCheckResult('aCab','C9V_NOMMAE','MAE ALTERADO')
		self.oHelper.UTCheckResult('aCab','C9V_NOMPAI','PAI ALTERADO')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()