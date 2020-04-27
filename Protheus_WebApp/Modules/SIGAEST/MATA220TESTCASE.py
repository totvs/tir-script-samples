from tir import Webapp
import unittest

class MATA220(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','20/09/2019','T1','D MG 01')
		inst.oHelper.Program('MATA220')		

	def test_MAT220_002(self):
		self.oHelper.AddParameter("MV_GRADE", "", ".F.", ".F.", ".F.")
		self.oHelper.SetParameters()
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Produto','ESTMATA220TIR00000000000000000')
		self.oHelper.SetValue('Armazem','01')
		self.oHelper.SetValue('Qtd.Inic.Mes','100,00')
		self.oHelper.SetButton('Outras Ações', 'Inf. lote')
		self.oHelper.SetValue('Lote','0000000001', grid=True)
		self.oHelper.SetValue('Potência','5,00', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()