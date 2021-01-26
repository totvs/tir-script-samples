from tir import Webapp
import unittest

class TECA640(unittest.TestCase):
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGATEC","11/12/2020","T1","D MG 01","28")
		inst.oHelper.Program("TECA640")
	def test_TECA640_001(self):
		
		self.oHelper.SetValue("Cliente de ?","")
		self.oHelper.SetValue("Cliente ate ?","zzzzzz")
		self.oHelper.SetValue("Produto de ?","")
		self.oHelper.SetValue("Produto ate ?","ZZZZZZ")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Cancelar")

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()