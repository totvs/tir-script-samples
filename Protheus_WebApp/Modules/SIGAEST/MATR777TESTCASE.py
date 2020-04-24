from tir import Webapp
import unittest

class MATR777(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','07/10/2019','T1','D MG 01')
		inst.oHelper.Program('MATR777')

	def test_MATR777_CT001(self):
		
		self.oHelper.SetButton('Param.')
		self.oHelper.SetValue('De pedido ?','')
		self.oHelper.SetValue('Ate pedido ?','ZZZZZ')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Sair')	
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
