from tir import Webapp
import unittest

class MATA430(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','03/07/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA430')

	def test_MATA430_CT001(self):
		self.oHelper.SetButton('Outras Ações','LeGenda')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()