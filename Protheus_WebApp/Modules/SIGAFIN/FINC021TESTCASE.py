from tir import Webapp
import unittest
import time
from datetime import datetime

DateSystem = datetime.today().strftime('%d/%m/%Y')
'''-------------------------------------------------------------------
/*/{Protheus.doc} FINC021TestCase
TIR - Casos de testes da rotina Consulta Fluxo de Caixa

@author TOTVS
@since 06/10/2020
@version 12
-------------------------------------------------------------------'''

class FINC021(unittest.TestCase):

	#-------------------------------------------
	# Inicialiação setUpClass para TIR - FINC021
	#-------------------------------------------
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFIN',DateSystem,'T1','M SP 04 ','06')

	#-------------------------------------------
	# Inicio dos casos de testes TIR - FINC021
	#-------------------------------------------
	'''-------------------------------------------------------------------
	{Protheus.doc} TEST_FINC021_CT021
	Consulta pedido de venda com adiantamento em 3 parcelas

	@author Karen Honda
	@since 06/10/2020
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T54845
	-------------------------------------------------------------------'''
	def test_FINC021_CT021(self):
		
		self.oHelper.ChangeEnvironment("08/09/2020","T1", "M SP 04 ","06")
		self.oHelper.Program("FINC021")

		time.sleep(5)
		
		#Opções do Checkbox para seleção

		#self.oHelper.ClickCheckBox("Titulos a Receber", 1)
		#self.oHelper.ClickCheckBox("Titulos a Pagar", 1)
		#self.oHelper.ClickCheckBox("Comissões", 1)
		#self.oHelper.ClickCheckBox("Pedido de Venda", 1)
		#self.oHelper.ClickCheckBox("Pedido de Compra", 1)
		#self.oHelper.ClickCheckBox("Aplicacoes/Emprestimos", 1)
		#self.oHelper.ClickCheckBox("Saldos Bancarios", 1)
		#self.oHelper.ClickCheckBox("Titulos em Atraso", 1)
		#self.oHelper.ClickCheckBox("Titulos com Emissäo Futura", 1)
		#self.oHelper.ClickCheckBox("Considera Data Base", 1)
		#self.oHelper.ClickCheckBox("Processa analitico", 1)
		self.oHelper.SetValue("Periodicidade", "01 Diario")
		self.oHelper.SetValue("Quantos periodos", "10")
		
		self.oHelper.SetButton('Ok')
		
		time.sleep(2)

		#checa o dia 09/09/2020 - STEP 1
		self.oHelper.ClickGridCell("Dia" , 2,1)
		self.oHelper.CheckResult("Dia", "09/09/2020", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Entradas", "0,00", grid=True, line=2, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.ClickFolder('Pedido de Venda')
		self.oHelper.CheckResult("Valor", "10.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Valor do Adiantamento", "10.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult("Total de Pedidos de Venda", "10.000,00" )

		self.oHelper.SetButton('Confirmar')
		time.sleep(2)

		#checa o dia 10/09/2020
		self.oHelper.ClickGridCell("Dia" , 3,1)
		self.oHelper.CheckResult("Dia", "10/09/2020", grid=True, line=3, grid_number=1)
		self.oHelper.CheckResult("Entradas", "10.000,00", grid=True, line=3, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.ClickFolder('Pedido de Venda')
		self.oHelper.CheckResult("Valor", "10.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Valor do Adiantamento", "0,00", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult("Total de Pedidos de Venda", "10.000,00" )

		self.oHelper.SetButton('Confirmar')
		time.sleep(2)

		#checa o dia 11/09/2020
		self.oHelper.ClickGridCell("Dia" , 4,1)
		self.oHelper.CheckResult("Dia", "11/09/2020", grid=True, line=4, grid_number=1)
		self.oHelper.CheckResult("Entradas", "8.000,00", grid=True, line=4, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.ClickFolder('Pedido de Venda')
		self.oHelper.CheckResult("Valor", "8.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Valor do Adiantamento", "0,00", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult("Total de Pedidos de Venda", "8.000,00" )

		self.oHelper.SetButton('Confirmar')

		time.sleep(2)
		self.oHelper.SetButton('Sair')

		#checa o dia 10/09/2020	- STEP 2	
		self.oHelper.ChangeEnvironment("10/09/2020","T1", "M SP 04 ","06")
		self.oHelper.Program("FINC021")

		time.sleep(5)
		
		self.oHelper.SetButton('Ok')
		
		time.sleep(2)

		self.oHelper.ClickGridCell("Dia" , 1,1)
		self.oHelper.CheckResult("Dia", "10/09/2020", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Entradas", "10.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.ClickFolder('Pedido de Venda')
		self.oHelper.CheckResult("Valor", "20.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Valor do Adiantamento", "10.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult("Total de Pedidos de Venda", "20.000,00" )

		self.oHelper.SetButton('Confirmar')
		time.sleep(2)

		self.oHelper.ClickGridCell("Dia" , 2,1)
		self.oHelper.CheckResult("Dia", "11/09/2020", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Entradas", "8.000,00", grid=True, line=2, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.ClickFolder('Pedido de Venda')
		self.oHelper.CheckResult("Valor", "8.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Valor do Adiantamento", "0,00", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult("Total de Pedidos de Venda", "8.000,00" )

		self.oHelper.SetButton('Confirmar')
		time.sleep(2)

		self.oHelper.SetButton('Sair')

		#checa o dia 11/09/2020 - STEP 3
		self.oHelper.ChangeEnvironment("11/09/2020","T1", "M SP 04 ","06")
		self.oHelper.Program("FINC021")

		time.sleep(5)
		
		self.oHelper.SetButton('Ok')
		
		time.sleep(2)

		self.oHelper.ClickGridCell("Dia" , 1,1)
		self.oHelper.CheckResult("Dia", "11/09/2020", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Entradas", "18.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.ClickFolder('Pedido de Venda')
		self.oHelper.CheckResult("Valor", "28.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Valor do Adiantamento", "10.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult("Total de Pedidos de Venda", "28.000,00" )

		self.oHelper.SetButton('Confirmar')
		time.sleep(2)

		self.oHelper.SetButton('Sair')		
		self.oHelper.AssertTrue()

	
	#-------------------------------------------
	# Inicio dos casos de testes TIR - FINC021
	#-------------------------------------------
	'''-------------------------------------------------------------------
	{Protheus.doc} TEST_FINC021_CT024
	Consulta de título a receber com visão gerencial - mostrar as casas decimais

	@author Simone Mie Sato Kakinaona
	@since 08/01/2021
	@version 12

	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/220612
	-------------------------------------------------------------------'''
	def test_FINC021_CT024(self):

		#ParametrizaÃ§Ã£o default
		self.oHelper.AddParameter("MV_NATSINT", "", "1", "1", "1")
		self.oHelper.SetParameters()
		
		time.sleep(10)
		
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("07/01/2021","T1", "D MG 01 ","06")
		self.oHelper.Program("FINC021")

		time.sleep(5)
		
		#Opções do Checkbox para seleção

		self.oHelper.ClickCheckBox("Titulos a Receber", 1)
		#self.oHelper.ClickCheckBox("Titulos a Pagar", 1)
		#self.oHelper.ClickCheckBox("Comissões", 1)
		self.oHelper.ClickCheckBox("Pedido de Venda", 1)
		#self.oHelper.ClickCheckBox("Pedido de Compra", 1)
		#self.oHelper.ClickCheckBox("Aplicacoes/Emprestimos", 1)
		#self.oHelper.ClickCheckBox("Saldos Bancarios", 1)
		#self.oHelper.ClickCheckBox("Titulos em Atraso", 1)
		#self.oHelper.ClickCheckBox("Titulos com Emissäo Futura", 1)
		#self.oHelper.ClickCheckBox("Considera Data Base", 1)
		#self.oHelper.ClickCheckBox("Processa analitico", 1)
		self.oHelper.SetValue("Visão Gerencial", "005")
		
		self.oHelper.SetButton('Ok')
		
		time.sleep(2)

		#checa o dia 08/01/2021 
		self.oHelper.ClickGridCell("Dia" , 3, 1)
		self.oHelper.CheckResult("Dia", "08/01/2021 01", grid=True, line=3, grid_number=1)
		self.oHelper.CheckResult("Entradas", "2.523,63", grid=True, line=3, grid_number=1)
		self.oHelper.LoadGrid()	
	
		self.oHelper.SetButton('Sair')		
		self.oHelper.AssertTrue()
	#-------------------------------------------
	# Fim dos casos de testes TIR - FINC021 
	#-------------------------------------------


	#-------------------------------------------
	# Encerramento class para TIR - FINC021 
	#-------------------------------------------
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()