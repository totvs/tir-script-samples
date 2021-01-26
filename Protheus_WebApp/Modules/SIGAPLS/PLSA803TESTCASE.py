from tir import Webapp
import unittest


"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA803TestCase
TIR - Casos de testes da rotina Observacoes padrao

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA803(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","10/09/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSA803")

	def test_PLSA803_001(self):
		self.oHelper.SetButton("Incluir")
		#self.oHelper.SetBranch('M SP 01')
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("B9N_OBSERV","PLS DSAUPC TIR INCLUSAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("B9N_OBSERV","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B9N_OBSERV","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Outras Ações",sub_item='Copiar')
		self.oHelper.SetValue("B9N_OBSERV","PLS DSAUPC TIR COPIA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SearchBrowse(f'{"M SP    0001PLS DSAUPC TIR COPIA"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9N_OBSERV","PLS DSAUPC TIR COPIA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SearchBrowse(f'{"M SP    0001PLS DSAUPC TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9N_OBSERV","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()