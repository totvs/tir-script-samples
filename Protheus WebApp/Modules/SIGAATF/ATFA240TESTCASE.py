from tir import Webapp
import unittest

class ATFA240(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAATF', '10/04/2016', 'T1', 'M PR 01 ')
        inst.oHelper.Program('ATFA240')
    
    @classmethod
    def test_ATFA240_CT001(self):

        self.oHelper.SearchBrowse('M PR 01 NFE00000250001')
        #N3_FILIAL+N3_CBASE+N3_ITEM+N3_TIPO+N3_BAIXA+N3_SEQ 

        self.oHelper.SetButton("Classificar")
        self.oHelper.SetBranch("M PR 01 ")

        self.oHelper.SetValue("Grupo","0001")
        self.oHelper.SetButton("Sim")
        
        self.oHelper.SetValue("Num.Plaqueta","NFE0000025")
        
        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow("Registro alterado com sucesso.")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse('M PR 01 NFE00000250001')

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult('N1_CBASE'   , 'NFE0000025')
        self.oHelper.CheckResult('N1_ITEM'    , '0001')
        self.oHelper.CheckResult('N1_AQUISIC' , '10/03/2016')

        self.oHelper.CheckResult('N3_TIPO'    , '01')
        self.oHelper.CheckResult('N3_CCONTAB' , '101010105')
        self.oHelper.CheckResult('N3_CDEPREC' , '101010105')
        self.oHelper.CheckResult('N3_TXDEPR1' , '10,0000')
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def test_ATFA240_CT002(self):

        self.oHelper.SearchBrowse('M PR 01 NFE00000270001')
        #N3_FILIAL+N3_CBASE+N3_ITEM+N3_TIPO+N3_BAIXA+N3_SEQ 

        self.oHelper.SetButton("Classificar")
        self.oHelper.SetBranch("M PR 01 ")

        self.oHelper.SetValue("Grupo","0002")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetValue("Num.Plaqueta","NFE0000027")
        
        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow("Registro alterado com sucesso.")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse('M PR 01 NFE00000270001')

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult('N1_CBASE'   , 'NFE0000027')
        self.oHelper.CheckResult('N1_ITEM'    , '0001')
        self.oHelper.CheckResult('N1_AQUISIC' , '31/03/2016')

        self.oHelper.CheckResult('N3_TIPO'    , '01')
        self.oHelper.CheckResult('N3_CCONTAB' , '101010105')
        self.oHelper.CheckResult('N3_TXDEPR1' , '12,0000')
        self.oHelper.CheckResult('N3_EC05DB' , '000001')
        self.oHelper.CheckResult('N3_EC05CR' , '000002')
        self.oHelper.CheckResult('N3_EC06DB' , '000001')
        self.oHelper.CheckResult('N3_EC06CR' , '000002')
        self.oHelper.CheckResult('N3_EC07DB' , '000001')
        self.oHelper.CheckResult('N3_EC07CR' , '000002')
        self.oHelper.CheckResult('N3_EC08DB' , '000001')
        self.oHelper.CheckResult('N3_EC08CR' , '000002')
        self.oHelper.CheckResult('N3_EC09DB' , '000001')
        self.oHelper.CheckResult('N3_EC09CR' , '000002')

        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()
##############################################################################################
##### Classificar mudando codigo do bem
# ############################################################################################
    @classmethod
    def test_ATFA240_CT003(self):

        #self.oHelper.AddParameter("MV_ULTDEPR","M PR 01 ", "20161004")
        #self.oHelper.SetParameters() ##Caso queira rodar a configuração do ultdepr pelo robo

        self.oHelper.SearchBrowse('M PR 01 NFE000002B0001')
                
        self.oHelper.SetButton("Classificar")
        self.oHelper.SetBranch("M PR 01 ")

        self.oHelper.SetValue("Grupo","0001")
        self.oHelper.SetButton("Sim")
        
        self.oHelper.CheckResult('N1_CBASE'   , 'NFE000002B') ##Verificando codigo anterior
        self.oHelper.SetValue('N1_CBASE'   , 'NFE0000MOD')
        self.oHelper.SetValue("N1_CHAPA","NFE000002T")#Num.Plaqueta   #N1_CHAPA
        
        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow("Registro alterado com sucesso.")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse('M PR 01 NFE0000MOD0001')

        self.oHelper.SetButton("Visualizar")

        ##Cabeçalho SN1
        self.oHelper.CheckResult('N1_CBASE'   , 'NFE0000MOD')
        self.oHelper.CheckResult('N1_ITEM'    , '0001')
        self.oHelper.CheckResult("N1_CHAPA","NFE000002T")#Num.Plaqueta #NFE0000MOD
        self.oHelper.CheckResult('N1_AQUISIC' , '10/04/2016')
        
        ##Cabeçalho SN3
        self.oHelper.CheckResult("N3_TIPO","01")
        self.oHelper.CheckResult('N3_VORIG1' , '2500,00')
        self.oHelper.CheckResult('N3_TIPO'    , '01')
        self.oHelper.CheckResult('N3_CCONTAB' , '101010105')
        self.oHelper.CheckResult('N3_CDEPREC' , '101010105')
        self.oHelper.CheckResult('N3_TXDEPR1' , '10,0000')
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
    @classmethod   
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()