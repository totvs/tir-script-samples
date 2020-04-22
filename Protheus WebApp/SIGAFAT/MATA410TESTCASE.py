from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest


class MATA410(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAFAT",DataSystem,"T1","D MG 01 ","05")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA410")

    def test_MATA410_199(self):
        '''
            Inclusão de Pedido de Venda
        '''

        order = 'FATT37'

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")
        
        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_TIPO","B")
        self.oHelper.SetValue("C5_TIPO","N")
        self.oHelper.SetValue("C5_CLIENTE","FAT001")
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetValue("C5_LOJAENT","00")
        self.oHelper.SetValue("C5_CONDPAG","003")
        
        self.oHelper.SetValue("Produto", "FAT000000000000000000000000001", grid=True)
        self.oHelper.SetValue("Quantidade", "1,00", grid=True)
        self.oHelper.SetValue("C6_OPER", "01", grid=True)
        self.oHelper.SetValue("C6_DESCONT", "5,00", grid=True)
        self.oHelper.SetValue("C6_TES", "503", grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)
        self.oHelper.CheckResult("C5_TIPO","N")
        self.oHelper.CheckResult("C5_CLIENTE","FAT001")
        self.oHelper.CheckResult("C5_CONDPAG","003")

        self.oHelper.CheckResult("Produto", " FAT000000000000000000000000001", grid=True, line=1)
        self.oHelper.CheckResult("C6_DESCONT", " 5,00", grid=True, line=1)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_MATA410_200(self):

        '''
            Adiantamento
        '''

        order = 'FATT38'        

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")
        
        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_TIPO","N")
        self.oHelper.SetValue("C5_CLIENTE","FAT001")
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetValue("C5_CONDPAG","006")
        
        self.oHelper.SetValue("Produto", "FAT001", grid=True)
        self.oHelper.SetValue("Quantidade", "1,00", grid=True)
        self.oHelper.SetValue("Prc Unitario", "1,00", grid=True)
        self.oHelper.SetValue("C6_VALOR", "1,00", grid=True)
        self.oHelper.SetValue("C6_TES", "503", grid=True)
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton('Outras Ações','Adiantam.')
        
        self.oHelper.SetButton('Ok') 
        
        self.oHelper.WaitShow("Contas a Receber") 

        self.oHelper.SetButton('Cancelar')


        self.oHelper.WaitHide("Contas a Receber")
        self.oHelper.SetKey('ENTER')
        self.oHelper.WaitHide("Pedidos de Venda - INCLUIR")
        self.oHelper.SetValue("Valor","1,00") 
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitShow("Contas a Receber") 
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Cancelar')        

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)
        self.oHelper.CheckResult("C5_TIPO","N")
        self.oHelper.CheckResult("C5_CLIENTE","FAT001")
        self.oHelper.CheckResult("C5_CONDPAG","006")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_MATA410_201(self):

        '''
            Alteração de Pedido de Venda
        '''

        order = 'FAT500'

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("C5_CLIENTE","FAT002")
        self.oHelper.SetValue("C5_LOJACLI","01")        
        self.oHelper.SetValue("C5_CONDPAG","001")

        self.oHelper.SetValue("Prc Unitario", "2,00", grid=True)
        self.oHelper.SetValue("C6_VALOR", "2,00", grid=True)        

        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton("Salvar")

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_CLIENTE","FAT002")
        self.oHelper.CheckResult("C5_CONDPAG", "001")

        self.oHelper.SetButton("Cancelar")   

        self.oHelper.AssertTrue()

    def test_MATA410_202(self): 
   
        '''
            Exclusão de Pedido de Venda
        '''

        order = 'FAT239'

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton('Outras Ações','Excluir, Excluir')
    
        self.oHelper.WaitShow("Pedidos de Venda - EXCLUIR")
        
        self.oHelper.SetButton("Confirmar")
        #Aguardando correção da Task 1558 subir para branch Master 
        self.oHelper.AssertTrue()
        '''
        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertFalse()
        '''

    def test_MATA410_203(self):
        '''
            Visualizar Planilha Financeira
        '''
        order = 'FAT240'

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton('Visualizar')

        self.oHelper.SetButton('Outras Ações','Planilha')
        self.oHelper.CheckResult("Vlr.Frete", "100,00")
        self.oHelper.CheckResult("Total da Nota", "12100,00")

        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertFalse()

    def test_MATA410_204(self):
        '''
            Teste com Grade - Não funciona
        '''

        order = 'FATT41'

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")
        '''
        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_CLIENTE","FAT001")
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetValue("C5_CONDPAG","003")
        '''
        
        self.oHelper.SetValue("Produto", "FAT000000000000000000000000001", grid=True)
        self.oHelper.LoadGrid()
        
        self.oHelper.SetFocus('Quantidade', grid_cell = True)
        self.oHelper.SetKey('F3')
        self.oHelper.SetButton('1')
        self.oHelper.SetButton('Ok')
        self.oHelper.SetKey('ENTER')
        #self.oHelper.SetValue("Quantidade", "1,00", grid=True)
        self.oHelper.WaitShow("Totais da Grade")
        self.oHelper.SetValue("[GG] GRANDE", "1,00", grid=True,row=1) 
        self.oHelper.LoadGrid()

        
        self.oHelper.SetValue("[GG] GRANDE", "1,00", grid=True,row=1)        

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_MATA410_205(self):
        '''
            Rateio Pedido de Venda
        '''

        order = 'FATT42'

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")
        
        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_TIPO","N")
        self.oHelper.SetValue("C5_CLIENTE","FAT001")
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetValue("C5_LOJAENT","01")
        self.oHelper.SetValue("C5_CONDPAG","003")
        
        self.oHelper.SetValue("Produto", "FAT001", grid=True)
        self.oHelper.SetValue("Quantidade", "1,00", grid=True)
        self.oHelper.SetValue("C6_OPER", "01", grid=True)
        self.oHelper.SetValue("C6_TES", "503", grid=True)
        self.oHelper.SetValue("Prc Unitario", "1,00", grid=True)
        self.oHelper.SetValue("C6_VALOR", "1,00", grid=True)        

        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Outras Ações','Rateio')
        self.oHelper.SetValue("% Rat.", "50,00", grid=True)
        self.oHelper.SetValue("C. de Custo", "000000001", grid=True)

        self.oHelper.SetKey("DOWN", grid=True)

        self.oHelper.SetValue("% Rat.", "50,00", grid=True)
        self.oHelper.SetValue("C. de Custo", "000000002", grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_MATA410_206(self):
        '''
            Aposentadoria Especial
        '''
        order = 'FATT43'

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")
        
        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_TIPO","N")
        self.oHelper.SetValue("C5_CLIENTE","FAT001")
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetValue("C5_LOJAENT","01")
        self.oHelper.SetValue("C5_CONDPAG","003")
        
        self.oHelper.SetValue("Produto", "FAT001", grid=True)
        self.oHelper.SetValue("Quantidade", "1,00", grid=True)
        self.oHelper.SetValue("C6_OPER", "01", grid=True)
        self.oHelper.SetValue("C6_TES", "503", grid=True)
        self.oHelper.SetValue("Prc Unitario", "100,00", grid=True)
        self.oHelper.SetValue("C6_VALOR", "100,00", grid=True)        

        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Outras Ações','Apos Especial')

        self.oHelper.SetValue("VlrAp 15anos", "60,00", grid=True)
        self.oHelper.SetValue("VlrAp 20anos", "30,00", grid=True)
        self.oHelper.SetValue("VlrAp 25anos", "10,00", grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)
        self.oHelper.CheckResult("C5_TIPO","N")
        self.oHelper.CheckResult("C5_CLIENTE","FAT001")
        self.oHelper.CheckResult("C5_CONDPAG","003")

        self.oHelper.CheckResult("Produto", " FAT001", grid=True, line=1)
        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_MATA410_207(self):
        '''
            Formas de Pagamento - Não Funciona
        '''
        order = 'FATT44'

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")
        
        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_TIPO","N")
        self.oHelper.SetValue("C5_CLIENTE","FAT001")
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetValue("C5_LOJAENT","01")
        self.oHelper.SetValue("C5_CONDPAG","003")
        
        self.oHelper.SetButton('Outras Ações','Formas')

        self.oHelper.SetValue("Forma Pagto.", "BOL", grid=True)
        self.oHelper.SetValue("CV_RATFOR", "100,00", grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetValue("Produto", "FAT001", grid=True)
        self.oHelper.SetValue("Quantidade", "1,00", grid=True)
        self.oHelper.SetValue("C6_TES", "503", grid=True)
        self.oHelper.SetValue("Prc Unitario", "100,00", grid=True)
        self.oHelper.SetValue("C6_VALOR", "100,00", grid=True)        

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)
        self.oHelper.CheckResult("C5_TIPO","N")
        self.oHelper.CheckResult("C5_CLIENTE","FAT001")
        self.oHelper.CheckResult("C5_CONDPAG","003")

        self.oHelper.CheckResult("Produto", " FAT001", grid=True, line=1)
        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_MATA410_208(self):
        '''
            Cópia Pedido de Venda
        '''

        order = 'FAT510'
        orderpai = 'FAT500'

        self.oHelper.SearchBrowse(f"D MG 01 {orderpai}", "Filial+numero")

        self.oHelper.SetButton('Outras Ações','Copiar')
        
        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetValue("C5_LOJAENT","01")        

        self.oHelper.SetButton("Salvar")

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)
        self.oHelper.CheckResult("C5_TIPO","N")
        self.oHelper.CheckResult("C5_CLIENTE","FAT002")
        self.oHelper.CheckResult("C5_CONDPAG","001")

        self.oHelper.CheckResult("Produto", " FAT001", grid=True, line=1)
        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_MATA410_209(self):
        '''
            Ativar parâmetro MV_EMPBN
        '''
        self.oHelper.AddParameter("MV_EMPBN","D MG 01",".T.",".T.",".T.")
        self.oHelper.SetParameters()

        order = 'FATT46'

        self.oHelper.SetButton('Incluir')

        self.oHelper.SetBranch("D MG 01 ")
        
        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_TIPO","B")
        self.oHelper.SetValue("C5_CLIENTE","FAT001")
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetValue("C5_CONDPAG","003")
        
        self.oHelper.SetValue("C6_PRODUTO", "FAT000000000000000000000000014", grid=True)
        self.oHelper.SetValue("C6_QTDVEN", "100,00", grid=True)
        self.oHelper.SetValue("C6_PRCVEN", "100,00", grid=True)
        self.oHelper.SetValue("C6_TES", "511", grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Outras Ações','Beneficia')

        self.oHelper.ClickBox("Ord Producao", "FAT00201001")
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)
        self.oHelper.CheckResult("C5_TIPO","B")
        self.oHelper.CheckResult("C5_CLIENTE","FAT001")
        self.oHelper.CheckResult("C5_CONDPAG","003")

        self.oHelper.CheckResult("Produto", " FAT000000000000000000000000014", grid=True, line=1)
        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.RestoreParameters()

        self.oHelper.AssertTrue()        

    def test_MATA410_210(self):
        '''
            Ativar parâmetro MV_CNPEDVE
        '''
        self.oHelper.AddParameter("MV_EMPBN","D MG 01",".T.",".T.",".T.")
        self.oHelper.AddParameter("MV_CNPEDVE","D MG 01",".T.",".T.",".T.")
        self.oHelper.SetParameters()

        order = 'FATT47'

        self.oHelper.SetButton('Incluir')

        self.oHelper.SetBranch("D MG 01 ")
        
        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_TIPO","N")
        self.oHelper.SetValue("C5_CLIENTE","FAT001")
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetFocus("C5_CLIENTE")

        self.oHelper.SetKey("F9")
        self.oHelper.SetValue("Nr. Contrato","GS_TECA870_0001")
        self.oHelper.ClickBox("Nr Planilha", "000001")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Cancelar")
        #Aguardando correção da Task 1558 subir para branch Master 
        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()        
        '''
        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)
        self.oHelper.SetButton("Cancelar")

        self.oHelper.RestoreParameters()

        self.oHelper.AssertFalse()       
        '''
    def test_MATA410_211(self):
        '''
            Código de barra - Não funciona
        '''

        order = 'FAT248'

        self.oHelper.SetButton('Cod.barra',sub_item='Incluir')

        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_TIPO","N")
        self.oHelper.SetValue("C5_CLIENTE","FAT001")
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetValue("C5_CONDPAG","003")

        self.oHelper.SetFocus('Produto', grid_cell = True)

        self.oHelper.SetValue("C6_PRODUTO", "FAT000000000000000000000000014", grid=True)
        self.oHelper.SetValue("C6_QTDVEN", "100,00", grid=True)
        self.oHelper.SetValue("C6_PRCVEN", "100,00", grid=True)
        self.oHelper.SetValue("C6_TES", "511", grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()        

    def test_MATA410_212(self):
        '''
            Teste com Grade - Alteraçõo
        '''

        self.oHelper.AddParameter("MV_GRADE","D MG 01",".T.",".T.",".T.")
        self.oHelper.SetParameters()

        order = 'FAT999'

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("C5_CONDPAG","001")
        
        self.oHelper.SetFocus('Quantidade', grid_cell = True)
        self.oHelper.SetKey('ENTER')
        self.oHelper.WaitShow("Totais da Grade")
        self.oHelper.SetValue("[GG] GRANDE", "1,00", grid=True,row=1) 
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)
        self.oHelper.CheckResult("C5_CONDPAG", "001")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.RestoreParameters()        

        self.oHelper.AssertTrue()
    
    def test_MATA410_213(self):
                
        self.oHelper.SetButton('Outras Ações','Retornar')
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Dt. Entrada De","01012001")
        self.oHelper.SetValue("Dt. Entrada Ate","31122049")        
        self.oHelper.SetFocus("Fornecedor")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse(f"FTR21301", "Código")
        self.oHelper.SetButton("Ok")        
        self.oHelper.ClickCheckBox("Documento",1)
        self.oHelper.SetButton("Ok")                
        self.oHelper.SetButton("Retorno")               
        self.oHelper.CheckResult("C5_TIPO","D")       
        self.oHelper.CheckResult("C5_CLIENTE","FTR213")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("X")
        self.oHelper.AssertTrue()

    def test_MATA410_214(self):
      
        self.oHelper.SetButton('Outras Ações','Retornar')
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Dt. Entrada De","01012001")        
        self.oHelper.SetValue("Dt. Entrada Ate","31122049")
        self.oHelper.SetFocus("Fornecedor")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse(f"FTR21301", "Código")
        self.oHelper.SetButton("Ok")        
        self.oHelper.ClickCheckBox("Fornecedor",2)
        self.oHelper.SetButton("Ok")
        self.oHelper.ClickBox("Filial", "D MG 01", grid_number=1 )
        self.oHelper.SetButton("Retorno")        
        self.oHelper.CheckResult("C5_TIPO","D")
        self.oHelper.CheckResult("C5_CLIENTE","FTR213")
        self.oHelper.SetButton("Salvar")
        self.oHelper.AssertTrue()

    def test_MATA410_223(self):

        '''
            Alteração de Pedido de Venda
        '''

        order = 'FAT509'

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Alterar")
  
        self.oHelper.SetValue("C5_CONDPAG","001")
        self.oHelper.WaitFieldValue("C5_DESC4", "0,00")

        self.oHelper.CheckResult("Prc Unitario", '1.000,00', grid=True, line=1)
        self.oHelper.CheckResult("Prc Unitario", '100,00', grid=True, line=2)
        self.oHelper.LoadGrid()

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()