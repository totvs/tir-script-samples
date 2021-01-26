from tir import Webapp
import unittest

class GTPA425(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP","10092020","T1","M SP 04","88")
		inst.oHelper.Program("GTPA425")
		inst.oHelper.AddParameter("MV_PAPONTA", "M SP 04", "20200811/20200910", "20200811/20200910", "20200811/20200910")
		inst.oHelper.AddParameter("MV_PONMES", "M SP 04", "20200811/20200910", "20200811/20200910", "20200811/20200910")
		inst.oHelper.SetParameters()
	def test_GTPA425_001(self):
		self.oHelper.SetValue("MV_PAR01","")
		self.oHelper.SetValue("MV_PAR02","ZZZZZZ")
		self.oHelper.SetValue("MV_PAR03","")
		self.oHelper.SetValue("MV_PAR04","ZZZZZZ")
		self.oHelper.SetValue("MV_PAR05","")
		self.oHelper.SetValue("MV_PAR06","")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Outras Ações", "Confirmar Todos")
		self.oHelper.SetButton("Outras Ações", "Simulação do ponto")
		self.oHelper.SetButton("Outras Ações", "Imprimir")
		self.oHelper.SetButton("Imprimir")
		self.oHelper.SetButton("Sair")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()