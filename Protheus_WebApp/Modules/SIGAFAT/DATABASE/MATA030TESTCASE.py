from tir import Webapp
import unittest
from datetime import datetime

class MATA030(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.grupo = "T1"

		inst.oHelper = Webapp() # INSTANCIAR A CLASSE
		inst.oHelper.Setup('SIGAFAT','23/02/2020', inst.grupo, 'D MG 01 ', '05')
		inst.oHelper.SetLateralMenu("Atualizações > Cadastros > Clientes")

	def test_MATA030_CT001(self):
		
		# Abaixo segue outra forma de conectar no banco, caso seja necessário conectar em mais de um banco dentro do script.
		
		# database_content_dictionary = self.oHelper.QueryExecute("SELECT * FROM SA1T10", driver_database="NOME_DO_DRIVER_ODBC", 
		# server_database="NOME_DO_SERVER", name_database="NOME_DO_BANCO", user_database="sa", password_database="123456")

		database_content_dictionary = self.oHelper.QueryExecute("SELECT * FROM SA1T10")

		a1_loja 	= database_content_dictionary['A1_LOJA']
		a1_pessoa	= database_content_dictionary['A1_PESSOA']
		a1_nome		= database_content_dictionary['A1_NOME']
		a1_nreduz	= database_content_dictionary['A1_NREDUZ']
		a1_end		= database_content_dictionary['A1_END']
		a1_tipo		= database_content_dictionary['A1_TIPO']
		a1_est		= database_content_dictionary['A1_EST']
		a1_cod_mun	= database_content_dictionary['A1_COD_MUN']
		a1_bairro	= database_content_dictionary['A1_BAIRRO']
		a1_cep		= database_content_dictionary['A1_CEP']

		for row, a1_cod in enumerate(database_content_dictionary['A1_COD'].values()):# Percorrer a mesma quantidade do A1_COD na tabela.

			self.oHelper.SetButton('Incluir')
			
			self.oHelper.SetBranch('D MG 01 ')
			self.oHelper.SetValue('A1_COD', a1_cod)
			self.oHelper.SetValue('A1_LOJA', a1_loja[row])
			self.oHelper.SetValue('A1_PESSOA', a1_pessoa[row])
			self.oHelper.SetValue('A1_NOME', a1_nome[row])
			self.oHelper.SetValue('A1_NREDUZ', a1_nreduz[row])
			self.oHelper.SetValue('A1_END', a1_end[row])
			self.oHelper.SetValue('A1_TIPO', a1_tipo[row])
			self.oHelper.SetValue('A1_EST', a1_est[row])
			self.oHelper.SetValue('A1_COD_MUN', a1_cod_mun[row])

			if a1_bairro[row].strip(): # Verificamos se tem conteudo no campo A1_BAIRRO coletado da tabela, caso sim, o preenchimento é realizado
				self.oHelper.SetValue('A1_BAIRRO', a1_bairro[row])

			if a1_cep[row].strip(): # Verificamos se tem conteudo no campo A1_CEP coletado da tabela, caso sim, o preenchimento é realizado
				self.oHelper.SetValue('A1_CEP', a1_cep[row])

			self.oHelper.SetButton('Salvar')
			self.oHelper.SetButton('Não')
			self.oHelper.SetButton('Cancelar')

			self.oHelper.SearchBrowse(f'D MG    {a1_cod}')
			self.oHelper.SetButton('Visualizar')
			self.oHelper.CheckResult('A1_COD', a1_cod)
			self.oHelper.CheckResult('A1_LOJA', a1_loja)
			self.oHelper.CheckResult('A1_PESSOA', a1_pessoa)
			self.oHelper.CheckResult('A1_NOME', a1_nome)
			self.oHelper.CheckResult('A1_NREDUZ', a1_nreduz)
			self.oHelper.CheckResult('A1_END', a1_end)			
			
			self.oHelper.SetButton('Cancelar')

			self.oHelper.AssertTrue()

			self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()