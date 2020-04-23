from tir import Webapp
import unittest

class MATR947(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFIS','21/06/2019','T1','D MG 01')
		inst.oHelper.Program('MATR947')

	def test_MATR947_CT001(self):
		self.oHelper.AddParameter("MV_TRANSF1", "", "SF1->F1_TRANSP", "SF1->F1_TRANSP", "SF1->F1_TRANSP")
		self.oHelper.AddParameter("MV_MTR947A", "", "B5_CERT", "B5_CERT", "B5_CERT")
		self.oHelper.SetParameters()
		self.oHelper.SetButton('Param.')
		self.oHelper.SetValue('Data Inicial ?','27/09/2019')
		self.oHelper.SetValue('Data Final ?','27/09/2019')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Sair')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
