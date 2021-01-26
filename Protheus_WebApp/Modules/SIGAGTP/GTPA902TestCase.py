from tir import Webapp
import unittest

class GTPA902(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA902')

	def test_GTPA902_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue('GQO_CODIGO','GTPTES')
		self.oHelper.SetValue('GQO_VALOR ','1,000')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue('GQO_MSBLQL ','1')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
