from tir import Webapp
import unittest

class CTBC400(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGACTB','10/08/2017','T1','D MG 01 ','05')
        inst.oHelper.Program('CTBC400')

    def test_CTBC400_CT001(self):

        cContaCtb   = '11101001'
                
        #Tela de parâmetros...
        self.oHelper.SetValue("mv_par01","05/05/2014", name_attr=True	)	# Data Inicial  
        self.oHelper.SetValue("mv_par02","05/05/2014", name_attr=True	)	# Data Final
        self.oHelper.SetValue("mv_par03","01"		)	                    # Moeda
        self.oHelper.SetValue("mv_par04","1"	    )	                    # Tipo de Saldo
        self.oHelper.SetValue("mv_par05","" )	                            # Configuração de Livros
        self.oHelper.SetValue("Considera Centro Custo ?", "Sim") 
        self.oHelper.SetValue("mv_par07","" )   	                        #Centro de custo inicial
        self.oHelper.SetValue("mv_par08","ZZZZZZZZZ" )	                    #Centro de custo Final
        self.oHelper.SetValue("Considera Item Contabil ?     ", "Sim" )     # Considera Item contábil
        self.oHelper.SetValue("mv_par10","" )   	                        #Item contábil INicial
        self.oHelper.SetValue("mv_par11","ZZZZZZZZZ" )	                    #Item Final
        self.oHelper.SetValue("Considera Cl Valor ?          ", "Sim")      # Considera Classe de Valor
        self.oHelper.SetValue("mv_par13","" )   	                        #Classe de valor inicial
        self.oHelper.SetValue("mv_par14","ZZZZZZZZZ" )	                    #Classe de valor Final
        self.oHelper.SetValue("Descrição na moeda","01" )	                #Descrição de moedas
        self.oHelper.SetValue("Seleciona Filiais ?           ", "Nao")	    #Seleciona Filiais
        self.oHelper.SetButton("OK")
        #...Fim Tela parametros
        
        #Browser de Consulta
        self.oHelper.SearchBrowse(f'D MG    {cContaCtb}', 'Filial+cod Conta')
        self.oHelper.SetButton("Visualizar")
        
        #Grid de Consultas...
        #self.oHelper.CheckResult("Saldo Atual", "1.000,00", grid=True, line=1)
        #self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        #....Fim Grid de Consultas

        self.oHelper.SetButton("Impressão")

        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("Imprimir")

        self.oHelper.SetButton("Sim")

        self.oHelper.WaitShow("Numero de copias")

        self.oHelper.SetButton("Sair")
               
        self.oHelper.AssertTrue()



    def test_CTBC400_CT002(self):

        cContaCtb   = '41101'
                
        #Tela de parâmetros...
        self.oHelper.SetValue("mv_par01","05/05/2014", name_attr=True	)	# Data Inicial  
        self.oHelper.SetValue("mv_par02","05/05/2014", name_attr=True	)	# Data Final
        self.oHelper.SetValue("mv_par03","01"		)	                    # Moeda
        self.oHelper.SetValue("mv_par04","1"	    )	                    # Tipo de Saldo
        self.oHelper.SetValue("mv_par05","" )	                            # Configuração de Livros
        self.oHelper.SetValue("Considera Centro Custo ?", "Sim") 
        self.oHelper.SetValue("mv_par07","" )   	                        #Centro de custo inicial
        self.oHelper.SetValue("mv_par08","ZZZZZZZZZ" )	                    #Centro de custo Final
        self.oHelper.SetValue("Considera Item Contabil ?     ", "Sim" )     # Considera Item contábil
        self.oHelper.SetValue("mv_par10","" )   	                        #Item contábil INicial
        self.oHelper.SetValue("mv_par11","ZZZZZZZZZ" )	                    #Item Final
        self.oHelper.SetValue("Considera Cl Valor ?          ", "Sim")      # Considera Classe de Valor
        self.oHelper.SetValue("mv_par13","" )   	                        #Classe de valor inicial
        self.oHelper.SetValue("mv_par14","ZZZZZZZZZ" )	                    #Classe de valor Final
        self.oHelper.SetValue("Descrição na moeda","01" )	                #Descrição de moedas
        self.oHelper.SetValue("Seleciona Filiais ?           ", "Nao")	    #Seleciona Filiais
        self.oHelper.SetButton("OK")
        #...Fim Tela parametros
        
        #Browser de Consulta
        self.oHelper.SearchBrowse(f'D MG    {cContaCtb}', 'Filial+cod Conta')
        self.oHelper.SetButton("Visualizar")
        
        #Grid de Consultas...
        #self.oHelper.CheckResult("Saldo Atual", "1.000,00", grid=True, line=1)
        #self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        #....Fim Grid de Consultas
               
        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()