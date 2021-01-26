from tir import Webapp
import unittest
import time

#-------------------------------------------------------------------
#{Protheus.doc} FINA100TestCase
#TIR - Casos de testes da rotina movimentos de caixinha

#@author Simone Mie Sato Kakinoana
#@since 06/10/2020
#@version 12
#-------------------------------------------------------------------

class FINA100(unittest.TestCase):

	#-------------------------------------------
	# Inicialiação setUpClass para TIR - FINA100 
	#-------------------------------------------
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN",'06/10/2020',"T1","D MG 01 ","06")
		inst.oHelper.Program('FINA100')

	#-----------------------------------------
	#{Protheus.doc} FINA100_CT026
	#Transferencia entre contas.
	#Verificar se o primeiro dígito do número do documento é *

	#author Simone Mie Sato Kakinoana
	#since 05/11/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T55443
	#-----------------------------------------	
	def test_FINA100_CT026(self):
		
		self.oHelper.SetButton('Outras Ações',sub_item='Transferência entre C/C')		

		self.oHelper.SetBranch('D MG 01')

		self.oHelper.SetValue(field = "Banco", value = "237", position = 1)
		self.oHelper.SetValue(field = "Agência", value = "00098", position = 1)
		self.oHelper.SetValue(field = "Conta", value = "0000000098", position = 1)
		self.oHelper.SetValue(field = "Natureza", value = "FINR018", position = 1)
	
		self.oHelper.SetValue(field = "Banco", value = "237", position = 2)
		self.oHelper.SetValue(field = "Agência", value = "00099", position = 2)
		self.oHelper.SetValue(field = "Conta", value = "0000000099", position = 2)
		self.oHelper.SetValue(field = "Natureza", value = "FINR018", position = 2)
	
		self.oHelper.SetValue("Data de Crédito"  ,"05/11/2020")

		self.oHelper.SetValue("Tipo Mov."  ,"TB")
		self.oHelper.SetValue("Número Doc."  ,"*DOC123")
		
		self.oHelper.CheckHelp(text='INVALIDDOC',button='Fechar')

		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()	

	#-----------------------------------------
	#{Protheus.doc} FINA100_CT066
	#Estorno de transferencia entre conta corrente.
	#Verificar se o banco, agencia e conta destino estao vindo preenchidos. 

	#author Simone Mie Sato Kakinoana
	#since 06/10/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T54839
	#-----------------------------------------	
	def test_FINA100_CT066(self):
		
		self.oHelper.SetButton('Outras Ações',sub_item='Estorno de Transferência entre C/C')		

		self.oHelper.WaitShow("Parametros")
		self.oHelper.SetValue("No. do Documento ?"  ,"SMSDOC01")
		self.oHelper.SetValue("Dt. da Movimentacao ?"  ,"06/10/2020")
		self.oHelper.SetValue("Banco ?"  ,"001")
		self.oHelper.SetValue("Agencia ?"  ,"SMS")
		self.oHelper.SetValue("Conta ?"  ,"001")
		self.oHelper.SetButton("Ok")
		
		self.oHelper.CheckResult("Banco Destino", "001", grid=True, line=1)
		self.oHelper.CheckResult("Agência Destino", "SMS", grid=True, line=1)
		self.oHelper.CheckResult("Conta Destino", "002", grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.SetButton('Outras Ações',sub_item='Estorno de Transferência entre C/C')	

		self.oHelper.WaitShow("Parametros")
		self.oHelper.SetValue("No. do Documento ?"  ,"SMSDOC01")
		self.oHelper.SetValue("Dt. da Movimentacao ?"  ,"06/10/2020")
		self.oHelper.SetValue("Banco ?"  ,"001")
		self.oHelper.SetValue("Agencia ?"  ,"SMS")
		self.oHelper.SetValue("Conta ?"  ,"002")
		self.oHelper.SetButton("Ok")
		
		self.oHelper.CheckResult("Banco Destino", "001", grid=True, line=1)
		self.oHelper.CheckResult("Agência Destino", "SMS", grid=True, line=1)
		self.oHelper.CheckResult("Conta Destino", "002", grid=True, line=1)
		self.oHelper.LoadGrid()	

		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()	

	#-----------------------------------------
	#{Protheus.doc} FINA100_CT067
	#CT067 - Incluir Movimentação Bancária a Pagar
	#(Rateio Bruto,Informa contas no rateio,Contabilização off-line)

	#author Vitor Duca
	#since 17/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56417
	#-----------------------------------------	
	def test_FINA100_CT067(self):
		
		self.oHelper.SetButton('Pagar')		
		self.oHelper.SetBranch('D MG 01')

		self.oHelper.SetValue("E5_MOEDA"  ,"M1")
		self.oHelper.SetValue("E5_VALOR"  ,"1.000,00")
		self.oHelper.SetValue("E5_NATUREZ"  ,"001")
		self.oHelper.SetValue("E5_BANCO"  ,"001")
		self.oHelper.SetValue("E5_AGENCIA"  ,"00001")
		self.oHelper.SetValue("E5_CONTA"  ,"0000000001")
		self.oHelper.SetValue("E5_RATEIO"  ,"S")

		#Tela para escolher o tipo de rateio
		self.oHelper.SetValue('Historico','TIR RATEIO FINA100')
		self.oHelper.SetButton('Ok')

		#Tela de cadastro dos rateios contabeis
		#Primeira linha
		self.oHelper.SetValue('Conta Debito','001LH001', grid=True, grid_number=1)
		self.oHelper.SetValue('Percentual','50,00', grid=True, grid_number=1)
		self.oHelper.SetValue("Valor Rateio","500,00", grid=True, grid_number=1)
		self.oHelper.CheckResult("Valor Rateio", "500,00", grid=True, line=1, grid_number=1)
		self.oHelper.SetValue('Historico','TESTE DE RATEIO', grid=True, grid_number=1)
		self.oHelper.SetValue('C Custo Deb','002', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		#Segunda linha
		self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
		self.oHelper.SetValue('Conta Credit','001LH002', grid=True, grid_number=1)
		self.oHelper.SetValue('Percentual','50,00', grid=True, grid_number=1)
		self.oHelper.SetValue("Valor Rateio","500,00", grid=True, grid_number=1)
		self.oHelper.CheckResult("Valor Rateio", "500,00", grid=True, line=2, grid_number=1)
		self.oHelper.SetValue('Historico','TESTE DE RATEIO', grid=True, grid_number=1)
		self.oHelper.SetValue('C Custo Crd','003', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')

		#Confirma inclusão do movimento bancario
		self.oHelper.SetButton('Salvar')
	
		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()

	#-------------------------------------------
	# Encerramento class para TIR - FINA110
	#-------------------------------------------
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()