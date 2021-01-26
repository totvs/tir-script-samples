from tir import Webapp
import unittest

class TMSA070(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGATMS','11/06/2020','T1','M SP 03 ','43')
		inst.oHelper.Program('TMSA070')  		

	def test_TMSA070_CT005(self): #Inclusão
		  
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 01')

		self.oHelper.SetValue('DG_CODDES','100100',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('DG_CODVEI','TMS001',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('DG_FILORI','M SP 01',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('DG_VIAGEM','000001',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('DG_CONTA','1010101001',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('DG_COND','001',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('DG_VALCOB','1000,21',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('DG_SEQMOV','001',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('DG_CODCAR','000001',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('DG_SEQCAR','01',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('DG_TIPUSO','1',grid=True,grid_number=1,row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()
		
	def test_TMSA070_CT006(self): #Visualizar

		self.oHelper.SearchBrowse("M SP 01 000000003100100")

		self.oHelper.SetButton("Visualizar")
		
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()
		
	def test_TMSA070_CT007(self): #Estornar Baixa

		self.oHelper.SearchBrowse("M SP 01 000000003100100")

		self.oHelper.SetButton("Outras Ações", "Estorna Baixa")

		self.oHelper.SetButton('Confirmar')		
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	def test_TMSA070_CT008(self): #Excluir

		self.oHelper.SearchBrowse("M SP 01 000000003100100")

		self.oHelper.SetButton("Outras Ações", "Excluir")

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()
	
	def test_TMSA070_CT009(self): #Legenda

		self.oHelper.SetButton("Outras Ações", "Legenda")
		
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

