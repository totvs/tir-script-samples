from tir import Webapp
import unittest


class CTBR295(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        # Endereção do webapp e o nome do Browser
        inst.oHelper = Webapp()

        # Parametros de inicialização
        inst.oHelper.Setup("SIGACTB", "15/04/2015", "T1", "D MG 01 ", "34")

        # Nome da rotina do Caso de Teste
        inst.oHelper.Program("CTBR295")

    @classmethod
    def test_CTBR295_001(self):

        self.oHelper.SetValue("mv_par01", "03/02/2017",
                              name_attr=True)  # Data Inicial
        self.oHelper.SetValue("mv_par02", "03/02/2017",
                              name_attr=True)  # Data Final
        self.oHelper.SetValue("mv_par03", "10000",
                              name_attr=True)  # Conta Inicial
        self.oHelper.SetValue("mv_par04", "10001",
                              name_attr=True)  # Conta Final
        # self.oHelper.SetValue("mv_par05","					", name_attr=True)  #C.C. Inicial
        self.oHelper.SetValue("mv_par06", "ZZZZZZZZZ",
                              name_attr=True)  # C.C. Final
        # self.oHelper.SetValue("mv_par07","					", name_attr=True)  #Item Inicial
        self.oHelper.SetValue("mv_par08", "ZZZZZZZZZ",
                              name_attr=True)  # Item Final
        # self.oHelper.SetValue("mv_par09","					", name_attr=True)  #Classe de Valor Inicial
        self.oHelper.SetValue("mv_par10", "ZZZZZZZZZ",
                              name_attr=True)  # Classe de Valor Final
        self.oHelper.SetValue("mv_par11", "01")  # Moeda? = Real
        self.oHelper.SetValue("mv_par12", "1")  # Saldos? = Reais
        self.oHelper.SetValue("mv_par13", "1")  # Saldos a Comp.? = Previsto
        self.oHelper.SetValue("mv_par14", "")  # Set Of Books
        self.oHelper.SetValue("Saldos Zerados ?", "Sim")  # Saldos Zerados?
        # Compara ? = Saldo.Acum.
        self.oHelper.SetValue("Comparar ?", "Mov. Periodo")
        self.oHelper.SetValue("mv_par17", "1")  # folha Inicial
        # Imprime Cod. Conta? = Normal
        self.oHelper.SetValue("Imprime Cod. Conta ?", "Normal")
        # Imprime Cod. C.Custo? = Normal
        self.oHelper.SetValue("Imprime Cod. C.C ?", "Normal")
        # Imprime Cod. Item ? Normal
        self.oHelper.SetValue("Imprime Cod. Item ?", "Normal")
        self.oHelper.SetValue("Imprime Valor 0,00 ?",
                              "Sim")  # Imprime Valor 0.00?
        # Divide por ? = Nao se aplica
        self.oHelper.SetValue("Divide por ?", "Nao Aplica")
        # Posicao Ant. L/P? = Nao
        self.oHelper.SetValue("Posicao Ant. L/P ?", "Nao")
        self.oHelper.SetValue("mv_par24", "")  # Data Lucros/Perdas?
        # Imprime Var. Percentual ?	= Sim/Todas
        self.oHelper.SetValue("Imp.Var.Percentual ?          ", "Sim/Todas")
        # Imprime Var. Valor ? = Sim/Todas
        self.oHelper.SetValue("Imp. Dif. em Valor ?", "Sim/Todas")
        # Imp.Descrições ? = Sim
        self.oHelper.SetValue("Imp.Descricoes ?", "Sim")
        self.oHelper.SetValue("Usa Conta ?", "Sim")  # Usa Conta ? = Sim
        self.oHelper.SetValue("Usa C.Custo ?", "Nao")  # Usa C.Custo ? = Não
        # Usa Item Contabil ? = Não
        self.oHelper.SetValue("Usa Item Contabil ?", "Nao")
        # Usa Classe de Valor? = Não
        self.oHelper.SetValue("Usa Classe de Valor ?", "Sim")
        self.oHelper.SetButton("OK")

        # Ordenar por ? MV_PAR01
        self.oHelper.SetValue("Ordenar por ?", "CONTA")
        # Depois por ?   MV_PAR02
        self.oHelper.SetValue("Depois por ?", "Cod Cl Val")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("OK")

        # self.oHelper.SetButton("Sim") #SOMENTE SE JA TIVER ARQUIVO GERADO
        #self.oHelper.SetButton("Sair")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
