from tir import Webapp
import unittest

class GFEA018(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','21/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA018')

	def test_GFEA018_CT001(self):
		
		self.oHelper.SetButton('Incluir')

		self.oHelper.SetValue('Praça','PRACA GFE')
		self.oHelper.SetValue('Descrição','PRACA TESTE GFE')
		self.oHelper.ClickFolder("Praças X Tarifas")
		self.oHelper.SetValue('Dat.Vig.Ini.','21/12/2020', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue('Cat. Pedagio','A2', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue('Valor','100', grid=True, check_value = False)
		self.oHelper.LoadGrid()
		
		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Alterar')

		self.oHelper.ClickFolder("Praças X Rotas")
		self.oHelper.SetValue('Cidade Orig.','1100205', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue('Cidade Dest.','1200401', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Reajuste')
		
		self.oHelper.SetValue('Nova data de vigência:','22/12/2020')
		self.oHelper.SetValue('Valor de reajuste:','10', check_value = False)

		self.oHelper.SetButton('OK')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()