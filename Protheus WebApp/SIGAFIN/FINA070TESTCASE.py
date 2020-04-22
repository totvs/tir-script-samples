import unittest
import time
from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

class FINA070(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN", DateSystem, "T1", "D MG 01 ", "06")
		inst.oHelper.Program("FINA070")


	### CT190
	### Baixar título.
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T40989
	def test_FINA070_CT190(self):
		prefixo = "FIN"
		titulo  = "A070TIR01"
		parcela = "A"
		tipo    = "NF "
		banco   = "001"
		agencia = "001"
		conta   = "001"
		data    = "30/05/2019"

		self.oHelper.AddParameter("MV_BR10925", "", "1", "1", "1")
		self.oHelper.SetParameters()

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Receb.", data)
		self.oHelper.SetValue("Data Crédito", data)
		self.oHelper.SetValue("= Valor Recebido", "3000,00")
		self.oHelper.CheckResult("- Pis", "19,50")
		self.oHelper.CheckResult("- Cofins", "90,00")
		self.oHelper.CheckResult("- Csll", "30,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.CheckResult("- Pagtos Parciais", "3000,00")
		self.oHelper.CheckResult("- Pis", "6,50")
		self.oHelper.CheckResult("- Cofins", "30,00")
		self.oHelper.CheckResult("- Csll", "10,00")
		self.oHelper.CheckResult("= Valor Recebido", "814,00")

		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	### CT191
	### Cancelar baixa.
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T40991
	def test_FINA070_CT191(self):
		prefixo = "FIN"
		titulo  = "A070TIR01"
		parcela = "B"
		tipo    = "NF "

		# O parâmetro está sendo configurado no CT190
		# self.oHelper.AddParameter("MV_BR10925", "", "1", "1", "1")
		# #self.oHelper.SetParameters()

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Outras Ações", "Canc Baixa")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.CheckResult("- Pagtos Parciais", "0,00")
		self.oHelper.CheckResult("- Pis", "26,00")
		self.oHelper.CheckResult("- Cofins", "120,00")
		self.oHelper.CheckResult("- Csll", "40,00")
		self.oHelper.CheckResult("= Valor Recebido", "3814,00")

		self.oHelper.SetButton("Cancelar")

		# verifica se foi cancelado
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.CheckResult("- Pagtos Parciais", "0,00")
		self.oHelper.CheckResult("- Pis", "26,00")
		self.oHelper.CheckResult("- Cofins", "120,00")
		self.oHelper.CheckResult("- Csll", "40,00")
		self.oHelper.CheckResult("= Valor Recebido", "3814,00")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	### CT192
	### Excluir baixa.
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T40992
	def test_FINA070_CT192(self):
		prefixo = "FIN"
		titulo  = "A070TIR01"
		parcela = "C"
		tipo    = "NF "

		# O parâmetro está sendo configurado no CT190
		# self.oHelper.AddParameter("MV_BR10925", "", "1", "1", "1")
		# self.oHelper.SetParameters()

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.CheckResult("- Pagtos Parciais", "0,00")
		self.oHelper.CheckResult("- Pis", "26,00")
		self.oHelper.CheckResult("- Cofins", "120,00")
		self.oHelper.CheckResult("- Csll", "40,00")
		self.oHelper.CheckResult("= Valor Recebido", "3814,00")

		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()
		# self.oHelper.AddParameter("MV_BR10925", "", "2", "1", "1")
		# self.oHelper.SetParameters()


	### CT193
	### Baixar título com multa.
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T40986
	def test_FINA070_CT193(self):
		prefixo = "FIN"
		titulo  = "FIN002152"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "001"
		conta   = "001"
		data    = "21/06/2019"

		self.oHelper.AddParameter("MV_BR10925", "", "2", "2", "2")# restaura do teste anterior
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
		#self.oHelper.AddParameterReset()

	### CT198
	### Baixar título com rateio de multi. naturezas
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T41643
	def test_FINA070_CT198(self):
		prefixo = "FIN"
		titulo  = "000000102"
		parcela = " "
		tipo    = "NF "

		self.oHelper.AddParameter("MV_JURTIPO", "", "M", "M", "M") # Restaura do teste anterior
		self.oHelper.AddParameter("MV_MULNATR", "", ".T.", ".T.", ".T.")
		self.oHelper.AddParameter("MV_IMPBXCR", "", "2", "2", "2") #Parametro para o CT260
		self.oHelper.AddParameter("MV_MOEDBCO", "", ".T.", ".T.", ".T.")
		self.oHelper.AddParameter("MV_SLDBXCR", "", "C", "C", "C") #CT220
		self.oHelper.AddParameter("MV_CMC7FIN", "", "S", "S", "S") #CT220

		self.oHelper.SetParameters()

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("", True)
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetValue("Natureza", "001", grid=True, row=1)
		self.oHelper.SetValue("Vlr.Movim.", "12000,00", grid=True, row=1)
		self.oHelper.SetValue("Rat. C.Custo", "1 - Sim", grid=True, row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Outras Ações", "Rateio")

		self.oHelper.SetValue("cCodRateio", "001", name_attr=True)
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Outras Ações", "Consulta Rateio Multi Naturezas")
		self.oHelper.WaitShow("Contas a Receber - Consulta Rateio Múltiplas Naturezas - Visualizar")
		self.oHelper.ClickFolder("Baixas")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
		#self.oHelper.AddParameterReset()


	### CT206
	### TIR - Baixa banco em moeda 1 e título com moeda 5 MV_MOEDBCO = .T.
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T42940
	def test_FINA070_CT206(self):
		prefixo = "RIC"
		titulo  = "RIC018263"
		parcela = " "
		tipo    = "NF "
		banco   = "RIC"
		agencia = "M1"
		conta   = "0"
		data    = "01/06/2019"

		# self.oHelper.AddParameter("MV_MOEDBCO", "", ".T.", ".T.", ".T.")
		# self.oHelper.SetParameters()
		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Receb.", data)
		self.oHelper.SetValue("Data Crédito", data)

		self.oHelper.CheckResult("Taxa contratada", "5,0000")
		self.oHelper.CheckResult("= Valor Recebido", "20000,00")
		self.oHelper.CheckResult("Valor IEN", "4000,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
		#self.oHelper.AddParameterReset()
	
	### CT208
	### Baixa de título moeda 1 em banco moeda 2
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T42944
	def test_FINA070_CT208(self):
		prefixo = "FIN"
		titulo  = "M1XX19447"
		parcela = " "
		tipo    = "NF "
		banco   = "FIN"
		agencia = "FINM2"
		conta   = "001"
		data    = "30/07/2019"

		#self.oHelper.AddParameter("MV_MOEDBCO", "", ".T.", ".T.", ".T.") setado no teste 206
		#self.oHelper.SetParameters()
		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Receb.", data)
		self.oHelper.SetValue("Data Crédito", data)

		self.oHelper.CheckResult("= Valor Recebido", "1500,00")
		self.oHelper.CheckResult("Valor R$", "6000,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
		# self.oHelper.AddParameterReset()


	### CT207
	### TIR - Baixa de título com valor acessório
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T42942
	def test_FINA070_CT207(self):
		prefixo = "FIN"
		titulo  = "000000101"
		parcela = "1"
		tipo    = "NF "
		banco   = "FIN"
		agencia = "00010"
		conta   = "0000000000"
		data    = "17/04/2019"

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.CheckResult("+ Valores Acessórios", "1000,00")
		self.oHelper.CheckResult("= Valor Recebido", "2000,00")

		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Receb.", data)
		self.oHelper.SetValue("Data Crédito", data)

		self.oHelper.SetButton("Outras Ações", "Valores Acessórios")
		self.oHelper.WaitShow("Contas a Receber - Valores Acessórios - Alteração")

		self.oHelper.SetValue("FKD_VLINFO", "500,00", grid=True, name_attr=True, row=1)
		self.oHelper.SetValue("FKD_VLINFO", "0,00",   grid=True, name_attr=True, row=2)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Confirmar")
		self.oHelper.CheckHelp("Registro alterado com sucesso.","Fechar")

		self.oHelper.CheckResult("+ Valores Acessórios", "500,00")
		self.oHelper.CheckResult("= Valor Recebido", "1500,00")
		self.oHelper.AssertTrue()
		self.oHelper.SetButton("Salvar")

	### CT093
	### Baixa por lote
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T15110
	def test_FINA070_CT093(self):
		banco = '161'
		agencia = '00161'
		conta = '0000000161'
		ntitulos = '3'
		lote ='LT161'
		natureza ='FIN161'
		dataDe='01/10/2016'
		dataAte='31/12/2016'
		prefixo = "161"
		titulo  = "FIN000001"
		titulo2  = "FIN000002"
		parcela = " "
		tipo    = "NF "

		self.oHelper.SetButton("Outras Ações", "Lote")
		self.oHelper.SetValue("cBancolt", banco, name_attr=True)
		self.oHelper.SetValue("cAgencialt", agencia, name_attr=True)
		self.oHelper.SetValue("cContalt", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("cNaturLote", natureza, name_attr=True)
		self.oHelper.SetValue("dVencDe", dataDe, name_attr=True)
		self.oHelper.SetValue("dVencAte", dataAte, name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Salvar")

		self.oHelper.ClickBox("Filial", select_all=True)
		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckResult("nValRec", "10.000,99", name_attr=True)
		self.oHelper.SetValue("cMotBx", "NORMAL", name_attr=True)
		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckResult("nValRec", "20.000,99", name_attr=True)
		self.oHelper.SetValue("cMotBx", "NORMAL", name_attr=True)
		self.oHelper.SetButton("Salvar")
		
		self.oHelper.CheckResult("nValRec", "30.000,99", name_attr=True)
		self.oHelper.SetValue("cMotBx", "NORMAL", name_attr=True)
		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Outras Ações", "Canc Baixa")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo2}{parcela}{tipo}")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.CheckHelp(text='VLDBXLOTE',button='Fechar')
		self.oHelper.AssertTrue()

	### CT220
	### Validações tela de cheque na baixa
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44213
	def test_FINA070_CT220(self):
		prefixo = "FIN"
		titulo  = "TIRCHEQUE"
		parcela = " "
		tipo    = "NF "
		# self.oHelper.AddParameter("MV_CMC7FIN", "", "S", "S", "S")
		# self.oHelper.SetParameters()
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")
		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetButton("Outras Ações", "Cheque(s)")
		self.oHelper.SetButton("Outras Ações", "CMC7")
		self.oHelper.SetValue("cCmc7", "<TIRTIR00<0180001265<577508114673:", name_attr=True)
		self.oHelper.SetButton("Ok")
		self.oHelper.SetValue("Valor Nominal", "500,00")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Não")
		
		self.oHelper.SetValue("Valor ref. baixa", "1.000,00", grid=True, row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Outras Ações", "Canc Baixa")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.AssertTrue()

	### CT261
	### PCC regra antiga
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T49802

	def test_FINA070_CT261(self):
		prefixo = "FIN"
		titulo  = "TITANTTIR"
		parcela = " "
		tipo    = "NF "
		data	='11/06/2015'
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")
		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Data Receb.", data)
		self.oHelper.SetValue("Data Crédito", data)
		# Verifica o valor calculado com a nova regra do pcc
		self.oHelper.CheckResult("- Pis", "14,30")
		self.oHelper.CheckResult("- Cofins", "22,00")
		self.oHelper.CheckResult("- Csll", "66,00")
		# Com a regra antiga do PCC não foi atingido o mínimo para retenção
		self.oHelper.SetValue("- Descontos", "25,00")
		self.oHelper.SetValue("+ Multa", "83,00")
		self.oHelper.SetValue("+ Tx.Permanenc.", "25,00")
		self.oHelper.SetValue("= Valor Recebido", "2.250,00")
		self.oHelper.CheckResult("- Pis", "0,00")
		self.oHelper.CheckResult("- Cofins", "0,00")
		self.oHelper.CheckResult("- Csll", "0,00")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Outras Ações", "Canc Baixa")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()

	### CT260
	### Alterar impostos na baixa
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T49799

	def test_FINA070_CT260(self):
		
		prefixo = "FIN"
		titulo  = "000000207"
		parcela = "1"
		tipo    = "NF "
		# self.oHelper.AddParameter("MV_MULNATR", "", ".T.", ".T.", ".T.")
		# self.oHelper.AddParameter("MV_IMPBXCR", "", "2", "2", "2")
		# self.oHelper.SetParameters()
		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")
		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("", True) #Rateio multiplas naturezas
		self.oHelper.SetValue("nValRec"	, "5.000,00", name_attr=True)
		self.oHelper.SetButton("Salvar") #Tela da baixa
		self.oHelper.SetButton("Salvar") #Tela do rateio
		
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")
		self.oHelper.SetButton("Outras Ações", "Impostos")
		self.oHelper.SetValue("nOrigPis"	, "60,00"	, name_attr=True)
		self.oHelper.SetValue("nOrigCofins"	, "250,00"	, name_attr=True)
		self.oHelper.SetValue("nOrigCsll"	, "190,00"	, name_attr=True)
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Sim")

		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("", True) #Rateio multiplas naturezas
		self.oHelper.CheckResult("nTotAbImp", "650,00"	, name_attr=True)
		self.oHelper.CheckResult("nValRec"	, "4.350,00", name_attr=True)
		self.oHelper.SetButton("Salvar") #Tela da baixa
		self.oHelper.SetButton("Salvar") #Tela do rateio

		self.oHelper.SetButton("Outras Ações", "Canc Baixa")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Confirmar")
		
		self.oHelper.SetButton("Outras Ações", "Canc Baixa")
		self.oHelper.SetButton("Confirmar")
		
		self.oHelper.AssertTrue()

	### CT152
	### Apenas tela consulta de impostos.
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T34862

	def test_FINA070_CT152(self):
		
		prefixo = "FIN"
		titulo  = "A110CT35A"
		parcela = " "
		tipo    = "NF "
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Outras Ações", "Consulta de Retenções")
		self.oHelper.CheckResult("Valor Calc.", "300,00", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Valor Calc.", "100,00", grid=True, line=2, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Valor Calc.", "1.100,00", grid=True, line=3, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Valor Calc.", "150,00", grid=True, line=4, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Valor Calc.", "65,00", grid=True, line=5, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Valor Calc.", "300,00", grid=True, line=1, grid_number=2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
	

	### CT263
	### Baixa elm lote com título que ja teve baixa parcial
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T49906

	def test_FINA070_CT263(self):
		
		banco = 'CX1'
		agencia = '00001'
		conta = '0000000001'
		ntitulos = '1'
		lote ='LT070'
		natureza ='FIN0000105'
		dataDe='27/03/2020'
		dataAte='27/03/2020'
		data='28/03/2020'
		prefixo = "FIN"
		titulo  = "000000208"
		parcela = "1"
		tipo    = "NF "
		self.oHelper.AddParameter("MV_IMPBAIX", "", "1", "1", "1")
		# self.oHelper.AddParameter("MV_BR10925", "", "1", "1", "1")
		self.oHelper.SetParameters()
		
		self.oHelper.SetButton("Outras Ações", "Lote")
		self.oHelper.SetValue("cBancolt", banco, name_attr=True)
		self.oHelper.SetValue("cAgencialt", agencia, name_attr=True)
		self.oHelper.SetValue("cContalt", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("cNaturLote", natureza, name_attr=True)
		self.oHelper.SetValue("dVencDe", dataDe, name_attr=True)
		self.oHelper.SetValue("dVencAte", dataAte, name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Salvar")

		self.oHelper.ClickBox("Filial", select_all=True) 
		self.oHelper.SetButton("Salvar")
		
		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Data Receb.", data)
		self.oHelper.SetValue("Data Crédito", data)
		self.oHelper.SetValue("nJuros", "25,00", name_attr=True)
		self.oHelper.SetValue("nMulta", "25,00", name_attr=True)
		self.oHelper.SetValue("nDescont", "50,00", name_attr=True)

		self.oHelper.SetValue("nJuros", "10,00", name_attr=True)
		self.oHelper.SetValue("nMulta", "10,00", name_attr=True)
		self.oHelper.SetValue("nDescont", "10,00", name_attr=True)

		self.oHelper.SetValue("nJuros", "25,00", name_attr=True)
		self.oHelper.SetValue("nMulta", "25,00", name_attr=True)
		self.oHelper.SetValue("nDescont", "50,00", name_attr=True)
		
		self.oHelper.CheckResult("- Pis", "32,50")
		self.oHelper.CheckResult("- Cofins", "150,00")
		self.oHelper.CheckResult("- Csll", "50,00")

		self.oHelper.CheckResult("= Valor Recebido", "4.385,00")
		self.oHelper.SetButton("Salvar")
		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')
				
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Outras Ações", "Canc Baixa")
		self.oHelper.SetButton("Ok")
		self.oHelper.CheckHelp(text='FINIMPBX',button='Fechar')
			
		self.oHelper.SetButton("Outras Ações", "Canc Baixa")
		self.oHelper.ClickListBox("FIN 000000208          1 NF  FIN292 01 28/03/2020        4.385,00   03")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Confirmar")
		
		self.oHelper.SetButton("Outras Ações", "Canc Baixa")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.AssertTrue()

	### CT150
	### Apenas tela consulta de impostos.
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T34860

	def test_FINA070_CT150(self):
		
		prefixo = "FIN"
		titulo  = "A110CT34A"
		parcela = " "
		tipo    = "NF "
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.SetButton("Outras Ações", "Retenção de impostos")
		self.oHelper.CheckResult("Valor Calculado", "16,50", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("Valor a Reter", "50,00", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.CheckResult("- Retenções", "50,00")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()

