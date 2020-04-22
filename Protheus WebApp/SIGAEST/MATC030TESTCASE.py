from tir import Webapp
import unittest

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATC030 - Inclusão e Visualização de Produto
#TABELA SB1
#
#@author ADRIANO VIEIRA
#@since 04/17/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATC030(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		'''
		SETUP
		Test Case Initial Setup
		'''

		#Endereço do webapp e o nome do Browser
		inst.oHelper = Webapp()

		#Parametros de inicializaçao
		inst.oHelper.Setup("SIGAEST","04/07/2019","T1","D MG 01 ","04")

		#Nome da rotina do Caso de Teste
		inst.oHelper.Program("MATC030")

	def test_MATC030_001(self):
		
		#Incluir/Visualização/Excluir
		cod = 'ESTSE0000000000000000000000144'

		self.oHelper.SetValue("Data Inicial dos Movimentos ?", "01/05/2018")
		self.oHelper.SetValue("Data Final dos Movimentos ?", "09/09/2019")
		self.oHelper.SetValue("Qual Armazem ?", "01")
		self.oHelper.SetButton("Ok")
		self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")

		self.oHelper.SetButton("Consulta")
		self.oHelper.SetButton("Imprimir")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Consulta")
		self.oHelper.SetButton("Gráfico")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("X")
		self.oHelper.SetButton("Ok")

		self.oHelper.AssertTrue()

	def test_MATC030_002(self):
		
		self.oHelper.AddParameter("MV_CUSFIL", "", "F", "F", "F")
		self.oHelper.SetParameters()
		cod = 'ESTSE0000000000000000000000613'

		self.oHelper.SetValue("Data Inicial dos Movimentos ?", "10/12/2019")
		self.oHelper.SetValue("Data Final dos Movimentos ?", "10/12/2019")
		self.oHelper.SetValue("Qual Armazem ?", "**")
		self.oHelper.SetButton("Ok")
		self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")

		self.oHelper.SetButton("Consulta")
		self.oHelper.CheckResult("CFO", "RE3*", grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("CFO", "RE3", grid=True, line=2)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Quantidade", "100,00", grid=True, line=3)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Custo Total", "100,00", grid=True, line=3)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Ok")		
		self.oHelper.AssertTrue()			
		self.oHelper.RestoreParameters()
	def test_MATC030_003(self):	
		#GTSER-T49031 consultando se a quantidade esta positiva em movimento de apropiaçao indireta
		
		cod = 'ESTSE0000000000000000000000727'

		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Data Inicial dos Movimentos ?", "18/02/2020")
		self.oHelper.SetValue("Data Final dos Movimentos ?", "18/02/2020")
		self.oHelper.SetValue("Qual Armazem ?", "99")
		self.oHelper.SetButton("OK")

		self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
		self.oHelper.SetButton("Consulta")
		self.oHelper.CheckResult("CFO", "RE3*", grid=True, line=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult("Quantidade", "10,00", grid=True, line=1)
		self.oHelper.LoadGrid()
	
		self.oHelper.SetButton("Ok")
		self.oHelper.AssertTrue()


	@classmethod
	def tearDownClass(inst):
		'''
		Method that finishes the test case.
		'''
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()