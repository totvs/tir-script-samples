from tir import Webapp
import unittest

class GFEA043(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA043')

	def test_GFEA043_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Unitizador  ', 'TESTE')
		self.oHelper.SetValue('Descricao   ', 'TESTE AUTOMACAO')
		self.oHelper.SetValue('Ident Unitiz', '1')
		self.oHelper.SetValue('Finalidade  ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        TESTE')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Descricao   ', 'TESTE AUTOMACAO - ALTERADO')
		self.oHelper.SetValue('Ident Unitiz', '2')
		self.oHelper.SetValue('Finalidade  ', '3')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        TESTE')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        TESTE')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

