from tir import Webapp
import unittest


class CTBR040(unittest.TestCase):
    @classmethod
    def setUpClass(inst):

        # Endereção do webapp e o nome do Browser
        inst.oHelper = Webapp()

        # Parametros de inicialização
        inst.oHelper.Setup("SIGACTB", "15/04/2015", "T1", "D MG 01 ", "34")

        # Nome da rotina do Caso de Teste
        inst.oHelper.Program("CTBR040")

    
    def test_CTBR040_011(self):
        self.oHelper.AddParameter("MV_TREPORT", "", "1")
        self.oHelper.SetParameters()

        self.oHelper.SetValue("mv_par01","19/06/2015",name_attr=True)       #Data Inicial ?
        self.oHelper.SetValue("mv_par02","19/06/2015",name_attr=True)       #Data Final ?
        self.oHelper.SetValue("mv_par03","CT0401",name_attr=True)          #Conta Inicial
        self.oHelper.SetValue("mv_par04","CT0404",name_attr=True)          #Conta final
        self.oHelper.SetValue("Imprime Contas ?", "Analiticas")
        self.oHelper.SetValue("mv_par06","",name_attr=True)                 #Cod. Config. Livros ?
        self.oHelper.SetValue("Saldos Zerados ?",   "Sim")
        self.oHelper.SetValue("mv_par08","01",name_attr=True)               #Moeda ?
        self.oHelper.SetValue("mv_par09","2",name_attr=True)                #Folha  Inicial ?
        self.oHelper.SetValue("mv_par10","1",name_attr=True)                #Tipo de Saldo ?

        self.oHelper.SetValue("Quebra por Natureza ?","por Grupo")
        self.oHelper.SetValue("mv_par12","",name_attr=True)                 #Filtra Segmento No. ?
        self.oHelper.SetValue("mv_par13","",name_attr=True)                 #Conteudo Ini Segmen ?
        self.oHelper.SetValue("mv_par14","",name_attr=True)                 #Conteudo Fim Segmen ?
        self.oHelper.SetValue("mv_par15","",name_attr=True)                 #Conteudo Contido em ?

        self.oHelper.SetValue("Imprime Coluna Mov. ?", "Sim")
        self.oHelper.SetValue("Salta Linha Sintet. ?", "Sim")
        self.oHelper.SetValue("Imprime Valor 0.00 ?",  "Sim")
        self.oHelper.SetValue("Imprime Codigo ?",	"Normal")
        self.oHelper.SetValue("Divide por ?",	"Nao se aplica")
        self.oHelper.SetValue("mv_par21","",name_attr=True)                 #Imprimir ate o seg. ?
        self.oHelper.SetValue("Posicao Ant. L/P ?",	"Sim")
        self.oHelper.SetValue("mv_par23","31/12/2015",name_attr=True)       #Data Lucros/Perdas ?
        self.oHelper.SetValue("Imp Quadros Contabeis ?", "Nao")
        self.oHelper.SetValue("Ignora Sl Ant.Rec/Des ?", "Nao")
        self.oHelper.SetValue("mv_par26","",name_attr=True)                 #Grupos Receitas/Despesas ?
        self.oHelper.SetValue("mv_par27","",name_attr=True)                 #Data Sld Ant. Receitas/Desp. ?
        self.oHelper.SetValue("mv_par28","30",name_attr=True)               #Num.linhas p/ o Balancete ?
        self.oHelper.SetValue("mv_par29","",name_attr=True)                 #Descricao na Moeda ?
        self.oHelper.SetValue("Seleciona Filiais ?",   "Nao")

        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Imprimir")
        
        self.oHelper.SetButton("Sair")

        self.oHelper.RestoreParameters()
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
