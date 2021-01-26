from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA940TestCase
TIR - Casos de testes da rotina Geração RPC

@author Silvia SantAnna
@since 10/2020
@version 12
-------------------------------------------------------------------"""
class PLSUARPC(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		#inst.oHelper.Program("PLSUARPC")

	#//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSUARPC_001
	# @author silvia.santanna
	# @since 02/10/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
	def test_PLSUARPC_001(self):
		self.oHelper.Program('PLSUARPC')
		self.oHelper.SetButton("Param.")
		self.oHelper.SetValue("mv_par01","0001")
		self.oHelper.SetValue("mv_par02","")
		self.oHelper.SetValue("mv_par03","ZZZZ")
		self.oHelper.SetValue("mv_par04","")
		self.oHelper.SetValue("mv_par05","ZZZZZZZZZZZZ")
		self.oHelper.SetValue("mv_par06","")
		self.oHelper.SetValue("mv_par07","ZZZZZZZZZ")
		self.oHelper.SetValue("mv_par08","")
		self.oHelper.SetValue("mv_par09","ZZZZ")
		self.oHelper.SetValue("mv_par10","01")
		self.oHelper.SetValue("mv_par11","2018")
		self.oHelper.SetValue("mv_par12","12")
		self.oHelper.SetValue("mv_par13","2020")
		self.oHelper.SetValue("mv_par14","/temp/")
		self.oHelper.SetValue("mv_par15","")
		self.oHelper.SetValue("mv_par16","")
		self.oHelper.SetValue("mv_par17","ZZZZZZ")
		self.oHelper.SetValue("mv_par18","")
		self.oHelper.SetValue("mv_par19","ZZZZZZ")

		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sim")

		time.sleep(5)
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()