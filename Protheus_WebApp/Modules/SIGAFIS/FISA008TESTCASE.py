from tir import Webapp
import unittest
from datetime import datetime

class FISA008(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        DateSystem = datetime.today()
        inst.oHelper.Setup("SIGAFIS",DateSystem.strftime('%d/%m/%Y'),"T1","XIFIS26","09")
        inst.oHelper.Program("FISA008")
        

    def FISA008_001(self):
        DateSystem = datetime.today()      
        self.oHelper.SetValue('Data Inicial: ?',DateSystem.strftime('%d/%m/%Y'))
        self.oHelper.SetValue('Data Final: ?',DateSystem.strftime('%d/%m/%Y'))
        self.oHelper.SetValue('Livro: ?','*')
        self.oHelper.SetValue('Seleciona Filial ?','2') 
        self.oHelper.SetValue('Diretorio ?','') 
        self.oHelper.SetValue('Arquivo ?','FISA008.TXT')  
        self.oHelper.SetValue('Agrupa por CNPJ ?','2')
        self.oHelper.SetValue('Regime PIS/COFINS ?','1')
        self.oHelper.SetValue('Tipo Escrituracao ?','0')
        self.oHelper.SetValue('Indicador Situacao Especial ?','')
        self.oHelper.SetValue('Indicaodor Natureza PJ ?','00')
        self.oHelper.SetValue('Atividade Preponderante?','0')
        self.oHelper.SetValue('Numero do Recibo ?','2019120390901940149103KAKDNXL9348928W912O')
        self.oHelper.SetValue('Sociedade Cooperativa ?','')
        self.oHelper.SetValue('Tipo Contribuicao ?','1')
        self.oHelper.SetValue('Indicador Regime Cumulativo ?','1')
        self.oHelper.SetValue('Indicador Bloco I ?','04')
        self.oHelper.SetValue('Gera Cupom Fiscal ?','1')
        self.oHelper.SetValue('Gera Bloco P ?','1')
        self.oHelper.SetValue('Incidencia Tributaria (0145) ?','1')
        self.oHelper.SetValue('Gera Registro 0400 ?','1')
        self.oHelper.SetValue('Dispensa ECD - 1.774/2017?','1')    
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('Nome ?','Antonio Alves')
        self.oHelper.SetValue('CNPJ ?','')
        self.oHelper.SetValue('CPF ?','48769306869')
        self.oHelper.SetValue('CRC ?','11111111111')
        self.oHelper.SetValue('CEP ?','03443000')
        self.oHelper.SetValue('Cod. Municipio ?','3550308')
        self.oHelper.SetValue('Endereco ?','Rua Baquia')
        self.oHelper.SetValue('Numero ?','736')
        self.oHelper.SetValue('Complemento ?','TERREO')
        self.oHelper.SetValue('Bairro ?','Nova Manchester')
        self.oHelper.SetValue('Telefone ?','1598130992')
        self.oHelper.SetValue('Fax ?','1598130992')
        self.oHelper.SetValue('Email ?','totvs@totvs.com.br')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Finalizar')
        self.oHelper.AssertTrue()
        self.oHelper.SetButton('Sair da página') 
 
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()