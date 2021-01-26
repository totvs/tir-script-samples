from tir import Webapp
import unittest

class GTPA140(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "05/08/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA140')

	def test_GTPA140_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('GIM_DESCRI', 'TESTE CUSTO')
		self.oHelper.SetValue('GIM_UM'    , 'SV')
		self.oHelper.SetValue('GIM_PRODUT', 'SV')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
	
	def test_GTPA140_CT002(self):
		self.oHelper.SearchBrowse("D MG    000002", "Filial+cód. Custo")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult('GIM_DESCRI', 'TESTE 1')
		self.oHelper.CheckResult('GIM_UM'    , 'SV')
		self.oHelper.CheckResult('GIM_PRODUT', 'SV')
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
