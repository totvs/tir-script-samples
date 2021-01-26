from tir import Webapp
import unittest

class PCOA520(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAPCO", "27/12/2019", "T1", "D MG 01 ", "57")

        inst.oHelper.Program("PCOA520")

    ###INCLUIR
    def test_PCOA520_001(self):
        
        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch('D MG 01')

        self.oHelper.SetKey('F3')

        self.oHelper.SearchBrowse('001')
        self.oHelper.SetButton('OK')

        self.oHelper.ClickGridCell('Usuario',row=1)
        self.oHelper.SetKey('F3',grid=True)
        self.oHelper.SearchBrowse('000239')
        self.oHelper.SetButton('OK')

        self.oHelper.SetButton('Salvar')
        self.oHelper.CheckHelp(text='NONIVELPCOA520',button='Fechar')

        self.oHelper.SetValue('Nivel','1',grid=True,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Cancelar')
        
        self.oHelper.AssertTrue()
    
        ##Visualizar
    def test_PCOA520_002(self):

        codigo ='BL2'
        self.oHelper.SearchBrowse(f"D MG 01 {codigo}01", "Filial+codigo + Item                                                         ") 

        self.oHelper.SetButton("Visualizar")

        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.AssertTrue()
    
        ##Alterar
    def test_PCOA520_003(self):

        codigo ='BL2'
        self.oHelper.SearchBrowse(f"D MG 01 {codigo}01", "Filial+codigo + Item                                                         ") 

        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue('Descrição','BLOQUEIO AUTOM ALTER')

        self.oHelper.SetButton("Salvar")
        
        self.oHelper.AssertTrue()
    
        ##Excluir
    def test_PCOA520_004(self):

        codigo ='BL '
        self.oHelper.SearchBrowse(f"M SP 01 {codigo}01", "Filial+codigo + Item                                                         ") 

        self.oHelper.SetButton("Outras Ações",'Excluir')

        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()