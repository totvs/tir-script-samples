from tir import Webapp
import unittest

class MATA030(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','11/04/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA030')
	
	def test_MATA030_CT133(self):

		cliente = 'FTC133'
		loja = '01'
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.SetValue('A1_COD',cliente)
		self.oHelper.SetValue('A1_LOJA',loja)
		self.oHelper.SetValue('A1_PESSOA','F - Fisica')
		self.oHelper.SetValue('A1_NOME','FAT TIR CT133 MATA030 INCLUSAO')
		self.oHelper.SetValue('A1_NREDUZ','TIR CT133 MATA030')
		self.oHelper.SetValue('A1_END','RUA DAS ORQUIDEAS, 100')
		self.oHelper.SetValue('A1_TIPO','F - Cons.Final')
		self.oHelper.SetValue('A1_EST','SP')
		self.oHelper.SetValue('A1_COD_MUN','50308')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.CheckResult('A1_COD',cliente)
		self.oHelper.CheckResult('A1_LOJA',loja)
		self.oHelper.CheckResult('A1_PESSOA','F - Fisica')
		self.oHelper.CheckResult('A1_NOME','FAT TIR CT133 MATA030 INCLUSAO')
		self.oHelper.CheckResult('A1_NREDUZ','TIR CT133 MATA030')
		self.oHelper.CheckResult('A1_END','RUA DAS ORQUIDEAS, 100')
		self.oHelper.CheckResult('A1_TIPO','F - Cons.Final')
		self.oHelper.CheckResult('A1_EST','SP')
		self.oHelper.CheckResult('A1_COD_MUN','50308')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()