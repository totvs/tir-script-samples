from tir import Webapp
import unittest


"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA728TestCase
TIR - Casos de testes da rotina Agente X Cidade

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA728(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","10/09/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSA728")

	def test_PLSA728_001(self):
		# Inclusao
		self.oHelper.SetButton("Incluir")
		#self.oHelper.SetBranch('M SP 01')
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("B9H_NOME","PLS DSAUPC TIR INCLUSAO")
		self.oHelper.SetValue("B9H_EMAIL","DSAUPC@EMAIL.COM")
		self.oHelper.SetValue("B9H_TEL","11332221234",check_value = False)
		## Grid
		#self.oHelper.SetValue("B9K_CODCID","3550308", grid=True, line=1, grid_number=1)
		self.oHelper.ClickGridCell("Cod Cidade")
		self.oHelper.SetKey("Enter", grid=True, grid_number=1, )
		self.oHelper.SetValue("B9K_CODCID","3550308")
		self.oHelper.ClickGridCell("Cidade")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Alteracao
		self.oHelper.SearchBrowse(f'{"M SP    0001000001"}', key=1, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("B9H_NOME","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Visualizacao
		self.oHelper.SearchBrowse(f'{"M SP    0001000001"}', key=1, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B9H_NOME","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Fechar")
		# Exclusao
		self.oHelper.SearchBrowse(f'{"M SP    0001000001"}', key=1, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9H_NOME","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()