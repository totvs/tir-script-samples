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


	### CT001
	### Compensação de título a receber.
	def test_FINA330_CT001(self):
		'''
        Test Case 001
        '''

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


	### CT002
	### Estorno de Compensação de título a receber.
	def test_FINA330_CT002(self):
		'''
        Test Case 002
        '''
		
		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")
				
		self.oHelper.SearchBrowse("D MG 01 FINFIN000281 RA ")
		self.oHelper.SetButton("Compensar")

		self.oHelper.CheckResult("Prefixo", "FIN")
		self.oHelper.CheckResult("Número", "FIN000281")
		self.oHelper.CheckResult("Tipo", "RA")
		self.oHelper.SetButton("Ok")
	
		self.oHelper.SetButton("Inverter seleção")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sim")

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")
		self.oHelper.SearchBrowse("D MG 01 FINFIN000281 RA ")
		self.oHelper.SetButton("Outras Ações", "Estorno")

		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")

		self.oHelper.SearchBrowse("D MG 01 FINFIN000281 RA ")
		self.oHelper.AssertTrue()


	### CT003
	### Estorno de Compensação de título a receber.
	def test_FINA330_CT003(self):
		'''
        Test Case 003
        '''
		
		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")
				
		self.oHelper.SearchBrowse("D MG 01 FINFIN000282 RA ")
		self.oHelper.SetButton("Compensar")

		self.oHelper.CheckResult("Prefixo", "FIN")
		self.oHelper.CheckResult("Número", "FIN000282")
		self.oHelper.CheckResult("Tipo", "RA")
		self.oHelper.ClickCheckBox("Tit. Marcados")
		self.oHelper.SetButton("Ok")
	
		self.oHelper.SetButton("Marcar todos")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sim")

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")
		self.oHelper.SearchBrowse("D MG 01 FINFIN000282 RA ")
		self.oHelper.SetButton("Outras Ações", "Estorno")

		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")

		self.oHelper.SearchBrowse("D MG 01 FINFIN000282 RA ")
		self.oHelper.AssertTrue()

	### CT046
	# Compensar um Título a Receber do tipo NF com todos os impostos, PCC e IR na baixa, 
	# contra três títulos adiantamento, considerando abatimentos.
	# https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T7552
	def test_FINA330_CT046(self):
		
		self.oHelper.AddParameter("MV_BR10925", "", "1", "1", "1")
		self.oHelper.AddParameter("MV_DATAFIN", "", "20000101", "20000101", "20000101")
		self.oHelper.SetParameters()

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")
		# Pergunte F12
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Cons.Abatimentos/Impostos ?"  ,"Sim")
		self.oHelper.SetButton("OK")

		self.oHelper.SearchBrowse("D MG 01 CMPFIN0035IB NF ")
		self.oHelper.SetButton("Compensar")
		self.oHelper.ClickCheckBox("Tit. Marcados")
		self.oHelper.SetButton("Ok")
	
		self.oHelper.SetButton("Marcar todos")
		self.oHelper.SetButton("Inverter seleção")
		self.oHelper.SetButton("Inverter seleção")
		self.oHelper.SetButton("Inverter seleção")
		
		self.oHelper.LoadGrid()
		self.oHelper.ClickBox("Número", "FIN0036IB")
		self.oHelper.CheckResult("Valor a compensar", "2.000,00")
		self.oHelper.SetButton("Ok")

		self.oHelper.ClickBox("Número", "FIN0037IB")
		self.oHelper.CheckResult("Valor a compensar", "3.000,00")
		self.oHelper.SetButton("Ok")

		self.oHelper.ClickBox("Número", "FIN0038IB")
		self.oHelper.CheckResult("Valor a compensar", "2.785,00")
		self.oHelper.SetButton("Ok")

		self.oHelper.CheckResult("Total selecionado", "7.785,00")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sim")
		
		
		# Precisa validar o saldo do título compensado ainda
		
		
		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")
		self.oHelper.SearchBrowse("D MG 01 CMPFIN0035IB NF ")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")

		# Refazendo o teste partindo do RA
		self.oHelper.SearchBrowse("D MG 01 CMPFIN0036IB RA ")
		self.oHelper.SetButton("Compensar")
		self.oHelper.ClickCheckBox("Tit. Marcados")
		self.oHelper.SetButton("Ok")

		self.oHelper.ClickBox("Número", "FIN0035IB")
		self.oHelper.CheckResult("Valor a compensar", "2.000,00")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sim")

		self.oHelper.SearchBrowse("D MG 01 CMPFIN0037IB RA ")
		self.oHelper.SetButton("Compensar")
		self.oHelper.ClickCheckBox("Tit. Marcados")
		self.oHelper.SetButton("Ok")

		self.oHelper.ClickBox("Número", "FIN0035IB")
		self.oHelper.CheckResult("Valor a compensar", "3.000,00")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sim")
		
		self.oHelper.SearchBrowse("D MG 01 CMPFIN0038IB RA ")
		
		# Precisa ajustar o calor comepnsado para ficar iguar quando parte da NF

		# self.oHelper.SetButton("Compensar")
		# self.oHelper.ClickCheckBox("Tit. Marcados")
		# self.oHelper.SetButton("Ok")

		# self.oHelper.ClickBox("Número", "FIN0035IB")
		# self.oHelper.CheckResult("Valor a compensar", "2.785,00")
		# self.oHelper.SetButton("Ok")
		# self.oHelper.SetButton("Ok")
		# self.oHelper.SetButton("Sim")

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")
		self.oHelper.SearchBrowse("D MG 01 CMPFIN0035IB NF ")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.SearchBrowse("D MG 01 CMPFIN0035IB NF ")
		self.oHelper.AssertTrue()

	### CT200
	### Excluir compensação realizada automática na devolução de mercadoria via documento de entrada.
	# https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T9794
	def test_FINA330_CT200(self):

		self.oHelper.AddParameter("MV_DATAFIN", "", "20000101", "20000101", "20000101")
		self.oHelper.SetParameters()

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")

		self.oHelper.SearchBrowse("D MG 01 A  000014    NF ")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")

		self.oHelper.SearchBrowse("D MG 01 A  000014    NF ")
		self.oHelper.SetButton("Compensar")
		self.oHelper.ClickCheckBox("Tit. Marcados")
		self.oHelper.SetButton("Ok")	

		self.oHelper.ClickBox("Número", "000015")
		self.oHelper.CheckResult("Valor a compensar", "2.000,00")
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sim")
		
		self.oHelper.SearchBrowse("D MG 01 A  000014    NF ")
		self.oHelper.AssertTrue()

	### CT201
	### Testar botões em tela
	# https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T9794
	def test_FINA330_CT201(self):

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")

		self.oHelper.SetButton("Outras Ações", "Legenda")
		self.oHelper.SetButton("Fechar")

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")

		self.oHelper.SetButton("Outras Ações", "Imprimir Browse")
		self.oHelper.SetButton("Fechar")

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")

		self.oHelper.SetButton("Outras Ações","Pesquisar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")

		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")

		self.oHelper.SetButton("MOSTRAR DETALHES")
		self.oHelper.SetButton("OCULTAR DETALHES")

		self.oHelper.SearchBrowse("D MG 01 CTR000000001")
		self.oHelper.SetButton("Compensar")
		self.oHelper.CheckHelp(text='NOCMPPROV',button='Fechar')

		self.oHelper.SearchBrowse("D MG 01 MTHMTH007")
		self.oHelper.SetButton("Compensar")
		self.oHelper.CheckHelp(text='FA330JABAI',button='Fechar')

	### CT202
	### Validar compensação pelo Painel Gestor
	# https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T9794
	def test_FINA330_CT202(self):

		self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")

		self.oHelper.SetButton("x")
		self.oHelper.Program("FINA704")

		self.oHelper.SetValue("Prefixo ?", "MTH")
		self.oHelper.SetValue("Num ?", "MTH000")
		self.oHelper.SetButton("Pesquisar")
		self.oHelper.ClickTree("Operaçoes")
		self.oHelper.ClickTree("Operaçoes > Compensação Cr > Compensar")
		
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Sim")

		self.oHelper.ClickLabel("Sair")
		self.oHelper.SetButton("Sim")

		self.oHelper.Program("FINA340")

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()