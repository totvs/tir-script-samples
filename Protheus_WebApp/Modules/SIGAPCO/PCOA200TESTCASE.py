from tir import Webapp
import unittest

class PCOA200(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAPCO", "05/09/2019", "T1", "M SP 01 ", "57")
        inst.oHelper.Program("PCOA200")

        
    def test_PCOA200_003(self):
        
        self.oHelper.SearchBrowse("M SP 01 SIM00000000  ")
        self.oHelper.SetButton("Outras Ações",'Efetivar')
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitShow('Simulacao efetivada com sucesso.')
        self.oHelper.SetButton("Ok")

        self.oHelper.AssertTrue()
            
    def test_PCOA200_001(self):

        self.oHelper.AddParameter("MV_PCOTHRD", "", "2") ###ao tentar efetivar com esse parametro gera error log
        self.oHelper.AddParameter("MV_PCOMTHR", "", "1") ###ao tentar efetivar com esse parametro gera error log
        self.oHelper.SetParameters()
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Planilha Orc", "PCOAUT_A22")
        self.oHelper.SetValue("Versao Sim.", "0002")
        self.oHelper.SetValue("Descricao", "AUTOMACAO PCOA122 - MULTITHR")

        self.oHelper.SetButton("Salvar")

        self.oHelper.WaitProcessing("Processando...")
        self.oHelper.WaitProcessing("Processando...")
 
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse("D MG 01 PCOAUT_A22")

        self.oHelper.AssertTrue()

    def test_PCOA200_002(self):
        
        self.oHelper.SearchBrowse("M SP 01 PCO0000010002")
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetFocus("Descricao",grid_cell=True,row_number=2)
        self.oHelper.ClickGridCell("Descricao", row=4,grid_number=1)

        self.oHelper.SetButton('Editar')
        self.oHelper.SetValue("Item Contab.", "PCOA200",grid=True,grid_number=2,row=1)
        self.oHelper.SetValue("Classe Orc.", "FORMT4",grid=True,grid_number=2,row=1)

        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Gravar')

        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
