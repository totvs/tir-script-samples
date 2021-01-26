from tir import Webapp
import unittest

class GFEA017(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','03/11/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA017')

	def test_GFEA017_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Especie     ', 'DACTE')
		self.oHelper.SetValue('Descricao   ', 'DACTE TESTE')
		self.oHelper.SetValue('Tipo Imposto', '1')
		self.oHelper.SetValue('Calc Normal ', '3')
		self.oHelper.SetValue('Numeracao   ', '3')
		self.oHelper.SetValue('Tamanho Max ', '16')
		self.oHelper.SetValue('Zeros Esqrda', '1')
		self.oHelper.SetValue('Chave CT-e  ', '1')
		self.oHelper.SetValue('PIS/COFINS  ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        DACTE')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Descricao   ', 'DACTE TESTE - ALTERADO')
		self.oHelper.SetValue('Tipo Imposto', '3')
		self.oHelper.SetValue('Calc Normal ', '2')
		self.oHelper.SetValue('Chave CT-e  ', '2')
		self.oHelper.SetValue('PIS/COFINS  ', '3')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        DACTE')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        DACTE')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Especie     ', 'NFSE')
		self.oHelper.SetValue('Descricao   ', 'NFSE TESTE')
		self.oHelper.SetValue('Tipo Imposto', '1')
		self.oHelper.SetValue('Calc Normal ', '3')
		self.oHelper.SetValue('Numeracao   ', '3')
		self.oHelper.SetValue('Tamanho Max ', '16')
		self.oHelper.SetValue('Zeros Esqrda', '1')
		self.oHelper.SetValue('Chave CT-e  ', '1')
		self.oHelper.SetValue('PIS/COFINS  ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        DACTE')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        NFSE')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()
