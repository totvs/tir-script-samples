from tir import Webapp
import unittest

class GFEA029(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA029')

	def test_GFEA029_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Ida e Volta ', '2')
		self.oHelper.SetValue('Ini Validade', '04/12/2020')
		self.oHelper.SetValue('Fim Validade', '31/12/2021')
		self.oHelper.SetValue('Cid Origem  ', '1100205')
		self.oHelper.SetValue('Cid Dest    ', '1200401')
		self.oHelper.SetValue('Transp      ', '101')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()