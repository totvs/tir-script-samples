from tir import Webapp
import unittest

class GTPA420(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "31/08/2020", "T1", "M SP 04")
		inst.oHelper.Program('GTPA420')
	
	def test_GTPA420_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
