from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA298TestCase
TIR - Casos de testes da rotina Nota Fiscal de Entrada X Guia

@author Silvia SantAnna
@since 11/2020
@version 12
-------------------------------------------------------------------"""
class PLSA298(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA298")

	def test_PLSA298_001(self):

		# EXCLUIR
		self.oHelper.SearchBrowse(f'{"M SP    0001000100000240000000022002"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações", sub_item='Excluir') 
		self.oHelper.SetButton("Confirmar")
		
		# INCLUIR
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")

		self.oHelper.SetFocus('Fornecedor') 
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse(f'{"000001"}', key=1, index=True)
		self.oHelper.SetButton("Ok")
		self.oHelper.SetValue("B19_LOJA","01")
		self.oHelper.SetFocus('Doc')
		time.sleep(5)
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse(f'{"111201   123"}', key=1, index=True)
		self.oHelper.SetButton("Ok")
		#self.oHelper.SetValue("B19_FORNEC","000001")
		#self.oHelper.SetValue("B19_LOJA","01")
		#self.oHelper.SetValue("B19_DOC","111201")
		#self.oHelper.SetValue("B19_SERIE","123")
		# Grid
		self.oHelper.ClickGridCell("Guia",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B19_GUIA","0001000100000240000000022002", check_value = False)

		#self.oHelper.SetKey("F3", grid=True,  grid_number=1)
		#self.oHelper.SetValue(field = "cChave", value = "ID 33", name_attr = True)
		#self.oHelper.SetKey("ENTER")

		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		# ALTERAR
		self.oHelper.SearchBrowse(f'{"M SP    0001000100000240000000022002"}', key=2, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.ClickGridCell("Guia",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B19_GUIA","0001000100000240000000022003", check_value = False)
		self.oHelper.SetButton("Salvar")
		
		# PESQUISA
		self.oHelper.SearchBrowse(f'{"M SP    0001000100000240000000022003"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações", sub_item='Pesquisar') 
		#self.oHelper.SetButton("Parâmetros")
		#self.oHelper.SetValue("Filial","M SP    ")											#B19_FILIAL
		#self.oHelper.SetValue("Guia","0001000100000240000000022003", check_value = False)	#B19_GUIA
		self.oHelper.SetButton("Ok")

		# VISUALIZAR
		self.oHelper.SearchBrowse(f'{"M SP    0001000100000240000000022003"}', key=2, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B19_FORNEC","000001")
		self.oHelper.CheckResult("B19_DOC","111201")
		self.oHelper.SetButton("Confirmar")

		# EXCLUIR
		self.oHelper.SearchBrowse(f'{"M SP    0001000100000240000000022003"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações", sub_item='Excluir') 
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton('x')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()