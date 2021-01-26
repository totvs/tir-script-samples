from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc}  MATA340 - ACERTO DE INVENTARIO
#
#@author ADRIANO VIEIRA
#@since 29/10/2019
#@version 1.0
#/*/
#//-------------------------------------------------------------------
class MATA340(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereco do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializacao
        inst.oHelper.Setup("SIGAEST","15/01/2020","T1","D MG 01 ","04")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA340")

    def test_MATA340_001(self):

        #MATA340 - CT021: Produto com Endereco e Numero de Serie

        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Detalhes")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")
        time.sleep(22)

        self.oHelper.AssertTrue()


    def test_MATA340_002(self):

        #MATA340 - Verifica se a tela de estornar reserva esta sendo apresentada
        self.oHelper.AddParameter("MV_RESORD","","1", "1", "1")
        self.oHelper.AddParameter("MV_RESSEQ","","1", "1", "1")
        self.oHelper.AddParameter("MV_M340THR","","", "", "")
        self.oHelper.AddParameter("MV_DELRES","",".T.", ".T.", ".T.")
        self.oHelper.AddParameter("MV_ESTNEG","","N", "N", "N")
        self.oHelper.AddParameter("MV_LIBNODP","","S", "S", "S")
        self.oHelper.AddParameter("MV_RESEST","",".T.", ".T.", ".T.")
        self.oHelper.SetParameters()
   
       
        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetValue("Data de Selecao ?","15/01/2020")
        self.oHelper.SetValue("Mostra Lanctos. Contabeis ?","Nao")
        self.oHelper.SetValue("Aglutina Lanctos. Contabeis ?","Nao")       
        self.oHelper.SetValue("Do  Produto ?","ESTSE0000000000000000000000381")
        self.oHelper.SetValue("Ate o Produto ?","ESTSE0000000000000000000000381")
        self.oHelper.SetValue("Do Armazem ?","01")
        self.oHelper.SetValue("Ate o Armazem ?","01")
        self.oHelper.SetValue("Do  Grupo ?","")
        self.oHelper.SetValue("Ate o Grupo ?","ZZZ")      
        self.oHelper.SetValue("Do  Documento ?","ESTSEX")
        self.oHelper.SetValue("Ate o Documento ?","ESTSEX")
        self.oHelper.SetValue("Considera os Empenhos ?","Todos")
        self.oHelper.SetValue("Atualiza Saldo do Fechamento ?","Nao")   

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")


        self.oHelper.WaitShow("Ajustes - Acerto do Inventario")
        time.sleep(15)

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()