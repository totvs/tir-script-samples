from tir import Webapp
import unittest

class GFEA011(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','03/11/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA011')

	def test_GFEA011_CT001(self):

		# Necessario corrigir campos de dicionario para permitir acessar campos da tela
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Grupo       ', '001')
		self.oHelper.SetValue('Descricao   ', 'GRUPO TESTE 001')
		self.oHelper.SetValue('Finalidade  ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        001')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Descricao   ', 'GRUPO TESTE 001 - ALTERADO')
		self.oHelper.SetValue('Finalidade  ', '2')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        001')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        001')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()
