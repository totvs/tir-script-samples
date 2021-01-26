from tir import Webapp
import unittest

class GTPA008(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA008')

	def test_GTPA008_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('Código', 'GTPAUT')
		'''self.oHelper.SetValue('Matrícula', 'GTP100')'''
		self.oHelper.SetValue('Nome', 'Teste')
		self.oHelper.SetValue('Data Nasc.', '25/09/1991')
		self.oHelper.SetValue('Número RG', '255330935')
		self.oHelper.SetValue('Usuário', '000579')
		self.oHelper.SetValue('Tipo Recurso', '01')
		self.oHelper.SetValue('Agência', 'GTPVAL')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("D MG    GTPAUT", "Filial+código")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue('Local Padrao', 'LOC001')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("D MG    GTPAUT", "Filial+código")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("D MG    GTPAUT", "Filial+código")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
