from tir import Webapp
import unittest

class MATA180(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','22/10/2019','T1','D MG 01')
		inst.oHelper.Program('MATA180')

	def test_MAT180_001(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Produto','ESTMATA180TIR00000000000000000')
		self.oHelper.SetValue('Nome Cientif','COMPLEMENTO PRODUTO INCLUSAO - TIR')
		self.oHelper.ClickFolder('Gestão de Serviços')
		self.oHelper.SetValue('Tipo Insumo','4')
		self.oHelper.ClickFolder('Outros')
		self.oHelper.ClickCheckBox('Protótipo',1)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()