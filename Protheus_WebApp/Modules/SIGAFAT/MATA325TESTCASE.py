from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest

class MATA325(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT',DataSystem,'T1','D MG 01 ','05')
		inst.oHelper.Program('MATA325')

	def test_MATA325_CT009(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Data de ?', '01/01/2019')
		self.oHelper.SetValue('Data ate ?', '31/12/2019')
		self.oHelper.SetValue('Filtro ?', 'Categoria')
		self.oHelper.SetValue('Categoria ate ?', 'ZZZ')
		self.oHelper.SetValue('Fornecedor Ate ?', 'ZZZ')
		self.oHelper.SetValue('Loja Ate ?', 'ZZ')
		self.oHelper.SetValue('Tabela de Preço ?', 'API')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('OK')
		self.oHelper.SetValue('AX_CODIGO', 'TIR001')
		self.oHelper.SetValue('AX_DESCRI', 'TESTE TIR')
		self.oHelper.SetValue('AX_DATAINI', '07/08/2019')
		self.oHelper.SetValue('AX_HORAINI', '08:00')
		self.oHelper.SetValue('AX_GRUPFIL', '001')	
		self.oHelper.SetValue("AY_PRODUTO", "FAT001", grid=True, row=1)
		self.oHelper.SetValue("AY_PRCSUG"  , "1,00"	, grid=True, row=1)
		self.oHelper.LoadGrid()		
		self.oHelper.SetButton("Outras Ações", "Produto")
		self.oHelper.SetButton("Sair")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse(f"TIR001")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Cancelar")		
		self.oHelper.CheckResult("AX_CODIGO", 'TIR001')		
		self.oHelper.SetButton("Fechar")		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()