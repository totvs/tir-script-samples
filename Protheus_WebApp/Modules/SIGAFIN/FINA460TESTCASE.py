from tir import Webapp
import unittest
import time
#from datetime import datetime
#DateSystem = datetime.today().strftime('%d/%m/%Y')

class FINA460(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicialização
        inst.oHelper.Setup("SIGAFIN","24/04/2020","T1","D MG 01 ","06")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("FINA460")

    def test_FINA460_202(self):
        '''
        Test Case 202
        '''
        self.oHelper.AddParameter("MV_FATOUT" , "", "21000", "21000", "21000") # restaura tempo do time para evitar tela de msg.
        self.oHelper.AddParameter("MV_MSGTIME", "", "21000", "21000", "21000")
        self.oHelper.AddParameter("MV_CMC7FIN", "", "S", "S", "S")
        self.oHelper.SetParameters()

        self.oHelper.WaitShow("Liquidação")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Contabiliza OnLine ?", "Nao")
        self.oHelper.SetValue("Mostra Lanc Contab ?", "Nao")
        self.oHelper.SetValue("Prefixo titulo a ser gerado ?", "TIR")
        self.oHelper.SetButton("Ok") 

        self.oHelper.SearchBrowse("D MG 01 TIRTIR460001")
        self.oHelper.SetButton("Liquidar")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Natureza Liquidação", "000001")
        self.oHelper.SetButton("Ok")

        #Fecha a tela do CMC7
        self.oHelper.WaitShow("Liquidação")
        self.oHelper.SetButton("Não")

        self.oHelper.SetValue("FO0_COND", "000")
        self.oHelper.SetValue("FO0_TIPO", "FT")

        self.oHelper.ClickBox("Número","TIR460001",grid_number=1)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_FINA460_203(self):
        '''
        Test Case 203
        '''
        self.oHelper.WaitShow("Liquidação")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Prefixo titulo a ser gerado ?", "TIR")
        self.oHelper.SetButton("Ok") 

        self.oHelper.SearchBrowse("D MG 01 TIRTIR460002")
        self.oHelper.SetButton("Liquidar")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Outras Moedas", "1 - Converte")
        self.oHelper.SetValue("Natureza Liquidação", "000001")
        self.oHelper.SetButton("Ok")

        #Fecha a tela do CMC7
        self.oHelper.WaitShow("Liquidação")
        self.oHelper.SetButton("Não")

        self.oHelper.SetValue("FO0_COND"  , "002")
        self.oHelper.SetValue("FO0_TIPO"  , "FT")
        self.oHelper.SetValue("FO0_TXMOED", "3,5000")

        self.oHelper.ClickBox("Número","TIR460002",grid_number=1)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_FINA460_204(self):
        '''
        Test Case 204
        '''
        self.oHelper.WaitShow("Liquidação")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Prefixo titulo a ser gerado ?", "LIQ")
        self.oHelper.SetButton("Ok") 

        self.oHelper.SearchBrowse("D MG 01 TIRTIR460003")
        self.oHelper.SetButton("Liquidar")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Natureza Liquidação", "000001")
        self.oHelper.SetButton("Ok")

        #Fecha a tela do CMC7
        self.oHelper.WaitShow("Liquidação")
        self.oHelper.SetButton("Não")

        self.oHelper.SetValue("FO0_COND", "002")
        self.oHelper.SetValue("FO0_TIPO", "FT")

        self.oHelper.ClickBox("Número","TIR460003",grid_number=1)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    def test_FINA460_205(self):
        '''
        Test Case 205
        '''
        self.oHelper.WaitShow("Liquidação")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Prefixo titulo a ser gerado ?", "LIQ")
        self.oHelper.SetButton("Ok") 

        self.oHelper.SearchBrowse("D MG 01 TIRTIR460004")
        self.oHelper.SetButton("Liquidar")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Natureza Liquidação", "000001")
        self.oHelper.SetButton("Ok")

        #Cadastro do Cheque 01
        self.oHelper.WaitShow("Liquidação")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetValue("Passe o cheque:", "<23701348<0180001265<577508114673:")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("Valor", "2000,00")
        self.oHelper.SetValue("Emitente", "EMITENTE DO CHEQUE 1")
        self.oHelper.SetButton("Ok")

        #Cadastro do Cheque 02
        self.oHelper.SetButton("Sim")

        self.oHelper.SetValue("Passe o cheque", "<23728016<0010002185>777500568207:")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("Emitente", "EMITENTE DO CHEQUE 2")
        self.oHelper.SetButton("Ok")

        #Cancelamento da tela de cadastro de cheque
        self.oHelper.SetButton("Não")

        self.oHelper.ClickBox("Número","TIR460004",grid_number=1)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    def test_FINA460_206(self):
        '''
        Test Case 206
        '''
        self.oHelper.WaitShow("Liquidação")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Prefixo titulo a ser gerado ?", "LIQ")
        self.oHelper.SetButton("Ok") 

        self.oHelper.SearchBrowse("D MG 01 TIRTIR460005")
        self.oHelper.SetButton("Liquidar")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Natureza Liquidação", "000001")
        self.oHelper.SetButton("Ok")

        #Fecha a tela do CMC7
        self.oHelper.WaitShow("Liquidação")
        self.oHelper.SetButton("Não")

        self.oHelper.SetValue("FO0_COND", "002")
        self.oHelper.SetValue("FO0_TIPO", "FT")

        self.oHelper.ClickBox("Parcela","A",grid_number=1)
        self.oHelper.ClickBox("Parcela","B",grid_number=1)

        self.oHelper.SetValue("Prefixo" , "TIR", grid=True, grid_number=2)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Sim")

        self.oHelper.SetValue("Número"      , "99AA99001" , grid=True, grid_number=2)
        self.oHelper.SetValue("Parcela"     , "1"         , grid=True, grid_number=2)
        self.oHelper.SetValue("Tp Titulo"   , "BOL"       , grid=True, grid_number=2)
        self.oHelper.SetValue("Vencimento"  , "23/05/2020", grid=True, grid_number=2)
        self.oHelper.SetValue("Val. Parcela", "2300,00"   , grid=True, grid_number=2)
        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    def test_FINA460_207(self):
        '''
        Test Case 207
        '''
        self.oHelper.SearchBrowse("D MG 01 TIR000000001AFT ")
        self.oHelper.SetButton("Outras Ações", "Cancelar")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()
    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()