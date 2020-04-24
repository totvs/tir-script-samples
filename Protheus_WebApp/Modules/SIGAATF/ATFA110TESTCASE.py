from tir import Webapp
import unittest
class ATFA110(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAATF", "30/03/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA110")

        inst.oHelper.AddParameter("MV_ULTDEPR", "", "20160229")
        inst.oHelper.AddParameter("MV_ATFCTAP", "", "1")
        inst.oHelper.SetParameters()

    def test_ATFA110_001(self):

        codigoATF   = 'ATF_APT001'
        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}0001")
        self.oHelper.SetButton("Outras Ações", "Apt. multiplos")
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("FNA_DATA", "25/03/2016")
        self.oHelper.SetValue("FNA_OCORR", "P8 - Estorno de revisão de estim. de produção")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetValue("Filial       ?", "D MG 01")
        self.oHelper.SetValue("ID Movto.    ?", "0000000016")

        self.oHelper.SetButton("OK")

        self.oHelper.ClickBox("Cod Base Bem", grid_number=1, select_all=True)
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}0001")
        self.oHelper.SetButton("Apontamento")

        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("FNA_DATA", "26/03/2016")
        self.oHelper.SetValue("FNA_OCORR", "P1 - Revisão de estimativa de produção")
        self.oHelper.SetValue("FNA_QUANTD", "2,00")
        
        self.oHelper.SetButton("Cancelar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

        
