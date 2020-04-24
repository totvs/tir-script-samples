from tir import Webapp
import unittest

class MATA240(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('MATA240')		

	def test_MATA240_CT001(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('TP Movimento','501')
		self.oHelper.SetValue('Produto','ESTSE0000000000000000000000332')
		self.oHelper.SetValue('Quantidade','12,00')
		self.oHelper.SetValue('Documento','ESTEA001')
		self.oHelper.SetValue('DT Emissao', '01/10/2019')
		self.oHelper.SetFocus('Lote')
		self.oHelper.SetValue('Lote', 'LT01')
		self.oHelper.SetFocus('Endereco')
		self.oHelper.SetValue('Endereco', 'ENDSE01')
		self.oHelper.SetButton('Outras Ações','R.Frota')
		self.oHelper.SetValue('Codigo da Despesa', '01')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')	
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()