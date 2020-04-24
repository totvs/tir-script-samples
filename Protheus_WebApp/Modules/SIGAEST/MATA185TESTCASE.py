from tir import Webapp
import unittest

class MATA185(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('MATA185')		

	def test_MATA185_CT001(self):
		self.oHelper.SearchBrowse("D MG 01 PMS032 01")
		self.oHelper.SetButton('Outras Ações', 'Tipo Baixa')
		self.oHelper.SetValue("Baixar Por ?", "Toda a Pre-Req")
		self.oHelper.SetButton('Ok')	
		self.oHelper.SetButton('Baixar')
		self.oHelper.SetButton('Confirma')
		self.oHelper.ClickCheckBox("Selecionar Todos os Itens",1)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('TM','501')
		self.oHelper.SetButton('Salvar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()