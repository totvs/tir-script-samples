from tir import Webapp
import unittest

class MATA290(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('MATA290')	

	def test_MATA290_CT001(self):
		self.oHelper.SetButton("Ok")
		self.oHelper.AssertTrue()
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()