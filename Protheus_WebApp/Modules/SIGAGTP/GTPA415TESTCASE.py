from tir import Webapp
import unittest
import time

class GTPA415(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP","25082020","T1","M SP 04","88")
		inst.oHelper.Program("GTPA415")
	def test_GTPA415_001(self):
		self.oHelper.SetButton("Proc de Comissões")
		self.oHelper.SetButton("OK") 
		self.oHelper.SetValue("MV_PAR01","01")
		self.oHelper.SetValue("MV_PAR02","")
		self.oHelper.SetValue("MV_PAR03","ZZZZZZ")
		self.oHelper.SetValue("MV_PAR04","01/01/2020")
		self.oHelper.SetValue("MV_PAR05","31/12/2020")
		self.oHelper.SetValue("MV_PAR06","000002")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()