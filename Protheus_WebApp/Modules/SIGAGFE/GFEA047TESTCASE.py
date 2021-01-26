from tir import Webapp
import unittest

class GFEA047(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','29/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA047')

	def test_GFEA047_CT001(self):

		self.oHelper.SetButton('Incluir')
		
		self.oHelper.SetValue('Tipo Oper', 'AUT')
		self.oHelper.SetValue('Descricao', 'TESTES AUTOMATIZADOS GFE')
				
		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('AUT')

		self.oHelper.SetButton('Visualizar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('AUT')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Descricao', 'TESTES AUTOMATIZADOS GFE - ALTERACAO')

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('AUT')
		
		self.oHelper.SetButton('Outras Ações','Copiar')

		self.oHelper.SetValue('Tipo Oper', 'AUT2')
		
		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('AUT')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('AUT2')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()