from tir import Webapp
import unittest

class GFEA070(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','30/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA070')

	def test_GFEA070_CT001(self):

		self.oHelper.SetButton('Incluir')

		self.oHelper.SetButton('OK')
		
		self.oHelper.SetValue('Emissor', '500')
		self.oHelper.SetValue('Nr Fatura', '3012201')
		self.oHelper.SetValue('Data Emissao', '30/12/2020')
		self.oHelper.SetValue('Data Venc', '30/12/2020')
		self.oHelper.SetValue('Vl Fatura', '1000', check_value = False)

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Vl Fatura', '1500', check_value = False)

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Dados da Conferência')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SetButton('Outras Ações','Documentos de Frete')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Pré-faturas')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Anexos')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SetButton('Outras Ações', 'Copiar')

		self.oHelper.SetValue('Nr Fatura', '3012202')
		self.oHelper.SetValue('Data Emissao', '30/12/2020')
		self.oHelper.SetValue('Data Venc', '30/12/2020')
		self.oHelper.SetValue('Vl Fatura', '1000', check_value = False)

		self.oHelper.SetButton('Confirmar')

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