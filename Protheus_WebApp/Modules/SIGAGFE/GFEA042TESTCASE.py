from tir import Webapp
import unittest

class GFEA042(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA042')

	def test_GFEA042_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Classific   ', 'TST')
		self.oHelper.SetValue('Descricao   ', 'TESTE AUTOMACAO')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        TST')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Descricao   ', 'TESTE AUTOMACAO - ALTERADO')
		self.oHelper.SetValue('Situacao', '2')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        TST')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        TST')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

