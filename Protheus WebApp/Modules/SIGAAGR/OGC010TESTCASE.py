from tir import Webapp
import unittest

class OGC010(unittest.TestCase):
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAAGR','08/10/2019','T1','D MG 01 ','67')		
		inst.oHelper.Program('OGC010')

		inst.oHelper.AddParameter("MV_AGRO002","",".T.",".T.",".T.") #Nova comercializacao		
		inst.oHelper.SetParameters()

	def test_OGC010_CT001(self):
		self.oHelper.SetValue("MV_PAR01", "07/10/2019") #Data Ini
		self.oHelper.SetValue("MV_PAR02", "09/10/2019") #Data Ini
		self.oHelper.SetValue("Take-Up Físico ?", "Ambos") 
		self.oHelper.SetValue("Tipo de Contrato?", "Venda") 
		self.oHelper.SetButton('Ok')
		self.oHelper.ClickGridCell("Contrato", 2)
		self.oHelper.SetButton('Reservar')
		self.oHelper.WaitFieldValue("DXP_SAFRA", "1920")
		self.oHelper.SetButton('Outras Ações', 'Selecionar Fardos')						
		self.oHelper.ClickLabel("Qtd. Disp.")											
		self.oHelper.ClickBox("Bloco", "000005", grid_number=3)									
		self.oHelper.SetButton('Salvar')		
		self.oHelper.ClickFolder("Take - Up")
		self.oHelper.SetValue(field="DXP_CLAINT", value="000001", name_attr=True)
		self.oHelper.SetButton('Confirmar')				
		self.oHelper.SetButton('Fechar')				
		self.oHelper.SetButton('Reservar')
		self.oHelper.CheckResult('TOTBRUTO', user_value="220,00", name_attr=True)		
		self.oHelper.SetButton('Confirmar')				
		self.oHelper.SetButton('Fechar')				
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()