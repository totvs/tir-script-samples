from tir import Webapp
import unittest

class MATC015(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','21/06/2019','T1','D MG 01')
		inst.oHelper.Program('MATC015')		

	def test_MATC015_CT001(self):
		self.oHelper.SetButton('Ok')
		self.oHelper.SearchBrowse('D MG 01 ESTSE0000000000000000000000212')
		self.oHelper.SetButton('POsicionado')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()