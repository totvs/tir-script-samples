from tir import Webapp
import unittest


class CTBA355(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "01/02/2016", "T1", "D MG 01 ", "34")
        inst.oHelper.Program("CTBA355")

# ==================================================================
#                 Conferir não conferidos.
# ==================================================================
    def test_CTBA355_001(self):
        self.oHelper.SetButton("Conferir") #Re-analise

        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Conferir ?",             "Nao conferidos")
        self.oHelper.SetValue("Da Data ?",              "01/02/2016")
        self.oHelper.SetValue("Ate a Data ?",           "01/02/2016")
        self.oHelper.SetValue("Valor minimo ?",               "0,00")
        self.oHelper.SetValue("Valor maximo ?",     "999.999.999.999,99")
        self.oHelper.SetValue("Do Lote ?",                      "")
        self.oHelper.SetValue("Ate o Lote ?",               "ZZZZZZ")
        self.oHelper.SetValue("Do SubLote ?",                   "")
        self.oHelper.SetValue("Ate o Sublote ?",            "ZZZ")
        self.oHelper.SetValue("Do Documento ?",                "")
        self.oHelper.SetValue("Ate o Documento ?",       "ZZZZZZ")
        self.oHelper.SetValue("Moeda ?",                     "01")
        self.oHelper.SetValue("Tipo de saldo ?",                 "1")
        self.oHelper.SetValue("Conta ?",                    "101020")
        self.oHelper.SetValue("Centro de custo ?",              "")
        self.oHelper.SetValue("Item contabil ?",                "")
        self.oHelper.SetValue("Classe de valor ?",              "")
        self.oHelper.SetValue("Acao do clique ?",       "Conferir")
        self.oHelper.SetButton("OK")

        self.oHelper.WaitShow("Conferencia de lancamentos - CONFERIR")
        self.oHelper.ClickBox("Data Lcto","01/02/2016" ,grid_number=1)
        self.oHelper.SetButton("Salvar")

        #self.oHelper.WaitShow("Deseja confirmar os registros marcados?")
        #self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Cancelar")
        
        self.oHelper.AssertTrue()

# ==================================================================
#                 Estornar conferidos.                     
# ==================================================================
    def test_CTBA355_002(self):
        self.oHelper.SetButton("Outras Ações","Estornar") #Estornar

        #self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Estornar ?",             "Conferidos")
        self.oHelper.SetValue("Da Data ?",              "01/02/2016")
        self.oHelper.SetValue("Ate a Data ?",           "01/02/2016")
        self.oHelper.SetValue("Valor minimo ?",               "0,00")
        self.oHelper.SetValue("Valor maximo ?",     "999.999.999.999,99")
        self.oHelper.SetValue("Do Lote ?",                      "")
        self.oHelper.SetValue("Ate o Lote ?",               "ZZZZZZ")
        self.oHelper.SetValue("Do SubLote ?",                   "")
        self.oHelper.SetValue("Ate o Sublote ?",            "ZZZ")
        self.oHelper.SetValue("Do Documento ?",                "")
        self.oHelper.SetValue("Ate o Documento ?",       "ZZZZZZ")
        self.oHelper.SetValue("Moeda ?",                     "01")
        self.oHelper.SetValue("Tipo de saldo ?",                 "1")
        self.oHelper.SetValue("Conta ?",                    "101030")
        self.oHelper.SetValue("Centro de custo ?",              "")
        self.oHelper.SetValue("Item contabil ?",                "")
        self.oHelper.SetValue("Classe de valor ?",              "")
        self.oHelper.SetValue("Acao do clique ?",       "Estornar")
        self.oHelper.SetButton("OK")

        self.oHelper.WaitShow("Conferencia de lancamentos - ESTORNAR")
        self.oHelper.ClickBox("Data Lcto","01/02/2016" ,grid_number=1)
        self.oHelper.SetButton("Confirmar")

        #self.oHelper.WaitShow("Deseja confirmar os registros marcados?")
        #self.oHelper.SetButton("Sim")
        #self.oHelper.SetButton("Cancelar")
        
        self.oHelper.AssertTrue()

