from tir import Webapp
import unittest

class GFEA016(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','21/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA016')

	def test_GFEA016_CT001(self):
		
		self.oHelper.SetButton('Gerar')

		self.oHelper.SetValue('Ano ?','2030')
		
		self.oHelper.SetButton('OK')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('01/01/2021')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Tipo Dia','2')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()