from tir import Webapp
import unittest

class MATR462(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','30/09/2019','T1','D MG 01')
		inst.oHelper.Program('MATR462')

	def test_MATR462_CT001(self):
		self.oHelper.SetButton('Param.')
		self.oHelper.SetValue('De  Produto ?','ESTSE0000000000000000000000550')
		self.oHelper.SetValue('Ate Produto ?','ESTSE0000000000000000000000550')
		self.oHelper.SetValue('De  Armazem ?','')
		self.oHelper.SetValue('Ate Armazem ?','ZZ')
		self.oHelper.SetValue('De  Grupo ?','')
		self.oHelper.SetValue('Ate Grupo ?','ZZ')
		self.oHelper.SetValue('De  Tipo ?','')
		self.oHelper.SetValue('Ate Tipo ?','ZZ')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')		
		self.oHelper.SetButton('sair')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
