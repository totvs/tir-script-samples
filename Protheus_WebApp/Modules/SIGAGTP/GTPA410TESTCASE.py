from tir import Webapp
import unittest

class GTPA410(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP","25/08/2020","T1","M SP 04","88")
		inst.oHelper.Program("GTPA410")
	def test_GTPA410_001(self):
		self.oHelper.SetButton("Proc de Comissões")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("MV_PAR01","000003")
		self.oHelper.SetValue("MV_PAR02","000003")
		self.oHelper.SetValue("MV_PAR03","03/07/2020")
		self.oHelper.SetValue("MV_PAR04","03/07/2020")
		self.oHelper.SetValue("MV_PAR05","000001")
		self.oHelper.SetButton("OK")
		self.oHelper.SearchBrowse("M SP    000010   ", "Filial+código + N Simulação")
		self.oHelper.SetButton("Outras Ações", "Exportação Folha Pgto.")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("MV_PAR01","000003")
		self.oHelper.SetValue("MV_PAR02","000003")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("M SP    000010   ", "Filial+código + N Simulação")
		self.oHelper.SetButton("Outras Ações", "Exportação Financeiro")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("MV_PAR01","000003")
		self.oHelper.SetValue("MV_PAR02","000003")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()