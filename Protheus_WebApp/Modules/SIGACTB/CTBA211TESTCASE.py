from tir import Webapp
import unittest


class CTBA211(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "30/06/2015", "T1", "M PR 02 ", "34")

        inst.oHelper.Program("CTBA211")

        
     ###########################################################################################
    # Caso de teste 001 - Incluir Rateio                                                       #
    # 29/08/2019                                                                               #
    ###########################################################################################

    def test_CTBA211_001(self):

        self.oHelper.ClickTree("Apuracao de Lucros / Perdas > Perguntas")
        
        #Perguntes
        self.oHelper.SetValue("mv_par01", "01062015")
        self.oHelper.SetValue("mv_par02", "30062015")
        self.oHelper.SetValue("mv_par03", "APUR15")
        self.oHelper.SetValue("mv_par04", "001")
        self.oHelper.SetValue("mv_par05", "000001")
        self.oHelper.SetValue("mv_par06", "001")
        self.oHelper.SetValue("mv_par07", "CTB211ELC")
        self.oHelper.SetValue("mv_par08", "CTB211ELD")
        self.oHelper.SetValue("Moedas ?", "Todas") #Todas / Específica
        self.oHelper.SetValue("mv_par10", "01")
        self.oHelper.SetValue("Considera Ent.Ponte ?", "Sim")
        self.oHelper.SetValue("mv_par12", "1")
        self.oHelper.SetValue("Considera Entidades ?", "Rotina de Apur.")
        self.oHelper.SetValue("mv_par14", "CTB211CP")
        self.oHelper.SetValue("mv_par15", "CTB211CA")
        self.oHelper.SetValue("mv_par16", "")
        self.oHelper.SetValue("mv_par17", "")
        self.oHelper.SetValue("mv_par18", "")
        self.oHelper.SetValue("mv_par19", "")
        self.oHelper.SetValue("mv_par20", "")
        self.oHelper.SetValue("mv_par21", "")
        self.oHelper.SetValue("mv_par22", "")
        self.oHelper.SetValue("mv_par23", "ZZZZZZZZZ")
        self.oHelper.SetValue("mv_par24", "")
        self.oHelper.SetValue("mv_par25", "ZZZZZZZZZ")
        self.oHelper.SetValue("mv_par26", "")
        self.oHelper.SetValue("mv_par27", "ZZZZZZZZZ")
        self.oHelper.SetValue("Reproces. Saldos ?", "Sim")#
        self.oHelper.SetValue("Seleciona Filiais ?", "Sim")#
        self.oHelper.SetValue("mv_par30", "M PR 02")
        self.oHelper.SetValue("mv_par31", "M PR 02")
        


        self.oHelper.ClickIcon("Iniciar Execução")

        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Sim")

        self.oHelper.Program("CTBA211")

        self.oHelper.AssertTrue()

    def test_CTBA211_002(self):
        
        self.oHelper.ClickTree("Apuracao de Lucros / Perdas > Perguntas")
        
        #Perguntes
        self.oHelper.SetValue("mv_par01", "01052014")
        self.oHelper.SetValue("mv_par02", "31052014")
        self.oHelper.SetValue("mv_par03", "")
        self.oHelper.SetValue("mv_par04", "")
        self.oHelper.SetValue("mv_par05", "")
        self.oHelper.SetValue("mv_par06", "006")
        self.oHelper.SetValue("mv_par07", "")
        self.oHelper.SetValue("mv_par08", "")
        self.oHelper.SetValue("Moedas ?", "Todas") #Todas / Específica
        self.oHelper.SetValue("mv_par10", "")
        self.oHelper.SetValue("Considera Ent.Ponte ?", "Sim")
        self.oHelper.SetValue("mv_par12", "")
        self.oHelper.SetValue("Considera Entidades ?", "Rotina de Apur.")
        self.oHelper.SetValue("mv_par14", "")
        self.oHelper.SetValue("mv_par15", "")
        self.oHelper.SetValue("mv_par16", "")
        self.oHelper.SetValue("mv_par17", "")
        self.oHelper.SetValue("mv_par18", "")
        self.oHelper.SetValue("mv_par19", "")
        self.oHelper.SetValue("mv_par20", "")
        self.oHelper.SetValue("mv_par21", "")
        self.oHelper.SetValue("mv_par22", "")
        self.oHelper.SetValue("mv_par23", "ZZZZZZZZZ")
        self.oHelper.SetValue("mv_par24", "")
        self.oHelper.SetValue("mv_par25", "ZZZZZZZZZ")
        self.oHelper.SetValue("mv_par26", "")
        self.oHelper.SetValue("mv_par27", "ZZZZZZZZZ")
        self.oHelper.SetValue("Reproces. Saldos ?", "Sim")#
        self.oHelper.SetValue("Seleciona Filiais ?", "Sim")#
        self.oHelper.SetValue("mv_par30", "M PR 02")
        self.oHelper.SetValue("mv_par31", "M PR 02")
        


        self.oHelper.ClickIcon("Iniciar Execução")

        self.oHelper.CheckHelp(text_help="CT210NOHP", button="Fechar")
        self.oHelper.CheckHelp(text_help="NOCT210LOT", button="Fechar")
        self.oHelper.CheckHelp(text_help="NOCTSUBLOT", button="Fechar")
        self.oHelper.CheckHelp(text_help="NOCT210DOC", button="Fechar")
        self.oHelper.CheckHelp(text_help="NOCT210CT", button="Fechar")
        self.oHelper.CheckHelp(text_help="NO210TPSLD", button="Fechar")
        self.oHelper.SetButton("Fechar")   

        self.oHelper.Program("CTBA211")

        self.oHelper.AssertTrue()

    def test_CTBA211_003(self):

        self.oHelper.ClickTree("Apuracao de Lucros / Perdas > Perguntas")
        
        #Perguntes
        self.oHelper.SetValue("mv_par01", "")
        self.oHelper.SetValue("mv_par02", "31052014")
        self.oHelper.SetValue("mv_par03", "")
        self.oHelper.SetValue("mv_par04", "")
        self.oHelper.SetValue("mv_par05", "")
        self.oHelper.SetValue("mv_par06", "")
        self.oHelper.SetValue("mv_par07", "")
        self.oHelper.SetValue("mv_par08", "")
        self.oHelper.SetValue("Moedas ?", "Específica") #Todas / Específica
        self.oHelper.SetValue("mv_par10", "01")
        self.oHelper.SetValue("Considera Ent.Ponte ?", "Não")
        self.oHelper.SetValue("mv_par12", "")
        self.oHelper.SetValue("Considera Entidades ?", "Rotina de Apur.") #Cadastros
        self.oHelper.SetValue("mv_par14", "")
        self.oHelper.SetValue("mv_par15", "")
        self.oHelper.SetValue("mv_par16", "")
        self.oHelper.SetValue("mv_par17", "")
        self.oHelper.SetValue("mv_par18", "")
        self.oHelper.SetValue("mv_par19", "")
        self.oHelper.SetValue("mv_par20", "")
        self.oHelper.SetValue("mv_par21", "")
        self.oHelper.SetValue("mv_par22", "")
        self.oHelper.SetValue("mv_par23", "ZZZZZZZZZ")
        self.oHelper.SetValue("mv_par24", "")
        self.oHelper.SetValue("mv_par25", "ZZZZZZZZZ")
        self.oHelper.SetValue("mv_par26", "")
        self.oHelper.SetValue("mv_par27", "ZZZZZZZZZ")
        self.oHelper.SetValue("Reproces. Saldos ?", "Sim")#
        self.oHelper.SetValue("Seleciona Filiais ?", "Sim")#
        self.oHelper.SetValue("mv_par30", "M PR 02")
        self.oHelper.SetValue("mv_par31", "M PR 02")
        


        self.oHelper.ClickIcon("Iniciar Execução")

        self.oHelper.CheckHelp(text_help="CTHPVAZIO", button="Fechar")
        self.oHelper.CheckHelp(text_help="NOCT210LOT", button="Fechar")
        self.oHelper.CheckHelp(text_help="NOCTSUBLOT", button="Fechar")
        self.oHelper.CheckHelp(text_help="NOCT210DOC", button="Fechar")
        self.oHelper.CheckHelp(text_help="NOCT210CT", button="Fechar")
        self.oHelper.CheckHelp(text_help="NO210TPSLD", button="Fechar")
        self.oHelper.SetButton("Fechar") 

        self.oHelper.Program("CTBA211")

        self.oHelper.AssertTrue()
    

    def test_CTBA211_004(self):

        self.oHelper.ClickTree("Apuracao de Lucros / Perdas > Perguntas")
        
        #Perguntes
        self.oHelper.SetValue("mv_par01", "01052014")
        self.oHelper.SetValue("mv_par02", "31052014")
        self.oHelper.SetValue("mv_par03", "")
        self.oHelper.SetValue("mv_par04", "")
        self.oHelper.SetValue("mv_par05", "")
        self.oHelper.SetValue("mv_par06", "")
        self.oHelper.SetValue("mv_par07", "")
        self.oHelper.SetValue("mv_par08", "")
        self.oHelper.SetValue("Moedas ?", "Específica") #Todas / Específica
        self.oHelper.SetValue("mv_par10", "")
        self.oHelper.SetValue("Considera Ent.Ponte ?", "Não")
        self.oHelper.SetValue("mv_par12", "")
        self.oHelper.SetValue("Considera Entidades ?", "Rotina de Apur.") #Cadastros
        self.oHelper.SetValue("mv_par14", "")
        self.oHelper.SetValue("mv_par15", "")
        self.oHelper.SetValue("mv_par16", "")
        self.oHelper.SetValue("mv_par17", "")
        self.oHelper.SetValue("mv_par18", "")
        self.oHelper.SetValue("mv_par19", "")
        self.oHelper.SetValue("mv_par20", "")
        self.oHelper.SetValue("mv_par21", "")
        self.oHelper.SetValue("mv_par22", "")
        self.oHelper.SetValue("mv_par23", "ZZZZZZZZZ")
        self.oHelper.SetValue("mv_par24", "")
        self.oHelper.SetValue("mv_par25", "ZZZZZZZZZ")
        self.oHelper.SetValue("mv_par26", "")
        self.oHelper.SetValue("mv_par27", "ZZZZZZZZZ")
        self.oHelper.SetValue("Reproces. Saldos ?", "Sim")#
        self.oHelper.SetValue("Seleciona Filiais ?", "Sim")#
        self.oHelper.SetValue("mv_par30", "M PR 02")
        self.oHelper.SetValue("mv_par31", "M PR 02")

        self.oHelper.ClickIcon("Iniciar Execução")
        self.oHelper.AssertTrue()
        self.oHelper.WaitShow("NOMOEDA")
        # self.oHelper.SetButton("Fechar") 
        self.oHelper.CheckHelp(text_help="NOMOEDA",button="Fechar")
        # self.oHelper.CheckHelp(text_problem="Moeda não preenchida e/ou não existente.",button="Fechar")
        self.oHelper.WaitShow("TOTVS")
        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
