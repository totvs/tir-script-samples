import unittest
import time

from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

"""-------------------------------------------------------------------
/*/{Protheus.doc} FINA050TestCase
TIR - Casos de testes da rotina contas a pagar 

@author Karen Honda
@since 07/05/2020
@version 12
-------------------------------------------------------------------"""

class FINA050(unittest.TestCase):

	#-------------------------------------------
	# Inicialiação setUpClass para TIR - FINA050 
	#-------------------------------------------
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN",DateSystem,"T1","D MG 01 ","06")
		inst.oHelper.Program('FINA050')

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT028
	#Inclusão de desdobramento, com rateio múltiplas naturezas e centro de custo 
	#MV_RATDESD = 1 ( Sem impostos )

	#author Vitor Duca
	#since 13/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T40666
	#-----------------------------------------	
	def test_FINA050_CT028(self):

		self.oHelper.AddParameter("MV_RATDESD","","1","1","1")  
		self.oHelper.AddParameter("MV_MULNATP","",".T.",".T.",".T.")  
		self.oHelper.SetParameters()

		self.oHelper.WaitShow("Contas a Pagar")
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO','FIN')
		self.oHelper.SetValue('E2_NUM','FN050_028')
		self.oHelper.SetValue('E2_TIPO','NF')
		self.oHelper.SetValue('E2_NATUREZ','AUT0000001')
		self.oHelper.SetValue('E2_FORNECE','FIN001')
		self.oHelper.SetValue('E2_LOJA','01')
		self.oHelper.SetValue('E2_EMISSAO',DateSystem)
		self.oHelper.SetValue('E2_VENCTO',DateSystem)
		self.oHelper.SetKey("Enter")
		self.oHelper.SetValue('E2_VALOR','5.000,00')
		self.oHelper.ClickFolder('Administrativo')
		self.oHelper.SetValue('E2_DESDOBR','S')

		#Tela do desdobramento
		self.oHelper.SetKey("Enter")
		self.oHelper.SetValue('Numero de Parcelas','2')
		self.oHelper.SetKey("Enter")
		self.oHelper.SetValue('Periodo de Vencto. (em dias)','30')
		self.oHelper.SetValue('Historico','Teste de dedobramento')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetValue('E2_MULTNAT','1')
		self.oHelper.SetButton('Salvar')

		#Tela de rateio por multiplas-naturezas 
		#Primeira linha
		self.oHelper.SetValue('Natureza','AUT0000002', grid=True, grid_number=1)
		self.oHelper.SetValue('Vlr.Movim.','2.500,00', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		#Segunda linha
		self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
		self.oHelper.SetValue('Natureza','AUT0000003', grid=True, grid_number=1)
		self.oHelper.SetValue('Vlr.Movim.','2.500,00', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Cancelar')
		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")
		self.oHelper.AssertTrue()

		self.oHelper.RestoreParameters()
	#-----------------------------------------
	#{Protheus.doc} FINA050_CT034
	#Substituição de titulos provisorios sem impostos

	#author Vitor Duca
	#since 19/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51321
	#-----------------------------------------	
	def test_FINA050_CT034(self):

		chavePR = "D MG 01 FINFN050_034 PR TIR00101"
		chaveNF  = "D MG 01 FINFN050_034 NF TIR00101"
			
		self.oHelper.WaitShow("Contas a Pagar") 
		
		#Altera pergunte da rotina
		self.oHelper.SetKey("F12")
		self.oHelper.WaitShow("Parametros")
		self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		self.oHelper.SetButton('Ok')

		#Pesquisa titulo provisorio
		self.oHelper.SearchBrowse(f'{chavePR}', key=1, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Substituição de Provisórios')
		
		#Tela de seleção de filiais
		time.sleep(5)
		self.oHelper.SetKey("Enter", grid=True, grid_number=1)
		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetValue('Fornecedor :', 'TIR001')
		self.oHelper.SetValue('Loja :','01')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Confirmar')

		time.sleep(5)
		self.oHelper.SetButton('Outras Ações',sub_item='Pesquisar')
		self.oHelper.SetButton('Ok')
		#Posiciona no item da grid de seleção e simula um "Enter", para selecionar o item
		self.oHelper.ClickBox("No. Titulo", "FN050_034")
		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetValue('E2_TIPO',"NF")
		self.oHelper.SetKey("Enter")
		self.oHelper.SetButton('Confirmar')

		#Deseja cadastrar os valores acessórios deste título agora?
		self.oHelper.SetButton('Não')
		
		#Exclusão do titulo efetivos, estorno da substituição 
		#self.oHelper.SearchBrowse(f'{chaveNF}', key=1, index=True)
		#self.oHelper.SetButton('Outras Ações',sub_item='Excluir')
		#self.oHelper.SetButton('Sim')
		#self.oHelper.SetButton('Confirmar')

		#Restaura pergunte da rotina
		self.oHelper.SetKey("F12")
		self.oHelper.WaitShow("Parametros")
		self.oHelper.SetValue('Mostra Lanc Contab ?', "Sim")
		self.oHelper.SetButton('Ok')

		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()
	
	#-----------------------------------------
	#{Protheus.doc} FINA050_CT040
	#Inclusão de titulo a pagar com desdobramento

	#author Vitor Duca
	#since 19/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51324
	#-----------------------------------------	
	def test_FINA050_CT040(self):

		self.oHelper.WaitShow("Contas a Pagar")
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO','FIN')
		self.oHelper.SetValue('E2_NUM','FN050_040')
		self.oHelper.SetValue('E2_TIPO','NF')
		self.oHelper.SetValue('E2_NATUREZ','TIR001')
		self.oHelper.SetValue('E2_FORNECE','TIR001')
		self.oHelper.SetValue('E2_LOJA','01')
		self.oHelper.SetValue('E2_EMISSAO',DateSystem)
		self.oHelper.SetValue('E2_VENCTO',DateSystem)
		self.oHelper.SetKey("Enter")
		self.oHelper.SetValue('E2_VALOR','10.000,00')
		self.oHelper.ClickFolder('Administrativo')
		self.oHelper.SetValue('E2_DESDOBR','S')

		#Tela do desdobramento
		self.oHelper.SetKey("Enter")
		self.oHelper.SetValue('Numero de Parcelas','2')
		self.oHelper.SetKey("Enter")
		self.oHelper.SetValue('Periodo de Vencto. (em dias)','30')
		self.oHelper.SetValue('Historico','Teste de dedobramento')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")
		self.oHelper.AssertTrue()

		#Exclusão
		self.oHelper.SetButton("Outras Ações", "Canc.Desdobr.")
		self.oHelper.SetButton('Confirmar')
		time.sleep(5)
		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")
		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT041
	#Inclusão de Pagamento antecipado sem impostos, com movimento bancario

	#author Vitor Duca
	#since 19/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51325 
	#-----------------------------------------	
	def test_FINA050_CT041(self):

		self.oHelper.WaitShow("Contas a Pagar")
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO','FIN')
		self.oHelper.SetValue('E2_NUM','FN050_041')
		self.oHelper.SetValue('E2_TIPO','PA')

		#Informações bancarias do PA
		self.oHelper.SetValue('Banco','001')
		self.oHelper.SetValue('Agência','00001')
		self.oHelper.SetValue('Conta','0000000001')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetValue('E2_NATUREZ','TIR001')
		self.oHelper.SetValue('E2_FORNECE','TIR001')
		self.oHelper.SetValue('E2_LOJA','01')
		self.oHelper.SetValue('E2_EMISSAO',DateSystem)
		self.oHelper.SetValue('E2_VENCTO',DateSystem)
		self.oHelper.SetKey("Enter")
		self.oHelper.SetValue('E2_VALOR','10.000,00')
	
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT043
	#Exclusão de titulo NF sem impostos com pendencia de contabilização online

	#author Vitor Duca
	#since 19/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51326
	#-----------------------------------------	
	def test_FINA050_CT043(self):

		chaveTit = "D MG 01 FINFN050_043 NF TIR00101"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		#Pesquisa titulo que sera excluido
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Excluir')
		
		self.oHelper.SetButton('Confirmar')

		#Tela de pendencias de contabilização
		self.oHelper.CheckResult("Motivo Baixa", "ES", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Histórico", "Estorno de Baixa", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Valor", "1000", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirma')
		
		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		#Restaura o filtro de pesquisa da browse
		chaveTit = " "
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT045
	#Inclusão de abatimento contendo mais de um titulo a 
	#pagar com a chave (E2_PREFIXO+E2_NUM+E2_PARCELA) igual

	#author Vitor Duca
	#since 19/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51328
	#-----------------------------------------	
	def test_FINA050_CT045(self):
	
		self.oHelper.WaitShow("Contas a Pagar") 

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO','FIN')
		self.oHelper.SetValue('E2_NUM','FN050_045')
		self.oHelper.SetValue('E2_TIPO','AB-')

		#Tela de seleção do pai do abatimento
		#Primeira linha
		self.oHelper.CheckResult("Prefixo", "FIN", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("No. Titulo", "FN050_045", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Parcela", " ", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Tipo", "BOL", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Vlr.Titulo", "2000", grid=True, line=1, grid_number=1)
		#Segunda linha
		self.oHelper.CheckResult("Prefixo", "FIN", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("No. Titulo", "FN050_045", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Parcela", " ", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Tipo", "NF", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Vlr.Titulo", "2000", grid=True, line=2, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Ok')

		#Checagem dos dados herdados do titulo pai
		self.oHelper.CheckResult('E2_NATUREZ','TIR001')
		self.oHelper.CheckResult('E2_FORNECE','TIR001')
		self.oHelper.CheckResult('E2_LOJA','01')
		self.oHelper.CheckResult('E2_EMISSAO','19/05/2020')
		self.oHelper.CheckResult('E2_VENCTO','19/05/2020')

		self.oHelper.SetValue('E2_VALOR','50,00')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT046
	#Visualização do rateio contabil 

	#author Vitor Duca
	#since 19/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51331
	#-----------------------------------------	
	def test_FINA050_CT046(self):
		chaveTit = "D MG 01 FINFN050_046 NF 00000201"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		#Pesquisa titulo que sera visualizado
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Vis Rateio')
		
		#Tela de Visualização dos rateios contabeis
		#Primeira linha
		self.oHelper.CheckResult("Conta Debito", "001LH001", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Conta Credit", "", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Percentual", "50,00", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Valor Rateio", "2.500,00", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Historico", "TESTE DE RATEIO", grid=True, line=1, grid_number=1)
		#Segunda linha
		self.oHelper.CheckResult("Conta Debito", "", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Conta Credit", "001LH002", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Percentual", "50,00", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Valor Rateio", "2.500,00", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Historico", "TESTE DE RATEIO", grid=True, line=2, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT047
	#Inclusão de titulo a pagar com rateio contabil por centro de custo

	#author Vitor Duca
	#since 22/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51333 
	#-----------------------------------------	
	def test_FINA050_CT047(self):

		self.oHelper.WaitShow("Contas a Pagar")
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO','FIN')
		self.oHelper.SetValue('E2_NUM','FN050_047')
		self.oHelper.SetValue('E2_TIPO','NF')
		self.oHelper.SetValue('E2_NATUREZ','TIR001')
		self.oHelper.SetValue('E2_FORNECE','TIR001')
		self.oHelper.SetValue('E2_LOJA','01')
		self.oHelper.SetValue('E2_EMISSAO',DateSystem)
		self.oHelper.SetValue('E2_VENCTO',DateSystem)
		self.oHelper.SetValue('E2_VALOR','10.000,00')

		self.oHelper.ClickFolder('Contábil')
		self.oHelper.SetValue('E2_RATEIO','S')

		#Tela para escolher o tipo de rateio
		self.oHelper.SetValue('Historico','TIR RATEIO')
		self.oHelper.SetButton('Ok')

		#Tela de cadastro dos rateios contabeis
		#Primeira linha
		self.oHelper.SetValue('Conta Debito','001LH001', grid=True, grid_number=1)
		self.oHelper.SetValue('Percentual','50,00', grid=True, grid_number=1)
		self.oHelper.SetValue("Valor Rateio","5.000,00", grid=True, grid_number=1)
		self.oHelper.CheckResult("Valor Rateio", "5.000,00", grid=True, line=1, grid_number=1)
		self.oHelper.SetValue('Historico','TESTE DE RATEIO', grid=True, grid_number=1)
		self.oHelper.SetValue('C Custo Deb','002', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		#Segunda linha
		self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
		self.oHelper.SetValue('Conta Credit','001LH002', grid=True, grid_number=1)
		self.oHelper.SetValue('Percentual','50,00', grid=True, grid_number=1)
		self.oHelper.SetValue("Valor Rateio","5.000,00", grid=True, grid_number=1)
		self.oHelper.CheckResult("Valor Rateio", "5.000,00", grid=True, line=2, grid_number=1)
		self.oHelper.SetValue('Historico','TESTE DE RATEIO', grid=True, grid_number=1)
		self.oHelper.SetValue('C Custo Crd','003', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')

		#Confirma inclusão do titulo
		self.oHelper.SetButton('Salvar')

		#Deseja cadastrar os valores acessórios deste título agora?
		self.oHelper.SetButton('Não')
		self.oHelper.SetButton('Cancelar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT050
	#Inclusão de titulo a pagar com valores acessorios

	#author Vitor Duca
	#since 22/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51336
	#-----------------------------------------	
	def test_FINA050_CT050(self):

		self.oHelper.WaitShow("Contas a Pagar")
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO','FIN')
		self.oHelper.SetValue('E2_NUM','FN050_050')
		self.oHelper.SetValue('E2_TIPO','NF')
		self.oHelper.SetValue('E2_NATUREZ','TIR001')
		self.oHelper.SetValue('E2_FORNECE','TIR001')
		self.oHelper.SetValue('E2_LOJA','01')
		self.oHelper.SetValue('E2_EMISSAO',DateSystem)
		self.oHelper.SetValue('E2_VENCTO',DateSystem)
		self.oHelper.SetValue('E2_VALOR','1500,00')

		#Confirma inclusão do titulo
		self.oHelper.SetButton('Salvar')

		#Deseja cadastrar os valores acessórios deste título agora?
		self.oHelper.SetButton('Sim')

		#Tela de valores acessorios do titulo
		self.oHelper.WaitShow("Valores Acessórios")
		self.oHelper.SetValue('Código','000002', grid=True, grid_number=1)
		self.oHelper.SetValue('Valor','100,00', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		#Confirma inclusão do valor acessorio
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.SetButton('Cancelar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT051
	#Visualização de titulo a pagar com impostos retidos pelo configurador de tributos

	#author Vitor Duca
	#since 22/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51337
	#-----------------------------------------	
	def test_FINA050_CT051(self):
		
		chaveTit = "D MG 01 FINFN050_051 NF TIR00201"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		#Pesquisa titulo a pagar
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.SetButton('Visualizar')

		self.oHelper.CheckResult("E2_VALOR", "10.000,00")
		self.oHelper.ClickFolder('Impostos')
		self.oHelper.CheckResult("E2_PIS", "0,00")
		self.oHelper.CheckResult("E2_CSLL", "0,00")
		self.oHelper.CheckResult("E2_COFINS", "0,00")

		self.oHelper.SetButton('Outras Ações',sub_item='Consulta de Retenções')
		
		#Tela de impostos calculados e retidos pelo configurador de tributos
		self.oHelper.WaitShow("Consulta de Impostos por Título")
		self.oHelper.ClickFolder('Baixas')
	
		#Informações de baixas
		self.oHelper.CheckResult("Valor Baixa", "9.535,00", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()
		
		#Impostos calculados - Baixa
		#Linha 01
		self.oHelper.CheckResult("Tipo Imposto", "PCC001", grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult("Imposto Calc", "INB", grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult("Base Calculo", "10.000,00", grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult("Valor Calc.", "65,00", grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult("Situação", "Retido", grid=True, line=1, grid_number=2)
		self.oHelper.LoadGrid()

		#Linha 02
		self.oHelper.CheckResult("Tipo Imposto", "PCC002", grid=True, line=2, grid_number=2)
		self.oHelper.CheckResult("Imposto Calc", "INB", grid=True, line=2, grid_number=2)
		self.oHelper.CheckResult("Base Calculo", "10.000,00", grid=True, line=2, grid_number=2)
		self.oHelper.CheckResult("Valor Calc.", "300,00", grid=True, line=2, grid_number=2)
		self.oHelper.CheckResult("Situação", "Retido", grid=True, line=2, grid_number=2)
		self.oHelper.LoadGrid()
		
		#Linha 03
		self.oHelper.CheckResult("Tipo Imposto", "PCC003", grid=True, line=3, grid_number=2)
		self.oHelper.CheckResult("Imposto Calc", "INB", grid=True, line=3, grid_number=2)
		self.oHelper.CheckResult("Base Calculo", "10.000,00", grid=True, line=3, grid_number=2)
		self.oHelper.CheckResult("Valor Calc.", "100,00", grid=True, line=3, grid_number=2)
		self.oHelper.CheckResult("Situação", "Retido", grid=True, line=3, grid_number=2)
		self.oHelper.LoadGrid()
		
		#Impostos retidos - Baixa
		#Linha 01
		self.oHelper.ClickGridCell("Tipo Imposto", 1, 2)
		self.oHelper.CheckResult("Título de Imposto Gerado", "D MG 01 |FIN|FN050_051|1|TX |UNIAO |00", grid=True, line=1, grid_number=3)
		self.oHelper.LoadGrid()

		#Linha 02
		self.oHelper.ScrollGrid("Tipo Imposto", "PCC002", grid_number=2)
		self.oHelper.CheckResult("Título de Imposto Gerado", "D MG 01 |FIN|FN050_051|2|TX |UNIAO |00", grid=True, line=1, grid_number=3)
		self.oHelper.LoadGrid()

		#Linha 03
		self.oHelper.ScrollGrid("Tipo Imposto", "PCC003", grid_number=2)
		self.oHelper.CheckResult("Título de Imposto Gerado", "D MG 01 |FIN|FN050_051|3|TX |UNIAO |00", grid=True, line=1, grid_number=3)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Cancelar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		chaveTit = "D MG 01 FINFN050_0511TX UNIAO 00"

		#Pesquisa titulo a pagar
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		
		#Tentar excluir o titulo de imposto
		self.oHelper.SetButton('Outras Ações',sub_item='Excluir')
		self.oHelper.CheckHelp(text='NO_DELETE2',button='Fechar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT064
	#Estorno da substituição de titulos provisorios sem impostos

	#author Vitor Duca
	#since 19/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56310
	#-----------------------------------------	
	def test_FINA050_CT064(self):

		chaveNF  = "D MG 01 FINFN050_064 NF TIR00101"
			
		self.oHelper.WaitShow("Contas a Pagar") 
		
		#Altera pergunte da rotina
		self.oHelper.SetKey("F12")
		self.oHelper.WaitShow("Parametros")
		self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		self.oHelper.SetButton('Ok')

		#Exclusão do titulo efetivos, estorno da substituição 
		self.oHelper.SearchBrowse(f'{chaveNF}', key=1, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Excluir')
		self.oHelper.SetButton('Sim')
		self.oHelper.SetButton('Confirmar')
	
		#Restaura pergunte da rotina
		self.oHelper.SetKey("F12")
		self.oHelper.WaitShow("Parametros")
		self.oHelper.SetValue('Mostra Lanc Contab ?', "Sim")
		self.oHelper.SetButton('Ok')

		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT162
	#Inclusão de título a pagar com rateio de IR por CPF 20/30/50

	#author Karen Honda
	#since 07/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50872
	#-----------------------------------------	
	def test_FINA050_CT162(self):

		cPrefixo = "FIN"
		cTitulo  = "FN050_162"
		cTipo    = "NF"
		cNatureza = "FINIRPROG"
		cFornece   = "FIRP06"
		cLoja = "01"

		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO', cPrefixo)
		self.oHelper.SetValue('E2_NUM',cTitulo)
		self.oHelper.SetValue('E2_TIPO',cTipo)
		self.oHelper.SetValue('E2_NATUREZ',cNatureza)
		self.oHelper.SetValue('E2_FORNECE',cFornece)
		self.oHelper.SetValue('E2_LOJA',cLoja)
		self.oHelper.SetValue('E2_EMISSAO','07/05/2020')
		self.oHelper.SetValue('E2_VENCTO','07/05/2020')
		self.oHelper.SetValue('E2_VENCREA','07/05/2020')
		self.oHelper.SetValue('E2_VALOR','10.000,00')
		self.oHelper.ClickFolder('Impostos')
		self.oHelper.SetValue('E2_DIRF','1')
		self.oHelper.SetValue('E2_CODRET','3208')

		self.oHelper.CheckResult("E2_IRRF", "679,74")
		self.oHelper.SetButton('Outras Ações',sub_item='Rateio de IR Progressivo')

		self.oHelper.WaitShow("Rateio de IR progressivo")
		
		self.oHelper.CheckResult("Rendimento total", "5000.00", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Imposto a ser retido", "548.85", grid=True, line=1, grid_number=1)

		self.oHelper.CheckResult("Rendimento total", "2000.00", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Imposto a ser retido", "15.92", grid=True, line=2, grid_number=1)

		self.oHelper.CheckResult("Rendimento total", "3000.00", grid=True, line=3, grid_number=1)
		self.oHelper.CheckResult("Imposto a ser retido", "114.97", grid=True, line=3, grid_number=1)

		self.oHelper.LoadGrid() 

		self.oHelper.SetButton('Fechar')
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT163
	#Inclusão de título a pagar com rateio de IR com título gerado no legado

	#author Karen Honda
	#since 07/05/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50887
	#-----------------------------------------	
	def test_FINA050_CT163(self):

		cPrefixo = "FIN"
		cTitulo  = "FIN163_2"
		cTipo    = "NF"
		cNatureza = "FINIRPROG"
		cFornece   = "FIRP07"
		cLoja = "01"

		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("07/05/2020","T1", "D MG 01 ","06")
		time.sleep(10)
		self.oHelper.SetLateralMenu('Atualizações > Contas a Pagar > Contas a Pagar')
		
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO', cPrefixo)
		self.oHelper.SetValue('E2_NUM',cTitulo)
		self.oHelper.SetValue('E2_TIPO',cTipo)
		self.oHelper.SetValue('E2_NATUREZ',cNatureza)
		self.oHelper.SetValue('E2_FORNECE',cFornece)
		self.oHelper.SetValue('E2_LOJA',cLoja)
		self.oHelper.SetValue('E2_EMISSAO','07/05/2020')
		self.oHelper.SetValue('E2_VENCTO','07/05/2020')
		self.oHelper.SetValue('E2_VENCREA','07/05/2020')
		self.oHelper.SetValue('E2_VALOR','10.000,00')
		self.oHelper.ClickFolder('Impostos')
		self.oHelper.SetValue('E2_DIRF','1')
		self.oHelper.SetValue('E2_CODRET','3208')

		self.oHelper.CheckResult("E2_IRRF", "4.673,85")
		self.oHelper.SetButton('Salvar')
		self.oHelper.CheckHelp(text='IRPROGLEGADO',button='Fechar')

		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT173
	#Substituição de provisório para NF

	#author Leandro Fini
	#since 04/06/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/193969
	#-----------------------------------------	
	def test_FINA050_CT173(self):
		
		prefixo = 'AUT'
		titulo  = 'LF005'
		parcela = '1'
		tipo    = 'PR'
		fornecedor = 'LF005'
		loja    = '00'
					
		self.oHelper.WaitShow("Contas a Pagar") 

		#Pesquisa titulo provisorio
		self.oHelper.SetButton('Outras Ações',sub_item='Substituição de Provisórios')
		
		#Tela de seleção de filiais
		self.oHelper.SetButton('Marca Todos -')
		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetValue('Fornecedor :', fornecedor)
		self.oHelper.SetValue('Loja :',loja)
		self.oHelper.SetValue('Moeda :','02 DOLAR')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.ClickBox("No. Titulo", titulo)
		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetValue('E2_TIPO',"NF")
		self.oHelper.SetValue('E2_NATUREZ',"LF005")
		self.oHelper.CheckResult("E2_VALOR", "1.000,00")

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		
	#-----------------------------------------
	#{Protheus.doc} FINA050_CT182
	# Inclusão de Abatimento, selecionando titulo Pai, sem inserir 
	# Prefixo, Número e Parcela 

	#author Rafael Sarracini
	#since 02/07/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T52422
	#-----------------------------------------	
	def test_FINA050_CT182(self):

		chaveTit = "D MG 01 RS RS4.1    1NF RS002 00"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		#Pesquisa titulo NF
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		
		#Inclusão de Abatimento sem colocar Prefixo,Numero e Parcela
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')

		self.oHelper.SetValue('E2_TIPO','AB-')
		self.oHelper.SetKey("Enter")
		self.oHelper.SetValue('E2_VALOR','500,00')
		self.oHelper.SetKey("Enter")
		
		#Confirma inclusão do titulo
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT187
	# Inclusão de título NF com complemento de título de INSS 

	#author Leandro Fini
	#since 28/07/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T52939
	#-----------------------------------------	
	def test_FINA050_CT187(self):

		cPrefixo = "FIN"
		cTitulo  = "LF008"
		cTipo    = "NF"
		cNatureza = "LF006"
		cFornece   = "LF008"
		cLoja = "00"	
		
		self.oHelper.WaitShow("Contas a Pagar")
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO', cPrefixo)
		self.oHelper.SetValue('E2_NUM',cTitulo)
		self.oHelper.SetValue('E2_TIPO',cTipo)
		self.oHelper.SetValue('E2_NATUREZ',cNatureza)
		self.oHelper.SetValue('E2_FORNECE',cFornece)
		self.oHelper.SetValue('E2_LOJA',cLoja)
		self.oHelper.SetValue('E2_EMISSAO','28/07/2020')
		self.oHelper.SetValue('E2_VENCTO','28/07/2020')
		self.oHelper.SetValue('E2_VENCREA','28/07/2020')
		self.oHelper.SetValue('E2_VALOR','433,25')

		self.oHelper.SetButton('Outras Ações',sub_item='Complemento do título')
		time.sleep(2)
		self.oHelper.ClickFolder('Complemento do Imposto X Títulos')

		#Tela de complemento de título
		self.oHelper.SetValue('Código','FIN054', grid=True, grid_number=1)
		self.oHelper.SetValue('Base de Calc','433,25', grid=True, grid_number=1)
		self.oHelper.LoadGrid()

		#Confirma inclusão do complemento de título
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Sim')
		self.oHelper.SetButton('Fechar')

		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.CheckResult("E2_VALOR", "376,94")

		self.oHelper.ClickFolder('Impostos')
		self.oHelper.CheckResult("E2_INSS", "56,31")

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		
	#-----------------------------------------
	#{Protheus.doc} FINA050_CT206
	# Alteração no agendamento de vencimento de um titulo a pagar, verificando
	# o conteudo do campo E2_DATAAGE 

	#author Vitor Duca
	#since 09/11/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T55522
	#-----------------------------------------	
	def test_FINA050_CT206(self):
		
		chaveTit = "D MG 01 FINFN050_206 NF TIR00101"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		#Pesquisa titulo a pagar
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Agendamento')
		
		#Tela de agendamento do vencimento 
		time.sleep(3)
		self.oHelper.SetValue('Data de Agendamento:', '09/11/2020')
		self.oHelper.SetButton('Confirmar')

		#Visualização do campo E2_DATAAGE
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Banco')
		self.oHelper.CheckResult("E2_DATAAGE", "09/11/2020")
		self.oHelper.SetButton('Cancelar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT207
	# Validação da recomposição de base na modalidade de retenção do PCC

	#author Vitor Duca
	#since 09/11/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T55540
	#-----------------------------------------	
	def test_FINA050_CT207(self):

		self.oHelper.AddParameter("MV_BX10925","","2","2","2")  
		self.oHelper.SetParameters()

		cPrefixo = "FIN"
		cTitulo = "FN050_207"
		cTipo = "NF "
		cNatureza = "003"
		cFornece = "FIN008"
		cLoja = "01"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO', cPrefixo)
		self.oHelper.SetValue('E2_NUM',cTitulo)
		self.oHelper.SetValue('E2_TIPO',cTipo)
		self.oHelper.SetValue('E2_NATUREZ',cNatureza)
		self.oHelper.SetValue('E2_FORNECE',cFornece)
		self.oHelper.SetValue('E2_LOJA',cLoja)
		self.oHelper.SetValue('E2_EMISSAO','09/11/2020')
		self.oHelper.SetValue('E2_VENCTO','09/11/2020')
		self.oHelper.SetValue('E2_VENCREA','09/11/2020')
		self.oHelper.SetValue('E2_VALOR','10.000,00')

		#Verifica valor dos impostos
		self.oHelper.ClickFolder('Impostos')
		self.oHelper.CheckResult("E2_COFINS", '300,00')
		self.oHelper.CheckResult("E2_PIS", '65,00')
		self.oHelper.CheckResult("E2_CSLL", '100,00')

		#Verifica valor liquido do titulo
		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.CheckResult("E2_VALOR", '9.535,00')

		#Tela de modalidade de retenção do PCC
		time.sleep(2)
		self.oHelper.SetButton('Outras Ações',sub_item='Impostos')
		self.oHelper.SetValue('Nao efetua retencäo', True, grid=False)
		self.oHelper.SetButton('Ok')

		#Verifica valor recomposto do titulo
		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.CheckResult("E2_VALOR", '10.000,00')
		
		#Verifica valor dos impostos
		self.oHelper.ClickFolder('Impostos')
		self.oHelper.CheckResult("E2_COFINS", '0,00')
		self.oHelper.CheckResult("E2_PIS", '0,00')
		self.oHelper.CheckResult("E2_CSLL", '0,00')

		#Tela de modalidade de retenção do PCC
		time.sleep(2)
		self.oHelper.SetButton('Outras Ações',sub_item='Impostos')
		self.oHelper.SetValue('Calculado pelo sistema', True, grid=False)
		self.oHelper.SetButton('Ok')

		#Verifica valor recomposto do titulo
		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.CheckResult("E2_VALOR", '9.535,00')
		
		#Verifica valor dos impostos
		self.oHelper.ClickFolder('Impostos')
		self.oHelper.CheckResult("E2_COFINS", '300,00')
		self.oHelper.CheckResult("E2_PIS", '65,00')
		self.oHelper.CheckResult("E2_CSLL", '100,00')

		self.oHelper.SetButton('Cancelar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")
		self.oHelper.AssertTrue()

		self.oHelper.RestoreParameters()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT208
	# Visualização do rastreio de contratos

	#author Vitor Duca
	#since 09/11/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T55544
	#-----------------------------------------	
	def test_FINA050_CT208(self):
		
		chaveTit = "D MG 01 GCTCTCN12188 NF GCT00101"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		#Pesquisa titulo a pagar
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Rastr.Contrato')
		
		#Tela de rastreio de contratos
		time.sleep(3)
		self.oHelper.ClickTree("Nota fiscal de entrada / Serie - CTCN12188/GCT > Titulo - Fornecedor/Loja/Prefixo/Numero/Parcela/Tipo - GCT001/01/GCT/CTCN12188/ /NF ")
		self.oHelper.SetButton('Ok')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT209
	#Manutenção de documentos no titulo a pagar

	#author Vitor Duca
	#since 10/11/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T55631
	#-----------------------------------------	
	def test_FINA050_CT209(self):
	
		chaveTit = "D MG 01 FINFN050_209 NF 001   00"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		#Pesquisa titulo a pagar
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Documentos')

		#Tela de manutenção dos documentos
		#Primeira linha
		time.sleep(5)
		self.oHelper.CheckResult("Cod.Document", "011", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Descricao", "DOCUMENTO TIR", grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult("Recebido", "Nao", grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid() 

		#inclusão da segunda linha
		self.oHelper.SetKey("DOWN", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("Cod.Document", "001", grid=True, grid_number=1, ignore_case = True, row=2)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Cod.Document", "001", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Descricao", "TIPO DOCUMENTO GCT", grid=True, line=2, grid_number=1)
		self.oHelper.CheckResult("Recebido", "Nao", grid=True, line=2, grid_number=1)	
		self.oHelper.LoadGrid() 

		self.oHelper.SetButton('Confirmar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		#Restaura o filtro de pesquisa da browse
		chaveTit = " "
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT211
	#Alteração de titulo gravando informações na tabela FI2
	#instruções de cobrança MV_INCOBBC

	#author Vitor Duca
	#since 30/11/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56070
	#-----------------------------------------	
	def test_FINA050_CT211(self):
		
		self.oHelper.AddParameter("MV_INCOBBC","","2","2","2")  
		self.oHelper.SetParameters()

		chaveTit = "D MG 01 FINFN050_211 NF 001   00"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		#Pesquisa titulo a pagar
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('E2_NATUREZ',"001")

		#Tela de justificativa
		self.oHelper.SetButton('Outras Ações',sub_item='Justificativa')
		self.oHelper.SetButton('Salvar')

		self.oHelper.SetButton('Salvar')
		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		#Restaura o filtro de pesquisa da browse
		chaveTit = " "
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.AssertTrue()

		self.oHelper.RestoreParameters()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT212
	# Inclusão de um titulo com ISS para validar a mensagem "Titulo com ISS: Municipio exige CPOM?"

	#author Vitor Duca
	#since 07/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56204
	#-----------------------------------------	
	def test_FINA050_CT212(self):

		cPrefixo = "FIN"
		cTitulo = "FN050_212"
		cTipo = "NF "
		cNatureza = "CPOM"
		cFornece = "CPOM01"
		cLoja = "01"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 02')
		self.oHelper.SetValue('E2_PREFIXO', cPrefixo)
		self.oHelper.SetValue('E2_NUM',cTitulo)
		self.oHelper.SetValue('E2_TIPO',cTipo)
		self.oHelper.SetValue('E2_NATUREZ',cNatureza)
		self.oHelper.SetValue('E2_FORNECE',cFornece)
		self.oHelper.SetValue('E2_LOJA',cLoja)
		self.oHelper.SetValue('E2_EMISSAO','08/12/2020')
		self.oHelper.SetValue('E2_VENCTO','08/12/2020')
		self.oHelper.SetValue('E2_VENCREA','08/12/2020')
		self.oHelper.SetValue('E2_VALOR','10.000,00')

		#Verifica valor dos impostos
		self.oHelper.ClickFolder('Impostos')
		self.oHelper.CheckResult("E2_ISS", '500,00')

		#Verificação do Help
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Sim')
		self.oHelper.CheckHelp(text='F050CODSER',button='Fechar')

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')

		#Deseja cadastrar os valores acessórios deste título agora?
		self.oHelper.SetButton('Não')

		self.oHelper.SetButton('Cancelar')
		
		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")
		self.oHelper.AssertTrue()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT213
	# Inclusão de NF a pagar informando o valor dos impostos manualmente

	#author Vitor Duca
	#since 08/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56242
	#-----------------------------------------	
	def test_FINA050_CT213(self):

		self.oHelper.AddParameter("MV_BX10925","","2","2","2")  
		self.oHelper.SetParameters()

		cPrefixo = "FIN"
		cTitulo = "FN050_213"
		cTipo = "NF "
		cNatureza = "001"
		cFornece = "FIN008"
		cLoja = "01"
			
		self.oHelper.WaitShow("Contas a Pagar") 

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO', cPrefixo)
		self.oHelper.SetValue('E2_NUM',cTitulo)
		self.oHelper.SetValue('E2_TIPO',cTipo)
		self.oHelper.SetValue('E2_NATUREZ',cNatureza)
		self.oHelper.SetValue('E2_FORNECE',cFornece)
		self.oHelper.SetValue('E2_LOJA',cLoja)
		self.oHelper.SetValue('E2_EMISSAO','08/12/2020')
		self.oHelper.SetValue('E2_VENCTO','08/12/2020')
		self.oHelper.SetValue('E2_VENCREA','08/12/2020')
		self.oHelper.SetValue('E2_VALOR','10.000,00')

		#Verifica valor dos impostos
		self.oHelper.ClickFolder('Impostos')
		self.oHelper.SetValue('E2_COFINS','300,00')
		self.oHelper.SetValue('E2_PIS','65,00')
		self.oHelper.SetValue('E2_CSLL','100,00')
		self.oHelper.SetValue('E2_IRRF','150,00')
		self.oHelper.SetValue('E2_INSS','110,00')

		#Verifica valor liquido do titulo
		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.CheckResult("E2_VALOR", '9.275,00')
		
		self.oHelper.SetButton('Salvar')

		#Deseja cadastrar os valores acessórios deste título agora?
		self.oHelper.SetButton('Não')

		self.oHelper.SetButton('Cancelar')
		
		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")
		self.oHelper.AssertTrue()

		self.oHelper.RestoreParameters()

	#-----------------------------------------
	#{Protheus.doc} FINA050_CT214
	#Inclusão de titulo a pagar com rateio contabil pré-configurado

	#author Vitor Duca
	#since 09/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56262
	#-----------------------------------------	
	def test_FINA050_CT214(self):

		self.oHelper.WaitShow("Contas a Pagar")
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO','FIN')
		self.oHelper.SetValue('E2_NUM','FN050_214')
		self.oHelper.SetValue('E2_TIPO','NF')
		self.oHelper.SetValue('E2_NATUREZ','TIR001')
		self.oHelper.SetValue('E2_FORNECE','TIR001')
		self.oHelper.SetValue('E2_LOJA','01')
		self.oHelper.SetValue('E2_EMISSAO',DateSystem)
		self.oHelper.SetValue('E2_VENCTO',DateSystem)
		self.oHelper.SetValue('E2_VALOR','10.000,00')

		self.oHelper.ClickFolder('Contábil')
		self.oHelper.SetValue('E2_RATEIO','S')

		#Tela para escolher o tipo de rateio
		self.oHelper.SetValue('Pre-Configurado', True, grid=False)
		self.oHelper.SetValue('Codigo Rateio:','0001  ')
		self.oHelper.SetValue('Historico','TIR RATEIO CONF')
		self.oHelper.SetButton('Ok')

		#Tela de cadastro dos rateios contabeis
		self.oHelper.SetButton('Salvar')

		#Confirma inclusão do titulo
		self.oHelper.SetButton('Salvar')

		#Deseja cadastrar os valores acessórios deste título agora?
		self.oHelper.SetButton('Não')
		self.oHelper.SetButton('Cancelar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()
		
	#-----------------------------------------
	#{Protheus.doc} FINA050_CT217
	#Inclusão de titulo a pagar validando o codigo de barras e linha digitavel

	#author Vitor Duca
	#since 22/12/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56540
	#-----------------------------------------	
	def test_FINA050_CT217(self):

		self.oHelper.WaitShow("Contas a Pagar")
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E2_PREFIXO','FIN')
		self.oHelper.SetValue('E2_NUM','FN050_217')
		self.oHelper.SetValue('E2_TIPO','NF')
		self.oHelper.SetValue('E2_NATUREZ','TIR001')
		self.oHelper.SetValue('E2_FORNECE','TIR001')
		self.oHelper.SetValue('E2_LOJA','01')
		self.oHelper.SetValue('E2_EMISSAO',DateSystem)
		self.oHelper.SetValue('E2_VENCTO',DateSystem)
		self.oHelper.SetValue('E2_VALOR','1.000,00')

		#Codigo de barras / linha digitavel
		self.oHelper.SetButton('Outras Ações',sub_item='Código de barras')
		self.oHelper.SetValue("Código de barras / linha digitável",'10499541322200010001012405542742484800000084564')
		self.oHelper.SetButton("OK")

		self.oHelper.ClickFolder('Banco')
		self.oHelper.CheckResult('E2_CODBAR','10494848000000845649541322000100011240554274')
		self.oHelper.CheckResult('E2_LINDIG','10499541322200010001012405542742484800000084564 ')

		#Confirma inclusão do titulo
		self.oHelper.SetButton('Salvar')

		#Deseja cadastrar os valores acessórios deste título agora?
		self.oHelper.SetButton('Não')
		self.oHelper.SetButton('Cancelar')

		#Verifica se voltou para a browse do contas a pagar
		self.oHelper.WaitShow("Contas a Pagar")

		self.oHelper.AssertTrue()	
	#-------------------------------------------
	# Encerramento class para TIR - FINA050 
	#-------------------------------------------
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()