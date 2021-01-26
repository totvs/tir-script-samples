from tir import Webapp
import unittest
import time

class GFEX010(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','28/06/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEX010')

	def test_GFEX010_CT001(self):

		time.sleep(5)

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()
