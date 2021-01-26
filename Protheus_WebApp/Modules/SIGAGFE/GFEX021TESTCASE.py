from tir import Webapp
import unittest

class GFEX021(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','28/06/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEX021')

	def test_GFEX021_CT001(self):

		self.oHelper.SetButton('Incluir')

		self.oHelper.SetValue('CFOP','1101')
		self.oHelper.SetValue('Tip Op Intel','1')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('1101000000')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('1101000000')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Tip Op Intel','2')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('1101000000')

		self.oHelper.SetButton('Outras Ações','Simulador de Regras')

		self.oHelper.SetValue('CFOP','1101')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SearchBrowse('1101000000')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()
