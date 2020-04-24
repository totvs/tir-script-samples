from tir import Webapp
import unittest

class CTBR295(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "15/04/2015", "T1", "D MG 01 ", "34")
        inst.oHelper.Program("CTBR295")

    @classmethod
    def test_CTBR295_001(self):
        self.oHelper.SetValue("mv_par01", "03/02/2017", name_attr=True)
        self.oHelper.SetValue("mv_par02", "03/02/2017", name_attr=True)
        self.oHelper.SetValue("mv_par03", "10000", name_attr=True)
        self.oHelper.SetValue("mv_par04", "10001", name_attr=True)
        self.oHelper.SetValue("mv_par06", "ZZZZZZZZZ", name_attr=True)
        self.oHelper.SetValue("mv_par08", "ZZZZZZZZZ", name_attr=True)
        self.oHelper.SetValue("mv_par10", "ZZZZZZZZZ", name_attr=True)
        self.oHelper.SetValue("mv_par11", "01")
        self.oHelper.SetValue("mv_par12", "1")
        self.oHelper.SetValue("mv_par13", "1")
        self.oHelper.SetValue("mv_par14", "")
        self.oHelper.SetValue("Saldos Zerados ?", "Sim")
        self.oHelper.SetValue("Comparar ?", "Mov. Periodo")
        self.oHelper.SetValue("mv_par17", "1")
        self.oHelper.SetValue("Imprime Cod. Conta ?", "Normal")
        self.oHelper.SetValue("Imprime Cod. C.C ?", "Normal")
        self.oHelper.SetValue("Imprime Cod. Item ?", "Normal")
        self.oHelper.SetValue("Imprime Valor 0,00 ?", "Sim")
        self.oHelper.SetValue("Divide por ?", "Nao Aplica")
        self.oHelper.SetValue("Posicao Ant. L/P ?", "Nao")
        self.oHelper.SetValue("mv_par24", "")
        self.oHelper.SetValue("Imp.Var.Percentual ?          ", "Sim/Todas")
        self.oHelper.SetValue("Imp. Dif. em Valor ?", "Sim/Todas")
        self.oHelper.SetValue("Imp.Descricoes ?", "Sim")
        self.oHelper.SetValue("Usa Conta ?", "Sim")
        self.oHelper.SetValue("Usa C.Custo ?", "Nao")
        self.oHelper.SetValue("Usa Item Contabil ?", "Nao")
        self.oHelper.SetValue("Usa Classe de Valor ?", "Sim")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("Ordenar por ?", "CONTA")
        self.oHelper.SetValue("Depois por ?", "Cod Cl Val")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("OK")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
