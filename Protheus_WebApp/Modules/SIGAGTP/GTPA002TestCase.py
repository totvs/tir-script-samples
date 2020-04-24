from tir import Webapp
import unittest

class GTPA002(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "10/04/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA002')

	def test_GTPA002_CT001(self):
		self.oHelper.SearchBrowse("D MG    GTPL04", "Filial+cód. Linha + Código Via")
		self.oHelper.SetButton("Outras Ações", "Replicar Perfil")
		self.oHelper.SetButton("Outras Ações", "Marcar/Desmarcar Todos")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
