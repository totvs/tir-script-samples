from tir import Webapp
import unittest


class CTBR200(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        # Endereção do webapp e o nome do Browser
        inst.oHelper = Webapp()

        # Parametros de inicialização
        inst.oHelper.Setup("SIGACTB", "15/04/2015", "T1", "D MG 01 ", "34")

        # Nome da rotina do Caso de Teste
        inst.oHelper.Program("CTBR200")

    @classmethod
    def test_CTBR200_001(self):

        self.oHelper.SetValue("Data Inicial ?", "15/04/2015")
        self.oHelper.SetValue("Data Final ?",   "15/04/2015")
        self.oHelper.SetValue("Do Centro de Custo ?",  "102030400")
        self.oHelper.SetValue("Ate Centro de Custo ?",  "102030400")
        self.oHelper.SetValue("Imprime C. Custo ?", "Analiticos")
        self.oHelper.SetValue("Cod. Config. Livros ?",    "CT2")
        self.oHelper.SetValue("Saldos Zerados ?",   "Nao")
        self.oHelper.SetValue("Moeda ?",   "01")
        self.oHelper.SetValue("Folha  Inicial ?",   "2")
        self.oHelper.SetValue("Tipo de Saldo ?",    "1")

        #self.oHelper.SetValue("Imprimir ate o seg. ?",    "")
        #self.oHelper.SetValue("Filtra Segmento No. ?",	"")
        #self.oHelper.SetValue("Conteudo Ini Segmen ?",	"")
        #self.oHelper.SetValue("Conteudo Fim Segmen ?",	"")
        #self.oHelper.SetValue("Conteudo Contido em ?",	"")

        self.oHelper.SetValue("Imprime Coluna Mov. ?",   "Sim")
        self.oHelper.SetValue("Salta Linha Sintet. ?",    "Nao")
        self.oHelper.SetValue("Imprime Valor 0.00 ?",  "Nao")
        self.oHelper.SetValue("Imprime Codigo ?",	"Normal")
        self.oHelper.SetValue("Divide por ?",	"Nao se aplica")
        self.oHelper.SetValue("Posicao Ant. L/P ?",	"Nao")
        #self.oHelper.SetValue("Data Lucros/Perdas ?",  "")
        self.oHelper.SetValue("Filt.Entid.Visao Geren ?", "Sim")
        self.oHelper.SetValue("Seleciona Filiais ?",   "Nao")

        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Imprimir")
        self.oHelper.WaitShow("Da Conta?")
        # ----------------------------------------------------------------------
        # TELA CONFIG PARAMETROS, FILTRO DE USUARIO DE ENTIDADES
        # ----------------------------------------------------------------------
        self.oHelper.SetValue("Da Conta?", "000000006")
        self.oHelper.SetValue("Ate a Conta?", "000000006")
        self.oHelper.SetValue("Do Centro de Custo?", "102030400")
        self.oHelper.SetValue("Ate o Centro de Custo?", "102030400")
        #self.oHelper.SetValue("Do Item?", "")
        #self.oHelper.SetValue("Ate o Item?", "")
        #self.oHelper.SetValue("Da Classe de Valor?", "")
        #self.oHelper.SetValue("Ate a Classe de Valor?", "")

        self.oHelper.SetButton("Ok")
        # self.oHelper.WaitShow("Sair")
        # self.oHelper.SetButton("Sair")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
