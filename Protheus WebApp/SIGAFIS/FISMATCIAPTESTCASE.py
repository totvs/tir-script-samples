from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')


class FISMATCIAP(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAFIS', DateSystem, 'T1', 'XIFIS14', '09')
        inst.oHelper.Program('MATA905')

        inst.oHelper.AddParameter("MV_HABCOEF" ,"",".T.")
        inst.oHelper.AddParameter("MV_FILTRAN" ,"","F9_FILTRAN")
        inst.oHelper.SetParameters()
 
    #Inclusao do CIAP Ativo 1
    def test_IndMCP_001(self):

        self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse("XIFIS14 ")
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('F9_CODIGO','FIS004')
        self.oHelper.SetValue('F9_DESCRI','ATIVO TESTE TIR')
        self.oHelper.SetValue('F9_FORNECE','MG0001')
        self.oHelper.SetValue('F9_LOJAFOR','01')
        self.oHelper.SetValue('F9_DOCNFE','MG0001')
        self.oHelper.SetValue('F9_PROPRIO','N')
        self.oHelper.SetValue('F9_DTENTNE',DateSystem)
        self.oHelper.SetValue('F9_DTEMINE',DateSystem)
        self.oHelper.SetValue('F9_VALICMS','100,00')

        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    #Inclusao do CIAP Ativo 2
    def test_IndMCP_002(self):

        self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse("XIFIS14 ")
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('F9_CODIGO','FIS005')
        self.oHelper.SetValue('F9_DESCRI','ATIVO TESTE TIR')
        self.oHelper.SetValue('F9_FORNECE','MG0001')
        self.oHelper.SetValue('F9_LOJAFOR','01')
        self.oHelper.SetValue('F9_DOCNFE','MG0001')
        self.oHelper.SetValue('F9_PROPRIO','N')
        self.oHelper.SetValue('F9_DTENTNE',DateSystem)
        self.oHelper.SetValue('F9_DTEMINE',DateSystem)
        self.oHelper.SetValue('F9_VALICMS','100,00')

        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()    

    #Alteracao do CIAP Ativo 1
    def test_IndMCP_003(self):

        self.oHelper.SearchBrowse("XIFIS14 FIS004")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('F9_DESCRI','ATIVO TESTE TIR ALTERACAO')
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.AssertTrue()
    
    #Exclusao do CIAP Ativo 1
    def test_IndMCP_004(self):

        self.oHelper.SearchBrowse("XIFIS14 FIS004")
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()
        #self.oHelper.TearDown()

    #Apropriacao do CIAP Ativo 2
    def test_IndMCP_005(self):
        
        self.oHelper = Webapp()
        
        self.oHelper.Setup('SIGAFIS', DateSystem, 'T1', 'XIFIS14', '09')
        self.oHelper.Program('MATA906')

        self.oHelper.SearchBrowse("XIFIS14 FIS005")
        self.oHelper.SetButton('Outras Ações', 'Apropriar')
        self.oHelper.SetButton('Param.')
        self.oHelper.SetValue("mv_par01", DateSystem)
        self.oHelper.SetValue("nTotTrib", "10000,00",name_attr=True)
        self.oHelper.SetValue("nTot", "10000,00",name_attr=True)
        self.oHelper.SetButton('Ok')
        self.oHelper.SetValue("mv_par08", "ZZZZ")
        self.oHelper.SetValue("mv_par10", "ZZZZZZ")
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()
    
    #Cancelar apropriacao do CIAP Ativo 2
    #def test_IndMCP_006(self):

        self.oHelper.SearchBrowse("XIFIS14 FIS005")
        self.oHelper.SetButton('Outras Ações', 'Cancela')
        self.oHelper.SetValue("Apropriacao",True)
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()
        #self.oHelper.TearDown() 

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
