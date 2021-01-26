from tir import Webapp
import unittest

class GTPA060(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "07/10/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA060')

	def test_GTPA060_CT001(self):
                self.oHelper.SetButton('Incluir')
                self.oHelper.SetBranch('D MG')
                self.oHelper.SetValue('GZR_UF', 'MG')
                self.oHelper.SetValue('GZR_FILREF', 'X FIS16')
                self.oHelper.SetButton('Confirmar')
                self.oHelper.AssertTrue()
                
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
