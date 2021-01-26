from tir import Webapp
import unittest

class GFEA015(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','26/06/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA015')

	def test_GFEA015_CT001(self):

		self.oHelper.SetButton('Incluir')
	
		self.oHelper.SetValue('Cod Emitente','1746')
		self.oHelper.SetValue('Nome','GFE - INCLUSAO CLIENTE TIR')
		self.oHelper.SetValue('Nome Fant','CLITIR')
		self.oHelper.SetValue('Nome Abrev','CLITIR')
		self.oHelper.SetValue('Natureza','J')
		self.oHelper.SetValue('Cliente?','1')

		self.oHelper.ClickFolder("Endereco")

		self.oHelper.SetValue('Endereco','RUA CENTRAL, 2000')
		self.oHelper.SetValue('Bairro','CENTRO')
		self.oHelper.SetValue('CEP','89300015')
		self.oHelper.SetValue('Nr Cidade','4209102')
				
		self.oHelper.ClickFolder("Fiscal")

		self.oHelper.SetValue('CNPJ/CPF','21829544000130')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('1746          ')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.CheckResult('Cod Emitente','1746')

		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Nome','GFE - ALTERACAO CLIENTE TIR')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')		

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	def test_GFEA015_CT002(self):

		self.oHelper.SetButton('Incluir')
	
		self.oHelper.SetValue('Cod Emitente','1747')
		self.oHelper.SetValue('Nome','GFE - INCLUSAO TRANSPORTADOR TIR')
		self.oHelper.SetValue('Nome Fant','TRPTIR')
		self.oHelper.SetValue('Nome Abrev','TRPTIR')
		self.oHelper.SetValue('Natureza','J')
		self.oHelper.SetValue('Transp?','1')

		self.oHelper.ClickFolder("Endereco")

		self.oHelper.SetValue('Endereco','RUA CENTRAL, 3000')
		self.oHelper.SetValue('Bairro','CENTRO')
		self.oHelper.SetValue('CEP','89300015')
		self.oHelper.SetValue('Nr Cidade','4209102')
				
		self.oHelper.ClickFolder("Fiscal")

		self.oHelper.SetValue('CNPJ/CPF','08688558000113')

		self.oHelper.ClickFolder("Transportador")

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('1747          ')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.CheckResult('Cod Emitente','1747')

		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Nome','GFE - ALTERACAO TRANSPORTADOR TIR')

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
