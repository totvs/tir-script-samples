import unittest
from tir import Webapp

class FINA910(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN", "02/08/2019", "T1", "D MG 01 ", "06")
		inst.oHelper.Program("FINA910")


	### CT028
	### Conciliação Individual FINA910 - Conciliador SITEF - Data de crédito diferentes. (Software Express).
	### TestCase: http://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T39903
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


	### CT029
	### Conciliação Individual FINA910 - Conciliador SITEF - Bancos diferentes. (Software Express)
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T39925
	def test_FINA910_CT029(self):
		self.oHelper.AddParameter("MV_EMPTEF","","0000002","0000002","0000002")  
		self.oHelper.SetParameters()

		self.oHelper.SetButton("Imp Arq SITEF")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetValue("Arquivo", "\\baseline\\FINA910_CT29_IND_BANCO.CSV")
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
		self.oHelper.SetValue("Pesq Dias Ant ?", "2")
		self.oHelper.SetValue("Tolerância em % ?", "12,00")
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
		# self.oHelper.RestoreParameters()


	### CT030
	### Conciliação por Lote FINA910 - Conciliador SITEF - Bancos Distintos. Usando MEP, processamento monousuário (Software Express)
	### TestCase: http://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T39934
	def test_FINA910_CT030(self):
		self.oHelper.AddParameter("MV_EMPTEF","","0000002","0000002","0000002")  
		self.oHelper.AddParameter("MV_USAMEP","",".T.",".T.",".T.")  
		self.oHelper.AddParameter("MV_BXCNAB","","N","N","N")  
		self.oHelper.AddParameter("MV_BLATHD","","1","1","1")  
		self.oHelper.AddParameter("MV_BLALOT","","50","50","50")  
		self.oHelper.SetParameters()

		self.oHelper.SetButton("Imp Arq SITEF")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetValue("Arquivo", "\\baseline\\FINA910_CT30_LOT_BANCOS.CSV")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetButton("Finalizar")

		self.oHelper.SetButton("Conciliacao")
		
		self.oHelper.SetValue("Da Filial ?", "")
		self.oHelper.SetValue("Ate Filial ?", "ZZZZZZZZ")
		self.oHelper.SetValue("Data Crédito De ?", "16/05/2019")
		self.oHelper.SetValue("Data Credito Até ?", "20/05/2019")
		self.oHelper.SetValue("Do Num NSU ?", "")
		self.oHelper.SetValue("Ate Num NSU ?", "ZZZZZZZZZ")
		self.oHelper.SetValue("Geração ?", "Por Lote")
		self.oHelper.SetValue("Tipo ?", "Ambos")
		self.oHelper.SetValue("Pesq Dias Ant ?", "2")
		self.oHelper.SetValue("Tolerância em % ?", "12,00")
		self.oHelper.SetValue("De Financeira ?", "")
		self.oHelper.SetValue("Ate Financeira ?", "")
		self.oHelper.SetValue("Data Baixa ?", "Database")
		self.oHelper.SetValue("Valida NSU p/ não Conc. ?", "Nao")
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Efetiva Conciliação")
		self.oHelper.CheckView("Aguarde...", "ProcRegua")
		self.oHelper.CheckHelp("Baixa efetuada com sucesso!!!", "Fechar")
		self.oHelper.ClickLabel("Sair")
		self.oHelper.SetButton("Sim")

		self.oHelper.SetButton("Outras Ações", "Visualizar")
		self.oHelper.CheckResult("FIF_STATUS", "7", name_attr=True)
		self.oHelper.SetButton("Cancelar")
		
		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()


	### CT031
	### Conciliação por Lote FINA910 - Conciliador SITEF - Data de crédito diferentes. Usando MEP, processamento monousuário (Software Express)
	### TestCase: http://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T39961
	def test_FINA910_CT031(self):
		self.oHelper.AddParameter("MV_EMPTEF","","0000002","0000002","0000002")  
		self.oHelper.AddParameter("MV_USAMEP","",".T.",".T.",".T.")  
		self.oHelper.AddParameter("MV_BXCNAB","","N","N","N")  
		self.oHelper.AddParameter("MV_BLATHD","","1","1","1")  
		self.oHelper.AddParameter("MV_BLALOT","","50","50","50")  
		self.oHelper.SetParameters()

		self.oHelper.SetButton("Imp Arq SITEF")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetValue("Arquivo", "\\baseline\\FINA910_CT31_LOT_CREDITO.CSV")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetButton("Finalizar")

		self.oHelper.SetButton("Conciliacao")
		
		self.oHelper.SetValue("Da Filial ?", "")
		self.oHelper.SetValue("Ate Filial ?", "ZZZZZZZZ")
		self.oHelper.SetValue("Data Crédito De ?", "16/05/2019")
		self.oHelper.SetValue("Data Credito Até ?", "20/05/2019")
		self.oHelper.SetValue("Do Num NSU ?", "")
		self.oHelper.SetValue("Ate Num NSU ?", "ZZZZZZZZZ")
		self.oHelper.SetValue("Geração ?", "Por Lote")
		self.oHelper.SetValue("Tipo ?", "Ambos")
		self.oHelper.SetValue("Pesq Dias Ant ?", "2")
		self.oHelper.SetValue("Tolerância em % ?", "12,00")
		self.oHelper.SetValue("De Financeira ?", "")
		self.oHelper.SetValue("Ate Financeira ?", "")
		self.oHelper.SetValue("Data Baixa ?", "Credito SITEF")
		self.oHelper.SetValue("Valida NSU p/ não Conc. ?", "Nao")
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


	### CT032
	### Conciliação por Lote FINA910 - Conciliador SITEF - Data de crédito diferentes. Usando MEP, processamento multithread (Software Express)
	### TestCase: http://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T39968
	def test_FINA910_CT032(self):
		self.oHelper.AddParameter("MV_EMPTEF","","0000002","0000002","0000002") 
		self.oHelper.AddParameter("MV_USAMEP","",".T.",".T.",".T.")  
		self.oHelper.AddParameter("MV_BXCNAB","","N","N","N")  
		self.oHelper.AddParameter("MV_BLATHD","","10","10","10")  
		self.oHelper.AddParameter("MV_BLALOT","","50","50","50")  
		self.oHelper.SetParameters()

		self.oHelper.SetButton("Imp Arq SITEF")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetValue("Arquivo", "\\baseline\\FINA910_CT32_LOT_MTHR_CREDITO.CSV")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetButton("Finalizar")

		self.oHelper.SetButton("Conciliacao")
		
		self.oHelper.SetValue("Da Filial ?", "")
		self.oHelper.SetValue("Ate Filial ?", "ZZZZZZZZ")
		self.oHelper.SetValue("Data Crédito De ?", "16/05/2019")
		self.oHelper.SetValue("Data Credito Até ?", "20/05/2019")
		self.oHelper.SetValue("Do Num NSU ?", "")
		self.oHelper.SetValue("Ate Num NSU ?", "ZZZZZZZZZ")
		self.oHelper.SetValue("Geração ?", "Por Lote")
		self.oHelper.SetValue("Tipo ?", "Ambos")
		self.oHelper.SetValue("Pesq Dias Ant ?", "2")
		self.oHelper.SetValue("Tolerância em % ?", "12,00")
		self.oHelper.SetValue("De Financeira ?", "")
		self.oHelper.SetValue("Ate Financeira ?", "")
		self.oHelper.SetValue("Data Baixa ?", "Credito SITEF")
		self.oHelper.SetValue("Valida NSU p/ não Conc. ?", "Nao")
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


	### CT033
	### Conciliação por Lote FINA910 - Conciliador SITEF - Bancos diferentes. Usando MEP, processamento multithread (Software Express)
	### TestCase: http://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T39977
	def test_FINA910_CT033(self):
		self.oHelper.AddParameter("MV_EMPTEF","","0000002","0000002","0000002")  
		self.oHelper.AddParameter("MV_USAMEP","",".T.",".T.",".T.")  
		self.oHelper.AddParameter("MV_BXCNAB","","N","N","N")  
		self.oHelper.AddParameter("MV_BLATHD","","10","10","10")  
		self.oHelper.AddParameter("MV_BLALOT","","50","50","50")  
		self.oHelper.SetParameters()

		self.oHelper.SetButton("Imp Arq SITEF")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetValue("Arquivo", "\\baseline\\FINA910_CT33_LOT_MTHR_BANCOS.CSV")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetButton("Finalizar")

		self.oHelper.SetButton("Conciliacao")
		
		self.oHelper.SetValue("Da Filial ?", "")
		self.oHelper.SetValue("Ate Filial ?", "ZZZZZZZZ")
		self.oHelper.SetValue("Data Crédito De ?", "16/05/2019")
		self.oHelper.SetValue("Data Credito Até ?", "20/05/2019")
		self.oHelper.SetValue("Do Num NSU ?", "")
		self.oHelper.SetValue("Ate Num NSU ?", "ZZZZZZZZZ")
		self.oHelper.SetValue("Geração ?", "Por Lote")
		self.oHelper.SetValue("Tipo ?", "Ambos")
		self.oHelper.SetValue("Pesq Dias Ant ?", "2")
		self.oHelper.SetValue("Tolerância em % ?", "12,00")
		self.oHelper.SetValue("De Financeira ?", "")
		self.oHelper.SetValue("Ate Financeira ?", "")
		self.oHelper.SetValue("Data Baixa ?", "Database")
		self.oHelper.SetValue("Valida NSU p/ não Conc. ?", "Nao")
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


	### CT034
	### Conciliação por Lote FINA910 - Conciliador SITEF. Usando MEP, processamento multithread 
	### porém com execução única volume menor que o necessário para iniciar uma thread. (Software Express)
	### TestCase: http://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T40030
	def test_FINA910_CT034(self):
		self.oHelper.AddParameter("MV_EMPTEF","","0000002","0000002","0000002")  
		self.oHelper.AddParameter("MV_USAMEP","",".T.",".T.",".T.")  
		self.oHelper.AddParameter("MV_BXCNAB","","S","S","S")  
		self.oHelper.AddParameter("MV_BLATHD","","10","10","10")  
		self.oHelper.AddParameter("MV_BLALOT","","50","50","50")  
		self.oHelper.SetParameters()

		self.oHelper.SetButton("Imp Arq SITEF")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetValue("Arquivo", "\\baseline\\FINA910_CT34_LOT_MTHR.CSV")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetButton("Finalizar")

		self.oHelper.SetButton("Conciliacao")
		
		self.oHelper.SetValue("Da Filial ?", "")
		self.oHelper.SetValue("Ate Filial ?", "ZZZZZZZZ")
		self.oHelper.SetValue("Data Crédito De ?", "16/05/2019")
		self.oHelper.SetValue("Data Credito Até ?", "20/05/2019")
		self.oHelper.SetValue("Do Num NSU ?", "")
		self.oHelper.SetValue("Ate Num NSU ?", "ZZZZZZZZZ")
		self.oHelper.SetValue("Geração ?", "Por Lote")
		self.oHelper.SetValue("Tipo ?", "Ambos")
		self.oHelper.SetValue("Pesq Dias Ant ?", "2")
		self.oHelper.SetValue("Tolerância em % ?", "12,00")
		self.oHelper.SetValue("De Financeira ?", "")
		self.oHelper.SetValue("Ate Financeira ?", "")
		self.oHelper.SetValue("Data Baixa ?", "Database")
		self.oHelper.SetValue("Valida NSU p/ não Conc. ?", "Nao")
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