from tir import Webapp
import unittest

class CRMA980(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		
		inst.oHelper.Setup('SIGAFAT','18/04/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA030')
	
	def test_CRMA980_CT137(self):

		cliente = 'FTC137'
		loja = '01'
		
		self.oHelper.AddParameter("MV_MVCSA1","D MG 01",".T.",".T.",".T.")
		self.oHelper.SetParameters()
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.SetValue('A1_COD',cliente)
		self.oHelper.SetValue('A1_LOJA',loja)
		self.oHelper.SetValue('A1_PESSOA','F - Fisica')
		self.oHelper.SetValue('A1_NOME','FAT TIR CT137 CRMA980 INCLUSAO')
		self.oHelper.SetValue('A1_NREDUZ','TIR CT137 CRMA980')
		self.oHelper.SetValue('A1_END','RUA DAS ROSAS, 100')
		self.oHelper.SetValue('A1_TIPO','F - Cons.Final')
		self.oHelper.SetValue('A1_EST','SP')
		self.oHelper.SetValue('A1_COD_MUN','50308')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.CheckResult('A1_COD',cliente)
		self.oHelper.CheckResult('A1_LOJA',loja)
		self.oHelper.CheckResult('A1_PESSOA','F - Fisica')
		self.oHelper.CheckResult('A1_NOME','FAT TIR CT137 CRMA980 INCLUSAO')
		self.oHelper.CheckResult('A1_NREDUZ','TIR CT137 CRMA980')
		self.oHelper.CheckResult('A1_END','RUA DAS ROSAS, 100')
		self.oHelper.CheckResult('A1_TIPO','F - Cons.Final')
		self.oHelper.CheckResult('A1_EST','SP')
		self.oHelper.CheckResult('A1_COD_MUN','50308')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()