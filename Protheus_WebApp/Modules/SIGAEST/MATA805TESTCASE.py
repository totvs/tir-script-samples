from tir import Webapp
import unittest

class MATA805(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','30/10/2019','T1','D MG 01')
		inst.oHelper.Program('MATA805')		

	def test_MATA805_CT001(self):
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetValue("Documento","EST000001")
		self.oHelper.SetValue("Produto","ESTSE0000000000000000000000568",grid=True)
		self.oHelper.SetValue("Armazem","01",grid=True)
		self.oHelper.SetValue("Endereco","END001",grid=True)
		self.oHelper.SetValue("Qtd Distribu","10,00",grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.AssertTrue()		

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()