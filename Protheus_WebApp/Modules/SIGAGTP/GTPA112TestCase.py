from tir import Webapp
import unittest

class GTPA112(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA112')

	def test_GTPA112_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('Código', 'GTPPR0')
		self.oHelper.SetValue('Matrícula', 'GTP300')
		self.oHelper.SetValue('Num. do Vale', 'GTP003')
		self.oHelper.SetValue('Dt. Nv. Vig.', '30/11/2022')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("D MG    GTP300", "Filial+matrícula")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("D MG    GTP300", "Filial+matrícula")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
