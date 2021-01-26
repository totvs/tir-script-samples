from tir import Webapp
import unittest

class GFEA046(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','21/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA046')

	def test_GFEA046_CT001(self):

		self.oHelper.AddParameter("MV_CADOMS", "D MG 01", "2", "2", "2")
		self.oHelper.SetParameters()

		self.oHelper.SetButton('Incluir')
		
		self.oHelper.SetValue('Cod Veiculo', 'LXT9999')
		self.oHelper.SetValue('Tipo Veiculo', 'TRUCK')
		self.oHelper.SetValue('Placa', 'LXT9999')
		
		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('LXT9999')

		self.oHelper.SetButton('Visualizar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('LXT9999')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('UF Placa', 'SC')

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('LXT9999')
		
		self.oHelper.SetButton('Outras Ações','Copiar')

		self.oHelper.SetValue('Cod Veiculo', 'MCQ8888')
		self.oHelper.SetValue('Tipo Veiculo', 'CARRETA')
		self.oHelper.SetValue('Placa', 'MCQ8888')

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('MCQ8888')

		self.oHelper.SetButton('Outras Ações','Anexos')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SearchBrowse('MCQ8888')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('LXT9999')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

