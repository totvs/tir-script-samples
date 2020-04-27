from tir import Webapp
import unittest

class MATA228(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST', '05/12/2019', 'T1', 'D MG 01')
		inst.oHelper.Program('MATA228')

	def test_MAT220_001(self):
		self.oHelper.AddParameter("MV_CUSFIFO", "", "T", "T", "T")
		self.oHelper.AddParameter("MV_CUSLIFO", "", "T", "T", "T")
		self.oHelper.SetParameters()
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Produto', 'ESTSE0000000000000000000000367')
		self.oHelper.SetValue('Armazem', '01')
		self.oHelper.SetValue('Qtd.Inicio  ', '100,00')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')	
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
