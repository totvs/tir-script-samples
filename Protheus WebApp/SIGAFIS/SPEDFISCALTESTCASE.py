from tir import Webapp
import unittest
from datetime import datetime


class SPEDFISCAL(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()
        DateSystem = datetime.today()
        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAFIS",DateSystem.strftime('%d/%m/%Y'),"T1","D MG 01","09")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("SPEDFISCAL")
        

    def SPEDFISCAL_001(self):
      
        DateSystem = datetime.today()

        self.oHelper.SetButton('vançar >>')

        #Parametros para geracao
        
        self.oHelper.SetValue('Data de',DateSystem.strftime('%d/%m/%Y'))
        self.oHelper.SetValue('Data até',DateSystem.strftime('%d/%m/%Y'))
        self.oHelper.SetValue('Livro','*')
        self.oHelper.SetValue('Diretório do Arquivo Destino','') 
        self.oHelper.SetValue('Nome do Arquivo Destino','SPEDFISCAL.TXT')  
        self.oHelper.SetValue('Gera Inventário','2')
        self.oHelper.SetValue('Gera Registros Complementares de Frete','2')
        self.oHelper.SetValue('Data de fechamento do estoque',DateSystem.strftime('%d/%m/%Y'))
        self.oHelper.SetValue('Gera Registros de ECF','2')
        self.oHelper.SetValue('Imprime Credito ST','2')
        self.oHelper.SetValue('Seleciona Filiais ?','2')
        #self.oHelper.ClickBox('Período de Apuração','0 - Mensal')
        self.oHelper.SetValue('Inicio Obrigação Escrituração Fiscal CIAP','2')
        #self.oHelper.SetValue('Considera Valores de Pis/Cofins?','1')
        self.oHelper.SetValue('Gera Bloco K','2')
        self.oHelper.SetValue('Reg. 0210 por Mov.?','2')
        self.oHelper.SetValue('Gera Registros DIFAL (EC 87/15)','1')
        self.oHelper.SetValue('Motivo do Inventário','01')
        self.oHelper.SetValue('Gera Registro 0400 - Natureza da Oper./Prest.?','2')
        self.oHelper.SetValue('Gera H020 - Motivo Inventário 01','1')
        self.oHelper.SetValue('Processa histórico do Bloco K','1')
        self.oHelper.SetValue('Gera Registro C191 - FECP','1')
        self.oHelper.SetValue('Gera Bloco G','1')   
        self.oHelper.SetValue('Gera Bloco B','1')

        self.oHelper.SetButton('vançar >>')

        #Identificacao do Contribuinte

        self.oHelper.SetValue('Código da Finalidade do Arquivo','0')
        self.oHelper.SetValue('Filial de','')
        self.oHelper.SetValue('Filial ate','')
        self.oHelper.SetValue('Perfil de Apresentação','B')
        self.oHelper.SetValue('Tipo de Atividade','0')
        self.oHelper.SetValue('Aglutina por CNPJ+IE ?','0')
        self.oHelper.SetValue('E-Mail','totvs@totvs.com.br')

        self.oHelper.SetButton('vançar >>')

        #Dados do Contabilista

        self.oHelper.SetValue('Nome','Antonio Alves')
        self.oHelper.SetValue('CNPJ','')
        self.oHelper.SetValue('CPF','48769306869')
        self.oHelper.SetValue('CRC','11111111111')
        self.oHelper.SetValue('CEP','03443000')
        self.oHelper.SetValue('Cod. Município','3550308')
        self.oHelper.SetValue('Endereço','Rua Baquia')
        #self.oHelper.SetValue('Número','736')
        self.oHelper.SetValue('Complemento','')
        self.oHelper.SetValue('Bairro','Nova Manchester')
        self.oHelper.SetValue('Fone','1598130992')
        self.oHelper.SetValue('Fax','1598130992')
        self.oHelper.SetValue('E-Mail','totvs@totvs.com.br')

        self.oHelper.SetButton('vançar >>')
        
        
        #Informacoes para processamento do bloco 1

        self.oHelper.SetValue('Gera Registro 1100 - Exportação?','1')
        self.oHelper.SetValue('Gera Registro 1200 - Créditos Fiscais?','1')
        self.oHelper.SetValue('Gera Registro 1300 - Combustíveis?','1')
        self.oHelper.SetValue('Gera Registro 1390 - Usina de açúcar/álcool?','1')
        self.oHelper.SetValue('Gera Registro 1400 - Valores Agregados?','1')
        self.oHelper.SetValue('Gera Registro 1500 - Energia Elétrica?','1')
        self.oHelper.SetValue('Gera Registro 1600 - Cartão de Crédito/Débito?','1')
        self.oHelper.SetValue('Gera Registro 1700 - Documentos Fiscais?','1')
        self.oHelper.SetValue('Gera Registro 1800 - Transporte Aéreo?','1')
        self.oHelper.SetValue('Gera Registro 1400 - Movimentação Anual?','1')
        self.oHelper.SetValue('Gera Registro 1960 - GIAF 1?','1')
        self.oHelper.SetValue('Gera Registros 1970 e 1975 - GIAF 3?','1')
        self.oHelper.SetValue('Gera Registro 1980 - GIAF 4?','1')

        self.oHelper.SetButton('inalizar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
       
        self.oHelper.AssertTrue()
 

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()