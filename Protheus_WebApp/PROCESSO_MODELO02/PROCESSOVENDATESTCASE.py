from tir import Webapp
import unittest

class PROCESSOVENDA(unittest.TestCase):

	cliente = '00000D'
	loja = '01'
	produto = '00000000000000000000000000000D'
	pedido = '00000D'

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','11/04/2019','T1','D MG 01')
	
	def test_MATA030_001(self):

		self.oHelper.Program('MATA030')
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.SetValue('A1_COD', self.cliente)
		self.oHelper.SetValue('A1_LOJA', self.loja)
		self.oHelper.SetValue('A1_PESSOA','F - Fisica')
		self.oHelper.SetValue('A1_NOME','MATA030 001')
		self.oHelper.SetValue('A1_NREDUZ','MATA030 001')
		self.oHelper.SetValue('A1_END','RUA DAS ORQUIDEAS, 100')
		self.oHelper.SetValue('A1_TIPO','F - Cons.Final')
		self.oHelper.SetValue('A1_EST','SP')
		self.oHelper.SetValue('A1_COD_MUN','50308')
		self.oHelper.ClickFolder('Adm/Fin.')
		self.oHelper.SetValue('A1_NATUREZ', '000002')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SearchBrowse(f'D MG    {self.cliente+self.loja}', key=1, index=True)
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.CheckResult('A1_COD', self.cliente)
		self.oHelper.CheckResult('A1_LOJA', self.loja)
		self.oHelper.CheckResult('A1_PESSOA','F - Fisica')
		self.oHelper.CheckResult('A1_NOME','MATA030 001')
		self.oHelper.CheckResult('A1_NREDUZ','MATA030 001')
		self.oHelper.CheckResult('A1_END','RUA DAS ORQUIDEAS, 100')
		self.oHelper.CheckResult('A1_TIPO','F - Cons.Final')
		self.oHelper.CheckResult('A1_EST','SP')
		self.oHelper.CheckResult('A1_COD_MUN','50308')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('X')

		self.oHelper.AssertTrue()

	def test_MATA010_001(self):

		self.oHelper.Program('MATA010')
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("D MG 01 ")
		self.oHelper.SetValue("B1_COD", self.produto)
		self.oHelper.SetValue("B1_DESC", 'PRODUTO TESTE')
		self.oHelper.SetValue("B1_TIPO",'PA')
		self.oHelper.SetValue("B1_UM",'UN')
		self.oHelper.SetValue("B1_LOCPAD",'01')
		self.oHelper.SetValue("B1_LOCALIZ",'S')
		self.oHelper.SetValue("B1_RASTRO",'L')

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Não")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SearchBrowse(f"D MG 01 {self.produto}", key=1, index=True)

		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B1_COD", self.produto)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton('X')
        
		self.oHelper.AssertTrue()

	def test_MATA410_001(self):

		self.oHelper.Program('MATA410')
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("D MG 01 ")
		self.oHelper.SetValue("C5_NUM", self.pedido)
		self.oHelper.SetValue("C5_TIPO","N")
		self.oHelper.SetValue("C5_CLIENTE", self.cliente)
		self.oHelper.SetValue("C5_LOJACLI", self.loja)
		self.oHelper.SetValue("C5_CONDPAG","003")
		self.oHelper.SetValue("Produto", self.produto, grid=True)
		self.oHelper.SetValue("Quantidade", "1,00", grid=True)
		self.oHelper.SetValue("C6_PRCVEN", "10,00", grid=True)
		self.oHelper.SetValue("C6_TES", "503", grid=True)
		self.oHelper.SetKey('DOWN', grid=True)
		self.oHelper.SetValue("Produto", self.produto, grid=True)
		self.oHelper.SetValue("Quantidade", "1,00", grid=True)
		self.oHelper.SetValue("C6_PRCVEN", "10,00", grid=True)
		self.oHelper.SetValue("C6_TES", "503", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SearchBrowse(f'D MG 01 {self.pedido}, "Filial+numero')
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("C5_NUM", self.pedido)
		self.oHelper.CheckResult("C5_TIPO","N")
		self.oHelper.CheckResult("C5_CLIENTE", self.cliente)
		self.oHelper.CheckResult("C5_CONDPAG","003")
		self.oHelper.CheckResult("Produto", self.produto, grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()