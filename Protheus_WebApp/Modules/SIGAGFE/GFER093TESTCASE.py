from tir import Webapp
import unittest

class GFER093(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "30/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFER093")
           
    def test_GFER093_CT001(self):

        self.oHelper.SetButton('Outras Ações','Parâmetros')
               
        self.oHelper.SetValue('Dados ?','Ambos')
        self.oHelper.SetValue('Filial Inicial ?','')
        self.oHelper.SetValue('Filial Final ?','ZZZZZZZZ')
        self.oHelper.SetValue('Data Base Filtro ?','Data de Criação')
        self.oHelper.SetValue('Data Inicial ?','01/01/2018')
        self.oHelper.SetValue('Data Final ?','31/12/2020')
        self.oHelper.SetValue('Tipo Relatório ?','Detalhado')
        self.oHelper.SetValue('Mostrar Lançamentos ?','Sim')
        self.oHelper.SetValue('Filtro Lançamentos ?','Todos')
        self.oHelper.SetValue('Lista Doc Carga ?','Sim')
        self.oHelper.SetValue('Pré-fatura Inicial ?','')
        self.oHelper.SetValue('Pré-fatura Final ?','99999999')
        self.oHelper.SetValue('Fatura Inicial ?','')
        self.oHelper.SetValue('Fatura Final ?','9999999999999999')
        self.oHelper.SetValue('Apenas Pendentes ?','Não')

        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Imprimir')
        self.oHelper.SetButton('Sair')
       
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()