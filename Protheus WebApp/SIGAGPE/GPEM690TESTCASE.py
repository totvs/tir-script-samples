from cawebhelper import CAWebHelper
import unittest


class GPEM690(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        """
        SETUP
        Configuração de inicialização dos Casos de Teste
        """
        # Endereço do webapp e o nome do Browser
        inst.oHelper = CAWebHelper()
        
        # Parametros de inicializaçao
        inst.oHelper.Setup('SIGAGPE','15/03/2018','T1','D RJ 02 ')

        # Nome da rotina do Caso de Teste
        inst.oHelper.UTProgram("GPEM690")

    """
    Calculo Dissidio Retroativo com Alteração Salarial no mês para categoria Mensalista
    @author Kaio Alves
    @since 28/03/2018
    @version 1.0
    """
    def test_GPEM690_025(self):  

        cMat = "200015"

        # Aciona o botão
        self.oHelper.SetButton("Calcular")
        self.oHelper.SetButton("Perguntas")
        
        # Perguntas da geração
        self.oHelper.UTSetValue("aCab","Processo ?",                 "00010")
        self.oHelper.UTSetValue("aCab","Roteiro ?",                    "FOL")
        self.oHelper.UTSetValue("aCab","Mes Ano De (MMAAAA) ?",     "012015")
        self.oHelper.UTSetValue("aCab","Mes Ano Ate (MMAAAA) ?",    "022015")
        self.oHelper.UTSetValue("aCab","Indice ?",                   "Unico")
        self.oHelper.UTSetValue("aCab","Filial ?",                "D RJ 02 ")
        self.oHelper.UTSetValue("aCab","Centro de Custo ?",              " ")
        self.oHelper.UTSetValue("aCab","Matricula ?",                   cMat)
        self.oHelper.UTSetValue("aCab","Nome ?",                         " ")

        self.oHelper.UTSetValue("aCab","Situacoes ?",                " ADFT")
        self.oHelper.SetButton("Salvar")

        self.oHelper.UTSetValue("aCab","Categorias ?",     "ACDEGHIJMPST***")
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.UTSetValue("aCab","Tipo Aumento ?",               "003")
        self.oHelper.SetButton("Salvar")

        self.oHelper.UTSetValue("aCab","Sindicato ?",                   "21")
        self.oHelper.UTSetValue("aCab","Data Acordo Coletivo ?","09/03/2015")
        self.oHelper.UTSetValue("aCab","Criterio de Arredond. ?",      "Nao")
        self.oHelper.UTSetValue("aCab","Arredonda em R$ ?",              "0")
        self.oHelper.UTSetValue("aCab","Proporc.a Admissao ?",         "Sim")
        self.oHelper.UTSetValue("aCab","No Meses p/Admissao Proporc. ?","12")
        self.oHelper.UTSetValue("aCab","Piso Salarial ?",                "0")
        self.oHelper.UTSetValue("aCab","Funcao ?",                       " ")
        self.oHelper.UTSetValue("aCab","Complemento ?",                  " ")

        self.oHelper.SetButton("Informações")        
        self.oHelper.SetButton("Executar")
        
        # Informar campos do grid
        self.oHelper.UTSetValue("aItens","SALDE"        ,             "0,01")
        self.oHelper.UTSetValue("aItens","SALATE"       ,         "5.000,00")
        self.oHelper.UTSetValue("aItens","ADMISSADT1"   ,       "01/01/2001")
        self.oHelper.UTSetValue("aItens","ADMISSADT2"   ,       "28/02/2015")
        self.oHelper.UTSetValue("aItens","SALPERC"      ,        "10,000000")
        
        self.oHelper.SetButton("Salvar")
        self.oHelper.UTWaitWhile("Processamento")
        
        # Filtrar funcionário
        self.oHelper.SearchBrowse("Filial+matricula","D RJ 02 %s" %cMat,True)

        # Perguntas da visualização
        self.oHelper.SetButton("Visualizar")

        self.oHelper.UTSetValue("aCab","Per. Inicial (MMAAAA) ?",   "012015")
        self.oHelper.UTSetValue("aCab","Per. Final  (MMAAAA) ?" ,   "022015")
        self.oHelper.SetButton("OK")

        # Conferir valores da tabela RHH do grid 
        self.oHelper.UTCheckResult("aItens","RHH_FILIAL"         ,"D RJ 02 ")
        self.oHelper.UTCheckResult("aItens","RHH_MAT"            ,      cMat)
        self.oHelper.UTCheckResult("aItens","RHH_DATA"           ,  "201501")
        self.oHelper.UTCheckResult("aItens","RHH_SEMANA"         ,      "01")
        self.oHelper.UTCheckResult("aItens","RHH_VB"             ,     "112")
        self.oHelper.UTCheckResult("aItens","RHH_VERBA"          ,     "894")
        self.oHelper.UTCheckResult("aItens","RHH_INDICE"         ,"0.000000")
        self.oHelper.UTCheckResult("aItens","RHH_VL"             , "2700.00")
        self.oHelper.UTCheckResult("aItens","RHH_CALC"           , "2970.00")
        self.oHelper.UTCheckResult("aItens","RHH_VALOR"          ,  "270.00")
        self.oHelper.UTCheckResult("aItens","RHH_ROTEIR"         ,     "FOL")
        self.oHelper.AssertTrue()


    """
    Calculo Dissidio Retroativo com Adicional Tempo de Serviço para categoria Mensalista
    @author Kaio Alves
    @since 28/03/2018
    @version 1.0
    """
    def test_GPEM690_026(self): 

        cMat = "200016"

        # Aciona o botão
        self.oHelper.SetButton("Calcular")
        self.oHelper.SetButton("Perguntas")
        
        # Perguntas da geração
        self.oHelper.UTSetValue("aCab","Processo ?",                 "00010")
        self.oHelper.UTSetValue("aCab","Roteiro ?",                    "FOL")
        self.oHelper.UTSetValue("aCab","Mes Ano De (MMAAAA) ?",     "012015")
        self.oHelper.UTSetValue("aCab","Mes Ano Ate (MMAAAA) ?",    "022015")
        self.oHelper.UTSetValue("aCab","Indice ?",                   "Unico")
        self.oHelper.UTSetValue("aCab","Filial ?",                "D RJ 02 ")
        self.oHelper.UTSetValue("aCab","Centro de Custo ?",              " ")
        self.oHelper.UTSetValue("aCab","Matricula ?",                   cMat)
        self.oHelper.UTSetValue("aCab","Nome ?",                         " ")

        self.oHelper.UTSetValue("aCab","Situacoes ?",                " ADFT")
        self.oHelper.SetButton("Salvar")

        self.oHelper.UTSetValue("aCab","Categorias ?",     "ACDEGHIJMPST***")
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.UTSetValue("aCab","Tipo Aumento ?",               "003")
        self.oHelper.SetButton("Salvar")

        self.oHelper.UTSetValue("aCab","Sindicato ?",                   "21")
        self.oHelper.UTSetValue("aCab","Data Acordo Coletivo ?","09/03/2015")
        self.oHelper.UTSetValue("aCab","Criterio de Arredond. ?",      "Nao")
        self.oHelper.UTSetValue("aCab","Arredonda em R$ ?",              "0")
        self.oHelper.UTSetValue("aCab","Proporc.a Admissao ?",         "Sim")
        self.oHelper.UTSetValue("aCab","No Meses p/Admissao Proporc. ?","12")
        self.oHelper.UTSetValue("aCab","Piso Salarial ?",                "0")
        self.oHelper.UTSetValue("aCab","Funcao ?",                       " ")
        self.oHelper.UTSetValue("aCab","Complemento ?",                  " ")

        self.oHelper.SetButton("Informações")        
        self.oHelper.SetButton("Executar")
        
        # Informar campos do grid
        self.oHelper.UTSetValue("aItens","SALDE"        ,             "0,01")
        self.oHelper.UTSetValue("aItens","SALATE"       ,         "5.000,00")
        self.oHelper.UTSetValue("aItens","ADMISSADT1"   ,       "01/01/2001")
        self.oHelper.UTSetValue("aItens","ADMISSADT2"   ,       "28/02/2015")
        self.oHelper.UTSetValue("aItens","SALPERC"      ,        "10,000000")
        
        self.oHelper.SetButton("Salvar")
        self.oHelper.UTWaitWhile("Processamento")
        
        # Filtrar funcionário
        self.oHelper.SearchBrowse("Filial+matricula","D RJ 02 %s" %cMat,True)

        # Perguntas da visualização
        self.oHelper.SetButton("Visualizar")

        self.oHelper.UTSetValue("aCab","Per. Inicial (MMAAAA) ?",   "012015")
        self.oHelper.UTSetValue("aCab","Per. Final  (MMAAAA) ?" ,   "022015")
        self.oHelper.SetButton("OK")

        # Conferir valores da tabela RHH do grid 
        self.oHelper.UTCheckResult("aItens","RHH_FILIAL"        ,"D RJ 02 ")
        self.oHelper.UTCheckResult("aItens","RHH_MAT"           ,      cMat)
        self.oHelper.UTCheckResult("aItens","RHH_DATA"          ,  "201501")
        self.oHelper.UTCheckResult("aItens","RHH_SEMANA"        ,      "01")
        self.oHelper.UTCheckResult("aItens","RHH_VB"            ,     "101")
        self.oHelper.UTCheckResult("aItens","RHH_VERBA"         ,     "894")
        self.oHelper.UTCheckResult("aItens","RHH_INDICE"        ,"0.000000")
        self.oHelper.UTCheckResult("aItens","RHH_VL"            ,   "38.00")
        self.oHelper.UTCheckResult("aItens","RHH_CALC"          ,   "41.80")
        self.oHelper.UTCheckResult("aItens","RHH_VALOR"         ,    "3.80")
        self.oHelper.UTCheckResult("aItens","RHH_ROTEIR"        ,     "FOL")
        self.oHelper.AssertTrue()


    """
    Calculo Dissidio Retroativo com Periculosidade para categoria Mensalista
    @author Kaio Alves
    @since 28/03/2018
    @version 1.0
    """
    def test_GPEM690_027(self):   

        cMat = "200017"

        # Aciona o botão
        self.oHelper.SetButton("Calcular")
        self.oHelper.SetButton("Perguntas")
        
        # Perguntas da geração
        self.oHelper.UTSetValue("aCab","Processo ?",                 "00010")
        self.oHelper.UTSetValue("aCab","Roteiro ?",                    "FOL")
        self.oHelper.UTSetValue("aCab","Mes Ano De (MMAAAA) ?",     "012015")
        self.oHelper.UTSetValue("aCab","Mes Ano Ate (MMAAAA) ?",    "022015")
        self.oHelper.UTSetValue("aCab","Indice ?",                   "Unico")
        self.oHelper.UTSetValue("aCab","Filial ?",                "D RJ 02 ")
        self.oHelper.UTSetValue("aCab","Centro de Custo ?",              " ")
        self.oHelper.UTSetValue("aCab","Matricula ?",                   cMat)
        self.oHelper.UTSetValue("aCab","Nome ?",                         " ")

        self.oHelper.UTSetValue("aCab","Situacoes ?",                " ADFT")
        self.oHelper.SetButton("Salvar")

        self.oHelper.UTSetValue("aCab","Categorias ?",     "ACDEGHIJMPST***")
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.UTSetValue("aCab","Tipo Aumento ?",               "003")
        self.oHelper.SetButton("Salvar")

        self.oHelper.UTSetValue("aCab","Sindicato ?",                   "21")
        self.oHelper.UTSetValue("aCab","Data Acordo Coletivo ?","09/03/2015")
        self.oHelper.UTSetValue("aCab","Criterio de Arredond. ?",      "Nao")
        self.oHelper.UTSetValue("aCab","Arredonda em R$ ?",              "0")
        self.oHelper.UTSetValue("aCab","Proporc.a Admissao ?",         "Sim")
        self.oHelper.UTSetValue("aCab","No Meses p/Admissao Proporc. ?","12")
        self.oHelper.UTSetValue("aCab","Piso Salarial ?",                "0")
        self.oHelper.UTSetValue("aCab","Funcao ?",                       " ")
        self.oHelper.UTSetValue("aCab","Complemento ?",                  " ")

        self.oHelper.SetButton("Informações")        
        self.oHelper.SetButton("Executar")
        
        # Informar campos do grid
        self.oHelper.UTSetValue("aItens","SALDE"        ,             "0,01")
        self.oHelper.UTSetValue("aItens","SALATE"       ,         "5.000,00")
        self.oHelper.UTSetValue("aItens","ADMISSADT1"   ,       "01/01/2001")
        self.oHelper.UTSetValue("aItens","ADMISSADT2"   ,       "28/02/2015")
        self.oHelper.UTSetValue("aItens","SALPERC"      ,        "10,000000")
        
        self.oHelper.SetButton("Salvar")
        self.oHelper.UTWaitWhile("Processamento")
        
        # Filtrar funcionário
        self.oHelper.SearchBrowse("Filial+matricula","D RJ 02 %s" %cMat,True)

        # Perguntas da visualização
        self.oHelper.SetButton("Visualizar")

        self.oHelper.UTSetValue("aCab","Per. Inicial (MMAAAA) ?",   "012015")
        self.oHelper.UTSetValue("aCab","Per. Final  (MMAAAA) ?" ,   "022015")
        self.oHelper.SetButton("OK")

        # Conferir valores da tabela RHH do grid 
        self.oHelper.UTCheckResult("aItens","RHH_FILIAL"        ,"D RJ 02 ")
        self.oHelper.UTCheckResult("aItens","RHH_MAT"           ,      cMat)
        self.oHelper.UTCheckResult("aItens","RHH_DATA"          ,  "201501")
        self.oHelper.UTCheckResult("aItens","RHH_SEMANA"        ,      "01")
        self.oHelper.UTCheckResult("aItens","RHH_VB"            ,     "117")
        self.oHelper.UTCheckResult("aItens","RHH_VERBA"         ,     "894")
        self.oHelper.UTCheckResult("aItens","RHH_INDICE"        ,"0.000000")
        self.oHelper.UTCheckResult("aItens","RHH_VL"            ,  "810.00")
        self.oHelper.UTCheckResult("aItens","RHH_CALC"          ,  "891.00")
        self.oHelper.UTCheckResult("aItens","RHH_VALOR"         ,   "81.00")
        self.oHelper.UTCheckResult("aItens","RHH_ROTEIR"        ,     "FOL")
        self.oHelper.AssertTrue()


    """
    Calculo Dissidio Retroativo com Insalubridade para categoria Mensalista
    @author Kaio Alves
    @since 28/03/2018
    @version 1.0
    """
    def test_GPEM690_028(self):   

        cMat = "200018"

        # Aciona o botão
        self.oHelper.SetButton("Calcular")
        self.oHelper.SetButton("Perguntas")
        
        # Perguntas da geração
        self.oHelper.UTSetValue("aCab","Processo ?",                 "00010")
        self.oHelper.UTSetValue("aCab","Roteiro ?",                    "FOL")
        self.oHelper.UTSetValue("aCab","Mes Ano De (MMAAAA) ?",     "012015")
        self.oHelper.UTSetValue("aCab","Mes Ano Ate (MMAAAA) ?",    "022015")
        self.oHelper.UTSetValue("aCab","Indice ?",                   "Unico")
        self.oHelper.UTSetValue("aCab","Filial ?",                "D RJ 02 ")
        self.oHelper.UTSetValue("aCab","Centro de Custo ?",              " ")
        self.oHelper.UTSetValue("aCab","Matricula ?",                   cMat)
        self.oHelper.UTSetValue("aCab","Nome ?",                         " ")

        self.oHelper.UTSetValue("aCab","Situacoes ?",                " ADFT")
        self.oHelper.SetButton("Salvar")

        self.oHelper.UTSetValue("aCab","Categorias ?",     "ACDEGHIJMPST***")
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.UTSetValue("aCab","Tipo Aumento ?",               "003")
        self.oHelper.SetButton("Salvar")

        self.oHelper.UTSetValue("aCab","Sindicato ?",                   "21")
        self.oHelper.UTSetValue("aCab","Data Acordo Coletivo ?","09/03/2015")
        self.oHelper.UTSetValue("aCab","Criterio de Arredond. ?",      "Nao")
        self.oHelper.UTSetValue("aCab","Arredonda em R$ ?",              "0")
        self.oHelper.UTSetValue("aCab","Proporc.a Admissao ?",         "Sim")
        self.oHelper.UTSetValue("aCab","No Meses p/Admissao Proporc. ?","12")
        self.oHelper.UTSetValue("aCab","Piso Salarial ?",                "0")
        self.oHelper.UTSetValue("aCab","Funcao ?",                       " ")
        self.oHelper.UTSetValue("aCab","Complemento ?",                  " ")

        self.oHelper.SetButton("Informações")        
        self.oHelper.SetButton("Executar")
        
        # Informar campos do grid
        self.oHelper.UTSetValue("aItens","SALDE"        ,             "0,01")
        self.oHelper.UTSetValue("aItens","SALATE"       ,         "5.000,00")
        self.oHelper.UTSetValue("aItens","ADMISSADT1"   ,       "01/01/2001")
        self.oHelper.UTSetValue("aItens","ADMISSADT2"   ,       "28/02/2015")
        self.oHelper.UTSetValue("aItens","SALPERC"      ,        "10,000000")
        
        self.oHelper.SetButton("Salvar")
        self.oHelper.UTWaitWhile("Processamento")
        
        # Filtrar funcionário
        self.oHelper.SearchBrowse("Filial+matricula","D RJ 02 %s" %cMat,True)

        # Perguntas da visualização
        self.oHelper.SetButton("Visualizar")

        self.oHelper.UTSetValue("aCab","Per. Inicial (MMAAAA) ?",   "012015")
        self.oHelper.UTSetValue("aCab","Per. Final  (MMAAAA) ?" ,   "022015")
        self.oHelper.SetButton("OK")

        # Conferir valores da tabela RHH do grid 
        self.oHelper.UTCheckResult("aItens","RHH_FILIAL"        ,"D RJ 02 ")
        self.oHelper.UTCheckResult("aItens","RHH_MAT"           ,      cMat)
        self.oHelper.UTCheckResult("aItens","RHH_DATA"          ,  "201501")
        self.oHelper.UTCheckResult("aItens","RHH_SEMANA"        ,      "01")
        self.oHelper.UTCheckResult("aItens","RHH_VB"            ,     "119")
        self.oHelper.UTCheckResult("aItens","RHH_VERBA"         ,     "894")
        self.oHelper.UTCheckResult("aItens","RHH_INDICE"        ,"0.000000")
        self.oHelper.UTCheckResult("aItens","RHH_VL"            ,  "760.00")
        self.oHelper.UTCheckResult("aItens","RHH_CALC"          ,  "836.00")
        self.oHelper.UTCheckResult("aItens","RHH_VALOR"         ,   "76.00")
        self.oHelper.UTCheckResult("aItens","RHH_ROTEIR"        ,     "FOL")
        self.oHelper.AssertTrue()


    """
    Calculo Dissidio Retroativo com Insalubridade e Periculosidade para categoria Mensalista.
    @author Kaio Alves
    @since 28/03/2018
    @version 1.0
    """
    def test_GPEM690_029(self):   
        
        cMat = "200019"

        # Aciona o botão
        self.oHelper.SetButton("Calcular")
        self.oHelper.SetButton("Perguntas")
        
        # Perguntas da geração
        self.oHelper.UTSetValue("aCab","Processo ?",                 "00010")
        self.oHelper.UTSetValue("aCab","Roteiro ?",                    "FOL")
        self.oHelper.UTSetValue("aCab","Mes Ano De (MMAAAA) ?",     "012015")
        self.oHelper.UTSetValue("aCab","Mes Ano Ate (MMAAAA) ?",    "022015")
        self.oHelper.UTSetValue("aCab","Indice ?",                   "Unico")
        self.oHelper.UTSetValue("aCab","Filial ?",                "D RJ 02 ")
        self.oHelper.UTSetValue("aCab","Centro de Custo ?",              " ")
        self.oHelper.UTSetValue("aCab","Matricula ?",                   cMat)
        self.oHelper.UTSetValue("aCab","Nome ?",                         " ")

        self.oHelper.UTSetValue("aCab","Situacoes ?",                " ADFT")
        self.oHelper.SetButton("Salvar")

        self.oHelper.UTSetValue("aCab","Categorias ?",     "ACDEGHIJMPST***")
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.UTSetValue("aCab","Tipo Aumento ?",               "003")
        self.oHelper.SetButton("Salvar")

        self.oHelper.UTSetValue("aCab","Sindicato ?",                   "21")
        self.oHelper.UTSetValue("aCab","Data Acordo Coletivo ?","09/03/2015")
        self.oHelper.UTSetValue("aCab","Criterio de Arredond. ?",      "Nao")
        self.oHelper.UTSetValue("aCab","Arredonda em R$ ?",              "0")
        self.oHelper.UTSetValue("aCab","Proporc.a Admissao ?",         "Sim")
        self.oHelper.UTSetValue("aCab","No Meses p/Admissao Proporc. ?","12")
        self.oHelper.UTSetValue("aCab","Piso Salarial ?",                "0")
        self.oHelper.UTSetValue("aCab","Funcao ?",                       " ")
        self.oHelper.UTSetValue("aCab","Complemento ?",                  " ")

        self.oHelper.SetButton("Informações")        
        self.oHelper.SetButton("Executar")
        
        # Informar campos do grid
        self.oHelper.UTSetValue("aItens","SALDE"        ,             "0,01")
        self.oHelper.UTSetValue("aItens","SALATE"       ,         "5.000,00")
        self.oHelper.UTSetValue("aItens","ADMISSADT1"   ,       "01/01/2001")
        self.oHelper.UTSetValue("aItens","ADMISSADT2"   ,       "28/02/2015")
        self.oHelper.UTSetValue("aItens","SALPERC"      ,        "10,000000")
        
        self.oHelper.SetButton("Salvar")
        self.oHelper.UTWaitWhile("Processamento")
        
        # Filtrar funcionário
        self.oHelper.SearchBrowse("Filial+matricula","D RJ 02 %s" %cMat,True)

        # Perguntas da visualização
        self.oHelper.SetButton("Visualizar")

        self.oHelper.UTSetValue("aCab","Per. Inicial (MMAAAA) ?",   "012015")
        self.oHelper.UTSetValue("aCab","Per. Final  (MMAAAA) ?" ,   "022015")
        self.oHelper.SetButton("OK")

        # Conferir valores da tabela RHH do grid 
        self.oHelper.UTCheckResult("aItens","RHH_FILIAL"        ,"D RJ 02 ")
        self.oHelper.UTCheckResult("aItens","RHH_MAT"           ,      cMat)
        self.oHelper.UTCheckResult("aItens","RHH_DATA"          ,  "201501")
        self.oHelper.UTCheckResult("aItens","RHH_SEMANA"        ,      "01")
        self.oHelper.UTCheckResult("aItens","RHH_VB"            ,     "119")
        self.oHelper.UTCheckResult("aItens","RHH_VERBA"         ,     "894")
        self.oHelper.UTCheckResult("aItens","RHH_INDICE"        ,"0.000000")
        self.oHelper.UTCheckResult("aItens","RHH_VL"            ,  "540.00")
        self.oHelper.UTCheckResult("aItens","RHH_CALC"          ,  "594.00")
        self.oHelper.UTCheckResult("aItens","RHH_VALOR"         ,   "54.00")
        self.oHelper.UTCheckResult("aItens","RHH_ROTEIR"        ,     "FOL")
        self.oHelper.AssertTrue()
        

    @classmethod
    def tearDownClass(inst):
        """
        Método que finaliza o TestCase
        """
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()