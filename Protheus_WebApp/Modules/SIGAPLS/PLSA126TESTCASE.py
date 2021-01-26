from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA126TestCase
TIR - Casos de testes da rotina Gerar Pagamentos Divididos

@author Silvia SantAnna
@since 11/2020
@version 12
-------------------------------------------------------------------"""
class PLSA126(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA126")

	def test_PLSA126_001(self):

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")

		self.oHelper.SetValue("BDP_OPERDA","0001")
		self.oHelper.SetValue("BDP_RDADE","000007")
		self.oHelper.SetValue("BDP_RDAATE","000007")
		self.oHelper.SetValue("BDP_ANO","2020")
		self.oHelper.SetValue("BDP_MES","11")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BDP_RDADE","000007")
		self.oHelper.CheckResult("BDP_RDAATE","000007")
		self.oHelper.CheckResult("BDP_ANO","2020")
		self.oHelper.CheckResult("BDP_MES","11")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Outras Ações", sub_item='Pesquisar')
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Excluir")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton('x')
		self.oHelper.AssertTrue()



	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()