# ==================================================================
#                 Re-analise náo conferidos                  
# ==================================================================
    def test_CTBA355_003(self):
        self.oHelper.SetButton("Conferir") #Re-analise

        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Conferir ?",             "Nao conferidos")
        self.oHelper.SetValue("Da Data ?",              "01/02/2016")
        self.oHelper.SetValue("Ate a Data ?",           "01/02/2016")
        self.oHelper.SetValue("Valor minimo ?",               "0,00")
        self.oHelper.SetValue("Valor maximo ?",     "999.999.999.999,99")
        self.oHelper.SetValue("Do Lote ?",                      "")
        self.oHelper.SetValue("Ate o Lote ?",               "ZZZZZZ")
        self.oHelper.SetValue("Do SubLote ?",                   "")
        self.oHelper.SetValue("Ate o Sublote ?",            "ZZZ")
        self.oHelper.SetValue("Do Documento ?",                "")
        self.oHelper.SetValue("Ate o Documento ?",       "ZZZZZZ")
        self.oHelper.SetValue("Moeda ?",                     "01")
        self.oHelper.SetValue("Tipo de saldo ?",                 "1")
        self.oHelper.SetValue("Conta ?",                    "101010")
        self.oHelper.SetValue("Centro de custo ?",              "")
        self.oHelper.SetValue("Item contabil ?",                "")
        self.oHelper.SetValue("Classe de valor ?",              "")
        self.oHelper.SetValue("Acao do clique ?",       "Re-analise")
        self.oHelper.SetButton("OK")

        self.oHelper.WaitShow("Conferencia de lancamentos - CONFERIR")
        self.oHelper.ClickBox("Data Lcto","01/02/2016" ,grid_number=1)
        self.oHelper.SetButton("Salvar")

        self.oHelper.CheckHelp("Deseja confirmar os registros marcados?","Sim")

        self.oHelper.SetButton("Cancelar")
        
        self.oHelper.AssertTrue()

# ==================================================================
#                 Tela de visualizar, teste abertura,caso tela, REGISTRO CORRENTE                   
# ==================================================================
    def test_CTBA355_004(self):
        self.oHelper.SetButton("Vis. Lancamento")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

# ==================================================================
#                 Tela detalhes, localizar, teste abertura, caso tela                    
# ==================================================================
    def test_CTBA355_005(self):
        self.oHelper.SetButton("Conferir") #Re-analise

        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Conferir ?",             "Nao conferidos")
        self.oHelper.SetValue("Da Data ?",              "01/02/2016")
        self.oHelper.SetValue("Ate a Data ?",           "01/02/2016")
        self.oHelper.SetValue("Valor minimo ?",               "0,00")
        self.oHelper.SetValue("Valor maximo ?",     "999.999.999.999,99")
        self.oHelper.SetValue("Do Lote ?",                      "")
        self.oHelper.SetValue("Ate o Lote ?",               "ZZZZZZ")
        self.oHelper.SetValue("Do SubLote ?",                   "")
        self.oHelper.SetValue("Ate o Sublote ?",            "ZZZ")
        self.oHelper.SetValue("Do Documento ?",                "")
        self.oHelper.SetValue("Ate o Documento ?",       "ZZZZZZ")
        self.oHelper.SetValue("Moeda ?",                     "01")
        self.oHelper.SetValue("Tipo de saldo ?",                 "1")
        self.oHelper.SetValue("Conta ?",                    "101040")
        self.oHelper.SetValue("Centro de custo ?",              "")
        self.oHelper.SetValue("Item contabil ?",                "")
        self.oHelper.SetValue("Classe de valor ?",              "")
        self.oHelper.SetValue("Acao do clique ?",       "Conferir")
        self.oHelper.SetButton("OK")

        ##Detalhes teste de abertura da tela
        self.oHelper.SetButton("Outras Ações","Detalhes")
        self.oHelper.SetButton("Confirmar")

        #Localizar teste de abertura de tela
        self.oHelper.SetButton("Outras Ações","Localizar")
        self.oHelper.SetValue("Campo:","Data Lcto")
        self.oHelper.SetValue("Operador:","Igual a")
        self.oHelper.SetValue("cExpr","01/02/2016",name_attr=True)
        self.oHelper.SetButton("Adiciona")
        self.oHelper.SetButton("Avançar")

        #self.oHelper.WaitShow("Conferencia de lancamentos - CONFERIR")
        #self.oHelper.ClickBox("Data Lcto","01/02/2016" ,grid_number=1)
        ##self.oHelper.ClickBox("Data Lcto","01/02/2016" ,grid_number=1)
        self.oHelper.SetButton("Salvar")

        #self.oHelper.WaitShow("Deseja confirmar os registros marcados?")
        #self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Cancelar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
