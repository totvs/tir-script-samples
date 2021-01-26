from tir import Webapp
import unittest


"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSUNISW1TestCase
TIR - Casos de testes da rotina W1 - Servicos de urgencia e emergencia do software de redes

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSUNISW1(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","01/09/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSUNISW1")

	def test_PLSUNISW1_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("B5U_CODIGO","20")
		self.oHelper.SetValue("B5U_DESCRI","TESTE TIR INCLUSAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("B5U_CODIGO","20")
		self.oHelper.SetValue("B5U_DESCRI","TESTE TIR ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B5U_CODIGO","20")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B5U_CODIGO","20")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()