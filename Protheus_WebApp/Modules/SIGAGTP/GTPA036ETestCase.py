from tir import Webapp
import unittest

class GTPA036E(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "05/08/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA036')

	def test_GTPA036E_CT001(self):
                self.oHelper.SetButton('Avançar')
                self.oHelper.ClickLabel("Arquivo não formatado")
                self.oHelper.SetButton('Avançar')
                self.oHelper.SetValue('XXX_DATADE', '02/08/2020')
                self.oHelper.SetValue('XXX_DATATE', '07/08/2020')
                self.oHelper.ScrollGrid(column='Agência', match_value='000048', grid_number=1)
                '''self.oHelper.ClickGridCell("", row=2, grid_number=1)'''
                self.oHelper.ClickBox("", contents_list='', select_all=False, grid_number=1)
                self.oHelper.SetButton('Concluir')
                self.oHelper.SetButton('Fechar')
                self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
