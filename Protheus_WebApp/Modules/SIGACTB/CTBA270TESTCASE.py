from tir import Webapp
import unittest

class CTBA270(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "29/06/2015", "T1", "M SP 02 ", "34")
        inst.oHelper.Program("CTBA270")

    def test_CTBA270_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 02")
        self.oHelper.SetValue("Codigo Rateio", "CTLR02")
        self.oHelper.SetValue("Descricao", "Rateio Incluido")
        self.oHelper.SetValue("Tipo", "1 - Movimento Mes")
        self.oHelper.SetValue("Ctq_CtOri", "11101001", name_attr=True)
        self.oHelper.SetValue("cCtq_CtPar", "11101001", name_attr=True)
        self.oHelper.SetValue("cCtq_CCOri", "01101", name_attr=True)
        self.oHelper.SetValue("cCtq_CCPar", "01101", name_attr=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetValue("CTQ_CTCPAR", "1110100101", grid=True, row=1)
        self.oHelper.SetValue("CTQ_CCCPAR", "0110101", grid=True, row=1)
        self.oHelper.SetValue("CTQ_VALOR", "80,00", grid=True, row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("Down", grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetValue("CTQ_CTCPAR", "1110100102", grid=True, row=2)
        self.oHelper.SetValue("CTQ_CCCPAR", "0110102", grid=True, row=2)
        self.oHelper.SetValue("CTQ_VALOR", "20,00", grid=True, row=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
