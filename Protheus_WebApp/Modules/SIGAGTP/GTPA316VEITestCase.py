from tir import Webapp
import unittest

class GTPA316VEI(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "17/08/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA316VEI')

	def test_GTPA316VEI_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('G6V_RECURS', 'GTPVEIC01')
		self.oHelper.ClickGridCell("Tp Documento", row=1)
		self.oHelper.SetValue('Tp Documento', '001', grid=True, grid_number=1, name_attr=True)
		self.oHelper.LoadGrid()
		self.oHelper.ClickGridCell("Dt. Inicial", row=1)
		self.oHelper.SetValue('Dt. Inicial', '17/08/2020', grid=True, grid_number=1, name_attr=True)	
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
