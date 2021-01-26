from tir import Webapp
import unittest

class CTBA012(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "08/07/2019", "T1", "M SP 02 ", "34")

        inst.oHelper.Program("CTBA010")

    def test_CTBA012_003(self):

        cCalend     = "235"
        cExerc      = "2035"
        cPeriod     = "04"

        self.oHelper.SearchBrowse(f"M SP 02 {cCalend+cExerc+cPeriod}")

        self.oHelper.SetButton("Outras ações", "Bloqueio de Processo")
        
        self.oHelper.ClickGridCell("Dt Final", row =3,grid_number=1)  
        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Outras ações", "Multipla")

        self.oHelper.SetValue("Status do Processo ? ", "2 - Bloquea")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"M SP 02 {cCalend+cExerc+cPeriod}")
        
        self.oHelper.SetButton("Outras ações", "Bloqueio de Processo")

        self.oHelper.WaitShow("Bloqueio de Processo - Alteração - Bloqueio de Processo")

        self.oHelper.ClickGridCell("Dt Final", row =3,grid_number=1)  

        self.oHelper.LoadGrid() 

        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=1, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=2, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=3, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=4, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=5, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=6, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=7, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=8, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=9, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=10, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=11, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=12, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=13, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=14, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=15, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=16, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=17, grid_number=2)
        self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=18, grid_number=2)
        # self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=19, grid_number=2)
        # self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=20, grid_number=2)
        # self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=21, grid_number=2)
        # self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=22, grid_number=2)
        # self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=23, grid_number=2)
        # self.oHelper.CheckResult("Status bloq.", "Bloqueado", grid=True, line=24, grid_number=2)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()


        
        