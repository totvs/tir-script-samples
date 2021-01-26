from tir import Webapp
import unittest


class PCOA195(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper =  Webapp()
        inst.oHelper.Setup('SIGAPCO', '30/11/2020', 'T1', 'D MG 01 ')
        inst.oHelper.Program('PCOA195')
        
    def test_PCOA195_CT001(self): # Copia

        sTpSaldo    = '99'
        sDescr  = 'TESTE TIR COPIA'

        self.oHelper.SearchBrowse(f"D MG 01 01")   
        
        self.oHelper.SetButton('Outras Ações','Copiar')
        #Preencher Código e Descrição do cubo
        self.oHelper.SetValue('AL2_TPSALD',sTpSaldo,name_attr=True)
        self.oHelper.SetValue('AL2_DESCRI',sDescr,name_attr=True)
     
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()
        

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()    