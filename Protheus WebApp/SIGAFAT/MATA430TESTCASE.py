from tir import Webapp
import unittest
import time

class MATA430(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','03/07/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA430')

	#CT005 - TIR - Controle de Reservas - Opção: Legenda
	def test_MATA430_CT001(self):

		self.oHelper.SetButton('Outras Ações','LeGenda')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	#CT006 - TIR - Controle de Reservas - Opção: Depurar
	def test_MATA430_CT002(self):

		self.oHelper.SetButton('Outras Ações','Depurar')
		self.oHelper.SetButton("Ok")
		self.oHelper.AssertTrue()

	#CT007 - TIR - Acessar F4 através do campo C0_QUANT
	def test_MATA430_CT003(self):

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue("C0_PRODUTO", "CT007MATA430", grid=True,row=1)
		self.oHelper.SetValue("C0_QUANT", "1,00", grid=True,row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetKey("F4")
		time.sleep(5)
		self.oHelper.SetButton('x')   
		time.sleep(5)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sair da Página")

		self.oHelper.AssertTrue()

	#CT008 - TIR - Acessar F4 através do campo C0_LOCALIZ
	def test_MATA430_CT004(self):

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue("C0_PRODUTO", "CT008MATA430", grid=True,row=1)
		self.oHelper.SetValue("C0_QUANT", "1,00", grid=True,row=1)
		self.oHelper.SetValue("C0_LOCALIZ", "END K001", grid=True,row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetKey("F4")
		time.sleep(5)
		self.oHelper.SetButton('x')   
		time.sleep(5)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sair da Página")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()