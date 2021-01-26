from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA320 - recalculo de custo
#@author JEFFERSON SILVA DE SOUSA
#@since 16/10/2019
#@version 1.0
#/*/
#//-------------------------------------------------------------------
class MATA320(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAEST","16/10/2019","T1","D MG 01 ","04")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA320")
    #CT001 Calculo de custo com base na estrutura
    def test_MATA320_001(self):
        Cod   = 'ESTSE0000000000000000000000565'
        Custo = 0
        #Variaveis de Verificaçao

        self.oHelper.SetButton("Parâmetros")     

        self.oHelper.SetValue("Utilizar Qual Moeda ?", 'Nenhuma')
        self.oHelper.SetValue("Utilizar Taxa ?", 'Mensal')       
        self.oHelper.SetValue('Calcular os Custos Por ?',"Estrutura")
        self.oHelper.SetValue('Considerar Ult. Preco Compra ?',"Sim")
        self.oHelper.SetValue('Dt.Final Ref.Taxa ?',"16/10/2019")
        self.oHelper.SetValue('Do Tipo do Produto',"")
        self.oHelper.SetValue('Ate o Tipo do Produto',"ZZ")      
        self.oHelper.SetValue('Do Grupo do Produto',"EST1") 
        self.oHelper.SetValue('Ate o Grupo do Produto',"EST1") 
        self.oHelper.SetValue("Considerar Qtdes. Negativa ?", 'Sim')
        self.oHelper.SetValue("Avisar Divergencia ?", 'Atualizar')
        self.oHelper.SetValue("Seleciona filiais ?", 'Nao')
        self.oHelper.SetValue("Considera Mão de Obra?", 'Ambos')
        self.oHelper.SetValue("Considera Tipo Dec. OP ?", 'Sim')
                              
      
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")
        #######################################################
        ##  Verificando se atualizou o valor de custo do PA  ##
        #######################################################

        self.oHelper.SetLateralMenu("Atualizações > Cadastros > Produto > Produtos")
        #self.oHelper.WaitShow("Atualizacao de Produtos")
        time.sleep(3)
        self.oHelper.SearchBrowse(f"D MG 01 {Cod}", "Filial+codigo")
        self.oHelper.SetButton("Visualizar")
        time.sleep(4)
      
        Custo = float(self.oHelper.GetValue("B1_CUSTD").replace(",","."))
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetKey("ESC")
        self.oHelper.Program('MATA320')    
        Custo > 0
        self.oHelper.AssertTrue()     

    def test_MATA320_002(self):
        #self.oHelper.WaitShow("Recálculo do Custo de Reposição")
        time.sleep(3)
        self.oHelper.SetButton("Parâmetros")     

        self.oHelper.SetValue("Utilizar Qual Moeda ?", 'Nenhuma')
        self.oHelper.SetValue("Utilizar Taxa ?", 'Mensal')       
        self.oHelper.SetValue('Calcular os Custos Por ?',"Ult Cust Compra")
        self.oHelper.SetValue('Considerar Ult. Preco Compra ?',"Sim")
        self.oHelper.SetValue('Dt.Final Ref.Taxa ?',"16/10/2019")
        self.oHelper.SetValue('Do Tipo do Produto',"")
        self.oHelper.SetValue('Ate o Tipo do Produto',"ZZ")      
        self.oHelper.SetValue('Do Grupo do Produto',"EST1") 
        self.oHelper.SetValue('Ate o Grupo do Produto',"EST1") 
        self.oHelper.SetValue("Considerar Qtdes. Negativa ?", 'Nao')
        self.oHelper.SetValue("Avisar Divergencia ?", 'Atualizar')
        self.oHelper.SetValue("Seleciona filiais ?", 'Nao')
        self.oHelper.SetValue("Considera Mão de Obra?", 'Rot. Operações')
        self.oHelper.SetValue("Considera Tipo Dec. OP ?", 'Sim')
                              
      
        self.oHelper.SetButton("Ok")
              
        self.oHelper.AssertTrue()

    def test_MATA320_003(self):
        #self.oHelper.WaitShow("Recálculo do Custo de Reposição")
        time.sleep(3)
        self.oHelper.SetButton("Parâmetros")     

        self.oHelper.SetValue("Utilizar Qual Moeda ?", '2a moeda')
        self.oHelper.SetValue("Utilizar Taxa ?", 'Diaria')       
        self.oHelper.SetValue('Calcular os Custos Por ?',"Ult Prec Compra")
        self.oHelper.SetValue('Considerar Ult. Preco Compra ?',"Sim")
        self.oHelper.SetValue('Dt.Final Ref.Taxa ?',"16/10/2019")
        self.oHelper.SetValue('Do Tipo do Produto',"")
        self.oHelper.SetValue('Ate o Tipo do Produto',"ZZ")      
        self.oHelper.SetValue('Do Grupo do Produto',"EST1") 
        self.oHelper.SetValue('Ate o Grupo do Produto',"EST1") 
        self.oHelper.SetValue("Considerar Qtdes. Negativa ?", 'Nao')
        self.oHelper.SetValue("Avisar Divergencia ?", 'Atualizar')
        self.oHelper.SetValue("Seleciona filiais ?", 'Nao')
        self.oHelper.SetValue("Considera Mão de Obra?", 'Rot. Operações')
        self.oHelper.SetValue("Considera Tipo Dec. OP ?", 'Sim')
                              
      
        self.oHelper.SetButton("Ok")
              
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()