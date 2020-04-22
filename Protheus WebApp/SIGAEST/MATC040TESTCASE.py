from tir import Webapp
import unittest

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATC040 - Consulta Geral ao Produto
#TABELA SB1
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 09/03/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATC040(unittest.TestCase):

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
		inst.oHelper.Program("MATC040")

	def test_MATC040_001(self):

		self.oHelper.SearchBrowse('D MG 01 ESTSE0000000000000000000000212')
		
		self.oHelper.SetButton("Parametros")
		
		self.oHelper.SetValue('De Data de Validade ?', '01/01/2018')
		self.oHelper.SetValue('Ate Data de Validade ?', '16/09/2019')
		self.oHelper.SetButton("Ok")
		
		self.oHelper.SetButton("Rastrear")
		self.oHelper.ClickTree('ESTSE0000000000000000000000212')
 
		self.oHelper.SetButton("Salvar")
		
		self.oHelper.AssertTrue()

	   
	@classmethod
	def tearDownClass(inst):
		'''
		Method that finishes the test case.
		'''
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()