from tir import Webapp
import unittest

class GTPA300(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "19/04/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA300')

	def test_GTPA300_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('GYN_LINCOD','000001')
		self.oHelper.SetValue('GYN_LINSEN','1')
		self.oHelper.SetValue('GYN_CODGID','00000000001')
		self.oHelper.SetValue('GYN_DTINI','01/01/2020')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
