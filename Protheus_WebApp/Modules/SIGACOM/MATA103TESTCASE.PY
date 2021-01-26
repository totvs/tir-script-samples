from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA103 - Nota fiscal de entrada
#@author Leandro Nishihata
#@since 14/05/2020
#@version P12
#//-------------------------------------------------------------------

class MATA103(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACOM","26/11/2020","T1","D MG 01 ","02")
        inst.oHelper.Program("MATA103")

    #CRUD
   
    def test_MATA103_001(self):
        nf1 = 'COMTIREXC'
        nf2 = 'COMTIRALC'

        #Incluir
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.WaitShow("Documento de Entrada - INCLUIR")
        self.oHelper.SetValue("Form. Prop.", 'Sim')
        self.oHelper.F3(field='Fornecedor', name_attr=False,send_key=True)
        self.oHelper.SearchBrowse(f'000003', 'Código')
        self.oHelper.SetButton("Ok")
        self.oHelper.F3(field='Espec.Docum.', name_attr=False,send_key=True)
        self.oHelper.SearchBrowse(f'SPED', 'Código')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetFocus("Produto", grid_cell = True)
        self.oHelper.SetKey("F3",grid=True)
        self.oHelper.SearchBrowse(f'COMTIR3', 'Código')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton('Outras Ações','Pedido')
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton('Outras Ações','Item Ped')
        self.oHelper.WaitShow("Documento de Entrada - INCLUIR")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetButton("Salvar")            
        self.oHelper.ClickFolder("Duplicatas")
        self.oHelper.SetValue("Cond. Pagto", "001")
        self.oHelper.SetButton('Outras Ações','Rat. CC')
        self.oHelper.SetButton('Outras Ações','Rat.Pre')  
        time.sleep(1)        
        self.oHelper.SetKey("F3")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetFocus("Tipo Entrada", grid_cell = True)
        self.oHelper.SetKey("F3",grid=True)
        self.oHelper.SearchBrowse(f'018', 'Código')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetKey("ENTER")     
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Ok")
        self.oHelper.AssertTrue()
        self.oHelper.SetButton("Cancelar")

        #Visualizar
        self.oHelper.SearchBrowse("D MG 01 "+ nf2)     
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Documento de Entrada - VISUALIZAR")
        self.oHelper.SetButton('Outras Ações','Cons.Aprov')        
        self.oHelper.SetButton("Fechar")      
        self.oHelper.SetButton('Outras Ações','Tracker')        
        self.oHelper.SetButton("Rastrear")
        self.oHelper.SetButton("Abandonar")            
        self.oHelper.SetButton('Outras Ações','Conhecim.')        
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton('Outras Ações','Rat.Veic')
        self.oHelper.WaitShow("Documento de Entrada - VISUALIZAR")
        self.oHelper.SetButton("Cancelar")        
        self.oHelper.SetButton('Outras Ações','Rat.Frota')
        self.oHelper.WaitShow("Documento de Entrada - VISUALIZAR")
        self.oHelper.SetButton("Cancelar")   
        self.oHelper.SetButton('Outras Ações','Rat. CC')
        self.oHelper.WaitShow("Documento de Entrada - VISUALIZAR")
        self.oHelper.SetButton("Cancelar")   
        self.oHelper.SetButton('Outras Ações','Historico')
        self.oHelper.SetButton("Sair")   
        self.oHelper.SetButton('Outras Ações','Apos.Especial')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
                
        #Excluir
        self.oHelper.SearchBrowse("D MG 01 "+ nf1)       
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.AssertTrue()
        

        #Retornar     
        self.oHelper.SetButton('Outras Ações','Retornar')
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.F3(field='Fornecedor', name_attr=False,send_key=True)
        self.oHelper.SearchBrowse(f'000005', 'Código')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton('Confirmar') 
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Ok")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
