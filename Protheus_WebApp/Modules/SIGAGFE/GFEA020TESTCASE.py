from tir import Webapp
import unittest

class GFEA020(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA020')

	def test_GFEA020_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Cidade      ', '4202404')
		self.oHelper.SetValue('Nome        ', 'Blumenau')
		self.oHelper.SetValue('Estado      ', 'SC')
		self.oHelper.SetValue('Pais        ', '105')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        4202404')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Sigla       ', 'SCBNU')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        4202404')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        4202404')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Cidade      ', '4202909')
		self.oHelper.SetValue('Nome        ', 'Brusque')
		self.oHelper.SetValue('Estado      ', 'SC')
		self.oHelper.SetValue('Pais        ', '105')
		self.oHelper.SetValue('Sigla       ', 'SCBSQ')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        4202404')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        4202909')
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

