import unittest
import time
from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

class FINA080(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN", DateSystem, "T1", "D MG 01 ", "06")
		inst.oHelper.Program("FINA080")
	
	
	#{Protheus.doc} test_FINA080_CT110
	#Baixa de título Moeda 2, com banco moeda 1 informando cheque

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/project/10231/testCase?folderId=17808

	def test_FINA080_CT110(self):
		prefixo = "TIR"
		titulo  = "F080CT110"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		cheque  = "F080CT110"
		
		
		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SetKey("F12")
		self.oHelper.WaitShow("Parametros")
		self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		self.oHelper.SetButton("Ok")
		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Cheque No.", cheque)
		self.oHelper.CheckResult("Taxa contratada", "5,0000")
		self.oHelper.CheckResult("= Valor Pago", "5.000,00")
		self.oHelper.CheckResult("Valor US$", "1.000,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()


	#{Protheus.doc} test_FINA080_CT113
	#Baixa de título Moeda 2 (com banco moeda 1 cheque cadastrado)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/project/10231/testCase?folderId=17808
	
	def test_FINA080_CT113(self):
		prefixo = "TIR"
		titulo  = "F080CT112"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		cheque   = "F080CT112"
		
		
		self.oHelper.WaitShow("Baixa de Titulos")
		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")
		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.CheckResult("Agência", agencia)
		self.oHelper.CheckResult("Conta", conta)
		self.oHelper.CheckResult("Cheque No.", cheque)
		self.oHelper.CheckResult("Taxa contratada", "5,0000")
		self.oHelper.CheckResult("= Valor Pago", "10.000,00")
		self.oHelper.CheckResult("Valor US$", "2.000,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT114
	#Baixa total de título Moeda 2, com taxa de permanência informada, (banco moeda 1, taxa do dia, – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50384
	
	def test_FINA080_CT114(self):
		prefixo = "TIR"
		titulo  = "F080CT114"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "16/04/2020"

		#Parametrização default
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.SetParameters()


		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")


		self.oHelper.WaitShow("Baixa de Titulos")
		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("Data Pagto.", data)
		self.oHelper.CheckResult("Data Debito", data)
		self.oHelper.SetValue("Taxa contratada", "140,0000")
		self.oHelper.SetValue("+ Tx.Permanenc.", "140,00")
		self.oHelper.CheckResult("= Valor Pago", "140.140,00")
		self.oHelper.CheckResult("Valor US$", "1.001,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "1.011,01")

		self.oHelper.SetButton("Salvar")

		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT115
	#Baixa total de título Moeda 2, com taxa de permanência calculada (banco moeda 1, taxa do Contratada – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50385
	
	def test_FINA080_CT115(self):
		prefixo = "TIR"
		titulo  = "F080CT115"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
				
		self.oHelper.WaitShow("Baixa de Titulos")

		#Parametrização default
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.SetParameters()

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("26/04/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")

		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Taxa contratada", "5,0000")
		self.oHelper.CheckResult("+ Tx.Permanenc.", "50,00")
		self.oHelper.CheckResult("= Valor Pago", "10.050,00")
		self.oHelper.CheckResult("Valor US$", "2.010,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "1.005,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT116
	#Baixa Parcial de título Moeda 2 com desconto informado, (banco moeda 1, taxa do dia – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50386
	
	def test_FINA080_CT116(self):
		prefixo = "TIR"
		titulo  = "F080CT116"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"


		#Parametrização default
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.SetParameters()
		
		
		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Taxa contratada", "140,0000")
		self.oHelper.SetValue("= Valor Pago", "56.000,00")
		self.oHelper.CheckResult("Valor US$", "400,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "404,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Taxa contratada", "135,0000")
		self.oHelper.CheckResult("- Pagtos.Parciais", "400,00")
		self.oHelper.SetValue("- Descontos", "1000,00")
		self.oHelper.CheckResult("= Valor Pago", "80.000,00")
		self.oHelper.CheckResult("Valor US$", "592,59")
		self.oHelper.CheckResult("+ Corr.Monetária", "-2.364,43")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT117
	#Baixa parcial de título Moeda 2 com acréscimo (banco moeda 1, taxa do Contratada – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50387
	
	def test_FINA080_CT117(self):
		prefixo = "TIR"
		titulo  = "F080CT117"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		
		self.oHelper.WaitShow("Baixa de Titulos")

		#Parametrização default
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.SetParameters()

		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Taxa contratada", "5,0000")
		self.oHelper.CheckResult("+ Acrescimo", "100,00")
		self.oHelper.SetValue("= Valor Pago", "2.000,00")
		self.oHelper.CheckResult("Valor US$", "400,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "200,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Taxa contratada", "4,8000")
		self.oHelper.CheckResult("+ Acrescimo", "0,00")
		self.oHelper.CheckResult("- Pagtos.Parciais", "300,00")
		self.oHelper.CheckResult("= Valor Pago", "8.160,00")
		self.oHelper.CheckResult("Valor US$", "1700,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "510,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT120
	#Baixa total de título Moeda 2 (banco moeda 2, taxa do dia – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50467
	
	def test_FINA080_CT120(self):
		prefixo = "TIR"
		titulo  = "F080CT120"
		parcela = " "
		tipo    = "NF "
		banco   = "002"
		agencia = "08000"
		conta   = "080110"

		#Data Definida no CT114
		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("= Valor Pago", "1.000,00")
		self.oHelper.CheckResult("Valor US$", "1.000,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
	
	
	
	#{Protheus.doc} test_FINA080_CT121
	#Baixa Parcial de título Moeda 2 (banco moeda 2, taxa do Contratada – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50468
	
	def test_FINA080_CT121(self):
		prefixo = "TIR"
		titulo  = "F080CT121"
		parcela = " "
		tipo    = "NF "
		banco   = "002"
		agencia = "08000"
		conta   = "080110"
				
		self.oHelper.WaitShow("Baixa de Titulos")
		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("= Valor Pago", "600,00")
		self.oHelper.CheckResult("Valor US$", "600,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("= Valor Pago", "1.400,00")
		self.oHelper.CheckResult("Valor US$", "1.400,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT122
	#Baixa em lote de título Moeda 2 (banco moeda 2, taxa do dia – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50469
	
	def test_FINA080_CT122(self):
    	
		banco   = "002"
		agencia = "08000"
		conta   = "080110"
		ntitulos = '2'
		lote ='LTC122'
		natureza ='FIN080SIMP'
		data    = "16/04/2020"
		titulo1  = "LOTACT122"
		titulo2  = "LOTBCT122"


		#Data Definida no CT114
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", data, name_attr=True)
		self.oHelper.SetValue("DVENCFIM", data, name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")
		self.oHelper.ClickBox("No. Titulo", titulo1)
		self.oHelper.ClickBox("No. Titulo", titulo2)
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("= Valor Pago", "1.000,00")
		self.oHelper.CheckResult("Valor US$", "1.000,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("= Valor Pago", "2.000,00")
		self.oHelper.CheckResult("Valor US$", "2.000,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')
		self.oHelper.AssertTrue()


	
	#{Protheus.doc} test_FINA080_CT123
	#Baixa lote de título Moeda 2 com multa informada (banco moeda 1, taxa do Contratada – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50470
	
	def test_FINA080_CT123(self):
    	
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		ntitulos = '2'
		lote ='LTC123'
		natureza ='FIN080SIMP'
		data    = "16/04/2020"
		titulo1  = "LOTACT123"
		titulo2  = "LOTBCT123"


		#Parametrização default
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.SetParameters()


		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", data, name_attr=True)
		self.oHelper.SetValue("DVENCFIM", data, name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")
		self.oHelper.ClickBox("No. Titulo", titulo1)
		self.oHelper.ClickBox("No. Titulo", titulo2)
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Taxa contratada", "5,0000")
		self.oHelper.SetValue("+ Multa", "20,00")
		self.oHelper.CheckResult("= Valor Pago", "5.020,00")
		self.oHelper.CheckResult("Valor US$", "1.004,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "502,00")

		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Taxa contratada", "5,0000")
		self.oHelper.SetValue("+ Multa", "30,00")
		self.oHelper.CheckResult("= Valor Pago", "10.030,00")
		self.oHelper.CheckResult("Valor US$", "2.006,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')
		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT124
	#Baixa total de título (Sem impostos, com acréscimo, valores acessórios - Moeda 1 – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50488
	
	def test_FINA080_CT124(self):
		prefixo = "TIR"
		titulo  = "F080CT124"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		
		
		self.oHelper.WaitShow("Baixa de Titulos")
		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("+ Acrescimo", "100,00")
		self.oHelper.CheckResult("+ Valores Acessórios", "35,00")
		self.oHelper.CheckResult("= Valor Pago", "10.135,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
		
	
	
	#{Protheus.doc} test_FINA080_CT125
	#Baixa parcial de título (Sem impostos, com acréscimo, valores acessórios - Moeda 1 – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50489
	
	def test_FINA080_CT125(self):
		prefixo = "TIR"
		titulo  = "F080CT125"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("+ Acrescimo", "90,00")
		self.oHelper.CheckResult("+ Valores Acessórios", "15,00")
		self.oHelper.SetValue("= Valor Pago", "600,00")

		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("- Pagtos.Parciais", "495,00")
		self.oHelper.CheckResult("+ Acrescimo", "0,00")
		self.oHelper.CheckResult("+ Valores Acessórios", "0,00")
		self.oHelper.CheckResult("= Valor Pago", "1.505,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT126
	#Baixa total de título (Com motivo de baixa DACAO – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50490
	
	def test_FINA080_CT126(self):
		prefixo = "TIR"
		titulo  = "F080CT126"
		parcela = " "
		tipo    = "NF "
		
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DACAO")
		self.oHelper.CheckResult("= Valor Pago", "1.000,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT127
	#Baixa total de título Moeda 1 (Motivo de baixa VENDOR – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50491

	def test_FINA080_CT127(self):
		prefixo = "TIR"
		titulo  = "F080CT127"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		Contrato = "000000000000001"
		data    = "16/04/2020"
		PrefVen = "VEN"
		tipoven	= "DP"

		#Data Definida no CT114
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "VENDOR")

		self.oHelper.SetValue("cContrato", Contrato, name_attr=True)
		self.oHelper.SetValue("cBancoV", banco, name_attr=True)
		self.oHelper.SetValue("cAgenciaV", agencia, name_attr=True)
		self.oHelper.SetValue("cPrefV", PrefVen, name_attr=True)
		self.oHelper.SetValue("cNumV", titulo, name_attr=True)
		self.oHelper.SetValue("cTipV", tipoven, name_attr=True)
		self.oHelper.SetValue("dDataVencV", data, name_attr=True)
		self.oHelper.CheckResult("nTxAcresV", "5,0000", name_attr=True)
		self.oHelper.CheckResult("cNaturV", "VENDOR", name_attr=True)
		self.oHelper.CheckResult("nValTitV", "3.000,00", name_attr=True)

		self.oHelper.SetButton("Ok")

		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", data)
		self.oHelper.CheckResult("= Valor Pago", "3.000,00")

		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {PrefVen}{titulo}{parcela}{tipoven}")

		self.oHelper.SetButton("Visualizar")
		self.oHelper.WaitShow("Baixa de Titulos - VISUALIZAR")

		self.oHelper.CheckResult("E2_SALDO", "3.000,00")

		self.oHelper.ClickFolder('Administrativo')
		self.oHelper.CheckResult("E2_ACRESC", "150,00")

		self.oHelper.SetButton("Cancelar")


		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT128
	#Baixa lote de título Moeda 1 (Sem impostos, com abatimento - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50492

	def test_FINA080_CT128(self):
    	
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		ntitulos = '2'
		lote ='LTC128'
		natureza='FIN080SIMP'
		data    = "17/04/2020"
		prefixo = "TIR"
		titulo1 = "LOTACT128"
		titulo2 = "LOTBCT128"
		parcela = " "
		tipo    = "NF"
		tipoabt = "AB-"
		fornecedor = "FINA01"
		loja = "01"

		#Data Definida no CT114
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", data, name_attr=True)
		self.oHelper.SetValue("DVENCFIM", data, name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")
		self.oHelper.ClickBox("No. Titulo", titulo1)
		self.oHelper.ClickBox("No. Titulo", titulo2)
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		
		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')
		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT135
	#Baixa total de título (Com PCC/IRF na baixa e ISS/INSS na emissão - Moeda 1 – Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50568
	
	def test_FINA080_CT135(self):
		prefixo = "TIR"
		titulo  = "F080CT135"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		self.oHelper.SetParameters()
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("- Irrf", "150,00")
		self.oHelper.CheckResult("- Pis", "65,00")
		self.oHelper.CheckResult("- Cofins", "300,00")
		self.oHelper.CheckResult("- Csll", "100,00")
		self.oHelper.CheckResult("= Valor Pago", "7.785,00")


		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	
	#{Protheus.doc} test_FINA080_CT136
	#Baixa parcial de título (Com PCC/IRF na baixa e ISS/INSS na emissão - Moeda 1 – Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50569
	
	def test_FINA080_CT136(self):
		prefixo = "TIR"
		titulo  = "F080CT136"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		
		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.SetParameters()
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("= Valor Pago", "4.000,00")
		self.oHelper.CheckResult("- Irrf", "60,00")
		self.oHelper.CheckResult("- Pis", "26,00")
		self.oHelper.CheckResult("- Cofins", "120,00")
		self.oHelper.CheckResult("- Csll", "40,00")

		self.oHelper.SetButton("Salvar")


		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("- Irrf", "90,00")
		self.oHelper.CheckResult("- Pis", "39,00")
		self.oHelper.CheckResult("- Cofins", "180,00")
		self.oHelper.CheckResult("- Csll", "60,00")
		self.oHelper.CheckResult("= Valor Pago", "3.785,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()



	#{Protheus.doc} test_FINA080_CT137
	#Baixa total de título (Com PCC/IRF/ ISS na baixa e INSS na emissão - Moeda 1 – Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50570
	
	def test_FINA080_CT137(self):
		prefixo = "TIR"
		titulo  = "F080CT137"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "16/04/2020"


		self.oHelper.AddParameter("MV_MRETISS", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		self.oHelper.SetParameters()

		#Data Definida no CT114
		#time.sleep(15)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", "17/04/2020")
		self.oHelper.CheckResult("- Iss", "500,00")
		self.oHelper.CheckResult("- Irrf", "150,00")
		self.oHelper.CheckResult("- Pis", "65,00")
		self.oHelper.CheckResult("- Cofins", "300,00")
		self.oHelper.CheckResult("- Csll", "100,00")
		self.oHelper.CheckResult("= Valor Pago", "7.785,00")


		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()


	#{Protheus.doc} test_FINA080_CT138
	#Baixa parcial de título (Com PCC/IRF/ ISS na baixa e INSS na emissão - Moeda 1 – Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50571

	def test_FINA080_CT138(self):
		prefixo = "TIR"
		titulo  = "F080CT138"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "16/04/2020"

		#Parametrização CT137
		#self.oHelper.AddParameter("MV_MRETISS", "", "2", "2", "2")
		#self.oHelper.SetParameters()

		#Data Definida no CT114
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
				
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", "17/04/2020")
		self.oHelper.SetValue("= Valor Pago", "4.000,00")
		self.oHelper.CheckResult("- Iss", "200,00")
		self.oHelper.CheckResult("- Irrf", "60,00")
		self.oHelper.CheckResult("- Pis", "26,00")
		self.oHelper.CheckResult("- Cofins", "120,00")
		self.oHelper.CheckResult("- Csll", "40,00")

		self.oHelper.SetButton("Salvar")


		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", "17/04/2020")
		self.oHelper.CheckResult("- Iss", "300,00")
		self.oHelper.CheckResult("- Irrf", "90,00")
		self.oHelper.CheckResult("- Pis", "39,00")
		self.oHelper.CheckResult("- Cofins", "180,00")
		self.oHelper.CheckResult("- Csll", "60,00")
		self.oHelper.CheckResult("= Valor Pago", "3.785,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
	
	#{Protheus.doc} test_FINA080_CT141
	#Baixa total de título (Com PCC/IRF na baixa e ISS/INSS na emissão - Moeda 1 – Acréscimo, desconto - Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50578
	
	def test_FINA080_CT141(self):
		prefixo = "TIR"
		titulo  = "F080CT139"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "16/04/2020"

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		self.oHelper.SetParameters()

		#Data Definida no CT114
		#time.sleep(15)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", "17/04/2020")
		self.oHelper.SetValue("- Descontos", "50,00")
		self.oHelper.CheckResult("+ Acrescimo", "200,00")
		self.oHelper.CheckResult("- Irrf", "150,00")
		self.oHelper.CheckResult("- Pis", "65,00")
		self.oHelper.CheckResult("- Cofins", "300,00")
		self.oHelper.CheckResult("- Csll", "100,00")
		self.oHelper.CheckResult("= Valor Pago", "7.935,00")


		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
	
	#{Protheus.doc} test_FINA080_CT142
	#Baixa parcial de título (Com PCC/IRF na baixa e ISS/INSS na emissão – Decréscimo, Valores acessórios e Multa - Moeda 1 – Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50579

	def test_FINA080_CT142(self):
		prefixo = "TIR"
		titulo  = "F080CT140"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "17/04/2020"

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.SetParameters()

		#Data Definida no CT114
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("= Valor Pago", "4.000,00")
		self.oHelper.CheckResult("- Decrescimo" , "50,00")
		self.oHelper.CheckResult("+ Valores Acessórios", "-15,00")
		self.oHelper.CheckResult("- Irrf", "60,75")
		self.oHelper.CheckResult("- Pis", "26,42")
		self.oHelper.CheckResult("- Cofins", "121,95")
		self.oHelper.CheckResult("- Csll", "40,65")

		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.CheckResult("- Decrescimo" , "0,00")
		self.oHelper.CheckResult("+ Valores Acessórios", "0,00")
		self.oHelper.CheckResult("- Irrf", "89,25")
		self.oHelper.CheckResult("- Pis", "38,57")
		self.oHelper.CheckResult("- Cofins", "178,05")
		self.oHelper.CheckResult("- Csll", "59,35")
		self.oHelper.CheckResult("= Valor Pago", "3.720,01")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT143
	#Baixa total de título em lote (Com PCC/IRF na baixa e ISS /INSS na emissão – Valores acessórios e multa - Moeda 1 – Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50580

	def test_FINA080_CT143(self):
    	
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		ntitulos = '2'
		lote ='LTC143'
		natureza='FIN080CIMP'
		data    = "16/04/2020"
		titulo1 = "LOTACT141"
		titulo2 = "LOTBCT141"

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.SetParameters()

		#Data Definida no CT114
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("16/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", data, name_attr=True)
		self.oHelper.SetValue("DVENCFIM", data, name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.ClickBox("No. Titulo", titulo1)
		self.oHelper.ClickBox("No. Titulo", titulo2)
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("+ Valores Acessórios", "35,00")
		self.oHelper.SetValue("+ Multa", "20,00")
		self.oHelper.CheckResult("- Irrf", "150,00")
		self.oHelper.CheckResult("- Pis", "65,00")
		self.oHelper.CheckResult("- Cofins", "300,00")
		self.oHelper.CheckResult("- Csll", "100,00")
		
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("+ Valores Acessórios", "58,00")
		self.oHelper.SetValue("+ Multa", "15,00")
		self.oHelper.CheckResult("- Irrf", "150,00")
		self.oHelper.CheckResult("- Pis", "65,00")
		self.oHelper.CheckResult("- Cofins", "300,00")
		self.oHelper.CheckResult("- Csll", "100,00")
		
		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')
		self.oHelper.AssertTrue()
	
	#{Protheus.doc} test_FINA080_CT144
	#Baixa total de título (Com PCC/IRF/ ISS na baixa e INSS na emissão - Moeda 1 – Taxa de permanência - Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50599
	
	def test_FINA080_CT144(self):
		prefixo = "TIR"
		titulo  = "F080CT144"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "27/04/2020"

		self.oHelper.AddParameter("MV_MRETISS", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		self.oHelper.SetParameters()

		time.sleep(30)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("26/04/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")
	
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("Data Pagto.", "26/04/2020")
		self.oHelper.SetValue("Data Debito", data)
		self.oHelper.CheckResult("+ Tx.Permanenc.", "10,00")
		self.oHelper.CheckResult("- Iss", "500,00")
		self.oHelper.CheckResult("- Irrf", "150,00")
		self.oHelper.CheckResult("- Pis", "65,00")
		self.oHelper.CheckResult("- Cofins", "300,00")
		self.oHelper.CheckResult("- Csll", "100,00")
		self.oHelper.CheckResult("= Valor Pago", "7.795,00")


		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT145
	#Baixa parcial de título (Com PCC/IRF/ ISS na baixa e INSS na emissão – Taxa de permanência - Moeda 1 – Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50601

	def test_FINA080_CT145(self):
		prefixo = "TIR"
		titulo  = "F080CT145"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "27/04/2020"

		#Definida no CT144
		#self.oHelper.AddParameter("MV_MRETISS", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.SetParameters()

		#Data Definida no CT144
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("26/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("Data Pagto.", "26/04/2020")
		self.oHelper.SetValue("Data Debito", data)
		self.oHelper.CheckResult("+ Tx.Permanenc.", "10,00")
		self.oHelper.SetValue("= Valor Pago", "4.000,00")
		self.oHelper.CheckResult("- Iss", "199,50")
		self.oHelper.CheckResult("- Irrf", "59,85")
		self.oHelper.CheckResult("- Pis", "25,93")
		self.oHelper.CheckResult("- Cofins", "119,70")
		self.oHelper.CheckResult("- Csll", "39,90")

		self.oHelper.SetButton("Salvar")


		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("Data Pagto.", "26/04/2020")
		self.oHelper.SetValue("Data Debito", data)
		self.oHelper.CheckResult("+ Tx.Permanenc.", "0,00")
		self.oHelper.CheckResult("- Iss", "300,50")
		self.oHelper.CheckResult("- Irrf", "90,15")
		self.oHelper.CheckResult("- Pis", "39,06")
		self.oHelper.CheckResult("- Cofins", "180,30")
		self.oHelper.CheckResult("- Csll", "60,10")
		self.oHelper.CheckResult("= Valor Pago", "3.795,01")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
	
	#{Protheus.doc} test_FINA080_CT146
	#Baixa total de título em lote (Com PCC/IRF/ ISS na baixa e INSS na emissão – taxa de permanecia - Moeda 1 – Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50602

	def test_FINA080_CT146(self):
    	
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		ntitulos = '2'
		lote ='LTC146'
		natureza='FIN080CIMP'
		data    = "16/04/2020"
		prefixo = "TIR"
		titulo1 = "LOTACT146"
		titulo2 = "LOTBCT146"
		parcela = " "
		tipo    = "NF"
		fornecedor = "FINA02"
		loja = "01"

		#Definida no CT144
		#self.oHelper.AddParameter("MV_MRETISS", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.SetParameters()

		#Data Definida no CT144
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("26/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", data, name_attr=True)
		self.oHelper.SetValue("DVENCFIM", data, name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.ClickBox("No. Titulo", titulo1)
		self.oHelper.ClickBox("No. Titulo", titulo2)
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("Data Pagto.", "26/04/2020")
		self.oHelper.SetValue("+ Tx.Permanenc.", "35,00")
		self.oHelper.CheckResult("- Iss", "500,00")
		self.oHelper.CheckResult("- Irrf", "150,00")
		self.oHelper.CheckResult("- Pis", "65,00")
		self.oHelper.CheckResult("- Cofins", "300,00")
		self.oHelper.CheckResult("- Csll", "100,00")
		
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("+ Tx.Permanenc.", "58,00")
		self.oHelper.CheckResult("- Iss", "500,00")
		self.oHelper.CheckResult("- Irrf", "150,00")
		self.oHelper.CheckResult("- Pis", "65,00")
		self.oHelper.CheckResult("- Cofins", "300,00")
		self.oHelper.CheckResult("- Csll", "100,00")
		
		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT147
	#Baixa total de título em  Moeda 2 (Com PCC/IRF na baixa e ISS na emissão - banco moeda 2, taxa do dia – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50672
	
	def test_FINA080_CT147(self):
		prefixo = "TIR"
		titulo  = "F080CT147"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "28/04/2020"


		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		self.oHelper.SetParameters()
		
		time.sleep(30)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("27/04/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", data)
		self.oHelper.CheckResult("Taxa contratada", "2,8965")
		self.oHelper.CheckResult("- Irrf", "43,45")
		self.oHelper.CheckResult("- Pis", "18,82")
		self.oHelper.CheckResult("- Cofins", "86,89")
		self.oHelper.CheckResult("- Csll", "28,96")
		self.oHelper.CheckResult("= Valor Pago", "2.573,56")
		self.oHelper.CheckResult("Valor US$", "888,51")
		self.oHelper.CheckResult("+ Corr.Monetária", "389,79")


		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
	
	#{Protheus.doc} test_FINA080_CT148
	#Baixa total de título em  Moeda 2 (Com PCC/IRF na baixa e ISS na emissão - banco moeda 2, taxa Contratada – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50673
	
	def test_FINA080_CT148(self):
		prefixo = "TIR"
		titulo  = "F080CT148"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "28/04/2020"

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.SetParameters()
		
		#Data definida no CT147
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("27/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", data)
		self.oHelper.SetValue("Taxa contratada", "3,0000")
		self.oHelper.CheckResult("- Irrf", "45,00")
		self.oHelper.CheckResult("- Pis", "19,50")
		self.oHelper.CheckResult("- Cofins", "90,00")
		self.oHelper.CheckResult("- Csll", "30,00")
		self.oHelper.CheckResult("= Valor Pago", "2.665,50")
		self.oHelper.CheckResult("Valor US$", "888,50")
		self.oHelper.CheckResult("+ Corr.Monetária", "888,50")


		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
	
	
	#{Protheus.doc} test_FINA080_CT149
	#Baixa parcial de título em Moeda 2 (Com PCC/IRF na baixa e ISS na emissão - banco moeda 2, taxa do dia – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50674
	
	def test_FINA080_CT149(self):
		prefixo = "TIR"
		titulo  = "F080CT149"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "28/04/2020"

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.SetParameters()
		
		#Data definida no CT147
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("27/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", data)
		self.oHelper.CheckResult("Taxa contratada", "2,8965")
		self.oHelper.SetValue("= Valor Pago", "1.000,00")
		self.oHelper.CheckResult("- Irrf", "15,00")
		self.oHelper.CheckResult("- Pis", "6,50")
		self.oHelper.CheckResult("- Cofins", "30,00")
		self.oHelper.CheckResult("- Csll", "10,00")
		self.oHelper.CheckResult("Valor US$", "345,24")
		self.oHelper.CheckResult("+ Corr.Monetária", "151,46")

		self.oHelper.SetButton("Salvar")
		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", data)
		self.oHelper.CheckResult("Taxa contratada", "2,8965")
		self.oHelper.CheckResult("- Irrf", "28,45")
		self.oHelper.CheckResult("- Pis", "12,32")
		self.oHelper.CheckResult("- Cofins", "56,89")
		self.oHelper.CheckResult("- Csll", "18,96")
		self.oHelper.CheckResult("= Valor Pago", "1.573,55")
		self.oHelper.CheckResult("Valor US$", "543,26")
		self.oHelper.CheckResult("+ Corr.Monetária", "238,33")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT150
	#Baixa parcial de título em  Moeda 2 (Com PCC/IRF na baixa e ISS na emissão - banco moeda 2, taxa Contratada – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50675
	
	def test_FINA080_CT150(self):
		prefixo = "TIR"
		titulo  = "F080CT150"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		data    = "28/04/2020"

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.SetParameters()
		
		#Data definida no CT147
		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("27/04/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", data)
		self.oHelper.SetValue("Taxa contratada", "3,0000")
		self.oHelper.SetValue("= Valor Pago", "1.000,00")
		self.oHelper.CheckResult("- Irrf", "15,00")
		self.oHelper.CheckResult("- Pis", "6,50")
		self.oHelper.CheckResult("- Cofins", "30,00")
		self.oHelper.CheckResult("- Csll", "10,00")
		self.oHelper.CheckResult("Valor US$", "333,33")
		self.oHelper.CheckResult("+ Corr.Monetária", "333,33")

		self.oHelper.SetButton("Salvar")
		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Data Debito", data)
		self.oHelper.SetValue("Taxa contratada", "3,0000")
		self.oHelper.CheckResult("- Irrf", "30,00")
		self.oHelper.CheckResult("- Pis", "13,00")
		self.oHelper.CheckResult("- Cofins", "60,00")
		self.oHelper.CheckResult("- Csll", "20,00")
		self.oHelper.CheckResult("= Valor Pago", "1.665,51")
		self.oHelper.CheckResult("Valor US$", "555,17")
		self.oHelper.CheckResult("+ Corr.Monetária", "555,17")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
	
	#{Protheus.doc} test_FINA080_CT151
	#Baixa total em lote de título em  Moeda 2 (Com PCC/IRF na baixa e ISS na emissão - banco moeda 1, taxa do dia – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50676

	def test_FINA080_CT151(self):
    	
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		ntitulos = '2'
		lote ='LTC151'
		natureza='FIN080SINS'
		data    = "28/04/2020"
		titulo1 = "LOTACT151"
		titulo2 = "LOTBCT151"

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.SetParameters()

		#Data definida no CT147
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("27/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", "27/04/2020", name_attr=True)
		self.oHelper.SetValue("DVENCFIM", "27/04/2020", name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.ClickBox("No. Titulo", titulo1)
		self.oHelper.ClickBox("No. Titulo", titulo2)
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.CheckResult("Taxa contratada", "2,8965")	
		self.oHelper.CheckResult("- Irrf", "43,44")
		self.oHelper.CheckResult("- Pis", "18,82")
		self.oHelper.CheckResult("- Cofins", "86,89")
		self.oHelper.CheckResult("- Csll", "28,96")
		self.oHelper.CheckResult("= Valor Pago", "2.573,57")
		self.oHelper.CheckResult("Valor US$", "888,51")
		self.oHelper.CheckResult("+ Corr.Monetária", "389,79")

		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.CheckResult("Taxa contratada", "2,8965")
		self.oHelper.CheckResult("- Irrf", "43,44")
		self.oHelper.CheckResult("- Pis", "18,82")
		self.oHelper.CheckResult("- Cofins", "86,89")
		self.oHelper.CheckResult("- Csll", "28,96")
		self.oHelper.CheckResult("= Valor Pago", "2.573,57")
		self.oHelper.CheckResult("Valor US$", "888,51")
		self.oHelper.CheckResult("+ Corr.Monetária", "389,79")

		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT152
	#Baixa em lote de título Moeda 2 (Com PCC/IRF na baixa e ISS na emissão - banco moeda 1, taxa Contratada – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50678

	def test_FINA080_CT152(self):
    	
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		ntitulos = '2'
		lote ='LTC152'
		natureza='FIN080SINS'
		data    = "28/04/2020"
		titulo1 = "LOTACT152"
		titulo2 = "LOTBCT152"


		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.SetParameters()

		#Data definida no CT147
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("27/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", "27/04/2020", name_attr=True)
		self.oHelper.SetValue("DVENCFIM", "27/04/2020", name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.ClickBox("No. Titulo", titulo1)
		self.oHelper.ClickBox("No. Titulo", titulo2)
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Taxa contratada", "3,0000")
		self.oHelper.CheckResult("- Irrf", "45,00")
		self.oHelper.CheckResult("- Pis", "19,50")
		self.oHelper.CheckResult("- Cofins", "90,00")
		self.oHelper.CheckResult("- Csll", "30,00")
		self.oHelper.CheckResult("= Valor Pago", "2.665,50")
		self.oHelper.CheckResult("Valor US$", "888,50")
		self.oHelper.CheckResult("+ Corr.Monetária", "888,50")

		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Data Pagto.", data)
		self.oHelper.SetValue("Taxa contratada", "4,0000")
		self.oHelper.CheckResult("- Irrf", "60,00")
		self.oHelper.CheckResult("- Pis", "26,00")
		self.oHelper.CheckResult("- Cofins", "120,00")
		self.oHelper.CheckResult("- Csll", "40,00")
		self.oHelper.CheckResult("= Valor Pago", "3.554,00")
		self.oHelper.CheckResult("Valor US$", "888,50")
		self.oHelper.CheckResult("+ Corr.Monetária", "1.777,00")

		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT186
	#Cancelamento de baixa total de título (Com PCC/IRF na baixa e ISS/INSS na emissão - Moeda 1 - Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51039
	def test_FINA080_CT186(self):
		prefixo = "TIR"
		titulo  = "F080CT186"
		parcela = " "
		tipo    = "NF "

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.SetParameters()

		#Data definida no CT147
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("27/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Outras Ações", "Cancelar Baixa")
		self.oHelper.SetButton("Confirmar")
		
		# verifica se foi cancelado
		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.WaitShow("Baixa de Titulos - VISUALIZAR")
		self.oHelper.CheckResult("E2_SALDO", "8.400,00")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT187
	#Cancelamento e exclusão de baixa parcial de título (Com PCC/IRF na baixa e ISS/INSS na emissão - Moeda 1 - Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51040
	def test_FINA080_CT187(self):
		prefixo = "TIR"
		titulo  = "F080CT187"
		parcela = " "
		tipo    = "NF "

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.SetParameters()

		#Data definida no CT147
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("27/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Outras Ações", "Cancelar Baixa")
		self.oHelper.ClickListBox("TIR F080CT187            NF  FINA02 01 20/04/2020        3.785,00   02")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")
		
		# verifica se foi cancelado
		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.WaitShow("Baixa de Titulos - VISUALIZAR")
		self.oHelper.CheckResult("E2_SALDO", "8.400,00")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()
	
	#{Protheus.doc} test_FINA080_CT188
	#Cancelamento de baixa total de título (Taxa contratada - Moeda 2 - Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51041
	def test_FINA080_CT188(self):
		prefixo = "TIR"
		titulo  = "F080CT188"
		parcela = " "
		tipo    = "NF "

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.SetParameters()

		#Data definida no CT147
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("27/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Outras Ações", "Cancelar Baixa")
		self.oHelper.SetButton("Confirmar")
		
		# verifica se foi cancelado
		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.WaitShow("Baixa de Titulos - VISUALIZAR")
		self.oHelper.CheckResult("E2_SALDO", "1.000,00")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT189
	#Cancelamento e exclusão de baixa parcial de título (Taxa contratada - Moeda 2 - Fornecedor PJ - TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51042
	def test_FINA080_CT189(self):
		prefixo = "TIR"
		titulo  = "F080CT189"
		parcela = " "
		tipo    = "NF "

		#Parametrização default
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.SetParameters()

		#Data definida no CT147
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("27/04/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Outras Ações", "Cancelar Baixa")
		self.oHelper.ClickListBox("TIR F080CT189            NF  FINA01 01 20/04/2020        1.400,00   02")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")
		
		# verifica se foi cancelado
		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.WaitShow("Baixa de Titulos - VISUALIZAR")
		self.oHelper.CheckResult("E2_SALDO", "1.000,00")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()


	#{Protheus.doc} test_FINA080_CT192
	#Baixa e cancelamento de título em moeda 1, sem impostos com banco moeda 2 - TIR

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51722
	
	def test_FINA080_CT192(self):
		prefixo = "TIR"
		titulo  = "F080CT192"
		parcela = " "
		tipo    = "NF "
		banco   = "002"
		agencia = "08000"
		conta   = "080110"

		#Parametrização 
		self.oHelper.AddParameter("MV_MOEDBCO", "", "T", "T", "T")
		self.oHelper.SetParameters()
		
		
		time.sleep(30)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("09/06/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		# Baixa do título
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("= Valor Pago", "384,62")

		self.oHelper.SetButton("Salvar")
		self.oHelper.WaitShow("Baixa de Titulos")

		#Cancelamento da Baixa
		self.oHelper.SetButton("Outras Ações", "Cancelar Baixa")
		self.oHelper.SetButton("Confirmar")
		
		# verifica se foi cancelado
		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.WaitShow("Baixa de Titulos - VISUALIZAR")
		self.oHelper.CheckResult("E2_SALDO", "1.000,00")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()


	#{Protheus.doc} test_FINA080_CT193
	#Baixar título moeda 1, com retenção de INSS/ISS na emissão e PCC/IRF na baixa, utilizando banco moeda 2.

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51723
	
	def test_FINA080_CT193(self):
		prefixo = "TIR"
		titulo  = "F080CT193"
		parcela = " "
		tipo    = "NF "
		banco   = "002"
		agencia = "08000"
		conta   = "080110"

		#Parametrização CT192
		#self.oHelper.AddParameter("MV_MOEDBCO", "", "T", "T", "T")
		#self.oHelper.SetParameters()
		
		#Definido no CT192
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("09/06/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		# Baixa do título
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		
		self.oHelper.CheckHelp(text='FA100NAT',button='Fechar')
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT194
	#Baixa parcial de título moeda 1, sem impostos, com banco moeda 3

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51724
	
	def test_FINA080_CT194(self):
		prefixo = "TIR"
		titulo  = "F080CT194"
		parcela = " "
		tipo    = "NF "
		banco   = "003"
		agencia = "08000"
		conta   = "080110"

		#Parametrização CT192
		#self.oHelper.AddParameter("MV_MOEDBCO", "", "T", "T", "T")
		#self.oHelper.SetParameters()
		
		#Definido no CT192
		#time.sleep(5)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("09/06/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("= Valor Pago", "1.200,00")
		
		self.oHelper.SetButton("Salvar")
		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("= Valor Pago", "356,42")
		
		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT196
	#Baixa total de título moeda 2, sem impostos, com banco moeda 1, multa, taxa de permanencia e correcao monetaria

	#author fabio.casagrande
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51813
	
	def test_FINA080_CT196(self):
		prefixo = "TIR"
		titulo  = "F080CT196"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"

		#Parametrização
		self.oHelper.AddParameter("MV_TIPOCM", "", "O", "O", "O")
		self.oHelper.SetParameters()

		#Definido no CT196
		time.sleep(30)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("18/02/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")
		
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")
		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)		
		self.oHelper.SetValue("Taxa contratada", "4,0000")
		self.oHelper.SetValue("+ Multa", "300,00")
        
		self.oHelper.CheckResult("+ Tx.Permanenc.", "82,00")
		self.oHelper.CheckResult("= Valor Pago", "40.382,00")
		self.oHelper.CheckResult("Valor US$", "10.095,50")
		self.oHelper.CheckResult("+ Corr.Monetária", "15.000,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT199
	#Baixa total em lote de título em  Moeda 2  com atraso  (Com PCC/IRF na baixa e ISS na emissão - banco moeda 1, taxa do contratada  – TIR)

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51855

	def test_FINA080_CT199(self):
    	
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		ntitulos = '2'
		lote ='LTC199'
		natureza='FIN080SINS'
		titulo1 = "LOTACT199"
		titulo2 = "LOTBCT199"


		#Parametrização 
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_TIPOCM", "", "O", "O", "O")
		self.oHelper.SetParameters()

		
		time.sleep(30)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("12/06/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", "12/06/2020", name_attr=True)
		self.oHelper.SetValue("DVENCFIM", "12/06/2020", name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.ClickBox("No. Titulo", titulo1)
		self.oHelper.ClickBox("No. Titulo", titulo2)
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Taxa contratada", "4,5000")
		self.oHelper.SetValue("+ Multa", "100,00")
		self.oHelper.CheckResult("- Irrf", "67,50")
		self.oHelper.CheckResult("- Pis", "29,25")
		self.oHelper.CheckResult("- Cofins", "135,00")
		self.oHelper.CheckResult("- Csll", "45,00")
		#self.oHelper.CheckResult("= Valor Pago", "4.098,25")
		self.oHelper.CheckResult("Valor US$", "910,72")
		self.oHelper.CheckResult("+ Corr.Monetária", "1.472,50")

		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Taxa contratada", "4,0000")
		self.oHelper.SetValue("+ Multa", "50,00")
		self.oHelper.CheckResult("- Irrf", "60,00")
		self.oHelper.CheckResult("- Pis", "26,00")
		self.oHelper.CheckResult("- Cofins", "120,00")
		self.oHelper.CheckResult("- Csll", "40,00")
		#self.oHelper.CheckResult("= Valor Pago", "3.604,00")
		self.oHelper.CheckResult("Valor US$", "901,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "1.615,00")

		self.oHelper.SetButton("Salvar")

		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')
		self.oHelper.AssertTrue()
	


	#{Protheus.doc} test_FINA080_CT203
	#Baixa parcial de título moeda 2, taxa dia, com ISS e INSS na emissão e IRF e PCC na baixa, com correção monetária 
	# e taxa de permanência calculada em um banco moeda 1 - TIR

	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T52048
	
	def test_FINA080_CT203(self):
		prefixo = "TIR"
		titulo  = "F080CT203"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		
		#Parametrização
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		self.oHelper.AddParameter("MV_BP10925", "", "2", "2", "2")
		self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		self.oHelper.SetParameters()

		time.sleep(30)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("22/06/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("= Valor Pago", "6.000,00")
		self.oHelper.CheckResult("Taxa contratada", "3,8000")
		self.oHelper.CheckResult("+ Tx.Permanenc.", "38,00")
		self.oHelper.CheckResult("- Irrf", "89,43")
		self.oHelper.CheckResult("- Pis", "38,75")
		self.oHelper.CheckResult("- Cofins", "178,86")
		self.oHelper.CheckResult("- Csll", "59,62")
		self.oHelper.CheckResult("= Valor Pago", "5.633,34")
		self.oHelper.CheckResult("Valor US$", "1.482,46")
		self.oHelper.CheckResult("+ Corr.Monetária", "1.482,46")

		self.oHelper.SetButton("Salvar")


		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Taxa contratada", "2,5000")
		self.oHelper.CheckResult("+ Tx.Permanenc.", "0,00")
		self.oHelper.CheckResult("- Irrf", "316,16")
		self.oHelper.CheckResult("- Pis", "137,00")
		self.oHelper.CheckResult("- Cofins", "632,32")
		self.oHelper.CheckResult("- Csll", "210,77")
		self.oHelper.CheckResult("= Valor Pago", "15.781,38")
		self.oHelper.CheckResult("Valor US$", "6.312,55")
		self.oHelper.CheckResult("+ Corr.Monetária", "-1.893,77")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT204
	#Baixa Parcial de título Moeda 2 (banco moeda 2, taxa do Contratada, MV_EASYFIN)

	#author Fabio Casagrande Lima
	#since 24/06/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T52150
	
	def test_FINA080_CT204(self):
		prefixo = "TIR"
		titulo  = "F080CT204"
		parcela = " "
		tipo    = "NF "
		banco   = "002"
		agencia = "08000"
		conta   = "080110"
				
		self.oHelper.WaitShow("Baixa de Titulos")
		
		#Parametrização
		self.oHelper.AddParameter("MV_EASYFIN", "", "S", "S", "S")
		self.oHelper.SetParameters()

		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")
		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("= Valor Pago", "600,00")
		self.oHelper.CheckResult("Valor US$", "600,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("= Valor Pago", "1.400,00")
		self.oHelper.CheckResult("Valor US$", "1.400,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
	
	#{Protheus.doc} test_FINA080_CT233
	#Baixa parcial de título em dólar com banco em reais, e retenção de INSS/ISS na emissão de PCC/IRF na baixa, 
	# informando valores em dólar, com taxa do dia
	
	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T52635
	
	def test_FINA080_CT233(self):
		prefixo = "TIR"
		titulo  = "F080CT233"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		
		#Parametrização
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		self.oHelper.AddParameter("MV_EASYFIN", "", "N", "N", "N")
		self.oHelper.SetParameters()

		time.sleep(30)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("22/06/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Valor US$", "4.000,00")
		self.oHelper.CheckResult("Taxa contratada", "3,8000")
		self.oHelper.CheckResult("- Irrf", "228,00")
		self.oHelper.CheckResult("- Pis", "98,80")
		self.oHelper.CheckResult("- Cofins", "456,00")
		self.oHelper.CheckResult("- Csll", "152,00")
		self.oHelper.CheckResult("= Valor Pago", "14.265,20")
		self.oHelper.CheckResult("Valor US$", "3.754,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "3.754,00")

		self.oHelper.SetButton("Salvar")


		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("- Irrf", "342,00")
		self.oHelper.CheckResult("- Pis", "148,20")
		self.oHelper.CheckResult("- Cofins", "684,00")
		self.oHelper.CheckResult("- Csll", "228,00")
		self.oHelper.CheckResult("= Valor Pago", "15.317,80")
		self.oHelper.CheckResult("Valor US$", "4.031,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "4.031,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT234
	#Baixa parcial de título em dólar com banco em reais, e retenção de INSS/ISS na emissão de PCC/IRF na baixa, 
	# informando valores em dólar, com taxa contratada
	
	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T52636
	
	def test_FINA080_CT234(self):
		prefixo = "TIR"
		titulo  = "F080CT234"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		
		#Parametrização
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_BP10925", "", "2", "2", "2")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.AddParameter("MV_EASYFIN", "", "N", "N", "N")
		#self.oHelper.SetParameters()

		#time.sleep(30)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("22/06/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Valor US$", "4.000,00")
		self.oHelper.CheckResult("Taxa contratada", "2,3500")
		self.oHelper.CheckResult("- Irrf", "141,00")
		self.oHelper.CheckResult("- Pis", "61,10")
		self.oHelper.CheckResult("- Cofins", "282,00")
		self.oHelper.CheckResult("- Csll", "94,00")
		self.oHelper.CheckResult("= Valor Pago", "8.821,90")
		self.oHelper.CheckResult("Valor US$", "3.754,00")

		self.oHelper.SetButton("Salvar")


		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("- Irrf", "211,50")
		self.oHelper.CheckResult("- Pis", "91,65")
		self.oHelper.CheckResult("- Cofins", "423,00")
		self.oHelper.CheckResult("- Csll", "141,00")
		self.oHelper.CheckResult("= Valor Pago", "9.472,85")
		self.oHelper.CheckResult("Valor US$", "4.031,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
	
	#{Protheus.doc} test_FINA080_CT240
	#Baixa parcial de título em dólar com banco em reais, e retenção de INSS/ISS na emissão de PCC/IRF na baixa, 
	# com acréscimo e taxa de permanência, com taxa do dia  
	
	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T52718
	
	def test_FINA080_CT240(self):
		prefixo = "TIR"
		titulo  = "F080CT240"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		
		#Parametrização
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_IMPBAIX", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.AddParameter("MV_EASYFIN", "", "N", "N", "N")
		self.oHelper.SetParameters()

		time.sleep(30)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("22/06/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("= Valor Pago", "4.000,00")
		self.oHelper.CheckResult("Taxa contratada", "3,8000")
		self.oHelper.CheckResult("+ Acrescimo", "100,00")
		self.oHelper.CheckResult("+ Tx.Permanenc.", "38,00")
		self.oHelper.CheckResult("- Irrf", "60,00")
		self.oHelper.CheckResult("- Pis", "26,00")
		self.oHelper.CheckResult("- Cofins", "120,00")
		self.oHelper.CheckResult("- Csll", "40,00")
		self.oHelper.CheckResult("= Valor Pago", "4.000,00")
		self.oHelper.CheckResult("Valor US$", "1.052,63")
		self.oHelper.CheckResult("+ Corr.Monetária", "1.052,63")

		self.oHelper.SetButton("Salvar")


		self.oHelper.WaitShow("Baixa de Titulos")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("+ Acrescimo", "0,00")
		self.oHelper.CheckResult("+ Tx.Permanenc.", "0,00")
		self.oHelper.CheckResult("- Irrf", "516,27")
		self.oHelper.CheckResult("- Pis", "223,71")
		self.oHelper.CheckResult("- Cofins", "1.032,54")
		self.oHelper.CheckResult("- Csll", "344,18")
		self.oHelper.CheckResult("= Valor Pago", "25.975,29")
		self.oHelper.CheckResult("Valor US$", "6.835,60")
		self.oHelper.CheckResult("+ Corr.Monetária", "6.835,60")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
	
	#{Protheus.doc} test_FINA080_CT241
	#Baixa total de título em dólar com banco em reais, e retenção de INSS/ISS na emissão de PCC/IRF na baixa, 
	# informando desconto, com taxa contratada  - TIR
	
	#author Pâmela Bernardo
	#since 16/04/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T52719
	
	def test_FINA080_CT241(self):
		prefixo = "TIR"
		titulo  = "F080CT241"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		
		#Parametrização
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.AddParameter("MV_EASYFIN", "", "N", "N", "N")
		#self.oHelper.SetParameters()

		#time.sleep(30)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("22/06/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("- Descontos", "100,00")
		self.oHelper.CheckResult("- Irrf", "351,00")
		self.oHelper.CheckResult("- Pis", "152,10")
		self.oHelper.CheckResult("- Cofins", "702,00")
		self.oHelper.CheckResult("- Csll", "234,00")
		self.oHelper.CheckResult("= Valor Pago", "18.200,90")
		self.oHelper.CheckResult("Valor US$", "7.745,06")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT243
	# MV_MB10925 = 1 Alteração do motivo de baixa de DACAO para DEBITO para recalcular os impostos	
	
	#author Karen Honda
	#since 23/07/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T37573
	
	def test_FINA080_CT243(self):
		prefixo = "FIN"
		titulo  = "MB001    "
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "0001"
		conta   = "000001"
		
		#Parametrização
		self.oHelper.AddParameter("MV_MB10925", "", "1", "1", "1")
		self.oHelper.SetParameters()

		time.sleep(30)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("23/07/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		
		self.oHelper.CheckResult("- Irrf", "150,00")
		self.oHelper.CheckResult("- Pis", "65,00")
		self.oHelper.CheckResult("- Cofins", "300,00")
		self.oHelper.CheckResult("- Csll", "100,00")
		self.oHelper.CheckResult("= Valor Pago", "7.785,00")

		self.oHelper.SetValue("Mot.Baixa", "DACAO")

		self.oHelper.CheckResult("- Irrf", "0,00")
		self.oHelper.CheckResult("- Pis", "0,00")
		self.oHelper.CheckResult("- Cofins", "0,00")
		self.oHelper.CheckResult("- Csll", "0,00")
		self.oHelper.CheckResult("= Valor Pago", "8.400,00")

		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

#{Protheus.doc} test_FINA080_CT251
	#Baixa parcial de título em dólar com banco em reais, acrescimo, taxa contratada, 
	# retenção de INSS/ISS na emissão, PCC/IRF na baixa, informando valores em dólar
	
	#author Fabio Casagrande Lima
	#since 12/08/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T53373
	
	def test_FINA080_CT251(self):
		prefixo = "TIR"
		titulo  = "F080CT251"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		
		#Parametrização
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_MRETISS", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_IMPBAIX", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_BP10925", "", "1", "1", "1")
		#self.oHelper.AddParameter("MV_TIPOCM", "", "T", "T", "T")
		#self.oHelper.AddParameter("MV_EASYFIN", "", "N", "N", "N")
		#self.oHelper.SetParameters()

		#time.sleep(30)
		#self.oHelper.SetButton("x")
		#self.oHelper.ChangeEnvironment("23/07/2020","T1", "D MG 01 ","06")
		#self.oHelper.Program("FINA080")
		
		self.oHelper.WaitShow("Baixa de Titulos")
		#Definido no CT110
		#self.oHelper.SetKey("F12")
		#self.oHelper.WaitShow("Parametros")
		#self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		#self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		#self.oHelper.SetValue("Utiliza Banco Anterior ?" ,"Nao")
		#self.oHelper.SetButton("Ok")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("Taxa contratada", "3,8000")
		self.oHelper.SetValue("Valor US$", "2.000,00")
		self.oHelper.CheckResult("Taxa contratada", "3,8000")
		self.oHelper.CheckResult("- Irrf", "114,00")
		self.oHelper.CheckResult("- Pis", "49,40")
		self.oHelper.CheckResult("- Cofins", "228,00")
		self.oHelper.CheckResult("- Csll", "76,00")
		self.oHelper.CheckResult("= Valor Pago", "7.600,00")
		self.oHelper.CheckResult("Valor US$", "2.000,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "2.000,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT263
	#Entrar na tela da baixa
	#Altear para motivo de baixa NORMAL,
	#Alterara para motivo de baixa DACAO
	#Validar o valor de pagamento.

	#author rafael rondon 
	#since 09/09/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/project/10231/testCase?folderId=2589
	
	def test_FINA080_CT263(self):
		prefixo = "FIN"
		titulo  = "FIN521311"
		parcela = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "00001"
		conta   = "0000000001"
				
		self.oHelper.WaitShow("Baixa de Titulos")
			
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.CheckResult("Agência", agencia)
		self.oHelper.CheckResult("Conta", conta)
				
		self.oHelper.SetValue("Mot.Baixa", "DACAO")

		self.oHelper.CheckResult("Taxa contratada", "2,0000")
		self.oHelper.CheckResult("= Valor Pago", "2.000,00")
		self.oHelper.CheckResult("Valor US$", "1.000,00")
		self.oHelper.CheckResult("+ Corr.Monetária", "0,00")

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	#{Protheus.doc} test_FINA080_CT264
	#Entrar na tela da baixa
	#Altear para motivo de baixa SPB_TESTE,
	#Validar preenchimento das telas do SPB

	#author Douglas de Oliveira Homem
	#since 26/11/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56222
	
	def test_FINA080_CT264(self):
		prefixo = "FIN"
		titulo  = "FIN000XX7"
		parcela = " "
		tipo    = "NF "
		
		#Parametrização default
		self.oHelper.AddParameter("MV_USASPB ", "", "S", "S", "S")
		self.oHelper.SetParameters()
				
		self.oHelper.WaitShow("Baixa de Titulos")
			
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")

		self.oHelper.SetButton("Baixar")
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")
		self.oHelper.SetValue("Mot.Baixa", "SPB")

		#self.oHelper.WaitShow("Informado")
		self.oHelper.SetValue("Baixado", "TED")
		self.oHelper.SetValue("Tipo Pgto.", "03")
		self.oHelper.SetValue("Hora Agendamento", "24:00")
		self.oHelper.CheckHelp('VLDHORA','Fechar')

		self.oHelper.SetValue("Hora Agendamento", "12:00")
		self.oHelper.SetButton("Ok")
		self.oHelper.CheckHelp('TOTVS','Fechar')

		self.oHelper.SetValue("Baixado", "CIP")
		self.oHelper.CheckResult("Tipo Pgto.", "03")
		self.oHelper.CheckResult("Hora Agendamento", "12:00")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()	
		#self.oHelper.RestoreParameters()


	#{Protheus.doc} test_FINA080_CT266
	#Entrar na tela da baixa e 
	#tentar realizar a baixa de um título referente ao PCC, que foi gerado na rotina FINA241
	#e o título principal está em aberto.
	
	#author Douglas de Oliveira Homem
	#since 02/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56225
	
	def test_FINA080_CT266(self):
		prefixo = "FIN"
		titulo  = "FIN000XX8"
		parc1   = "1"
		parc2   = "2"
		parc3   = "3"
		tipo    = "TX "
				
		#Parametrização default
		self.oHelper.AddParameter("MV_BX10925 ", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_USASPB ", "", "N", "N", "N")
		self.oHelper.SetParameters()
				
		self.oHelper.WaitShow("Baixa de Titulos")
			
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc1}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.CheckHelp('BXIMPBOR','Não')

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc1}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.CheckHelp('BXIMPBOR','Sim')

		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc2}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.CheckHelp('BXIMPBOR','Não')

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc2}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.CheckHelp('BXIMPBOR','Sim')

		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc3}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.CheckHelp('BXIMPBOR','Não')

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc3}{tipo}")
		self.oHelper.SetButton("Baixar")
		self.oHelper.CheckHelp('BXIMPBOR','Sim')

		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()	
		#self.oHelper.RestoreParameters()	

	#{Protheus.doc} test_FINA080_CT275
	#Entrar na tela da baixa e 
	#alterar o valor do imposto em outras ações/retenção de impostos, confirmar e não realizar a baixa do título
		
	#author Douglas de Oliveira Homem
	#since 02/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56226
	
	def test_FINA080_CT275(self):
		prefixo = "FIN"
		titulo  = "FIN000XX9"
		parc1   = " "
		tipo    = "NF "
		banco   = "001"
		agencia = "08000"
		conta   = "080110"

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("07/12/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")
				
		#Parametrização default
		self.oHelper.AddParameter("MV_BX10925 ", "", "1", "1", "1")
		self.oHelper.SetParameters()
				
		self.oHelper.WaitShow("Baixa de Titulos")
			
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc1}{tipo}")
		self.oHelper.SetButton("Baixar")

		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("= Valor Pago", "9.535,00")

		self.oHelper.SetButton("Outras Ações", "Retenção de Impostos")

		self.oHelper.SetValue("Valor a Reter", "200,00", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.CheckResult("= Valor Pago", "9.635,00")

		self.oHelper.AssertTrue()	


	#{Protheus.doc} test_FINA080_CT276
	#Entrar na tela da baixa e tentar realizar a baixa de um título que esteja em borderô, com baixa com lote e conciliado.
	#Entrar na tela da baixa e tentar realizar a baixa de um título que esteja conciliado.
			
	#author Douglas de Oliveira Homem
	#since 11/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56427
	
	def test_FINA080_CT276(self):
		prefixo1 = "FIN"
		titulo1  = "FIN000X13"
		parc1    = " "
		tipo1    = "NF "
		prefixo2 = "FIN"
		titulo2  = "FIN000X14"
		parc2    = " "
		tipo2    = "NF "

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("11/12/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")

			
		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo1}{titulo1}{parc1}{tipo1}")
		self.oHelper.SetButton("Outras Ações", "Cancelar Baixa")
		self.oHelper.CheckHelp('F080BORD','Fechar')

		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo2}{titulo2}{parc2}{tipo2}")
		self.oHelper.SetButton("Outras Ações", "Cancelar Baixa")
		self.oHelper.CheckHelp('BXCONCIL','Fechar')
		
		self.oHelper.AssertTrue()	

	#{Protheus.doc} test_FINA080_CT277
	#Ativar o parâmetro MV_VLTITAD e tentar realizar a baixa em lote de um título cujo fornecedor
	#já tenha um adiantamento existente.
			
	#author Douglas de Oliveira Homem
	#since 16/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56428
	
	def test_FINA080_CT277(self):
    		
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		ntitulos = '1'
		lote ='LTC277'
		natureza ='FIN0000X13'
		data    = "16/12/2020"

		prefixo = "FIN"
		titulo  = "FIN000X13"
		parc    = " "
		tipo    = "NF "

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("16/12/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")

		#Parametrização default
		self.oHelper.AddParameter("MV_VLTITAD ", "", ".T.", ".T.", ".T.")
		self.oHelper.SetParameters()
	
			
		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc}{tipo}")
		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", data, name_attr=True)
		self.oHelper.SetValue("DVENCFIM", data, name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")
		self.oHelper.ClickBox("No. Titulo", titulo)
		self.oHelper.CheckHelp(text='TOTVS',button='Não')

		self.oHelper.SetButton("Cancelar")		
		self.oHelper.AssertTrue()	

	#{Protheus.doc} test_FINA080_CT280
	#Simulação de Baixa do título com origem MNTA765/MNTA766, verificação do desconto
			
	#author Douglas de Oliveira Homem
	#since 18/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56484
	
	def test_FINA080_CT280(self):
    				
		prefixo = "MNT"
		titulo  = "000015   "
		parc    = "A  "
		tipo    = "BOL"
		banco   = "001"
		agencia = "08000"
		conta   = "080110"

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("18/12/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")

		#Parametrização default
		self.oHelper.AddParameter("MV_NGMNTFI ", "", "S", "S", "S")
		self.oHelper.SetParameters()

		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc}{tipo}")
		self.oHelper.SetButton("Baixar")
				
		self.oHelper.WaitShow("Baixa de Titulos - BAIXAR")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.CheckResult("- Descontos", "25,54")
		
		self.oHelper.SetButton("Cancelar")		
		self.oHelper.AssertTrue()	

	#{Protheus.doc} test_FINA080_CT281
	#Simulação de baixa de título com cheque amarrado.
			
	#author Douglas de Oliveira Homem
	#since 18/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56485
	
	def test_FINA080_CT281(self):
    				
		banco    = "001"
		agencia  = "08000"
		conta    = "080110"
		ntitulos = '1'
		lote     ='LTC281'
		natureza ='FIN0000X17'
		data     = "18/12/2020"

		prefixo = "FIN"
		titulo  = "FIN000X17"
		parc    = " "
		tipo    = "NF "

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("21/12/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")

		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc}{tipo}")
		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", data, name_attr=True)
		self.oHelper.SetValue("DVENCFIM", data, name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")
		self.oHelper.ClickBox("No. Titulo", titulo)
		self.oHelper.SetButton("Salvar")
		self.oHelper.CheckHelp(text='CH_BAIXA',button='Fechar')

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "NORMAL")
		self.oHelper.SetValue("- Descontos", "50,00")

		self.oHelper.SetButton("Salvar")	
		self.oHelper.CheckHelp(text='JACHQSTIT',button='Fechar')	
		self.oHelper.SetButton("Cancelar")	
		self.oHelper.AssertTrue()


	#{Protheus.doc} test_FINA080_CT285
	#Ativar os parâmetros MV_FINVDOC e MV_MULNATP para realização de baixa em lote com contabilização.
				
	#author Douglas de Oliveira Homem
	#since 23/12/2020
	#version 1.0
	#See FAZER KANOAH
	
	def test_FINA080_CT285(self):
    		
		banco   = "001"
		agencia = "08000"
		conta   = "080110"
		ntitulos = '1'
		lote ='LTC285'
		natureza ='FIN0000X20'
		data    = "23/12/2020"

		prefixo = "FIN"
		titulo  = "FIN000X20"
		parc    = " "
		tipo    = "NF "

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("23/12/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA080")

		#Parametrização default
		self.oHelper.AddParameter("MV_FINVDOC ", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_MULNATP ", "", ".T.", ".T.", ".T.")
		self.oHelper.SetParameters()
	
			
		self.oHelper.WaitShow("Baixa de Titulos")
		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parc}{tipo}")
		self.oHelper.SetButton("Outras Ações", "Lote")
				
		self.oHelper.SetValue("cBanco", banco, name_attr=True)
		self.oHelper.SetValue("cAgencia", agencia, name_attr=True)
		self.oHelper.SetValue("cConta", conta, name_attr=True)
		self.oHelper.SetValue("nNroTit", ntitulos, name_attr=True)
		self.oHelper.SetValue("cLoteFin", lote, name_attr=True)
		self.oHelper.SetValue("DVENCINI", data, name_attr=True)
		self.oHelper.SetValue("DVENCFIM", data, name_attr=True)
		self.oHelper.SetValue("cNatDe", natureza, name_attr=True)
		self.oHelper.SetValue("cNatAte", natureza, name_attr=True)

		self.oHelper.SetButton("Ok")
				
		self.oHelper.WaitShow("Baixa de Titulos - LOTE")
		self.oHelper.ClickBox("No. Titulo", titulo)
		self.oHelper.SetButton("Salvar")

		self.oHelper.WaitShow("Baixa de Titulos - LOTE")

		self.oHelper.SetValue("Mot.Baixa", "DEBITO CC")
		self.oHelper.SetValue("Banco", banco)
		self.oHelper.SetValue("Agência", agencia)
		self.oHelper.SetValue("Conta", conta)
		self.oHelper.SetValue("", True)
		self.oHelper.SetButton("Salvar")

		#Tela de rateio por multiplas-naturezas 
		#Primeira linha
		self.oHelper.SetValue('Natureza','0001', grid=True, grid_number=1)
		self.oHelper.SetValue('Vlr.Movim.','500,00', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		#Segunda linha
		self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
		self.oHelper.SetValue('Natureza','001', grid=True, grid_number=1)
		self.oHelper.SetValue('Vlr.Movim.','500,00', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Salvar")
		
		self.oHelper.CheckHelp(text='TOTGERAL',button='Fechar')
		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()
							
		
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()