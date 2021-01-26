from datetime import date
import unittest
from tir import Webapp
from tir.technologies.apw_internal import ApwInternal
from datetime import datetime
import time

DateSystem = datetime.today().strftime('%d/%m/%Y')
DateVal = datetime(2120, 5, 17)
DateTime = datetime.now()
Mes = DateTime.month
Ano = DateTime.year

# -------------------------------------------------------------------
# /*/{Protheus.doc} PLSA260TestCase
# TIR - Casos de testes da rotina Odontologica 

# @author v.alves
# @since 16/10/2020
# @version 12
# -------------------------------------------------------------------


class PLSA260(unittest.TestCase):
    #-------------------------------------------
    # Inicialiação setUpClass para TIR - PLSA260
    #-------------------------------------------
    @classmethod
    def setUpClass(self):
        # inst.oHelper = ApwInternal("config.json")
        # inst.oHelper.Setup()
        self.oHelper = Webapp()
        self.oHelper.SetTIRConfig(config_name="User", value="admin")
        self.oHelper.SetTIRConfig(config_name="Password", value="1234")
        self.oHelper.Start()
        self.oHelper.Setup("SIGAPLS", DateSystem, "T1", "M SP 01 ", "33")
        self.oHelper.Program('PLSA174')

    #-------------------------------------------
    # Inicio dos casos de testes TIR - PLSA260 
    #-------------------------------------------

