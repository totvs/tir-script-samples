import unittest
import time

from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

"""-------------------------------------------------------------------
/*/{Protheus.doc} FINA560TestCase
TIR - Casos de testes da rotina movimentos de caixinha

@author Karen Honda
@since 23/06/2020
@version 12
-------------------------------------------------------------------"""

class FINA560(unittest.TestCase):

	#-------------------------------------------
	# Inicialiação setUpClass para TIR - FINA560 
	#-------------------------------------------
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN",DateSystem,"T1","D MG 01 ","06")
		inst.oHelper.Program('FINA560')

	#-----------------------------------------
	#{Protheus.doc} FINA560_CT010
	#Valida褯 de inclus䯠de adiantamento com valor maior que o saldo.

	#author Simone Kakinoana
	#since 23/06/2020
	#version 1.0
	#See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-
	#-----------------------------------------	
	def test_FINA560_CT010(self):

		self.oHelper.WaitShow("Movimento do Caixinha") 

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('EU_CAIXA','110')
		self.oHelper.SetValue('EU_TIPO','01')
		self.oHelper.SetValue('EU_HISTOR','TESTE VALOR')
		self.oHelper.SetValue('EU_NRCOMP','00001')
		self.oHelper.SetValue('EU_VALOR',"10.000,00")
		self.oHelper.SetValue('EU_BENEF','BENEF. TESTE')

		self.oHelper.SetValue('EU_CAIXA','120')
		
		self.oHelper.SetButton('Salvar')

		self.oHelper.CheckHelp(text='FA560SALDO',button='Fechar')

		self.oHelper.WaitShow("Movimento do Caixinha")

		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()	

	#-------------------------------------------
	# Encerramento class para TIR - FINA560 
	#-------------------------------------------
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()