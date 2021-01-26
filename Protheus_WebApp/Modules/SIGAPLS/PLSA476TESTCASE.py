from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA476TestCase
TIR - Casos de testes da rotina Grupo Redutor de Custo

@author Silvia SantAnna
@since 11/2020
@version 12
-------------------------------------------------------------------"""
class PLSA476(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.SetLateralMenu('Atualizações > Cadastro Contas > Grupo Redutor de Custo')

	def test_PLSA476_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")

		self.oHelper.SetValue("B65_CODINT","0001")
		self.oHelper.SetValue("B65_DESCRI","PLS DSAUPC TIR INCLUSAO")
		self.oHelper.SetValue("B65_PERPRI","100", check_value = False)
		self.oHelper.SetValue("B65_PERSUB","50", check_value = False)
		self.oHelper.SetValue("B65_AUTOMA", "1 - Sim")
		self.oHelper.SetValue("B65_TPAPLI", "0 - Valor de Pagamento")
		# Grid
		self.oHelper.ClickGridCell("Cd. Grp. Red",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B66_CODIGO","001")
		self.oHelper.SetValue("B66_CODTAB","01")
		self.oHelper.SetValue("B66_CODPSA","10106014")
		self.oHelper.SetValue("B66_LISUNM","HM")
		self.oHelper.SetValue("B66_VIGDE","01/01/2020")
		self.oHelper.SetValue("B66_VIGATE","31/12/2020")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		# ALTERAR
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("B65_DESCRI","PLS DSAUPC TIR ALTERADO")
		self.oHelper.SetValue("B65_TPAPLI", "1 - Apenas cobrança de intercâmbio") #0=Valor de Pagamento;1=Apenas cobrança de intercâmbio 
		self.oHelper.SetValue("B65_PERTER","40", check_value = False)
		# Grid
		self.oHelper.ClickGridCell("Cd. Grp. Red",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B66_CODPSA","10106014")
		self.oHelper.SetKey("F3")
		self.oHelper.WaitShow('Procedimentos Incomp. X Face')
		self.oHelper.SetKey("ESC")
		self.oHelper.WaitShow('Grupo Redutor de Custo - ALTERAR')
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Salvar")

		# VISUALIZAR
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B65_DESCRI","PLS DSAUPC TIR ALTERADO")
		self.oHelper.SetButton("Confirmar")
		
		self.oHelper.SetButton("Outras Ações", sub_item='Excluir') 
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton('x')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()