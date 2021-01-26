from tir import Webapp
import unittest

"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA804TestCase
TIR - Casos de testes da rotina Cadastro de servicos

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA804(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","10/09/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSA804")

	def test_PLSA804_001(self):
		# Inclusao
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("B9O_DESSER","PLS DSAUPC TIR INCLUSAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Alteracao
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR INCLUSAO"}', key=1, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("B9O_DESSER","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Visualizacao
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR ALTERACAO"}', key=1, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B9O_DESSER","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Fechar")
		# Copia
		self.oHelper.SetButton("Outras Ações",sub_item='Copiar')
		self.oHelper.SetValue("B9O_DESSER","PLS DSAUPC TIR COPIA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Exclusao
		## Copia
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR COPIA"}', key=1, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9O_DESSER","PLS DSAUPC TIR COPIA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		## Original
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR ALTERACAO"}', key=1, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9O_DESSER","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()