from tir import Webapp
import unittest

class GFEA010(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','03/11/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA010')

	def test_GFEA010_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Cod Emit    ', '001')
		self.oHelper.SetValue('GU2_NOME', 'Contato 001')
		self.oHelper.SetValue('E-mail      ', 'contato@emitente.com.br')
		self.oHelper.SetValue('Fone 1      ', '47-1234-5678')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        001           2')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('GU2_NOME', 'Contato 001 - Alterado')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        001           2')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        001           2')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Cod Emit', '003')
		self.oHelper.SetValue('GU2_NOME', 'Contato 003')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        001           2')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        003           2')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()
