from tir import Webapp
import unittest

class TAFR122(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATAF','06/05/2019','T1','D MG 01 ','84')
        inst.oHelper.Program('TAFR122') #chama a rotina pelo campo de pesquisa
        
    def test_TAFR122_CT001(self):

        #-------------------------Seleção dos Parametros-------------------------------------------------------------------------------

        self.oHelper.SetValue('Período de Apuração', '102018')
        self.oHelper.SetValue('Apenas Inconsistências:','1-Sim')
        self.oHelper.SetButton('Ok')
             
        #--------------------------Seleção de Filiais-----------------------------------------------------------------------------------
        
        self.oHelper.ClickBox('Filial', 'D MG 01')
        self.oHelper.SetButton('Ok')        

        #--------------------------Browse Conferencia de Incidencias de Verbas----------------------------------------------------------

        #self.oHelper.SearchBrowse('D MG 01 000000000000000000000000000000000023 704', key='Filial+id + Cod. Rub Taf + Iden.tab.rub')

        self.oHelper.SetButton('Visualizar')

        self.oHelper.CheckResult('V3I_RUBRH', '703')
        self.oHelper.CheckResult('V3I_RUBTAF','703')
        self.oHelper.CheckResult('V3I_FLFGTS','00 - Não é Base de Cálculo')
        self.oHelper.CheckResult('V3I_TFFGTS','11 - Base Cálculo')

        self.oHelper.SetButton('Fechar')        

        #--------------------------Gerar Relatorio---------------------------------------------------------------------------------------

        self.oHelper.SetButton('Gerar Relatório')
        self.oHelper.SetButton('Fechar') 

        #--------------------------Avaliar Pendencias RH x TAF---------------------------------------------------------------------------- 

        self.oHelper.SetButton('Outras Ações', 'Reavaliar RH x TAF')

        #self.oHelper.SearchBrowse('D MG 01 000000000000000000000000000000000011 704', key='Filial+id + Cod. Rub Taf + Iden.tab.rub')

        self.oHelper.SetButton('Visualizar')

        self.oHelper.CheckResult('V3I_RUBRH', '703')
        self.oHelper.CheckResult('V3I_RUBTAF','703')
        self.oHelper.CheckResult('V3I_FLFGTS','00 - Não é Base de Cálculo')
        self.oHelper.CheckResult('V3I_TFFGTS','11 - Base Cálculo')

        self.oHelper.SetButton('Fechar')
        # 
        # 
        # Aguardando implementação da pesquisa via coluna  - Equipe Automação  
               
                
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()