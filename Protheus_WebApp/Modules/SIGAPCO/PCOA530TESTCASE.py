from tir import Webapp
import unittest

class PCOA530(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAATF", "01/04/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA012")
            
        inst.oHelper.AddParameter("MV_ULTDEPR","", "20160331")
        inst.oHelper.AddParameter("MV_ALTLCTO", "", "N")
        inst.oHelper.AddParameter("MV_PRELAN", "", "S")
        inst.oHelper.AddParameter("MV_PCOINTE", "", "1")
        inst.oHelper.AddParameter("MV_PCOSDCT", "", ".T.")
        inst.oHelper.AddParameter("MV_PCOCTGP", "", ".T.")
        inst.oHelper.AddParameter("MV_PCOEMCT", "", ".T.")
        inst.oHelper.SetParameters()

    def test_PCOA530_001(self): #PCO INTEGRACAO
                   
        codigoATF = 'TESTE'

        self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")
        

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01")
                
        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_AQUISIC", "01/04/2016")

        
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "TSTE530")

        self.oHelper.SetValue("N3_TIPO", "01", grid=True, row=1)
        self.oHelper.SetValue("N3_HISTOR", "TESTE", grid=True, row=1)
        self.oHelper.SetValue("N3_CCONTAB", "CTBXATUD", grid=True, row=1)
        self.oHelper.SetValue("N3_VORIG1", "1000,00", grid=True, row=1)
        self.oHelper.SetValue("N3_TXDEPR1", "10,0000", grid=True, row=1)
        self.oHelper.SetValue("N3_VRDACM1", "10,00", grid=True, row=1)

        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")
        # self.oHelper.SetButton("Confirmar") ## quebro aqui
        self.oHelper.SetButton("Contingencia")
        self.oHelper.SetButton("Outras Ações","Solicitar")
        self.oHelper.SetButton("Enviar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
              
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")                           

        self.oHelper.SetButton("Sair da página")

        self.oHelper.AssertTrue()

    def test_PCOA530_003(self): #PCO INTEGRACAO
                   
        codigoATF = 'TESTE'

        self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")
        

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01")
                
        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_AQUISIC", "01/04/2016")

        
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "TESTE53")

        self.oHelper.SetValue("N3_TIPO", "01", grid=True, row=1)
        self.oHelper.SetValue("N3_HISTOR", "TESTE", grid=True, row=1)
        self.oHelper.SetValue("N3_CCONTAB", "CTBXATUD", grid=True, row=1)
        self.oHelper.SetValue("N3_VORIG1", "1000,00", grid=True, row=1)
        self.oHelper.SetValue("N3_TXDEPR1", "10,0000", grid=True, row=1)
        self.oHelper.SetValue("N3_VRDACM1", "10,00", grid=True, row=1)

        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")
        # self.oHelper.SetButton("Confirmar") ## quebro aqui
        self.oHelper.SetButton("Contingencia")
        self.oHelper.SetButton("Outras Ações","Solicitar")
        self.oHelper.SetButton("Enviar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetFocus('Nome Solic.',grid_cell=True,row_number=1)
        self.oHelper.SetButton("OK")
              
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")                           

        self.oHelper.SetButton("Sair da página")

        self.oHelper.AssertTrue()

    def test_PCOA530_002(self): #PCO INTEGRACAO
                   
        
        self.oHelper.AddParameter("MV_PCOWFCT", "", "2")
        self.oHelper.SetParameters()
       
        codigoATF = 'TESTE2'

        self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")
        

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01")
                
        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_AQUISIC", "01/04/2016")

        
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "TEST530")

        self.oHelper.SetValue("N3_TIPO", "01", grid=True, row=1)
        self.oHelper.SetValue("N3_HISTOR", "TESTE", grid=True, row=1)
        self.oHelper.SetValue("N3_CCONTAB", "CTBXATUD", grid=True, row=1)
        self.oHelper.SetValue("N3_VORIG1", "1000,00", grid=True, row=1)
        self.oHelper.SetValue("N3_TXDEPR1", "10,0000", grid=True, row=1)
        self.oHelper.SetValue("N3_VRDACM1", "10,00", grid=True, row=1)

        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")
        # self.oHelper.SetButton("Confirmar") # quebro aqui
        self.oHelper.SetButton("Contingencia")
        self.oHelper.SetButton("Outras Ações","Solicitar")

        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")


        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")

        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
