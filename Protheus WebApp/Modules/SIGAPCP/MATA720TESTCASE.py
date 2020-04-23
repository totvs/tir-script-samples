from tir import Webapp
import unittest

class MATA720(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPCP','23/04/2019','T1','D MG 01 ','10')
		inst.oHelper.Program('MATA720')

	def test_MATA720_001(self):		
		self.oHelper.SetButton('Parâmetros')
		self.oHelper.SetValue('Op Inicial ?','PCP13001001')
		self.oHelper.SetValue('Op Final ?','PCP13201001')
		self.oHelper.SetValue('Data de Entrega de ?','01/01/2019')
		self.oHelper.SetValue('Data de Entrega até ?','31/12/2019')
		self.oHelper.SetValue('Considera já aglut. ?','Nao')
		self.oHelper.SetValue('OP Aglut. Inicial ?','')
		self.oHelper.SetValue('Considera Niveis ?','Nao')
		self.oHelper.SetValue('Atualiza Ped.Venda ?','Nao')
		self.oHelper.SetValue('De  Armazem ?','01')
		self.oHelper.SetValue('Ate Armazem ?','01')
		self.oHelper.SetValue('Produto de ?','PCP_TIR_MATA720_001_PA00000001')
		self.oHelper.SetValue('Produto Ate ?','PCP_TIR_MATA720_001_PA00000001')
		self.oHelper.SetValue('OPs Com Grd/Sem Grd ?','Cons.Tipo Orig')
		self.oHelper.SetValue('Dt. Prev. Fim a Considerar ?','Menor Dt. Fim')
		
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Sim')

		self.oHelper.Program('MATA650')
		self.oHelper.WaitShow("Ordens de Producao")
		self.oHelper.SearchBrowse('D MG 01 PCP_TIR_MATA720_001_PA0000000123042019', 'Filial+produto + Entrega')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('C2_PRODUTO', 'PCP_TIR_MATA720_001_PA00000001')
		self.oHelper.CheckResult('C2_QUANT','30,00')
		self.oHelper.CheckResult('C2_DATPRI','23/04/2019')
		self.oHelper.CheckResult('C2_DATPRF','23/04/2019')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()