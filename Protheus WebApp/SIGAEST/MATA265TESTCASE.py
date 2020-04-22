from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA265 - Endereçamento 
#TABELA sda sdb
#
#@author JEFFERSON SILVA DE SOUSA
#@since 13/09/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATA265(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAEST","13/09/2019","T1","D MG 01 ","04")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA265")
    #CT001 ENDEREÇAR COM GERAÇAO DE NUMERO DE SERIE 
    def test_MATA265_001(self):
        
        #Variaveis de inclusar
        prod     = 'ESTSE0000000000000000000000554'
        endereco = 'ENDSE01'
        filial   = 'D MG 01 '
        seqserie = 'MATA265001'

        self.oHelper.SearchBrowse(f"{filial}{prod}", "Filial+produto + Armazem + Sequen..")

        self.oHelper.SetButton("EnDerecar")
        time.sleep(3)

        self.oHelper.SetButton('Outras Ações','Gerar Números de Série')       

        self.oHelper.SetValue("Endereco", endereco)
        self.oHelper.SetValue("Valor Inicial:",seqserie)       

        self.oHelper.SetButton("Confirmar")

        self.oHelper.CheckResult('DB_NUMSERI','MATA265001', grid=True, line=1)
        self.oHelper.CheckResult('DB_NUMSERI','MATA265002', grid=True, line=2)
        self.oHelper.CheckResult('DB_NUMSERI','MATA265003', grid=True, line=3)
        self.oHelper.CheckResult('DB_NUMSERI','MATA265004', grid=True, line=4)
        self.oHelper.CheckResult('DB_NUMSERI','MATA265005', grid=True, line=5)
        self.oHelper.CheckResult('DB_NUMSERI','MATA265006', grid=True, line=6)
        self.oHelper.CheckResult('DB_NUMSERI','MATA265007', grid=True, line=7)
        self.oHelper.CheckResult('DB_NUMSERI','MATA265008', grid=True, line=8)
        self.oHelper.CheckResult('DB_NUMSERI','MATA265009', grid=True, line=9)
        self.oHelper.CheckResult('DB_NUMSERI','MATA26500A', grid=True, line=10)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")
     
        self.oHelper.AssertTrue()     

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()