from tir import Webapp
import unittest

class GTPA412(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP","25/08/2020","T1","D MG 01","88")
		inst.oHelper.Program("GTPA412")
	def test_GTPA412_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("G5D_AGENCI","")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()