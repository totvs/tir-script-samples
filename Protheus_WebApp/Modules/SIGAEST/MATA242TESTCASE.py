from tir import Webapp
import unittest

class MATA242(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','21/06/2019','T1','D MG 01')
		inst.oHelper.Program('MATA242')

	def test_MATA242_CT001(self):
		self.oHelper.AddParameter("MV_CUSMED", "", "O", "O", "O")
		self.oHelper.SetParameters()
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Produto Origem','ESTSE0000000000000000000000215')
		self.oHelper.SetValue('Armazem','01')
		self.oHelper.SetValue('Endereco','ENDSE01')
		self.oHelper.SetKey("F4")
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Quantidade','1,00')
		self.oHelper.SetValue('Data','21/06/2019')
		self.oHelper.SetValue('Documento','ESTSE0005')
		self.oHelper.SetButton('Outras Ações', '1o.Nivel')
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000216", grid=True)
		self.oHelper.SetValue("Quantidade", "1,00", grid=True)
		self.oHelper.SetValue("% Rateio", "20,00", grid=True)
		self.oHelper.SetValue("Lote", "LT01", grid=True)
		self.oHelper.SetValue("Endereco", "ENDSE01", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.ClickGridCell("Produto", 2)
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000217", grid=True)
		self.oHelper.SetValue("Quantidade", "2,00", grid=True)
		self.oHelper.SetValue("% Rateio", "50,00", grid=True)
		self.oHelper.SetValue("Lote", "LT01", grid=True)
		self.oHelper.SetValue("Endereco", "ENDSE01", grid=True)
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
	