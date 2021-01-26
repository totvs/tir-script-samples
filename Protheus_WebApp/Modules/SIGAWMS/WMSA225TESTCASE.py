from tir import Webapp
import unittest
import time

class WMSA225(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAWMS", "10/12/2020", "T1", "M SP 01", "42")
        inst.oHelper.Program("WMSA225")

    def test_WMSA225_CT001(self):
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 01')
        
        self.oHelper.SetValue('Armazém De ?','')
        self.oHelper.SetValue('Armazém Até ?','ZZ')
        self.oHelper.SetValue('Produto De ?','')
        self.oHelper.SetValue('Produto Até ?','ZZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Endereço De ?','')
        self.oHelper.SetValue('Endereço Até ?','ZZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Unitizador De ?','')
        self.oHelper.SetValue('Unitizador Até ?','ZZZZZZ')
        self.oHelper.SetValue('Tipo Transf. ?','Produto')
        self.oHelper.SetButton('Ok')
        
        self.oHelper.ClickBox('Produto','WMS00000G010')
        self.oHelper.SetValue('Quantidade', '1,00', grid=True, grid_number=2)
        self.oHelper.SetValue('Ender Des', 'A010001', grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton('Fechar')

        #self.oHelper.SearchBrowse('M SP 01 005WMS000000047                  ')
        #self.oHelper.SetButton('Outras Ações','Visualizar')
        #self.oHelper.SetButton('Fechar')

        #self.oHelper.SearchBrowse(key=2, index=True)
        #self.oHelper.SearchBrowse('M SP 01 005WMS000025')
        #self.oHelper.SetButton('Excluir')
        #elf.oHelper.SetButton('Confirmar')
        #self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('X')
                
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()

