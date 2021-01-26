from tir import Webapp
import unittest
import time

class GFEX061(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','23/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEX061')

	def test_GFEX061_CT001(self):

		self.oHelper.SetValue('Transportadora','101')
		self.oHelper.SetValue('Período De','01/01/2018')
		self.oHelper.SetValue('Período Até','31/12/2018')
		self.oHelper.SetValue('Transp. Comp.','111')
		self.oHelper.SetValue('Nr Tab Comp','1111')

		self.oHelper.SetButton('Comparar')

		self.oHelper.ClickGridCell("Trecho", 1)

		self.oHelper.SetKey("Enter", grid=True)

		self.oHelper.ClickFolder("Simular 1 documento(s) com outras transportadoras")

		self.oHelper.SetButton('Simular')

		time.sleep(10)

		self.oHelper.SetButton('Sair')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()