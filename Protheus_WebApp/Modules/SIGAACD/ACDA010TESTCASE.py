#//-------------------------------------------------------------------
#/*/{Protheus.doc} ACDA010 - 										
#
#@author Jefferson Silva de Sousa 
#@since 09/12/2019
#@version P12
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class ACDA010(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','09/12/2019','T1','D MG 01')
		inst.oHelper.Program('ACDA010')	
		inst.oHelper.AddParameter("MV_CBPE012", "", ".T.", ".T.", ".T.")
		inst.oHelper.AddParameter("MV_INTACD", "", "1", "1", "1")
		inst.oHelper.SetParameters()

	#CT001 - Teste de Exclusao de operador com registro de inventario cadastrado	
	#@author: Jefferson Silva de Sousa 
	#@date: 09/12/2019
	
	def test_ACDA010_CT001(self):
		
		self.oHelper.SearchBrowse("D MG 01 EST001")
		time.sleep(5)
		self.oHelper.SetButton("Outras Ações","Excluir")
		self.oHelper.SetButton("Confirmar")
		time.sleep(3)		
		self.oHelper.WaitShow("Exclusão não permitida")		
	
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()