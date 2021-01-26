from tir import Webapp
import unittest

class PCOA120(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAPCO", "05/09/2019", "T1", "M SP 01 ", "57")
        inst.oHelper.Program("PCOA120")

    def test_PCOA120_001(self):

        self.oHelper.SearchBrowse("D MG 01 0000001")
        
        self.oHelper.SetButton("Iniciar Revisao")
        self.oHelper.SetButton("Salvar")

        self.oHelper.AssertTrue()

    def test_PCOA120_002(self):

        self.oHelper.AddParameter("MV_PCOBLRM", "", "1")
        self.oHelper.SetParameters()
        
        self.oHelper.SearchBrowse("D MG 01 PCOA120REVISAR")
        self.oHelper.SetButton("Outras Ações",'Revisar')

        self.oHelper.SetFocus("Descricao",grid_cell=True,row_number=2)
        self.oHelper.ClickGridCell("Descricao", row=3,grid_number=1)
        self.oHelper.SetButton("Outras Ações",'Ferram.')

        self.oHelper.ClickMenuPopUpItem("Reajustar Valores Orcados")
        self.oHelper.ClickLabel('Por Percentual Embutido')
        self.oHelper.ClickLabel('Substituir Valor')

        self.oHelper.SetValue('Valor ou Percentual ?','100,00')

        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
