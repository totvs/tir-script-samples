from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

class FINA330(unittest.TestCase):
	
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN",DateSystem,"T1","D MG 01 ","06")
		inst.oHelper.Program("FINA330")

	def test_FINA330_CT001(self):
		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		self.oHelper.SetButton("OK")			
		self.oHelper.SearchBrowse("D MG 01 FINFIN000280 RA ")
		self.oHelper.SetButton("Compensar")
		self.oHelper.CheckResult("Prefixo", "FIN")
		self.oHelper.CheckResult("Número", "FIN000280")
		self.oHelper.CheckResult("Tipo", "RA")
		self.oHelper.SetButton("OK")
		self.oHelper.CheckResult("Total selecionado", "10000,00")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Sim")
		self.oHelper.AssertTrue()
		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")
		self.oHelper.SearchBrowse("D MG 01 FINFIN000280 RA ")
		self.oHelper.SetButton("Outras Ações", "Estorno")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.SearchBrowse("D MG 01 FINFIN000280 RA ")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()