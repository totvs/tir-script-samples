from tir import Webapp
import unittest

class TMSA040(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGATMS','19/06/2019','T1','M SP 01 ','43')
		inst.oHelper.Program('TMSA040')

	#Cenário CT009 - Inclusão de cotação com tipo de veiculo (Automatizado Web)
	def test_TMA040_CT009(self):		
		  
		self.oHelper.AddParameter("MV_TESDR", "", "482")
		self.oHelper.AddParameter("MV_CLIGEN", "", "TMSCLIGE")
		self.oHelper.AddParameter("MV_CDRORI", "", "Q50308")
		self.oHelper.AddParameter("MV_TMSCFEC", "", ".T.")
		self.oHelper.AddParameter("MV_CLICOT", "", ".T.")
		self.oHelper.AddParameter("MV_COTVFEC", "", ".F.")
		self.oHelper.SetParameters()	

		self.oHelper.SetButton('Incluir') 
		self.oHelper.SetBranch('M SP 01') 

		self.oHelper.SetValue('DT4_CODSOL', '000000009')
		self.oHelper.SetValue('DVF_CODPRO', 'TMS_PROGEN', grid=True)
		self.oHelper.SetValue('DVF_CODEMB', 'CX', grid=True)
		self.oHelper.SetValue('DVF_QTDVOL', '10', grid=True)
		self.oHelper.SetValue('DVF_PESO', '100,0000', grid=True)
		self.oHelper.SetValue('DVF_VALMER', '1000,00', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.ClickFolder('Aprovacao')
		self.oHelper.SetValue('DT4_CLIREM', 'TMS010')
		self.oHelper.SetValue('DT4_LOJREM', '01')
		self.oHelper.SetValue('DT4_CLIDES', 'TMS001')
		self.oHelper.SetValue('DT4_LOJDES', '01')

		self.oHelper.ClickFolder('Servico')
		self.oHelper.SetValue('DT4_CDRORI', 'Q38709')
		self.oHelper.SetValue('DT4_CDRDES', 'Q50308')
		self.oHelper.SetValue('DT4_SERTMS', '2')
		self.oHelper.SetValue('DT4_TIPTRA', '1')		
		self.oHelper.ClickBox('Serviço','306')	#Selecionar o documento	
		
		self.oHelper.SetButton('Outras Ações', 'Tipos de Veículo - ') 
		self.oHelper.SetValue('DVT_TIPVEI', '01', grid=True)
		self.oHelper.SetValue('DVT_QTDVEI', '1', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar') 

		cNumCot = self.oHelper.GetValue('DT4_NUMCOT')
		self.oHelper.SetButton('Salvar') 
		self.oHelper.SetButton('Nao')		# Deseja Solicitar Coleta? Não
		self.oHelper.SetButton('Cancelar')	# Fechar tela de nova inclusão.

		self.oHelper.SearchBrowse('M SP 01 M SP 01 '+cNumCot, 'Filial+fil.origem + No.cotacao')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('DT4_NUMCOT', cNumCot)
		self.oHelper.CheckResult('DT4_CODSOL', '000000009')

		self.oHelper.SetButton('Outras Ações', 'Composição do Frete') 
		self.oHelper.ClickGridCell("Composição", row=4)
		self.oHelper.LoadGrid()
		self.oHelper.SetKey('DOWN')	
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		
	#Cenário CT019 - Inclusão de cotação com valor fechado percentual de desconto 25% (Automatizado Web)
	def test_TMA040_CT019(self):
		
		self.oHelper.SetButton('Incluir') 
		self.oHelper.SetBranch('M SP 01')

		self.oHelper.SetValue('DT4_CODSOL', '000000003')
		self.oHelper.SetValue('DVF_CODPRO', 'TMS-DIVERSOS000000000000000000', grid=True)
		self.oHelper.SetValue('DVF_CODEMB', 'CX', grid=True)
		self.oHelper.SetValue('DVF_QTDVOL', '100', grid=True)
		self.oHelper.SetValue('DVF_PESO'  , '15,0000', grid=True)
		self.oHelper.SetValue('DVF_VALMER', '1500,00', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.ClickFolder('Aprovacao')
		self.oHelper.SetValue('DT4_CLIREM', 'TMS001')
		self.oHelper.SetValue('DT4_LOJREM', '01')
		self.oHelper.SetValue('DT4_CLIDES', 'TMS002')
		self.oHelper.SetValue('DT4_LOJDES', '01')

		self.oHelper.ClickFolder('Servico')
		self.oHelper.SetValue('DT4_CDRORI', 'Q50308')
		self.oHelper.SetValue('DT4_CDRDES', 'Q18800')
		self.oHelper.SetValue('DT4_SERTMS', '2')
		self.oHelper.SetValue('DT4_TIPTRA', '1')

		self.oHelper.SetKey('F5')	# Atualiza a composicao do frete
		self.oHelper.SetKey('F6')	# Valor Fechado

		self.oHelper.ClickFolder('% Desconto')
		self.oHelper.SetValue(field="25 %", value=True)
		#self.oHelper.SetValue(field='RADIO9012', value=True, name_attr=True, position=4)		
		self.oHelper.SetButton('Salvar') 
	
		cNumCot = self.oHelper.GetValue('DT4_NUMCOT')
		self.oHelper.SetButton('Salvar') 
		self.oHelper.SetButton('Nao') 		# Deseja Solicitar Coleta? Não
		self.oHelper.SetButton('Cancelar')  # Fechar tela de nova inclusão.

		self.oHelper.SearchBrowse('M SP 01 M SP 01 '+cNumCot, 'Filial+fil.origem + No.cotacao')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('DT4_NUMCOT', cNumCot)		# Verifica a cotação incluida

		# Visualiza o valor do componente após alteração do valor fechado, se está conforme a alteração.
		self.oHelper.SetButton('Outras Ações', 'Composição do Frete - ')  
		self.oHelper.ClickGridCell("Valor + Imposto", row=6)
		self.oHelper.LoadGrid()
		self.oHelper.SetKey('DOWN')	
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
	
	#Cenário CT041 - Cópia de Cotação (Automatizado Web)
	def test_TMA040_CT041(self):
		
		self.oHelper.SearchBrowse("M SP 01 M SP 01 000003")
		self.oHelper.SetButton('Outras Ações', 'Copiar')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Nao')		# Deseja Solicitar Coleta? Não
		self.oHelper.AssertTrue()
		

	#Cenário CT051 - Visualização de Cotação (Automatizado Web)
	def test_TMA040_CT051(self):

		self.oHelper.SearchBrowse("M SP 01 M SP 01 000009")
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()
		

	#Cenário CT037 - Cancelamento de Cotação (Automatizado Web)
	def test_TMA040_CT037(self):
 		
		self.oHelper.AddParameter("MV_COTVFEC", "", ".F.")
		self.oHelper.SetParameters()	

		self.oHelper.SearchBrowse("M SP 01 M SP 01 000020")
		self.oHelper.SetButton('Outras Ações', 'Cancelar')
		self.oHelper.ClickFolder("Cancelamento")
		self.oHelper.SetValue('DT4_DATCAN','19/06/2019')
		self.oHelper.SetValue('DT4_OBSCAN','Cancelamento de cotação como teste automático.')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
		
	
	# Cenário CT026 - Inclusão de cotação com regras de restrições com produtos diferentes (Automatizado Web)
	def test_TMA040_CT026(self):

		self.oHelper.SetButton('Incluir') 
		self.oHelper.SetBranch('M SP 01')

		self.oHelper.SetValue('DT4_CODSOL', '000000003')
			
		self.oHelper.SetValue('DVF_CODPRO', 'TMS-DIVERSOS000000000000000000', grid=True, row=1)
		self.oHelper.SetValue('DVF_CODEMB', 'CX', grid=True, row=1)
		self.oHelper.SetValue('DVF_QTDVOL', '20', grid=True, row=1)
		self.oHelper.SetValue('DVF_PESO'  , '1,0000', grid=True, row=1)
		self.oHelper.SetValue('DVF_VALMER', '50,00', grid=True, row=1)
		self.oHelper.LoadGrid()	
		self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
		self.oHelper.LoadGrid()	

		self.oHelper.SetValue('DVF_CODPRO', 'TMS_PROGEN', grid=True, row=2)
		self.oHelper.SetValue('DVF_CODEMB', 'CX', grid=True, row=2)
		self.oHelper.SetValue('DVF_QTDVOL', '20', grid=True, row=2)
		self.oHelper.SetValue('DVF_PESO'  , '1,0000', grid=True, row=2)
		self.oHelper.SetValue('DVF_VALMER', '50,00', grid=True, row=2)
		self.oHelper.LoadGrid()		

		self.oHelper.ClickFolder('Aprovacao')
		self.oHelper.SetValue('DT4_CLIREM', 'TMS001')
		self.oHelper.SetValue('DT4_LOJREM', '01')
		self.oHelper.SetValue('DT4_CLIDES', 'TMS002')
		self.oHelper.SetValue('DT4_LOJDES', '01')

		self.oHelper.ClickFolder('Servico')
		self.oHelper.SetValue('DT4_CDRORI', 'Q50308')
		self.oHelper.SetValue('DT4_CDRDES', 'Q18800')
		self.oHelper.SetValue('DT4_SERTMS', '2')
		self.oHelper.SetValue('DT4_TIPTRA', '1')
		self.oHelper.ClickBox('Serviço','306')	#Selecionar o documento	

		cNumCot = self.oHelper.GetValue('DT4_NUMCOT')
		self.oHelper.SetButton('Salvar') 
		self.oHelper.SetButton('Fechar') 
		self.oHelper.SetButton('Nao') 

		self.oHelper.SearchBrowse('M SP 01 M SP 01 '+cNumCot, 'Filial+fil.origem + No.cotacao')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('DT4_NUMCOT', cNumCot)		
		self.oHelper.CheckResult('DT4_CODSOL', '000000003')
		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()
		self.oHelper.TearDown()
	
	# Cenário CT040 - Retomar Cotação
	def test_TMA040_CT040(self):

		self.oHelper.SearchBrowse('M SP 01 M SP 01 000004')
		self.oHelper.SetButton('Outras Ações', 'Retomar')
		self.oHelper.SetButton('Sim')
		self.oHelper.SetValue('nQtdDias', '10', name_attr=True)
		self.oHelper.SetButton('Ok')
	
		self.oHelper.AssertTrue()
	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

