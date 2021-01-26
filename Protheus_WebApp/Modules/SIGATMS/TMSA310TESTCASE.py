from tir import Webapp
import unittest
import datetime


class TMSA310(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		dataAtual = str(datetime.datetime.now().strftime("%d/%m,%Y"))
		inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 04','43')
		inst.oHelper.Program('TMSA310D')

	def test_TMSA310_CT001(self):
		
		self.oHelper.SearchBrowse(f'M SP    000051')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetBranch('M SP 04')
		self.oHelper.SetButton('OK')
		self.oHelper.WaitProcessing('Processando...')
		self.oHelper.AssertTrue()

	def test_TMSA310_CT002(self):

		self.oHelper.SearchBrowse(f'M SP    000051')
		self.oHelper.SetButton('Visualizar')
		
		self.oHelper.SetButton('Outras Ações','Comp.Via.')
		self.oHelper.SetButton('Outras Ações','Mot.Viag.')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Outras Ações','Aju.Viag.')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Outras Ações','Lac.Veic.')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Outras Ações','Adiantam./Desp.')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Outras Ações','Val. Inf.')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Outras Ações','Configurar')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Outras Ações','Leg. Doc.')
		self.oHelper.SetButton('Fechar')	
		self.oHelper.SetButton('Outras Ações','Rota')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Outras Ações','Obs.')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('Outras Ações','Fornecedores Adicionais')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Outras Ações','Prd. Doc.')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Outras Ações','Configurar')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	def test_TMSA310_CT003(self):
		
		self.oHelper.SearchBrowse(f'M SP    000051')
		self.oHelper.SetButton('Outras Ações','Estornar')
		self.oHelper.SetButton('Sim')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()


