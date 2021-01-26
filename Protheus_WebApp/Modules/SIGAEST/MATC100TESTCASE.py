#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATC100 - 										
#
#@author Paulo V. Beraldo
#@since Jun/2020
#@version P12
#
# 	CT001 - Consulta Posicao da Solicitacao de Almoraxifado
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATC100(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','17/06/2020','T1','D MG 01')
		inst.oHelper.Program('MATC100')	

	#CT001 - Consulta Posicao da Solicitacao de Almoraxifado
	#@author: Paulo V. Beraldo
	#@date: Jun/2020

	def test_MATC100_CT001(self):
		self.oHelper.SearchBrowse( 'D MG 01 PMS06602        ' )
		self.oHelper.SetButton( 'Consultar' )
		
		self.oHelper.CheckResult('Numero','PMS066')
		self.oHelper.CheckResult("Produto"	 , "0000001000"	, grid=True,line=1)
		self.oHelper.CheckResult("Quantidade", "2,00"		, grid=True,line=1)
		self.oHelper.CheckResult("Armazem"	 , "1"			, grid=True,line=1)
		self.oHelper.LoadGrid()

		self.oHelper.CheckResult("Produto"	 , "0000001001"	, grid=True,line=2)
		self.oHelper.CheckResult("Quantidade", "2,00"		, grid=True,line=2)
		self.oHelper.CheckResult("Armazem"	 , "1"			, grid=True,line=2)
		self.oHelper.LoadGrid()
		
		self.oHelper.CheckResult("Produto"	 , "0000001002"	, grid=True,line=3)
		self.oHelper.CheckResult("Quantidade", "2,00"		, grid=True,line=3)
		self.oHelper.CheckResult("Armazem"	 , "1"			, grid=True,line=3)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton( 'Confirmar' )
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()