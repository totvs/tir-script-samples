from tir import Webapp
import unittest

class GFEA039(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA039')

	def test_GFEA039_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Res Obs     ', 'TESTE AUTOMACAO')
		self.oHelper.SetValue('Txt Obs     ', 'TESTE')
		self.oHelper.SetValue('Tipo Obs    ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        000001')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Res Obs     ', 'TESTE ALTERADO')
		self.oHelper.SetValue('Txt Obs     ', 'TESTE ALTERADO')
		self.oHelper.SetValue('Tipo Obs    ', '3')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        000001')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        000001')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Res Obs     ', 'TESTE 2 AUTOMACAO')
		self.oHelper.SetValue('Txt Obs     ', 'TESTE 2')
		self.oHelper.SetValue('Tipo Obs    ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        000001')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        000002')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

