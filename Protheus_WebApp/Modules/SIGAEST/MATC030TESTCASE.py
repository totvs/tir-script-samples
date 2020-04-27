from tir import Webapp
import unittest

class MATC030(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAEST","04/07/2019","T1","D MG 01 ","04")
		inst.oHelper.Program("MATC030")

	def test_MATC030_001(self):
		cod = 'ESTSE0000000000000000000000144'

		self.oHelper.SetValue("Data Inicial dos Movimentos ?", "01/05/2018")
		self.oHelper.SetValue("Data Final dos Movimentos ?", "09/09/2019")
		self.oHelper.SetValue("Qual Armazem ?", "01")
		self.oHelper.SetButton("Ok")
		self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
		self.oHelper.SetButton("Consulta")
		self.oHelper.SetButton("Imprimir")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Consulta")
		self.oHelper.SetButton("Gráfico")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("X")
		self.oHelper.SetButton("Ok")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()