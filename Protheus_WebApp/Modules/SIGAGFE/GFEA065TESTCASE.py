from tir import Webapp
import unittest

class GFEA065(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','15/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA065')

	def test_GFEA065_CT001(self):

		self.oHelper.SetButton('Outras Ações','Inclusão Rápida')

		self.oHelper.SetButton('OK')
		
		self.oHelper.SetValue('Nr Documento', '1512201')
		self.oHelper.SetValue('Tipo', 'NFS')
		self.oHelper.SetValue('Série', '1')
		self.oHelper.SetValue('Emissor', '001')

		self.oHelper.SetButton('Salvar')

		self.oHelper.SetValue('Nr Documento', '1512201')
		self.oHelper.SetValue('Valor Docto', '1000', check_value = False)
		self.oHelper.SetValue('Aliq Imp.', '12', check_value = False)

		self.oHelper.SetButton('Salvar')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Dados da Conferência')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()