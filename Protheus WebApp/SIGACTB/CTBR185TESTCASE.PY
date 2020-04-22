from tir import Webapp
import unittest


class CTBR185(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        # Endereção do webapp e o nome do Browser
        inst.oHelper = Webapp()

        # Parametros de inicialização
        inst.oHelper.Setup("SIGACTB", "15/04/2015", "T1", "D RJ 01 ", "34")

        # Nome da rotina do Caso de Teste
        inst.oHelper.Program("CTBR185")

    @classmethod
    def test_CTBR185_001(self):

        self.oHelper.SetButton("Outras Ações", "Parametros")
        # Tela de config parametros
        self.oHelper.SetValue("Conta Tot. Ativo?", "")
        self.oHelper.SetValue("Conta Tot. Passivo?", "")
        self.oHelper.SetValue("Conta Tot. Resultado a Debito?", "")
        self.oHelper.SetValue("Conta Tot. Resultado a Credito?", "")
        self.oHelper.SetValue("Conta Tot. Patrimonio Liquido?", "")
        self.oHelper.SetValue("Conta Tot. das Receitas?", "")
        self.oHelper.SetValue("Conta Tot. das Despesas?", "")
        self.oHelper.SetValue("Conta Tot. do PL Corrigido?", "")

        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("Data Inicial ?", "01/04/2015")
        self.oHelper.SetValue("Data Final ?", "30/04/2015")
        self.oHelper.SetValue("Conta Inicial ?", "300333001")
        self.oHelper.SetValue("Conta Final ?", "300333001")
        self.oHelper.SetValue("Do Centro de Custo ?", "30033301")
        self.oHelper.SetValue("Ate o Centro de Custo ?", "30033301")
        self.oHelper.SetValue("Do Item Contabil ?", "CTB33301")
        self.oHelper.SetValue("Ate o Item Contabil ?", "CTB33301")

        self.oHelper.SetValue("Imprime Contas ?", "Ambas")
        self.oHelper.SetValue("Cod. Config. Livros ?", "")
        self.oHelper.SetValue("Moeda ?", "01")
        self.oHelper.SetValue("Pagina Inicial ?", "2")
        self.oHelper.SetValue("Tipo de Saldo ?", "1")
        self.oHelper.SetValue("Quebra por Grupo ?            ", "Näo")

        self.oHelper.SetValue("Imprime ate o Segmento ?", "")
        self.oHelper.SetValue("Filtra Segmento No. ?", "")
        self.oHelper.SetValue("Conteudo Inicial Segmento ?", "")
        self.oHelper.SetValue("Conteudo Final Segmento ?", "")
        self.oHelper.SetValue("Conteudo Contido em ?", "")
        self.oHelper.SetValue("Imprime Coluna Mov. ?", "Sim")
        self.oHelper.SetValue("Pula Pagina ?", "Sim")

        self.oHelper.SetValue("Salta Linha Sintetica ?", "Sim")
        self.oHelper.SetValue("Imprime Valor 0,00 ?", "Sim")

        self.oHelper.SetValue("Imprime Cod. C.Custo ?", "Normal")
        self.oHelper.SetValue("Imprime Cod. Item ?", "Normal")

        self.oHelper.SetValue("Divide Por ?", "Cem")
        self.oHelper.SetValue("Posicao Ant. L/P ?", "Näo")
        self.oHelper.SetValue("Data Lucros/Perdas ?", "")
        self.oHelper.SetValue("Imprime Quadros Contabeis ?", "Sim")
        self.oHelper.SetButton("OK")
        self.oHelper.WaitShow("Conta Tot. Ativo?")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Imprimir")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
