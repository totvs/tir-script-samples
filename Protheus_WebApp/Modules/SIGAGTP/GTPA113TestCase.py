from tir import Webapp
import unittest

class GTPA113(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA113')

	def test_GTPA113_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('Código', 'GTPAUT')
		self.oHelper.SetValue('Matrícula', 'GTP200')
		self.oHelper.SetValue('Num.Vale', 'GTP002')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("D MG    GTP002", "Filial+num.vale")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
