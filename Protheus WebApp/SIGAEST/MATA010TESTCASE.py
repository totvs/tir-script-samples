from tir import Webapp
import unittest
import time
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")
#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA010 - Inclusão e Visualização de Produto
#TABELA SB1
#
#@author ADRIANO VIEIRA
#@since 04/17/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATA010(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAADV","25/11/2019","T1","D MG 01 ","04")
        # inst.oHelper.Program("MATA010")
        inst.oHelper.SetLateralMenu('Atualizações > Cadastros > Produto > Produtos')

    def test_MATA010_001(self):
        
        self.oHelper.AddParameter("MV_CADPROD", "","|SA5|SBZ|SB5|DH5|SGI|","|SA5|SBZ|SB5|DH5|SGI|","|SA5|SBZ|SB5|DH5|SGI|")
        self.oHelper.AddParameter("MV_QALOGIX", "","0","0","0")
        self.oHelper.AddParameter("MV_RASTRO", "","S","S","S")
        self.oHelper.AddParameter("MV_LOCALIZ", "","S","S","S")

        self.oHelper.SetParameters()

        #Incluir/Visualização/Excluir
        cod = 'ESTSE0001100221'
        desc = 'MATA010TIR'

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("B1_COD", cod)
        self.oHelper.SetValue("B1_DESC",desc)
        self.oHelper.SetValue("B1_TIPO",'PA')
        self.oHelper.SetValue("B1_UM",'UN')
        self.oHelper.SetValue("B1_LOCPAD",'01')
        self.oHelper.SetValue("B1_LOCALIZ",'S')
        self.oHelper.SetValue("B1_RASTRO",'L')
        

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("B1_COD", cod)

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")

        self.oHelper.SetButton('Outras Ações','Excluir')

        self.oHelper.CheckResult("B1_COD", cod)

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    
    def test_MATA010_002(self):
        
        #Incluir/Alterar/Excluir
        cod2 = 'ESTSE0001200221'
        desc2 = 'MATA010TIR'
        descAlt = 'MATA010TIR ALTERADO'

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("B1_COD", cod2)
        self.oHelper.SetValue("B1_DESC",desc2)
        self.oHelper.SetValue("B1_TIPO",'PA')
        self.oHelper.SetValue("B1_UM",'UN')
        self.oHelper.SetValue("B1_LOCPAD",'01')

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {cod2}", "Filial+codigo")

        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("B1_DESC",descAlt)

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {cod2}", "Filial+codigo")

        self.oHelper.SetButton('Outras Ações','Excluir')

        self.oHelper.CheckResult("B1_COD", cod2)

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()
    
    def test_MATA010_003(self):
        
        #Incluir/Copia
        cod3 = 'ESTSE0001300221'
        cod31 = 'ESTSE0003100221'
        desc3 = 'MATA010TIR'
        desc31 = 'MATA010TIR COPIA'

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue("B1_COD", cod3)
        self.oHelper.SetValue("B1_DESC",desc3)
        self.oHelper.SetValue("B1_TIPO",'PA')
        self.oHelper.SetValue("B1_UM",'UN')
        self.oHelper.SetValue("B1_LOCPAD",'01')
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {cod3}", "Filial+codigo")

        self.oHelper.SetButton('Outras Ações','Copia')

        self.oHelper.SetValue("B1_COD", cod31)
        self.oHelper.SetValue("B1_DESC",desc31)
        self.oHelper.SetValue("B1_TIPO",'PA')
        self.oHelper.SetValue("B1_UM",'UN')
        self.oHelper.SetValue("B1_LOCPAD",'01')

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()   
    
    def test_MATA010_004(self):
        
        #Inclusao Preechendo B1/B5/A5/GI - MV_CADPROD - Alteração/Vizualização/Exclusão

        cod = 'ESTSE0000000000000000000000T20'
        desc = 'ESTSE0000000000000000000000T20'
        cod2 = "ESTSE0000000000000000000000T19"

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("B1_COD", cod)
        self.oHelper.SetValue("B1_DESC",desc)

        self.oHelper.F3(field='B1_TIPO', name_attr=True)
        self.oHelper.SearchBrowse(f'PA', 'Código')
        self.oHelper.SetButton('Ok')

        self.oHelper.F3(field='B1_UM', name_attr=True)
        self.oHelper.SearchBrowse(f'UN', 'Código')
        self.oHelper.SetButton('Ok')

        self.oHelper.F3(field='B1_LOCPAD', name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue("B1_CONV", "1,00")
        self.oHelper.SetValue("B1_PRV1", "1,00")
        self.oHelper.SetValue("B1_CUSTD", "1,00")
        self.oHelper.SetValue("B1_UPRC", "1,00")

        self.oHelper.SetValue("B5_CEME",cod)
        self.oHelper.ClickGridCell("Fornecedor", 1)
        self.oHelper.SetValue("A5_FORNECE","FORN01", grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.ClickGridCell("Alternativo", 1, grid_number=2)
        self.oHelper.SetValue("GI_PRODALT",cod2, grid=True, grid_number=2)
        self.oHelper.LoadGrid()

        self.oHelper.ClickFolder("Impostos")
        self.oHelper.SetValue("B1_PICM", "1,00")
        self.oHelper.SetValue("B1_IPI", "1,00")
        self.oHelper.SetValue("B1_ORIGEM", "1")

        self.oHelper.ClickFolder("MRP / Suprimentos")
        self.oHelper.SetValue("B1_QE", "1.00")

        self.oHelper.ClickFolder("C.Q.")
        self.oHelper.SetValue("B1_NOTAMIN", "1")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")

        self.oHelper.SetButton("Alterar")
        self.oHelper.SetValue("B1_DESC","ALTERADO")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")

        self.oHelper.SetButton('Outras Ações','Excluir')

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    def test_MATA010_005(self):

        
        #Incluir/Visualização/Excluir
        cod = 'ESTSE00000000000000000023750PA'

        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")

        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("B1_LOCALIZ",'S')
        self.oHelper.SetButton("Fechar")
              

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("B1_LOCALIZ", 'S')
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    def test_MATA010_006(self):    
        
        cod = 'ESTSE0000000000000000000000001'
        cod2 = 'ESTSE0000000000000000000000002'
        
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton('Outras Ações','Alternativos')
        self.oHelper.SetValue("Alternativo",cod2, grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')
        
        self.oHelper.AssertTrue()

    def test_MATA010_007(self):    
        
        cod = 'ESTSE0000000000000000000000001'
        
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton('Outras Ações','Facilitador')
        self.oHelper.SetButton('Cancelar')
        
        self.oHelper.AssertTrue()   

    def test_MATA010_008(self):    
        
        self.oHelper.AddParameter("MV_HISTFIS", "",".T.",".T.",".T.")
        self.oHelper.SetParameters()
        
        
        cod = 'EST000000000000000000000000016'
        
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetButton('Outras Ações','Opcionais')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Histórico')
        self.oHelper.SetButton('Sair')
        
        self.oHelper.AssertTrue() 

    def test_MATA010_009(self):    
        
        cod = 'EST000000000000000000000000016'
        
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton('Outras Ações','Consulta')
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.AssertTrue()          

    def test_MATA010_010(self):    
        
        cod = 'EST000000000000000000000000016'

        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        time.sleep(5)
        self.oHelper.SetKey("F4")
        self.oHelper.SetButton("Voltar")
        
        self.oHelper.AssertTrue()  

    def test_MATA010_011(self):    

        # self.oHelper.AddParameter("MV_QALOGIX", "","0","0","0")
        # self.oHelper.SetParameters()
        
        cod = 'ESTSE0000000000000000000000420'
        
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton("Alterar")
        self.oHelper.SetValue("Forn. Padrao", "")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()  

    def test_MATA010_012(self):    
        
        cod = 'ESTSE0000000000000000000009999'
        desc = 'PROD COM COD BARRA'

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("B1_COD", cod)
        self.oHelper.SetValue("B1_DESC",desc)
        self.oHelper.SetValue("B1_TIPO",'PA')
        self.oHelper.SetValue("B1_UM",'UN')
        self.oHelper.SetValue("B1_LOCPAD",'01')
        self.oHelper.SetValue("B1_CODBAR", "1635")
        self.oHelper.SetValue("B1_CODGTIN", "1635")
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")     
        
        self.oHelper.AssertTrue()  

    def test_MATA010_013(self):    
        
        self.oHelper.AddParameter("MV_QALOGIX", "","1","1","1")
        self.oHelper.SetParameters()

        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Fechar") 
        
        self.oHelper.AssertTrue()  

    def test_MATA010_014(self):    
        
        time.sleep(5)
        self.oHelper.SetButton("x")
        self.oHelper.ChangeEnvironment("25/11/2019", "T1","D MG 01 ","73")
        time.sleep(10)
        self.oHelper.SetLateralMenu('Atualizações > Administração > Portfólio > Produtos')
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Fechar") 
        self.oHelper.SetButton("Outras Ações", "Relacionadas, Conhecimento")
        self.oHelper.SetButton("Cancelar")   
        
        self.oHelper.AssertTrue()   

    def test_MATA010_015(self):    
        
        self.oHelper.AddParameter("MV_EIC0011", "",".T.",".T.",".T.")
        self.oHelper.SetParameters()

        time.sleep(5)
        self.oHelper.SetButton("x")
        self.oHelper.ChangeEnvironment("25/11/2019", "T1","D MG 01 ","17")
        time.sleep(10)

        self.oHelper.SetLateralMenu('Atualizações > Cadastros > Produtos')
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()            
 
    def test_MATA010_016(self):    
        
        self.oHelper.AddParameter("MV_QALOGIX", "","0","0","0")
        self.oHelper.SetParameters()

        cod = 'ESTSE0000000000000000000000422'
        
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()          

    def test_MATA010_017(self):    

        cod = 'ESTSE0000000000000000000000423'
        
        self.oHelper.AddParameter("MV_QALOGIX", "","0","0","0")
        self.oHelper.SetParameters()
        time.sleep(5)
        self.oHelper.SetButton("x")
        self.oHelper.ChangeEnvironment("25/11/2019", "T1","D MG 01 ","17")
        time.sleep(10)
        self.oHelper.SetLateralMenu('Atualizações > Cadastros > Produtos')
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_MATA010_018(self):

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("B1_COD", "DMANMAT01-26543PROD00000000001")
        self.oHelper.SetValue("B1_DESC", "DMANMAT01-26543PROD00000000001")
        self.oHelper.SetValue("B1_TIPO", "PA")
        self.oHelper.SetValue("B1_UM", "UN")
        self.oHelper.SetValue("B1_LOCPAD", "01")
        self.oHelper.SetValue("B1_PROC", "ESTBLQ")
        self.oHelper.SetValue("B1_LOJPROC", "01")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("REGBLOQ")
        self.oHelper.AssertTrue()

    def test_MATA010_019(self):     
        #GTSER-T49508 
        #Consulta padrao de armazem e ncm     
        cod = 'ESTSE0000000000000000000000424'         
        desc = 'ESTSE0000000000000000000000424'

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("B1_COD", cod)
        self.oHelper.SetValue("B1_DESC",desc)
        self.oHelper.SetValue("B1_TIPO",'PA')
        self.oHelper.SetValue("B1_UM",'UN')

        #consulta padrao armazem
        self.oHelper.SetFocus("B1_LOCPAD")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse("02")
        self.oHelper.SetButton("OK")

        #Consulta padrao ncm         
        self.oHelper.ClickFolder("Impostos")
        self.oHelper.SetFocus("B1_POSIPI")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse("01019090")
        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("B1_COD", cod)

        self.oHelper.SetButton("Fechar")      
        
        self.oHelper.AssertTrue()
   
    def test_MATA010_020(self):
        #GTSER-T28892
        #Incluir/Visualização/Excluir
        cod = 'ESTSE0000000092'

        time.sleep(5)
        self.oHelper.SetButton("x")
        self.oHelper.ChangeEnvironment(DateSystem, "T1","D MG 01 ","04")
        self.oHelper.SetLateralMenu('Atualizações > Cadastros > Produto > Produtos')

        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")

        self.oHelper.SetButton("Alterar")
        self.oHelper.ClickFolder("Impostos")
        self.oHelper.SetButton("Outras Ações","Opcionais")      
        self.oHelper.ClickBox("Grupos/Itens Opcionais","01 - OPCIONAL 01")
        
        self.oHelper.SetButton("OK")
       
       
        self.oHelper.SetButton("Confirmar")
        
              
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton("Visualizar")    
        self.oHelper.CheckResult("B1_OPC", '7701  /')
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()


        
    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()