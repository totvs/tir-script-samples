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

		csv_content_dictionary = self.oHelper.OpenCSV(delimiter=";", csv_file="SA1.csv", header=True)
		
		# Alguns casos abaixo o meu .CSV precisou de ajustes no conteudo retornado, 
		# isso é mais um exemplo do poder de programação que pode ser utilizado aqui no script 

		a1_loja 	= csv_content_dictionary['A1_LOJA']
		# a1_loja usando uma dict comprehension para criar um novo dicionario e dar um upgrade no valor
		a1_loja 	= {k: '0'+str(v) for k, v in a1_loja.items()} # Converto tudo para string e insiro o prefixo 0.
		a1_pessoa	= csv_content_dictionary['A1_PESSOA']
		a1_nome		= csv_content_dictionary['A1_NOME']
		a1_nreduz	= csv_content_dictionary['A1_NREDUZ']
		a1_end		= csv_content_dictionary['A1_END']
		a1_tipo		= csv_content_dictionary['A1_TIPO']
		# a1_tipo usando uma dict comprehension para criar um novo dicionario e dar um upgrade no valor
		a1_tipo 	= {k: 'F' for k, v in a1_tipo.items()}# Insiro no valor do dicionario o conteudo 'F'.
		a1_est		= csv_content_dictionary['A1_EST']
		a1_cod_mun	= csv_content_dictionary['A1_COD_MUN']
		a1_bairro	= csv_content_dictionary['A1_BAIRRO']
		a1_cep		= csv_content_dictionary['A1_CEP']

		for row, a1_cod in enumerate(csv_content_dictionary['A1_COD'].values()):# Percorrer a mesma quantidade do A1_COD na tabela.

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
			# Condição para realizar o preenchimento somente se tem conteúdo a ser preenchido neste campo
			if a1_bairro[row].strip(): # strip() é utilizado para remover os espaços em branco da string
				self.oHelper.SetValue('A1_BAIRRO', a1_bairro[row])
			# Condição para realizar o preenchimento somente se tem conteúdo a ser preenchido neste campo
			if a1_cep[row].strip(): # strip() é utilizado para remover os espaços em branco da string
				self.oHelper.SetValue('A1_CEP', a1_cep[row])

			self.oHelper.SetButton('Salvar')
			self.oHelper.SetButton('Não')
			self.oHelper.SetButton('Cancelar')

			self.oHelper.SearchBrowse(f'D MG    {a1_cod}')
			self.oHelper.SetButton('Visualizar')
			self.oHelper.ClickFolder('Cadastrais')
			self.oHelper.CheckResult('A1_COD', a1_cod)
			self.oHelper.CheckResult('A1_LOJA', a1_loja)
			self.oHelper.CheckResult('A1_PESSOA', a1_pessoa)
			self.oHelper.CheckResult('A1_NOME', a1_nome)
			self.oHelper.CheckResult('A1_NREDUZ', a1_nreduz)
			self.oHelper.CheckResult('A1_END', a1_end)
			
			self.oHelper.SetButton('Cancelar')

			self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()