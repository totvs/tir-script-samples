from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA269TestCase
TIR - Casos de testes da rotina Cadastro de Datas de Pagamento

@author Silvia SantAnna
@since 11/2020
@version 12
-------------------------------------------------------------------"""
class PLSA269(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA269")
		inst.oHelper.AddParameter("MV_PLSDTPG","" , ".T.")
		inst.oHelper.SetParameters()

	def test_PLSA269_001(self):
		# Incluir
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("BXT_CODINT","0001", check_value = False)
		self.oHelper.SetValue("BXT_ANO","2020")
		self.oHelper.SetValue("BXT_MES","11")
		self.oHelper.SetValue("BXT_REEMB", "0 - Nao")
		# Grid
		self.oHelper.ClickGridCell("Data de Pgto", row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True, grid_number=1)
		self.oHelper.SetValue("BXU_DATPAG","01/12/2020", check_value = False)
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		# Alterar
		self.oHelper.SetButton("Alterar")
		# Grid
		self.oHelper.ClickGridCell("Data de Pgto",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("BXU_DATPAG","01/01/2021", check_value = False)
		self.oHelper.SetButton("Ok")	# A data não pode ser Sabado, Domingo ou Feriado
		self.oHelper.SetValue("BXU_DATPAG","04/01/2021", check_value = False)
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Salvar")

		# Visualizar
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BXT_ANO","2020")
		self.oHelper.SetButton("Confirmar")

		# Pesquisar
		self.oHelper.SetButton("Outras Ações",  sub_item='Pesquisar')
		self.oHelper.SetButton("Ok")

		# Legenda
		self.oHelper.SetButton("Outras Ações",  sub_item='Legenda')
		self.oHelper.SetButton("Fechar")

		# Excluir
		self.oHelper.SetButton("Outras Ações",  sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")


		self.oHelper.SetButton('x')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()