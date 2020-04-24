from tir import Webapp
import unittest

class MATA270(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAEST","24/10/2019","T1","D MG 01")
		inst.oHelper.Program("MATA270")

	def test_MAT270_001(self):
		self.oHelper.AddParameter("MV_CONTINV", "", ".T.", ".T.", ".T.")
		self.oHelper.SetParameters()
		self.oHelper.SetValue("Valida Existencia do Produto ?","Sim")
		self.oHelper.SetValue("Sugere inform. inventario ?","Por Codigo")
		self.oHelper.SetValue("Data p/ opcao sel. autom. ?","24/10/2019")
		self.oHelper.SetValue("Selecionar contagem por ?","Produto")
		self.oHelper.SetValue("Data da contagem ?","24/10/2019")
		self.oHelper.SetValue("Contagem ?","1")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetValue("Produto","ESTMATA270TIR00000000000000000")
		self.oHelper.SetValue("Armazem","01")
		self.oHelper.SetValue("Tp Material","PA")
		self.oHelper.SetValue("Documento","000000003")
		self.oHelper.SetValue("Quantidade","10,00")
		self.oHelper.SetValue("Contagem","3")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()