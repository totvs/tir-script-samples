import unittest
from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

class FINA070(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN", DateSystem, "T1", "D MG 01 ", "06")
		inst.oHelper.Program("FINA070")

	def test_FINA070_CT193(self):
		prefixo = "FIN"
		titulo  = "FIN002152"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "001"
		conta   = "001"
		data    = "21/06/2019"

		self.oHelper.AddParameter("MV_BR10925", "", "2", "2", "2")
		self.oHelper.AddParameter("MV_JURTIPO", "", "L", "L", "L")
		self.oHelper.AddParameter("MV_FINJRTP", "", "2", "2", "2")
		self.oHelper.AddParameter("MV_LJMULTA", "", "0.10", "0.10", "0.10")
		self.oHelper.SetParameters()
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")
		self.oHelper.SetValue("Data Receb.", data)
		self.oHelper.SetValue("Data Crédito", data)
		self.oHelper.CheckResult("+ Multa", "0,00")
		self.oHelper.CheckResult("= Valor Recebido", "10000,00")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		data = "28/06/2019"
		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Receb.", data)
		self.oHelper.SetValue("Data Crédito", data)
		self.oHelper.CheckResult("+ Multa", "10,00")
		self.oHelper.CheckResult("= Valor Recebido", "10010,00")
		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()

