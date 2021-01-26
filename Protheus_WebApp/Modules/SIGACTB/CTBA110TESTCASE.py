from tir import Webapp
import unittest

class CTBA110(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGACTB','15/06/2015','T1','D MG 01 ','01')
		inst.oHelper.Program('CTBA110') 
		inst.oHelper.AddParameter("MV_SEGOFI","" , "1")
		inst.oHelper.SetParameters() 

	def test_CTBA110_CT001(self):
        
		#Browse
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("D MG 01 ")
		#Cabeçalho
		self.oHelper.SetValue("Codigo", "CT")
		self.oHelper.SetValue("Descricao", "CONTROLE DIARIO TIR CT01")
		
		#Grid
		self.oHelper.SetValue("Radical", "01", grid=True , row=1)
		self.oHelper.SetValue("Seq. Inicial", "000001", grid=True , row=1)
		self.oHelper.SetValue("Descricao", "LINHA 1", grid=True , row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Salvar")

		#Fechar tela de inclusão que será aberta
		self.oHelper.SetButton("Cancelar")
		
		#Conferência
		self.oHelper.SearchBrowse("D MG 01 CT")
		self.oHelper.SetButton("Visualizar")

		self.oHelper.CheckResult("CVL_COD", "CT", name_attr=True)
		self.oHelper.CheckResult("CVL_DESCR", "CONTROLE DIARIO TIR CT01", name_attr=True)

		self.oHelper.AssertTrue()

		self.oHelper.RestoreParameters()		


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()