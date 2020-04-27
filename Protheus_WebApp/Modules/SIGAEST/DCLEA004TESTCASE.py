from tir import Webapp
import unittest

class DCLEA004(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAEST","17/10/2019","T1","D MG 01 ","04")
		inst.oHelper.Program("DCLEA004")

	def test_DCLEA004_001(self):
		self.oHelper.SetValue("Tanque Inicial.... ?", "000001")
		self.oHelper.SetValue("Tanque Final...... ?", "000001")
		self.oHelper.SetValue("Modo da Consulta.. ?", "Encerra Tanque")
		self.oHelper.SetValue("Impr.Observacoes.. ?", "Sim")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.Program("DCLEA004")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()