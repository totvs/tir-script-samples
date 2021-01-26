import unittest
import time
from tir import Webapp
from datetime import datetime

class FINA340(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN","06/04/2020","T1","M SP 01 ","06")
		inst.oHelper.Program("FINA340")
	
	"""============================================================
	/*/{Protheus.doc} test_FINA340_CT043
	Seleção de título (DIC com valor maior do que o saldo da NF)

	@author pedro.alencar
	@since 06/04/2020
	@version 1.0
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50157
	============================================================"""
	def test_FINA340_CT043(self):
		chaveTit = "M SP 01 TIRF340T1NF1 NF F340T101"
		
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		
		self.oHelper.SetButton("Compensar")
		self.oHelper.SetBranch("M SP 01")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Compensaçäo de Titulos")
		
		#Posiciona no item da grid de seleção de DIC e simula um "Enter", para selecionar o item
		#O método de marcação de checkbox não funuciona aqui, por conta da janela de definição de valor que o FINA340 abre ao marcar o título.
		self.oHelper.ClickGridCell("Prefixo", 1, 1)
		self.oHelper.SetKey("Enter", grid=True, grid_number=1)

		#Clica em ok na tela de definição de valor a compensar para o título selecionado
		self.oHelper.SetButton("Ok")

		#Fecha o alerta indicando que não pode selecionar o DIC e fecha as demais telas.
		self.oHelper.SetButton("Fechar")
		
		#Volta pra browse
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()
	
	"""============================================================
	/*/{Protheus.doc} test_FINA340_CT054
	Compensação total dos tipos DIC vs NF sem impostos na baixa - TIR

	@author Pâmela Bernardo
	@since 26/05/2020
	@version 1.0
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51280
	============================================================"""
	def test_FINA340_CT054(self):
		prefixo = "NF2"
		titulo  = "NF2000001"
		parcela = " "
		tipo    = "NF "
		
		#Parametrização
		#self.oHelper.AddParameter("MV_BX10925", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_BP10925", "", "2", "2", "2")
		self.oHelper.AddParameter("MV_PABRUTO", "", "2", "2", "2")
		self.oHelper.AddParameter("MV_PAPRIME", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_COMPCP", "", "T", "T", "T")
		self.oHelper.AddParameter("MV_DATAFIN", "", "20000101", "20000101", "20000101")
		self.oHelper.SetParameters()

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("22/05/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA340")

		self.oHelper.WaitShow("Compensaçäo de Titulos")

		self.oHelper.SetKey("F12")
		self.oHelper.WaitShow("Parametros")
		self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		self.oHelper.SetButton("Ok")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		
		self.oHelper.SetButton("Compensar")
		self.oHelper.SetBranch("D MG 01")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Compensaçäo de Titulos")
		#Clica em ok na tela de definição de valor a compensar para o título selecionado
		self.oHelper.SetButton("Ok")

		self.oHelper.AssertTrue()


	"""============================================================
	/*/{Protheus.doc} test_FINA340_CT058
	Compensação Entre NF e PA
	com data inferior ao MV_DATAFIN e MV_BXDTFIN = 2 (TESTE NEGATIVO)

	@author Rafael Sarracini
	@since 25/08/2020
	@version 1.0
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T53705
	============================================================"""
	def test_FINA340_CT058(self):
		prefixo = "RS "
		titulo  = "RS14.1   "
		parcela = " "
		tipo    = "NF "
		
		#Parametrização

		self.oHelper.AddParameter("MV_DATAFIN", "", "20200827", "20200827", "20200827")

		self.oHelper.SetParameters()

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("27/08/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA340")

		self.oHelper.WaitShow("Compensaçäo de Titulos")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		
		self.oHelper.SetButton("Compensar")
		#self.oHelper.SetBranch("D MG 01")
		self.oHelper.SetButton("Ok")

		#self.oHelper.WaitShow("Compensaçäo de Titulos a pagar")

		self.oHelper.SetValue("Data da Baixa", "26/08/2020")
		#verifica help, pois não poderá permitir alterar a data inferior ao parametro.
		self.oHelper.CheckHelp(text_help="DTMOVFIN", button="Fechar")

		#Clica em ok na tela de definição de valor a compensar para o título selecionado
		self.oHelper.SetButton("Cancelar")
		
		#sistema não poderá permitir a compensção em data inferior a MV_DATAFIN
		self.oHelper.AssertTrue()		
	"""============================================================
	/*/{Protheus.doc} test_FINA340_CT072
	Cancelamento de Compensaçao 1 NF x 2 PA, posicionando no primeiro PA
	
	@author Matheus Ribeiro
	@since 16/11/2020
	@version 1.0
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T53705
	============================================================"""
	def test_FINA340_CT072(self):
		prefixo = "MTH"
		titulo  = "MTH021   "
		parcela = " "
		tipo    = "PA "

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("16/11/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA340")

		self.oHelper.WaitShow("Compensaçäo de Titulos")

		self.oHelper.SetKey("F12")
		self.oHelper.WaitShow("Parametros")
		self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
		self.oHelper.SetButton("Ok")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		
		self.oHelper.SetButton("Outras Ações","Estorno")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Compensaçäo de Titulos")

		self.oHelper.SetButton("Confirmar")

		self.oHelper.WaitShow("Compensaçäo de Titulos")
		
		self.oHelper.AssertTrue()
	"""============================================================
	/*/{Protheus.doc} test_FINA340_CT076
	Testes de marcação em tela
	
	@author Matheus Ribeiro
	@since 16/11/2020
	@version 1.0
	@See 
	============================================================"""
	def test_FINA340_CT076(self):
		prefixo = "MTH"
		titulo  = "MTH023   "
		parcela = " "
		tipo    = "NF "

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("17/11/2020","T1", "D MG 01 ","06")
		self.oHelper.Program("FINA340")

		self.oHelper.WaitShow("Compensaçäo de Titulos")

		self.oHelper.SearchBrowse(f"D MG 01 {prefixo}{titulo}{parcela}{tipo}")
		
		self.oHelper.SetButton("Compensar")
		self.oHelper.SetBranch("D MG 01")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Compensaçäo de Titulos")
		self.oHelper.ClickGridCell("Prefixo", 1, 1)
		self.oHelper.SetKey("Enter", grid=True, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True, grid_number=1)
		self.oHelper.SetButton("Ok")
		self.oHelper.SetKey("Enter", grid=True, grid_number=1)

		self.oHelper.SetButton("Marcar Todos")
		self.oHelper.SetButton("Inverter selecao")

		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Compensaçäo de Titulos")
		
		self.oHelper.AssertTrue()
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()