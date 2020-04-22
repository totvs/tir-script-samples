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
        # self.oHelper.SetButton("Param")
        # --
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


    def test_CTBA280_002(self):
        
        self.oHelper.Program("CTBA280")

        self.oHelper.SetButton("Param.")

        self.oHelper.SetValue("Data de Referência ?", "10/05/2015"	)	#Data de ReferÃªncia ?
        self.oHelper.SetValue("Numero do Lote ?","RATOFF"	)	#Numero do Lote ?
        self.oHelper.SetValue("Numero do Sub-Lote ?","001"	)	#Numero do Sub-Lote ?
        self.oHelper.SetValue("Numero do Documento ?","000001"	)	#Numero do Documento ?
        self.oHelper.SetValue("Cod. Hist Padrao ?","002"	)	#Cod. Hist Padrao ?
        self.oHelper.SetValue("Do rateio ?","000001"	)	#Do rateio ?
        self.oHelper.SetValue("Ate o rateio ?","000001"	)	#Ate o rateio ?
        self.oHelper.SetValue("Moedas ?","Especifica"	)	#Moedas ?
        self.oHelper.SetValue("Qual Moeda ?","01"	)	#Qual Moedas ?
        self.oHelper.SetValue("Tipo de Saldo ?","1"	)	#Tipo de Saldo ?
        self.oHelper.SetValue("Seleciona Filiais ?","Sim"	)	#Seleciona Filiais ?
        self.oHelper.SetValue("Filial de ?", "D RJ 02")	#Filial de ?
        self.oHelper.SetValue("Filial Até ?", "D RJ 02"	)	#Filial até ?
        self.oHelper.SetValue("Atualiza Saldo ?", "No Final"	)	#Atualiza Saldo ?

        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_CTBA280_003(self):
        
        self.oHelper.Program("CTBA280")
        
        self.oHelper.SetButton("Param.")

        self.oHelper.SetValue("Data de Referência ?","11/05/2015"	)	#Data de ReferÃªncia ?
        self.oHelper.SetValue("Numero do Lote ?","RATOFF"	)	#Numero do Lote ?
        self.oHelper.SetValue("Numero do Sub-Lote ?","001"	)	#Numero do Sub-Lote ?
        self.oHelper.SetValue("Numero do Documento ?","000001"	)	#Numero do Documento ?
        self.oHelper.SetValue("Cod. Hist Padrao ?","002"	)	#Cod. Hist Padrao ?
        self.oHelper.SetValue("Do rateio ?","000002"	)	#Do rateio ?
        self.oHelper.SetValue("Ate o rateio ?","000002"	)	#Ate o rateio ?
        self.oHelper.SetValue("Moedas ?","Especifica"	)	#Moedas ?
        self.oHelper.SetValue("Qual Moeda ?","01"	)	#Qual Moedas ?
        self.oHelper.SetValue("Tipo de Saldo ?","1"	)	#Tipo de Saldo ?
        self.oHelper.SetValue("Seleciona Filiais ?","Sim"	)	#Seleciona Filiais ?
        self.oHelper.SetValue("Filial de ?","D RJ 02"	)	#Filial de ?
        self.oHelper.SetValue("Filial Até ?","D RJ 02"	)	#Filial AtÃ© ?
        self.oHelper.SetValue("Atualiza Saldo ?","Durante"	)	#Atualiza Saldo ?

        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

#----
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
