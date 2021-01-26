from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA515TestCase
TIR - Casos de testes da rotina Coparticipacao da Operadora

@author Silvia SantAnna
@since 10/2020
@version 12
-------------------------------------------------------------------"""
class PLSA515(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA515")

	def test_PLSA515_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")

		self.oHelper.SetValue("BWK_CODINT","0001",check_value = False)
		self.oHelper.SetValue("BWK_ANO","2020")
		self.oHelper.SetValue("BWK_MES","10")
		self.oHelper.ClickGridCell("Reg Atendto",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("BWW_TIPO", "3 - Ambos")
		self.oHelper.SetValue("BWW_QTD","99")
		self.oHelper.SetValue("BWW_PERCOP","10",check_value = False)
		self.oHelper.SetValue("BWW_VALUS","1",check_value = False)
		self.oHelper.SetValue("BWW_TXADM","5",check_value = False)
		self.oHelper.SetValue("BWW_LIMFRA","4",check_value = False)
		self.oHelper.SetValue("BWW_CODTAB","0001001",check_value = False)
		self.oHelper.SetValue("BWW_VIGINI","01/10/2020",check_value = False)
		self.oHelper.SetValue("BWW_VIGFIN","31/10/2020",check_value = False)
		self.oHelper.SetValue("BWW_FINATE","1")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse(f'{"M SP    0001202010"}', key=1, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.ClickGridCell("Reg Atendto",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("BWW_QTD","50")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SearchBrowse(f'{"M SP    0001202010"}', key=1, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.ClickGridCell("Reg Atendto",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.CheckResult("BWW_QTD","50")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Outras Ações",sub_item='impRimir')
		self.oHelper.SetButton("Param.")
		self.oHelper.SetValue("mv_par01","0001")
		self.oHelper.SetValue("mv_par02","2020")
		self.oHelper.SetValue("mv_par03","01")
		self.oHelper.SetValue("mv_par04","2020")
		self.oHelper.SetValue("mv_par05","12")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Sair")
		
		self.oHelper.SearchBrowse(f'{"M SP    0001202010"}', key=1, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("x")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()