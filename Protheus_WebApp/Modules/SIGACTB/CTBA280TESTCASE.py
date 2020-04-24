from tir import Webapp
import unittest

class CTBA280(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "29/06/2015", "T1", "M SP 02 ", "34")
        inst.oHelper.Program("CTBA280")

    def test_CTBA280_001(self):
        self.oHelper.SetButton("Param")
        self.oHelper.SetValue("mv_par01", "29/06/2015")  # Data de Referencia ?
        self.oHelper.SetValue("mv_par02", "777776")  # Numero do Lote ?
        self.oHelper.SetValue("mv_par03", "001")  # Numero do Sub-Lote ?
        self.oHelper.SetValue("mv_par04", "777776")  # Numero do Documento ?
        self.oHelper.SetValue("mv_par05", "01")  # Cod. Hist Padrao ?
        self.oHelper.SetValue("mv_par06", "CTLR02")  # Do rateio ?CTRL02
        self.oHelper.SetValue("MV_PAR07", "CTLR02")  # Ate o rateio ?CTRL02
        self.oHelper.SetValue("Moedas ?", "Especifica")  # Moedas ?
        self.oHelper.SetValue("mv_par09", "01")  # Qual Moedas ?
        self.oHelper.SetValue("mv_par10", "1")  # Tipo de Saldo ?
        self.oHelper.SetValue("Seleciona Filiais ?","Sim")  # Seleciona Filiais ?
        self.oHelper.SetValue("Filial de ?", "M SP 02")  # Filial de ?
        self.oHelper.SetValue("Filial Até ?", "M SP 02")  # Filial Ate ?"
        self.oHelper.SetValue("Atualiza Saldo ?", "No Final")  # Atualiza Saldo ?
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Sim")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
