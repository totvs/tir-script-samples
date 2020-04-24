import unittest
from tir import Webapp

class FINA910(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN", "02/08/2019", "T1", "D MG 01 ", "06")
		inst.oHelper.Program("FINA910")

	def test_FINA910_CT028(self):
		self.oHelper.AddParameter("MV_EMPTEF","","0000002","0000002","0000002")  
		self.oHelper.SetParameters()
		self.oHelper.SetButton("Imp Arq SITEF")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetValue("Arquivo", "\\baseline\\FINA910_CT28_IND_CREDITO.CSV")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetButton("Finalizar")
		self.oHelper.SetButton("Conciliacao")
		self.oHelper.SetValue("Da Filial ?", "")
		self.oHelper.SetValue("Ate Filial ?", "ZZZZZZZZ")
		self.oHelper.SetValue("Data Crédito De ?", "16/05/2019")
		self.oHelper.SetValue("Data Credito Até ?", "20/05/2019")
		self.oHelper.SetValue("Do Num NSU ?", "")
		self.oHelper.SetValue("Ate Num NSU ?", "ZZZZZZZZZ")
		self.oHelper.SetValue("Geração ?", "Individual")
		self.oHelper.SetValue("Tipo ?", "Ambos")
		self.oHelper.SetValue("Pesq Dias Ant ?", "0")
		self.oHelper.SetValue("Tolerância em % ?", "10,00")
		self.oHelper.SetValue("De Financeira ?", "")
		self.oHelper.SetValue("Ate Financeira ?", "")
		self.oHelper.SetValue("Data Baixa ?", "Database")
		self.oHelper.SetValue("Valida NSU p/ não Conc. ?", "Sim")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Efetiva Conciliação")
		self.oHelper.WaitProcessing("Aguarde...")
		self.oHelper.CheckHelp("Baixa efetuada com sucesso!!!", "Fechar")
		self.oHelper.ClickLabel("Sair")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Outras Ações", "Visualizar")
		self.oHelper.CheckResult("FIF_STATUS", "7", name_attr=True)
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()