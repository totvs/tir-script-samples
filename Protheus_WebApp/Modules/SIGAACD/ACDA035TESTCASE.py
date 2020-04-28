from tir import Webapp
import unittest

class ACDA035(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('ACDA035')	
		inst.oHelper.AddParameter("MV_CBPE012", "", ".T.", ".T.", ".T.")
		inst.oHelper.SetParameters()

	def test_ACDA035_CT001(self):

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Codigo Inv.', '000000005')
		self.oHelper.SetValue('Usuario', '000010')
		self.oHelper.SetValue('Quantidade', '1', grid=True)
		self.oHelper.SetValue('Endereco', 'ENDSE01', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()