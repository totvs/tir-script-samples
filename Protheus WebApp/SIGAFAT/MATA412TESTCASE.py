from tir import Webapp
import unittest
import time

class MATA412(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','02/09/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA412')

	#CT004 - TIR - Visualizar as Legendas
	def test_MATA412_CT001(self):
		self.oHelper.SetButton('Outras Ações', 'Legenda')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	#CT005 - TIR - Gerar Pedido de Venda a partir de uma Programação de Entrega
	def test_MATA412_CT002(self):
		self.oHelper.SearchBrowse("D MG 01 000000005")
		self.oHelper.SetButton('Outras Ações', 'Gerar Pedido de Venda')
		self.oHelper.WaitProcessing('Aguarde, gerando o Pedido de Venda.')
		time.sleep(5)

		self.oHelper.SearchBrowse("D MG 01 000000005")
		self.oHelper.SetButton('Outras Ações', 'Visualizar')
		time.sleep(5)
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	#CT007 - TIR - Cancelar pedido de venda gerado pela Programação de Entrega
	def test_MATA412_CT003(self):
		self.oHelper.SearchBrowse("D MG 01 000000006")
		self.oHelper.SetButton('Outras Ações', 'Cancelar Pedido de Venda')
		self.oHelper.WaitProcessing('Aguarde, excluindo Pedido de Venda.')
		time.sleep(5)

		self.oHelper.SearchBrowse("D MG 01 000000006")
		self.oHelper.SetButton('Outras Ações', 'Visualizar')
		time.sleep(5)
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	#CT008 - TIR - Desmembrar itens de uma Programação de Entrega
	def test_MATA412_CT004(self):
		self.oHelper.SearchBrowse("D MG 01 000000007")
		self.oHelper.SetButton('Alterar')
		time.sleep(5)
		self.oHelper.SetButton('Outras Ações', 'Desmembrar item')

		self.oHelper.SetValue('Tipo Entrega:', '1 - Firme')
		self.oHelper.SetValue('Quantidade:', '2,00')
		self.oHelper.SetValue('Data Entrega:', "02/09/2019")
		self.oHelper.SetButton('Desmembrar')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	#CT009 - TIR - Incluir: Opção Inserir TES
	def test_MATA412_CT005(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("D MG 01 ")
		self.oHelper.SetValue('D0_CLIENTE', 'FAT412')
		self.oHelper.SetValue('D0_LOJA', '01')
		self.oHelper.SetValue('D0_PEDCLI', 'CT009')

		self.oHelper.SetValue('DX_PRODUTO', 'FAT000000000000000000000000001', grid=True, grid_number=1,row=1 )
		self.oHelper.SetValue('DX_QUANT', '2,00', grid=True, grid_number=1,row=1)
		self.oHelper.LoadGrid()
		time.sleep(5)

		self.oHelper.SetButton('Outras Ações', 'Inserir TES')
		self.oHelper.SetValue('Tipo Saída', '501')
		self.oHelper.SetButton('Inserir TES')
		self.oHelper.SetButton('Confirmar')


		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()