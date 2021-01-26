from tir import Webapp
import unittest

class GTPA702(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "29/05/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA702')

	def test_GTPA702_CT001(self):
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