# -------------------------------------------------------------------
    # /*/{Protheus.doc} TEST_PLSA260_PL001
    # TIR - Casos de testes da rotina Grupo Familiar
    # Incluindo Beneficiário

    # @author v.alves
    # @since 27/05/2020
    # @version 12
    # # # -------------------------------------------------------------------
    def test_PLSA260_PL001(self):

        #Dados para teste
        cpf     = '71289920818'
        cdPlan  = '0007'
        vers    = '001' 

        self.oHelper.SetValue('Tipo ?', 'Pessoa Juridica')
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Selecionar')
        self.oHelper.SetBranch("M SP 01")
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch("M SP 01")
        self.oHelper.ClickFolder('Dados do Plano')
        self.oHelper.SetValue('BA3_CODPLA', cdPlan)
        self.oHelper.SetValue('BA3_VERSAO', vers)
        self.oHelper.ClickFolder('Cobranca')
        self.oHelper.SetValue('BA3_COBNIV', '1 - Sim')
        self.oHelper.SetValue('BA3_VENCTO', '15')
        self.oHelper.SetKey('F5')
        self.oHelper.SetValue('BA1_CPFUSR', cpf)
        self.oHelper.SetValue('BA1_DATINC', DateSystem)
        self.oHelper.SetValue('BA1_DATCAR', DateSystem)
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('X')
        self.oHelper.SetButton('X')
        self.oHelper.AssertTrue()

    # -------------------------------------------------------------------
    # /*/{Protheus.doc} TEST_PLSA260_PL002
    # TIR - Casos de testes da rotina Grupo Familiar
    # Incluindo Beneficiário no tipo de pessoa Física

    # @author r.soares
    # @since 12/11/2020
    # @version 12
    # # # -------------------------------------------------------------------
    def test_PLSA260_PL002(self):

        cpf     = '71289920818'
        cdPlan  = '0007'
        vers    = '001' 
        vcto    = '15'
        codCli  = '000001'
        nature  = '001'
        chave = "M SP    00010022"

        self.oHelper.Program('PLSA174')

        #Dados para teste
        self.oHelper.SetValue('Tipo ?', 'Pessoa Fisica')
        self.oHelper.SetButton('Ok')
			
        self.oHelper.SearchBrowse(f'{chave}', key=1, index=True)
        self.oHelper.SetButton('Selecionar')
        self.oHelper.SetBranch("M SP 01")
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch("M SP 01")
        self.oHelper.ClickFolder('Dados do Plano')
        self.oHelper.SetValue('BA3_CODPLA', cdPlan)
        self.oHelper.SetValue('BA3_VERSAO', vers)
        self.oHelper.ClickFolder('Cobranca')
        self.oHelper.SetValue('BA3_VENCTO', vcto)
        self.oHelper.SetValue('BA3_CODCLI', codCli)
        self.oHelper.SetValue('BA3_NATURE', nature)
        self.oHelper.SetKey('F5')
        self.oHelper.SetValue('BA1_CPFUSR', cpf)
        self.oHelper.SetValue('BA1_DATINC', DateSystem)
        self.oHelper.SetValue('BA1_DATCAR', DateSystem)
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Sim')
        self.oHelper.AssertTrue()
    
    #//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA260_PL003

	# Teste 03 - Bloqueio de Família
	
	# @author r.soares
	# @since 12/11/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
    def test_PLSA260_PL003(self):
		
		# Dados para o teste
        chave = "M SP    71289920818"
        chaveDep = 'M SP    07483982012'

        # Busca do Dependente
			
        self.oHelper.SearchBrowse(f'{chaveDep}', key=4, index=True)
        self.oHelper.SetButton('Visualizar')
        self.oHelper.CheckResult('BA3_CODEMP', '0022')
        self.oHelper.SetButton('Confirmar')    
        
        #Bloqueando o Dependente
        self.oHelper.SetButton('Outras Ações',sub_item='(Des)Bloqu. Benef.')
        self.oHelper.SetValue('BCA_DATA', DateSystem)
        self.oHelper.F3(field='BCA_MOTBLO')
        self.oHelper.SetButton('Ok')    
        self.oHelper.SetButton('Salvar')    


        #Desbloqueando o Dependente
        self.oHelper.SetButton('Outras Ações',sub_item='(Des)Bloqu. Benef.')
        self.oHelper.SetValue('BCA_DATA', DateSystem)
        self.oHelper.F3(field='BCA_MOTBLO')
        self.oHelper.SetButton('Ok')   
        self.oHelper.SetButton('Salvar')            
        self.oHelper.SetButton('Sim') 
        self.oHelper.SetButton('Ok')   

        # Busca do titular

        self.oHelper.SearchBrowse(f'{chave}', key=4, index=True)
        self.oHelper.SetButton('Visualizar')
        self.oHelper.CheckResult('BA3_CODEMP', '0022')
        self.oHelper.SetButton('Confirmar')    

        self.oHelper.SetButton('Outras Ações',sub_item='Valor Cobranca')
        self.oHelper.SetValue('Ano Base ?', '2020')
        self.oHelper.SetValue('Mes Base ?', '11')
        self.oHelper.SetButton('Ok')    
        self.oHelper.SetButton('Confirmar')    

        #Bloqueando a Família
        self.oHelper.SetButton('Outras Ações',sub_item='(Des)Bloqu. Fam')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetValue('BC3_DATA', DateSystem)
        self.oHelper.F3(field='BC3_MOTBLO')
        self.oHelper.SetButton('Ok')    
        self.oHelper.SetButton('Salvar')    


        #Desbloqueando a família
        self.oHelper.SetButton('Outras Ações',sub_item='(Des)Bloqu. Fam')
        self.oHelper.SetValue('BC3_DATA', DateSystem)
        self.oHelper.F3(field='BC3_MOTBLO')
        self.oHelper.SetButton('Ok')   
        self.oHelper.SetButton('Salvar')            
        self.oHelper.SetButton('Sim')    

        self.oHelper.AssertTrue()

    #//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA260_PL004

	# Teste 04 - Incluindo os demais dados dos folders do grupo familiar
	
	# @author r.soares
	# @since 12/11/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
    def test_PLSA260_PL004(self):
		
		# Dados para o teste
        chave    = "M SP    71289920818"
	 
        self.oHelper.SearchBrowse(f'{chave}', key=4, index=True)
        self.oHelper.SetButton('Alterar')
        self.oHelper.ClickFolder('Comercial')
        self.oHelper.F3(field='BA3_EQUIPE')
        self.oHelper.SetButton('OK')        
        self.oHelper.ClickFolder('Opcional')
        self.oHelper.ClickGridCell("Versao")
        self.oHelper.SetKey("ENTER", grid=True)
        self.oHelper.F3(field='BF1_CODPRO')
        self.oHelper.SetButton('Salvar')        
        self.oHelper.SetValue('BF1_DATBAS', DateSystem)
        self.oHelper.SetButton('Salvar')        
        self.oHelper.ClickGridCell("Forma Cobr.", grid_number=2)
        self.oHelper.SetKey("ENTER", grid=True)
        self.oHelper.F3(field='BK0_CODFOR')
        self.oHelper.SetButton('OK')        
        self.oHelper.SetButton('Salvar')     
        self.oHelper.ClickFolder('Gratuidade')
        self.oHelper.ClickGridCell("Cod Gratuid.")
        self.oHelper.SetKey("ENTER", grid=True)
        self.oHelper.F3(field='BH5_CODGRA')
        self.oHelper.SetButton('Ok') 
        self.oHelper.SetValue('BH5_ANOINI', str(Ano))
        self.oHelper.SetValue('BH5_MESINI', str(Mes))
        self.oHelper.SetValue('BH5_ANOFIM', str(Ano))
        self.oHelper.SetValue('BH5_MESFIM', str(Mes))
        self.oHelper.SetButton('Salvar') 
        self.oHelper.SetButton('Salvar') 
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Salvar')

        self.oHelper.AssertTrue()

    #-------------------------------------------
    # Fim dos casos de testes TIR - PLSA260 
    #-------------------------------------------

    #-------------------------------------------
    # Encerramento class para TIR - PLSA260 
    #-------------------------------------------
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()