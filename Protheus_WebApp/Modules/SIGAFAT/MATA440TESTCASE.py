from tir import Webapp
import unittest

class MATA440(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','24/04/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA440')

	def test_MATA440_002(self):
		pedido = 'FAT232'
		
		self.oHelper.AddParameter("MV_ESTADO","D MG 01","AL","AL","AL")
		self.oHelper.SetParameters()
		self.oHelper.SearchBrowse(f'D MG 01 {pedido}', 'Filial+numero')
		self.oHelper.SetButton('Liberar')
		self.oHelper.SetValue("Qtd.Liberada", "1,00", grid=True)
		self.oHelper.LoadGrid()		
		self.oHelper.SetButton('Salvar')
		self.oHelper.SearchBrowse(f'D MG 01 {pedido}', 'Filial+numero')
		self.oHelper.SetButton('Liberar')
		self.oHelper.CheckResult("Qtd.Liberada", "9,00", grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Cancelar")
		self.oHelper.RestoreParameters()
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()