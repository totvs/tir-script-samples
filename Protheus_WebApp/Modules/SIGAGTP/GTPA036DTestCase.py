from tir import Webapp
import unittest

class GTPA036D(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "05/08/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA036')

	def test_GTPA036D_CT001(self):
                self.oHelper.SetButton('Avançar')
                self.oHelper.ClickLabel("Arquivo Flash (exportação)")
                self.oHelper.ClickLabel("Layout: FS420")
                self.oHelper.SetButton('Avançar')
                '''self.oHelper.ScrollGrid(column='Descrição', match_value='AG. IMPORTACAO DARUMA', grid_number=1)'''
                self.oHelper.ClickGridCell("", row=1, grid_number=1)
                self.oHelper.ClickBox("", contents_list='', select_all=False, grid_number=1)
                self.oHelper.SetButton('Concluir')
                '''self.oHelper.WaitShow("Processando arquivos")
                self.oHelper.WaitHide("Processando arquivos")'''
                self.oHelper.SetButton('Fechar')
                self.oHelper.SetButton('Fechar')
                self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
