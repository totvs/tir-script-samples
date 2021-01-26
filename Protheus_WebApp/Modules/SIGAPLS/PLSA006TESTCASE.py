from tir import Webapp
import unittest


"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA006TestCase
TIR - Casos de testes da rotina Copia de Local de Atendimento

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA006(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","10/09/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSA006")

	def test_PLSA006_001(self):
		# Inclusao
		self.oHelper.SearchBrowse(f'{"M SP    000007"}', key=1, index=True)
		self.oHelper.SetButton("Selecionar")
		self.oHelper.SetButton("Copiar")
		self.oHelper.SetButton("OK")		# Deseja realmente realizar a Clonagem
		self.oHelper.SetButton("Fechar")	# Clonagem realizada com sucesso

		self.oHelper.SetButton("x")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()