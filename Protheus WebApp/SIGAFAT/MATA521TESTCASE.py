from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')
import time


class MATA521(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAFAT",DateSystem,"T1","D MG 01 ","05")
        self.oHelper.Program("MATA521A")
                
    def test_MATA521_025(self): 
        
        '''
         Test Case CT025 - Excluir Documento de saida com interface de selecao, com os itens.
        '''
        self.oHelper.SetValue("Modelo de Interface ?"   ,"Marcacao")
        self.oHelper.SetValue("Selecionar itens ?"      ,"Nao")
        self.oHelper.SetValue("Dt.Emissao de ?"         ,"01/01/1980")
        self.oHelper.SetValue("Dt.Emissao ate ?"        ,"31/12/2045")
        self.oHelper.SetValue("Serie de ?"              ,"000")
        self.oHelper.SetValue("Serie ate ?"             ,"ZZZ")
        self.oHelper.SetValue("Documento de ?"          ,"000000000")
        self.oHelper.SetValue("Documento ate ?"         ,"ZZZZZZZZZ")
        self.oHelper.SetButton("OK") 
         
        self.oHelper.SearchBrowse("D MG 01 000740   1  FAT001", "Filial+numero + Serie Docto. + Clien.")
        self.oHelper.ClickBox("Numero","000740")
        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.SetButton("Sim")
        self.oHelper.WaitProcessing("Estorno dos documentos de saida")
        self.oHelper.AssertTrue() 
        
    def test_MATA521_028(self):

        '''
        Test Case CT028 - Visualizar o Documento de saida (Pela rotina de Exclusao de Documento de Saida).
        ''' 
        '''
        self.oHelper.SetValue("Modelo de Interface ?"   ,"Marcacao")
        self.oHelper.SetValue("Selecionar itens ?"      ,"Nao")
        self.oHelper.SetValue("Dt.Emissao de ?"         ,"01/04/2016")
        self.oHelper.SetValue("Dt.Emissao ate ?"        ,"01/04/2016")
        self.oHelper.SetValue("Serie de ?"              ,"000")
        self.oHelper.SetValue("Serie ate ?"             ,"ZZZ")
        self.oHelper.SetValue("Documento de ?"          ,"000000000")
        self.oHelper.SetValue("Documento ate ?"         ,"ZZZZZZZZZ")
        self.oHelper.SetButton("OK") 
        '''
        self.oHelper.SearchBrowse("D MG 01 000742   1  FAT001", "Filial+numero + Serie Docto. + Clien.")
        self.oHelper.ClickBox("Numero","000742")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        self.oHelper.TearDown()
       
    def test_MATA521_065(self):

        '''
        Test Case CT065 - Exclusão do Documento de Saída para um pedido de venda do tipo Normal com Adiantamento e 3 parcelas
        '''  
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAFIN",DateSystem,"T1","D MG 01 ","06")
        self.oHelper.Program("FINA330")
        self.oHelper.WaitShow("Compensaçäo de Titulos a Receber")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
        self.oHelper.SetValue("Contabiliza On Line ?" ,"Nao")
        self.oHelper.SetButton("OK")
        self.oHelper.AssertTrue()
        self.oHelper.TearDown()
        

        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAFAT",DateSystem,"T1","D MG 01 ","05")
        self.oHelper.Program("MATA521A")

        self.oHelper.AddParameter("MV_ESTADO","D MG 01","SP","SP","SP") 
        self.oHelper.AddParameter("MV_VLDSBT","D MG 01",".T.",".T.",".T.") 
        self.oHelper.AddParameter("MV_EXCNFS","D MG 01","0","0","0") 
        self.oHelper.AddParameter("MV_TIPOPRZ","D MG 01","1","1","1") 
        self.oHelper.SetParameters() 
          
        self.oHelper.SetValue("Modelo de Interface ?"   ,"Selecao")
        self.oHelper.SetValue("Selecionar itens ?"      ,"Nao")
        self.oHelper.SetValue("Dt.Emissao de ?"         ,"15/04/2019")
        self.oHelper.SetValue("Dt.Emissao ate ?"        ,"15/04/2019")
        self.oHelper.SetValue("Serie de ?"              ,"FAT")
        self.oHelper.SetValue("Serie ate ?"             ,"FAT")
        self.oHelper.SetValue("Documento de ?"          ,"000000027")
        self.oHelper.SetValue("Documento ate ?"         ,"000000027")
     
        self.oHelper.SetButton("OK")
        
        self.oHelper.SearchBrowse("D MG 01 000000027FATFAT001", "Filial+numero + Serie Docto. + Clien.")
        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Sim") 
        self.oHelper.AssertTrue()
        self.oHelper.TearDown()
        
if __name__ == '__main__':
    unittest.main()
