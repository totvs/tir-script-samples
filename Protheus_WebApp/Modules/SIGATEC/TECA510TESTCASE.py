from tir import Webapp
import unittest

class TECA510(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGATEC","11/12/2020","T1","D MG 01","28")
		inst.oHelper.Program("TECA510")
	def test_TECA510_001(self):
		self.oHelper.SetValue("MV_PAR01","")
		self.oHelper.SetValue("MV_PAR02","ZZZZZZZZZZZZZZ")
		self.oHelper.SetValue("MV_PAR03","")
		self.oHelper.SetValue("MV_PAR04","ZZZZZZ")
		self.oHelper.SetValue("MV_PAR05","")
		self.oHelper.SetValue("MV_PAR06","ZZZZZZZZZZZZZZZ")
		self.oHelper.SetValue("MV_PAR07","")
		self.oHelper.SetValue("MV_PAR09","ZZZZZZZZZZZZZZZ")
		self.oHelper.SetValue("MV_PAR10","ZZZZZZZZZZZZZZZZZZZZ")
		self.oHelper.SetValue("MV_PAR11","")
		self.oHelper.SetValue("MV_PAR12","ZZZ")
		self.oHelper.SetValue("MV_PAR13","")
		self.oHelper.SetValue("MV_PAR14","ZZZZZZ")
		self.oHelper.SetValue("MV_PAR15","")
		self.oHelper.SetValue("MV_PAR16","ZZZZZZ")
		self.oHelper.SetValue("MV_PAR19","ZZZZZZZZ")
		self.oHelper.SetValue("MV_PAR20","")
		self.oHelper.SetValue("MV_PAR21","ZZZZZZZZZZZZZZZ")
		self.oHelper.SetValue("MV_PAR22","")
		self.oHelper.SetValue("MV_PAR23","ZZZZZZZZZZZZZZ")
		self.oHelper.SetButton("OK")
		self.oHelper.ClickGridCell("Codigo",row=2)
		self.oHelper.SetValue("Perspectiva", "Contrato")
		self.oHelper.CheckResult("Perspectiva", "Contrato")
		self.oHelper.SetValue("Perspectiva", "Cliente")
		self.oHelper.CheckResult("Perspectiva", "Cliente")
		self.oHelper.SetValue("Perspectiva", "Base Atendimento")
		self.oHelper.CheckResult("Perspectiva", "Base Atendimento")


		self.oHelper.ClickIcon("Proximo Mes")
		self.oHelper.ClickIcon("Mes Anterior")
		self.oHelper.ClickIcon("Proximo Ano")
		self.oHelper.ClickIcon("Ano Anterior")
		self.oHelper.ClickIcon("Sair")
		self.oHelper.AssertTrue()

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()