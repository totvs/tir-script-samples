from tir import Webapp
import time
import unittest

class MATA440(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','24/04/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA440')


	def test_MATA440_002(self):

		pedido = 'FAT232'
		
		self.oHelper.AddParameter("MV_ESTADO","D MG 01","AL","AL","AL")#Parametro de ultima depreciaÃƒÂ§ÃƒÂ£o 
		self.oHelper.SetParameters()#Realizando a mudanÃƒÂ§a caso seja diferente
		
		self.oHelper.SearchBrowse(f'D MG 01 {pedido}', 'Filial+numero')

		self.oHelper.SetButton('Liberar')

		self.oHelper.SetValue("Qtd.Liberada", "1,00", grid=True)
		self.oHelper.LoadGrid()		
		'''	
		self.oHelper.SetFocus('Qtd.Liberada', grid_cell = True)
		self.oHelper.SetKey('F4')
		self.oHelper.SetButton('Voltar')
		self.oHelper.SetKey('ENTER')
		'''

		self.oHelper.SetButton('Salvar')

		self.oHelper.SearchBrowse(f'D MG 01 {pedido}', 'Filial+numero')
		self.oHelper.SetButton('Liberar')
		self.oHelper.CheckResult("Qtd.Liberada", "9,00", grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Cancelar")
		
		self.oHelper.RestoreParameters()
		
		self.oHelper.AssertTrue()

	def test_MATA440_003(self):

		pedido = 'FAT233'

		self.oHelper.SetButton('Automatico')
		self.oHelper.SetBranch("D MG 01")

		self.oHelper.SetValue("Pedido de ?","FAT233")
		self.oHelper.SetValue("Pedido ate ?","FAT233")
		self.oHelper.SetValue("Cliente de ?","FAT001")
		self.oHelper.SetValue("Cliente ate ?","FAT001")
		self.oHelper.SetValue("Data Entrega de ?","01/01/2011")
		self.oHelper.SetValue("Data Entrega ate ?","01/01/2099")
		self.oHelper.SetValue("Loja De ?","01")
		self.oHelper.SetValue("Loja Até ?","01")

		self.oHelper.SetButton("OK") 
		self.oHelper.SetButton("OK")  

		self.oHelper.SearchBrowse(f'D MG 01 {pedido}', 'Filial+numero')
		self.oHelper.SetButton('Liberar')
		self.oHelper.CheckResult("Qtd.Liberada", "0,00", grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()

	def test_MATA440_004(self):

		pedido = 'FAT234'

		self.oHelper.SearchBrowse(f'D MG 01 {pedido}', 'Filial+numero')
		self.oHelper.SetButton('Liberar')		
		
		self.oHelper.SetFocus('Sub-Lote', grid_cell = True)
		self.oHelper.SetKey('F4')
		time.sleep(20)
		self.oHelper.SetButton('Ok')
		time.sleep(20)
		self.oHelper.SetKey('ENTER')

		self.oHelper.SetButton('Salvar')

		self.oHelper.SearchBrowse(f'D MG 01 {pedido}', 'Filial+numero')
		self.oHelper.SetButton('Liberar')
		self.oHelper.CheckResult("Qtd.Liberada", "0,00", grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()