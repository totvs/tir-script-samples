from tir import Webapp
import unittest

class GFEX011(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','28/06/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEX011')

	def test_GFEX011_CT001(self):

		self.oHelper.SetValue('Tipo Operação','1')
		self.oHelper.SetValue('Cod. Remetente','001')
		self.oHelper.SetValue('Cod. Destinatário','003')
		self.oHelper.SetValue('Cidade Origem','4209102')
		self.oHelper.SetValue('Cidade Destino','3550308')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()
