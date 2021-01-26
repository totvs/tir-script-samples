from tir import Webapp
import unittest

class GTPA110(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA110')

	def test_GTPA110_CT001(self):
		self.oHelper.SearchBrowse("D MG    TESTE", "Filial+num.vale")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('Num.Vale', 'GTP001')
		self.oHelper.SetValue('Finalidade', 'TESTE 1')
		self.oHelper.SetValue('Tipo do Vale', '000001')
		self.oHelper.SetValue('Cod. Agência', 'AGVAL1')
		self.oHelper.SetValue('Cód. Func.', 'GTP100')
		self.oHelper.SetValue('Valor', '500,00')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("D MG    GTP001", "Filial+num.vale")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
