from tir import Webapp
import unittest

class TECA500(unittest.TestCase):
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGATEC","11/12/2020","T1","D MG 01","28")
		inst.oHelper.Program("TECA500")
	def test_TECA500_001(self):
		self.oHelper.SetButton("Agenda")
		self.oHelper.SetButton("Editar")

		self.oHelper.SetValue("ABB_CODTEC","00000000002TEC")
		self.oHelper.SetValue("ABB_DTINI","14/12/2020",grid=True)
		self.oHelper.SetValue("ABB_HRINI","09:00",grid=True)
		self.oHelper.SetValue("ABB_DTFIM","14/12/2020",grid=True)
		self.oHelper.SetValue("ABB_HRFIM","12:00",grid=True)
		self.oHelper.SetValue("ABB_OBSERV","TEST TIR",grid=True)
		self.oHelper.SetValue("ABB_ENTIDA","AB6",grid=True)
		self.oHelper.SetValue("ABB_CHAVE","000073",grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.CheckResult("ABB_CODTEC","00000000002TEC")
		self.oHelper.CheckResult("ABB_DTINI","14/12/2020",grid=True, line=1)
		self.oHelper.CheckResult("ABB_HRINI","09:00",grid=True, line=1)
		self.oHelper.CheckResult("ABB_DTFIM","14/12/2020",grid=True, line=1)
		self.oHelper.CheckResult("ABB_HRFIM","12:00",grid=True, line=1)
		self.oHelper.CheckResult("ABB_OBSERV","TEST TIR",grid=True, line=1)
		self.oHelper.CheckResult("ABB_ENTIDA","AB6",grid=True, line=1)
		self.oHelper.CheckResult("ABB_CHAVE","000073",grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()