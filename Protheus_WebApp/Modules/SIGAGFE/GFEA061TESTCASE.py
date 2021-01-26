from tir import Webapp
import unittest

class GFEA061(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','15/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA061')

	def test_GFEA061_CT001(self):
		
		self.oHelper.SetButton('Incluir')

		self.oHelper.SetValue('Emitente','500')
		self.oHelper.SetValue('Tabela','151220')
		self.oHelper.SetValue('Descricao','TABELA GFE - 151220')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('500           151220')

		self.oHelper.SetButton('Outras Ações','Anexo')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Descricao','TABELA GFE - ALTERACAO')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('500           151220')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()