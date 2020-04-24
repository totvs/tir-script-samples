from tir import Webapp
import unittest

class JURA108(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.SetTIRConfig(config_name="user", value="daniel.frodrigues")
		inst.oHelper.SetTIRConfig(config_name="password", value="1")
		inst.oHelper.Setup('SIGAJURI','','T1','D MG 01 ','76')
		inst.oHelper.Program('JURA106')
		inst.oHelper.AddParameter("MV_JHBPESF", "", "1", "", "")
		inst.oHelper.SetParameters()

	def test_JURA108_CT001(self):
		self.oHelper.SetValue("cValor","Contencioso - Fup",name_attr=True)
		self.oHelper.WaitFieldValue("NTA_CTIPO","")
		self.oHelper.SetValue('NTA_CTIPO', '00001')
		self.oHelper.ClickLabel('Pesquisar')
		self.oHelper.ClickGridCell("Código Assunto Jurídico",row=1)
		self.oHelper.ClickLabel('Exportação Personalizada')
		self.oHelper.SetValue("cCmbTabela","000011 - Acordos (NYP001)",name_attr=True)
		self.oHelper.SetButton("Add. Todos >>")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("<< Rem. Todos")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetValue("cCmbTabela","000005 - Follow-ups (NTA001)",name_attr=True)
		self.oHelper.SetValue("cGetSearch","HORA",name_attr=True)
		self.oHelper.SetButton("Pesquisar")
		self.oHelper.SetButton("Adicionar >>")
		self.oHelper.SetValue("cGetSearch","DT FOLLOW-UP",name_attr=True)
		self.oHelper.SetButton("Pesquisar")
		self.oHelper.SetButton("Adicionar >>")
		self.oHelper.SetValue("cGetSearch","NOME DO PARTICI",name_attr=True)
		self.oHelper.SetButton("Pesquisar")
		self.oHelper.SetButton("Adicionar >>")
		self.oHelper.SetButton("Mover para Baixo")
		self.oHelper.SetButton("Mover para Cima")
		self.oHelper.SetValue("cGetRename","Hora F-Up",name_attr=True)
		self.oHelper.SetButton("Renomear")
		self.oHelper.SetButton("<< Remove")
		self.oHelper.SetButton("Filt. Agrup.")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Exportar")
		self.oHelper.SetValue("cGetNewConfig","FOLLOW UP - MULTIPLOS RESPONSAVEIS",name_attr=True)
		self.oHelper.SetButton("Salvar Como")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sair")
		self.oHelper.ClickLabel("Sair")
		self.oHelper.AssertTrue()
		
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
