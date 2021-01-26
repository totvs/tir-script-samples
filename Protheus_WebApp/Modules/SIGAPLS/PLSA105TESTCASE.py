from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA105TestCase
TIR - Casos de testes da rotina RDA X Tabela de Precos

@author Silvia SantAnna
@since 10/2020
@version 12
-------------------------------------------------------------------"""
class PLSA105(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA105")

	def test_PLSA105_001(self):

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")

		self.oHelper.SetValue("BC5_CODINT","0001",check_value = False)
		self.oHelper.SetValue("BC5_CODRDA","000007")
		self.oHelper.SetValue("BC5_DESCRI","PLS DSAUPC TIR INCLUSAO")
		self.oHelper.SetValue("BC5_VPPP","10",check_value = False)
		self.oHelper.SetValue("BC5_VRPP","10",check_value = False)
		self.oHelper.SetValue("BC5_VPCO","10",check_value = False)
		self.oHelper.SetValue("BC5_VRCO","10",check_value = False)
		self.oHelper.SetValue("BC5_DATINI","01/01/2020",check_value = False)
		self.oHelper.SetValue("BC5_BANDAP","10",check_value = False)
		self.oHelper.SetValue("BC5_BANDAR","10",check_value = False)
		self.oHelper.SetValue("BC5_UCO","10",check_value = False)
		self.oHelper.SetValue("BC5_TABPRE","004")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR INCLUSAO"}', key=2, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("BC5_DESCRI","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BC5_DESCRI","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Procedimentos')
		#incllusao de procedimento
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue("BC6_CDPRRA","10101012")
		self.oHelper.SetValue("BC6_CODPRO","10101012")
		self.oHelper.SetValue("BC6_TIPLAN", "1 - Aplicado a todas as acomodacoes")
		self.oHelper.SetValue("BC6_USPCO","11",check_value = False)
		self.oHelper.SetValue("BC6_USRCO","11",check_value = False)
		self.oHelper.SetValue("BC6_USPPP","11",check_value = False)
		self.oHelper.SetValue("BC6_USRPP","11",check_value = False)
		self.oHelper.SetValue("BC6_TPLAN", "1 - Aplicado a todas as operadoras")
		self.oHelper.SetValue("BC6_TPLANP", "1 - Aplicado a todos os produtos")
		self.oHelper.SetValue("BC6_CODPAD","01")
		self.oHelper.SetValue("BC6_VIGINI","01/01/2020",check_value = False)
		self.oHelper.SetValue("BC6_BANDAP","11",check_value = False)
		self.oHelper.SetValue("BC6_BANDAR","11",check_value = False)
		self.oHelper.SetValue("BC6_PERDES","11",check_value = False)
		self.oHelper.SetValue("BC6_UCO","11",check_value = False)
		self.oHelper.SetValue("BC6_PERACR","11",check_value = False)
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("BC6_USPCO","20,0000")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BC6_USPCO","20,0000")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton('x')
		#fim da inclusao do procedimento

		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Copiar')
		self.oHelper.SetValue("BC5_DATFIM","31/12/2020",check_value = False)
		self.oHelper.SetValue("BC5_DESCRI","PLS DSAUPC TIR COPIA")
		self.oHelper.SetButton("Confirmar")


		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR COPIA"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Procedimentos')
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("x")

		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR COPIA"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("x")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()