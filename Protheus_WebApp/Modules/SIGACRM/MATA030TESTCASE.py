from tir import Webapp
import unittest

class MATA030(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','11/04/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA030')
	
	def test_MATA030_CT133(self):

		cliente = 'FTC133'
		loja = '01'
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.SetValue('A1_COD',cliente)
		self.oHelper.SetValue('A1_LOJA',loja)
		self.oHelper.SetValue('A1_PESSOA','F - Fisica')
		self.oHelper.SetValue('A1_NOME','FAT TIR CT133 MATA030 INCLUSAO')
		self.oHelper.SetValue('A1_NREDUZ','TIR CT133 MATA030')
		self.oHelper.SetValue('A1_END','RUA DAS ORQUIDEAS, 100')
		self.oHelper.SetValue('A1_TIPO','F - Cons.Final')
		self.oHelper.SetValue('A1_EST','SP')
		self.oHelper.SetValue('A1_COD_MUN','50308')

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.CheckResult('A1_COD',cliente)
		self.oHelper.CheckResult('A1_LOJA',loja)
		self.oHelper.CheckResult('A1_PESSOA','F - Fisica')
		self.oHelper.CheckResult('A1_NOME','FAT TIR CT133 MATA030 INCLUSAO')
		self.oHelper.CheckResult('A1_NREDUZ','TIR CT133 MATA030')
		self.oHelper.CheckResult('A1_END','RUA DAS ORQUIDEAS, 100')
		self.oHelper.CheckResult('A1_TIPO','F - Cons.Final')
		self.oHelper.CheckResult('A1_EST','SP')
		self.oHelper.CheckResult('A1_COD_MUN','50308')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	def test_MATA030_CT134(self):

		cliente = 'FTU134'
		loja = '01'
		
		self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')

		self.oHelper.SetButton('Alterar')
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.SetValue('A1_PESSOA','J - Juridica')
		self.oHelper.SetValue('A1_NOME','FAT TIR CT134 CT136 MATA030 ALTERACAO OK')
				
		self.oHelper.SetButton('Salvar')

		self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.CheckResult('A1_COD',cliente)
		self.oHelper.CheckResult('A1_LOJA',loja)
		self.oHelper.CheckResult('A1_PESSOA','J - Juridica')
		self.oHelper.CheckResult('A1_NOME','FAT TIR CT134 CT136 MATA030 ALTERACAO OK')
			
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()	

	def test_MATA030_CT135(self):

		cliente = 'FTD135'
		loja = '01'

		self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.CheckResult('A1_COD',cliente)
		self.oHelper.CheckResult('A1_LOJA',loja)

		if self.oHelper.GetValue("A1_COD") == cliente and self.oHelper.GetValue("A1_LOJA") == loja:
			self.oHelper.SetButton('Confirmar')
		else:
			self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()	

	def test_MATA030_CT136(self):

		cliente = 'FTU134'
		loja = '01'
		
		self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Outras Ações','Referencias')
		self.oHelper.SetBranch('D MG 01')

		self.oHelper.ClickFolder('Instituicao')

		self.oHelper.SetValue('AO_NOMINS','CT136',grid=True)
		self.oHelper.SetValue('AO_NOMFUN','CT136 TIR',grid=True)
		self.oHelper.SetValue('AO_OBSERV','TESTE REFERENCIAS CT136 TIR',grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Outras Ações','Referencias')
		self.oHelper.SetBranch('D MG 01')
		
		self.oHelper.CheckResult('A1_COD',cliente)
		self.oHelper.CheckResult('A1_LOJA',loja)
		self.oHelper.CheckResult('AO_NOMINS','CT136',grid=True)
		self.oHelper.CheckResult('AO_NOMFUN','CT136 TIR',grid=True)
		self.oHelper.CheckResult('AO_OBSERV','TESTE REFERENCIAS CT136 TIR',grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()

	def test_MATA030_CT154(self):

		cliente = 'FATU01'
		loja = '01'

		self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetButton("Outras Ações", "Complemento do Cliente")

		self.oHelper.SetValue('AI0_CLIFUN', "2 - Não")
		self.oHelper.SetValue('AI0_STATUS', "00 - credito liberado")

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Salvar')

		self.oHelper.AssertTrue()

	def test_MATA030_CT170(self):

		cliente = 'FTU170'
		loja = '01'
		cgc = '54991972027'

		self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton("Alterar")

		self.oHelper.CheckResult('A1_CGC',cgc)

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	def test_MATA030_CT171(self):
		'''
		CT171 - Acionar a opção do 'Facilitador'
		'''

		self.oHelper.SetButton("Outras Ações", "Facilitador")

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SetButton('X')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()