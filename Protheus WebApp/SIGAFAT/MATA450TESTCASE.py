from tir import Webapp
import unittest

class MATA450(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','17/07/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA450')

	#CT001 - TIR - Análise de Crédito de Pedido Manual - Liberação por item - Opção OK
	def test_MATA450_CT001(self):

		self.oHelper.SetValue('Somente Bloqueados ?', 'Sim')
		self.oHelper.SetButton('Ok')
		self.oHelper.SearchBrowse("D MG 01 FAT175")
		self.oHelper.SetButton('Manual')
		self.oHelper.SetButton('Ok')
		self.oHelper.SearchBrowse("D MG 01 FAT175")
		self.oHelper.SetButton('Manual')
		self.oHelper.SetButton('Pedido')
		pedido = self.oHelper.GetValue("C5_NUM")
		if pedido == 'FAT175':
			self.oHelper.AssertFalse()
		else:
			self.oHelper.SetButton('Cancelar')
			self.oHelper.SetButton('Estoque')
			self.oHelper.SetButton('Ok')
			self.oHelper.SetButton('Cancelar')
			self.oHelper.AssertTrue()

	#CT002 - TIR - Análise de crédito automática com cliente de risco B
	def test_MATA450_CT002(self):

		self.oHelper.SetButton('Automatica')
		self.oHelper.SetValue('Pedido de ?', 'FTI02B')
		self.oHelper.SetValue('Pedido ate ?', 'FTI02B')
		self.oHelper.SetValue('Cliente de ?', 'FAT500')
		self.oHelper.SetValue('Cliente ate ?', 'FAT500')
		self.oHelper.SetValue('Data de Entrega de ?', '20/08/2019')
		self.oHelper.SetValue('Data de Entrega ate ?', '20/08/2019')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Sim')
		self.oHelper.SearchBrowse("D MG 01 FTI02B")
		self.oHelper.SetButton('Manual')
		self.oHelper.SetButton('Pedido')
		pedido = self.oHelper.GetValue("C5_NUM")
		if pedido == 'FTI02B':
			self.oHelper.AssertFalse()
		else:
			self.oHelper.SetButton('Cancelar')
			self.oHelper.SetButton('Cancelar')
			self.oHelper.RestoreParameters()
			self.oHelper.AssertTrue()

	#CT003 - TIR - Análise de Crédito de Pedido de Vendas - Opção: Legenda
	def test_MATA450_CT003(self):

		self.oHelper.AddParameter("MV_RISCOB","D MG 01","30","30","30")
		self.oHelper.SetParameters()

		self.oHelper.SetValue('Somente Bloqueados ?', 'Sim')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Outras Ações', 'Legenda')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	#CT004 - TIR - Análise de Crédito de Pedido Manual - Liberação por pedido - Opção: Lib. Todos
	def test_MATA450_CT004(self):

		self.oHelper.SearchBrowse("D MG 01 FAT177")
		self.oHelper.SetButton('Manual')
		self.oHelper.SetButton('Lib.Todos')
		self.oHelper.SearchBrowse("D MG 01 FAT177")
		self.oHelper.SetButton('Manual')
		self.oHelper.SetButton('Pedido')
		pedido = self.oHelper.GetValue("C5_NUM")
		if pedido == 'FAT177':
			self.oHelper.AssertFalse()
		else:
			self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()