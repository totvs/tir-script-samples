from tir import Webapp
import unittest
import time

class WMSA332(unittest.TestCase):
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAWMS", "10/12/2020", "T1", "M SP 01", "42")
		inst.oHelper.Program("WMSA332")
		
	def test_WMSA332_CT001(self):

		self.oHelper.SetValue('Serviço De','')
		self.oHelper.SetValue('Serviço Até','ZZZ')
		self.oHelper.SetValue('Data De','01/01/2000')
		self.oHelper.SetValue('Data Até','31/12/2050')
		self.oHelper.SetValue('Carga De','')
		self.oHelper.SetValue('Carga Até','ZZZZZZ')
		self.oHelper.SetValue('Doct.Conferência Recebt.De ?','')
		self.oHelper.SetValue('Doct.Conferência Recebt.Até ?','ZZZZZZ')
		self.oHelper.SetValue('Documento De ?','')
		self.oHelper.SetValue('Documento Até ?','ZZZZZZZZZ')
		self.oHelper.SetValue('Armazém De ?','')
		self.oHelper.SetValue('Armazém Até ?','ZZ')
		self.oHelper.SetValue('Produto De ?','')
		self.oHelper.SetValue('Produto Até ?','ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')
		self.oHelper.SetValue('Filtrar Finalizados ?','Não')
		self.oHelper.SetValue('Atualiza Autom.Tela ?','Sem Refresh')
		self.oHelper.SetValue('Estorna Serviço Automático ?','Não')
		self.oHelper.SetValue('Cliente/Fornec De ?','')
		self.oHelper.SetValue('Cliente/Fornec Até ?','ZZZZZZ')
		self.oHelper.SetValue('Loja De ?','')
		self.oHelper.SetValue('Loja Até ?','ZZ')
		self.oHelper.SetValue('Mapa de Separação ?','')
		self.oHelper.SetButton('OK')

		self.oHelper.SetButton('Outras Ações','Recurso Humano')
		self.oHelper.SetValue('Rec. Humano','000300')
		self.oHelper.ClickGridHeader(column = 1 , grid_number =  1)
		self.oHelper.ClickBox('Documento','WMS000114')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('X')
		
		self.oHelper.AssertTrue()
		
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
		
if __name__ == "__main__":
	unittest.main()
