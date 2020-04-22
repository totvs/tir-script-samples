#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA180
#
#@author carlos.capeli
#@since 22/10/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

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

	def test_MAT180_002(self):

		self.oHelper.SearchBrowse("D MG 01 ESTMATA180TIR00000000000000001")
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Nome Cientif','COMPLEMENTO PRODUTO ALTERACAO - TIR')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	def test_MAT180_003(self):

		self.oHelper.SearchBrowse("D MG 01 ESTMATA180TIR00000000000000002")
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('Produto','ESTMATA180TIR00000000000000002')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	def test_MAT180_004(self):

		self.oHelper.SearchBrowse("D MG 01 ESTMATA180TIR00000000000000003")
		self.oHelper.SetButton('Outras Ações', 'Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()