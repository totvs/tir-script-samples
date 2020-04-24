from tir import Webapp
import unittest

class MATA241(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAEST","11/03/2020","T1","D MG 01 ","04")
		inst.oHelper.Program("MATA241")

	def test_MATA241_001(self):
		self.oHelper.AddParameter("MV_CUSMED", "", "M", "M", "M")
		self.oHelper.SetParameters()
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("D MG 01 ")
		self.oHelper.SetValue("Número Documento", "EST136")
		self.oHelper.SetValue("TM", "550")
		self.oHelper.SetValue("Centro de Custo", "ESTSE0001")
		self.oHelper.SetValue("Produto", "ESTSE0003000000000000000000346", grid=True)
		self.oHelper.SetValue("Quantidade","1,00", grid=True)
		self.oHelper.SetValue("Endereco","EST001", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()