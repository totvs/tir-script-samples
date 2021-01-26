from tir import Webapp
import unittest

class ATFA006(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAATF', '01042019', 'T1', 'D MG 01 ')
        inst.oHelper.Program('ATFA006')
    
    @classmethod
    def test_ATFA006_CT001(self): #Inclusão

        self.oHelper.SetButton("Incluir")
        
        self.oHelper.SetValue('FNT_CODIND', '06')
        self.oHelper.SetValue('FNT_DATA', '01/04/2019')
        self.oHelper.SetValue('FNT_TAXA', "5,00000000")    # 0,00000000
        

        self.oHelper.CheckResult('FNT_CODIND', '06')
        self.oHelper.CheckResult('FNT_DATA', '01/04/2019')
        self.oHelper.CheckResult('FNT_TAXA', "5,00000000")    # 0,00000000
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
       
        
    @classmethod
    def test_ATFA006_CT002(self): #Revisar

        self.oHelper.SearchBrowse('07000120180901  ') #posiciona no registro 
        

        self.oHelper.SetButton("Outras Ações", "Revisar")
        
        self.oHelper.SetValue('FNT_TAXA', "10,00000000")    # 6,00000000
        

        self.oHelper.CheckResult('FNT_TAXA', "10,00000000")    # 6,00000000
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def test_ATFA006_CT003(self): #Bloquear

        self.oHelper.SearchBrowse('08000120170801  ') #posiciona no registro 
        

        self.oHelper.SetButton("Bloq. / Desbloq.") 
        
        self.oHelper.SetValue('FNT_MSBLQL', "1 - Sim")    # 0,00000000
        

        self.oHelper.CheckResult('FNT_MSBLQL', "1 - Sim")    # 0,00000000
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    
    @classmethod
    def test_ATFA006_CT004(self): #Exclusão

        self.oHelper.SearchBrowse('09000120170501  ') #posiciona no registro 
        

        self.oHelper.SetButton("Outras Ações", "Excluir")
                   
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def test_ATFA006_CT005(self): #Visualizacao

        self.oHelper.SearchBrowse('10000120170401  ') #posiciona no registro 
        

        self.oHelper.SetButton("Visualizar") 
        
        self.oHelper.CheckResult('FNT_CODIND', '10')
        self.oHelper.CheckResult('FNT_DATA', '01/04/2017')
        self.oHelper.CheckResult('FNT_TAXA', "15,00000000")    # 0,00000000

        
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()  

    @classmethod
    def test_ATFA006_CT006(self): #Desbloqueio

        self.oHelper.SearchBrowse('11000120171201  ') #posiciona no registro 
        

        self.oHelper.SetButton("Bloq. / Desbloq.") 
        
        self.oHelper.SetValue('FNT_MSBLQL', "2 - Nao")

        self.oHelper.CheckResult('FNT_MSBLQL', "2 - Nao")
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()       

    @classmethod
    def test_ATFA006_CT007(self): #Inclusão com curva

        self.oHelper.SetButton("Incluir")   

        self.oHelper.SetValue('FNT_CODIND', '12')
        self.oHelper.SetValue('FNT_DATA', '01/06/2019')
        self.oHelper.SetValue('FNT_CURVA', "10,00")    # 0,00000000
        

        self.oHelper.CheckResult('FNT_CODIND', '12')
        self.oHelper.CheckResult('FNT_DATA', '01/06/2019')
        self.oHelper.CheckResult('FNT_CURVA', "10,00")    # 0,00000000
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")



        self.oHelper.AssertTrue()         

    @classmethod
    def test_ATFA006_CT008(self): #Revisão com curva

        self.oHelper.SearchBrowse('13000120170901  ') #posiciona no registro 
        

        self.oHelper.SetButton("Outras Ações", "Revisar")
        
        self.oHelper.SetValue('FNT_CURVA', "5,00")    # 6,00000000
        

        self.oHelper.CheckResult('FNT_CURVA', "5,00")    # 6,00000000
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")



        self.oHelper.AssertTrue()  

    @classmethod
    def test_ATFA006_CT009(self): #Exportar

        self.oHelper.SearchBrowse('10000120170401  ')         

        self.oHelper.SetButton("Outras Ações", "Exportar")
        
        self.oHelper.SetValue('MV_PAR01', "\\baseline\\atfa006_tir09.csv")
        
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")

        self.oHelper.AssertTrue()      

    @classmethod
    def test_ATFA006_CT010(self): #Importar

        self.oHelper.SetButton("Outras Ações", "Importar")
        
        self.oHelper.SetValue('MV_PAR01', "\\baseline\\atfa006_tir10.csv")
        self.oHelper.SetValue("Gerar rev. para taxa existente  ?","Sim")
        
        self.oHelper.SetButton("Ok")       

        self.oHelper.SearchBrowse('07000220180901  ')          

        self.oHelper.AssertTrue()          

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()