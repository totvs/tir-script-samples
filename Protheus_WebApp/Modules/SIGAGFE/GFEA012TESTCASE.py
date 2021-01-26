from tir import Webapp
import unittest

class GFEA012(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','03/11/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA012')
		
	def test_GFEA012_CT001(self):

		self.oHelper.AddParameter("MV_CADOMS", "D MG 01", "2", "2", "2")
		self.oHelper.SetParameters()

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Cod Mot/Ajud', '900001')
		self.oHelper.SetValue('Nome        ', 'BINO')
		self.oHelper.SetValue('Pseud/Apelid', 'BINO')
		self.oHelper.SetValue('Tipo        ', '1')
		self.oHelper.SetValue('CPF         ', '12345678912345')
		self.oHelper.SetValue('RG          ', '678941235854879')
		self.oHelper.SetValue('Orgao Exped ', 'SSPSC')
		self.oHelper.SetValue('Mot Situacao', 'MOTORISTA ATIVO')
		self.oHelper.SetValue('Observacoes ', 'TESTE INCLUSAO')
		self.oHelper.ClickFolder('Documentos')
		self.oHelper.SetValue('Nr CNH      ', '12345678912')
		self.oHelper.SetValue('Reg CNH     ', '3131313131')
		self.oHelper.SetValue('Dt Exped CNH', '05/12/2020')
		self.oHelper.SetValue('Dt Venct CNH', '05/12/2025')
		self.oHelper.SetValue('Munici CNH  ', 'JOINVILLE')
		self.oHelper.SetValue('Estado CNH  ', 'SC')
		self.oHelper.SetValue('Cat CNH     ', 'E')
		self.oHelper.SetValue('MOPP        ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Observacoes ', 'TESTE ALTERACAO')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Cod Mot/Ajud', '900002')
		self.oHelper.SetValue('Nome        ', 'PEDRO')
		self.oHelper.SetValue('Pseud/Apelid', 'PEDRO')
		self.oHelper.SetValue('Tipo        ', '2')
		self.oHelper.SetValue('CPF         ', '92345678912345')
		self.oHelper.SetValue('RG          ', '978941235854879')
		self.oHelper.SetValue('Mot Situacao', 'AJUDANTE ATIVO')
		self.oHelper.SetValue('Observacoes ', 'TESTE COPIAR')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900002')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()
		
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()
