from tir import Webapp
import unittest

class TECA190D(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATEC','01/12/2020','T1','D MG 01 ','28')
        inst.oHelper.Program('TECA190D')
    def test_TECA190D_CT001(self):
        self.oHelper.SetValue('Código do Atendente', 'TEC01900000002')
        self.oHelper.SetValue('Data Inicial', '01/02/2020')
        self.oHelper.SetValue('Data Final', '30/03/2020')

        self.oHelper.CheckResult('Código do Atendente', 'TEC01900000002')
        self.oHelper.CheckResult('Data Inicial', '01/02/2020')
        self.oHelper.CheckResult('Data Final', '30/03/2020')

        self.oHelper.SetButton("Outras Ações","Calendario")
        self.oHelper.WaitHide("Montando calendário...")
        self.oHelper.ClickIcon("SAIR")
        self.oHelper.AssertTrue()
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
