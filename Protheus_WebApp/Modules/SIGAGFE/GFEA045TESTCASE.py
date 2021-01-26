from tir import Webapp
import unittest

class GFEA045(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA045')

	def test_GFEA045_CT001(self):

		self.oHelper.AddParameter("MV_CADOMS", "D MG 01", "2", "2", "2")
		self.oHelper.SetParameters()

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Tipo Veiculo', 'FOGUETE')
		self.oHelper.SetValue('Descricao   ', 'FOGUETE DA LOGISTICA')
		self.oHelper.SetValue('Nr Eixos    ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        FOGUETE')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Descricao   ', 'TESTE DE AUTOMACAO - ALTERADO')
		self.oHelper.SetValue('Nr Eixos    ', '2')
		self.oHelper.SetValue('Cat.Vei.Ped.', 'E')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        FOGUETE')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        FOGUETE')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Tipo Veiculo', 'LAMBRETA')
		self.oHelper.SetValue('Descricao   ', 'LAMBRETA TESTE AUTOMACAO')
		self.oHelper.SetValue('Nr Eixos    ', '1')
		self.oHelper.SetValue('Cat.Vei.Ped.', 'M')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        FOGUETE')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        LAMBRETA')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

