from tir import Webapp
import unittest

class GTPA008X(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "10/04/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA008')

	def test_GTPA008X_CT001(self):
		self.oHelper.SetButton("Outras Ações", "Imp. Funcionarios")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetValue('Cargo de ?', '00001')
		self.oHelper.SetValue('Cargo até ?', '00001')
		self.oHelper.SetValue('Função de ?', '00001')
		self.oHelper.SetValue('Função até ?', '00001')
		self.oHelper.SetValue('Filtrar Matriculas sem Colab ?', 'Não')
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
