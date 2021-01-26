from tir import Webapp
import unittest

class GFEA049(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','29/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA049')

	def test_GFEA049_CT001(self):

		self.oHelper.SetButton('Incluir')
		
		self.oHelper.SetValue('Item', 'GFE')
		self.oHelper.SetValue('Desc Item', 'TESTES AUTOMATIZADOS GFE')
		self.oHelper.SetValue('Clas Frete', '1')
		
		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('GFE')

		self.oHelper.SetButton('Visualizar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('GFE')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Clas Frete', '2')

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('GFE')
		
		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()