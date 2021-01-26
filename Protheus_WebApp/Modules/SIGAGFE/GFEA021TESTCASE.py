from tir import Webapp
import unittest

class GFEA021(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA021')

	def test_GFEA021_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Regiao      ', '900001')
		self.oHelper.SetValue('Nome        ', 'VALE DO ITAJAI')
		self.oHelper.SetValue('Estado      ', 'SC')
		self.oHelper.SetValue('Pais        ', '105')
		self.oHelper.SetValue('Sigla       ', 'SCVIT')
		self.oHelper.SetValue('Demais Cid? ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Demais Cid? ', '2')
		self.oHelper.ClickGridCell('Cidade', 1)
		self.oHelper.SetValue('Cidade', '4214805', grid=True)
		self.oHelper.SetKey("DOWN", grid=True)
		self.oHelper.SetValue('Cidade', '4207502', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Regiao      ', '900002')
		self.oHelper.SetValue('Nome        ', 'GRANDE FLORIANOPOLIS')
		self.oHelper.SetValue('Sigla       ', 'SCFLP')
		self.oHelper.SetValue('Demais Cid? ', '2')
		self.oHelper.SetValue('Cidade', '4205407', grid=True)
		self.oHelper.SetKey("DOWN", grid=True)
		self.oHelper.SetValue('Cidade', '4216602', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900002')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

