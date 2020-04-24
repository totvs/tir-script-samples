from tir import Webapp
import unittest

class MATR924(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFIS','21/06/2019','T1','D MG 01')
		inst.oHelper.Program('MATR924')

	def test_MATR924_CT001(self):
		self.oHelper.SetButton('Param.')
		self.oHelper.SetValue('Do Produto ?','')
		self.oHelper.SetValue('Ate Produto ?','ZZZZ')
		self.oHelper.SetValue('Do Periodo ?','01/09/2019')
		self.oHelper.SetValue('Ate Periodo ?','30/09/2019')
		self.oHelper.SetValue('Armazem ?','01')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Sair')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
