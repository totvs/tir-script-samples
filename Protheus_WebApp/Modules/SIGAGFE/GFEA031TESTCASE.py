from tir import Webapp
import unittest

class GFEA031(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA031')

	def test_GFEA031_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Motivo      ', '900001')
		self.oHelper.SetValue('Descricao   ', 'MOTIVO TESTE AUTOMACAO')
		self.oHelper.SetValue('Provocador  ', '3')
		self.oHelper.SetValue('Aprova Auto?', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Descricao   ', 'MOTIVO TESTE AUTOM X')
		self.oHelper.SetValue('Provocador  ', '4')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Motivo      ', '900002')
		self.oHelper.SetValue('Descricao   ', 'MOTIVO 2 TESTE AUTOMACAO')
		self.oHelper.SetValue('Provocador  ', '3')
		self.oHelper.SetValue('Aprova Auto?', '2')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900002')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

