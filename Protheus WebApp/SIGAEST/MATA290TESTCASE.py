#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA290 - 										
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 26/09/2019
#@version P12
#
# 	CT001 - Processamento do Lote Único
#
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA290(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('MATA290')	

	#CT001 - Processamento do Lote Único		
	#@author: Pedro Antonio Missaglia
	#@date: 26/09/2019

	def test_MATA290_CT001(self):

		self.oHelper.SetButton("Ok")
		time.sleep(20)
		self.oHelper.AssertTrue()
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()