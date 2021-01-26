from tir import Webapp
import unittest

class CTBC403(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGACTB','08/11/2017','T1','D MG 01 ','05')
        inst.oHelper.Program('CTBC403')

    def test_CTBC403_CT002(self):
    #https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T45822

        cContaCtb   = '1110227'
                
        #Tela de parâmetros...
        self.oHelper.SetValue("mv_par01","08/11/2019", name_attr=True	)	# Data Inicial  
        self.oHelper.SetValue("mv_par02","08/11/2019", name_attr=True	)	# Data Final
        self.oHelper.SetValue("mv_par03","01"		)	                    # Moeda
        self.oHelper.SetValue("mv_par04","1"	    )	                    # Tipo de Saldo
        self.oHelper.SetValue("mv_par05","01" )	  
        #self.oHelper.SetValue("mv_par06","   " )	                          # Configuração de Livros
        self.oHelper.SetValue("mv_par07","05" )	
        self.oHelper.SetValue("Seleciona filiais ?", "Nao")	    #Seleciona Filiais
        self.oHelper.SetButton("OK")
        #...Fim Tela parametros

        self.oHelper.SetValue("Da Conta ?","1110227")
        self.oHelper.SetValue("Ate a Conta ?","1110227")
        #self.oHelper.SetValue("Do Centro de Custo ?","         "		)		  
        #self.oHelper.SetValue("Ate o Centro de Custo ?","ZZZZZZZZZ"		)	                   
        #self.oHelper.SetValue("Do Item ?","         "	    )
        #self.oHelper.SetValue("Ate o Item ?","ZZZZZZZZZ"	    )	
        #self.oHelper.SetValue("Da Classe de Valor ?","         "	    )	
        #self.oHelper.SetValue("Ate a Classe de Valor ?","ZZZZZZZZZ"	    )	
        self.oHelper.SetValue("ENTIDADE05 De ?","005"	    )
        self.oHelper.SetValue("ENTIDADE05 Até ? ?","005"	    )		     
        
        self.oHelper.SetButton("OK")
        
        #Browser de Consulta
        self.oHelper.SearchBrowse(f'D MG    {cContaCtb}', 'Filial+cod Conta')
        self.oHelper.SetButton("Visualizar")
        
        #Grid de Consultas...
        #self.oHelper.CheckResult("Saldo Atual", "8.011,00", grid=True, line=1)
        #self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        #....Fim Grid de Consultas
               
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()