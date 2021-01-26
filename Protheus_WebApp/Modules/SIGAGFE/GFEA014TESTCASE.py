from tir import Webapp
import unittest

class GFEA014(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','03/11/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA014')

	def test_GFEA014_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Tipo de Item', '9999')
		self.oHelper.SetValue('Descricao   ', 'TIPO DE ITENS PARA TESTE AUTOMACAO')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        9999')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Descricao   ', 'TIPO DE ITENS PARA TESTE AUTOMACAO - ALTERACAO')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        9999')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        9999')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()
