from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA097TestCase
TIR - Casos de testes da rotina Confirmação de liberação

@author Silvia SantAnna
@since 10/2020
@version 12
-------------------------------------------------------------------"""
class PLSA097(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA097")
		inst.oHelper.AddParameter("MV_PLCALPG","" , "2")
		inst.oHelper.SetParameters()

	def test_PLSA097_001(self):
		self.oHelper.SetValue("BEN_OPERDA","0001")
		self.oHelper.SetValue("BEN_CODRDA","000007")
		self.oHelper.SetValue("BEN_ANO","2020")
		self.oHelper.SetValue("BEN_MES","09")

		self.oHelper.ClickGridCell("Numero Lib.",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("BEP_NUMLIB","000120200600000001", check_value = False)

		#self.oHelper.ClickGridCell("Ano Movto",row=1, grid_number=1)
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		#self.oHelper.SetValue("BEP_ANO","2020")
#
		#self.oHelper.ClickGridCell("Mes Movto",row=1, grid_number=1)
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		#self.oHelper.SetValue("BEP_MES","09")
		self.oHelper.SetButton("Salvar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()