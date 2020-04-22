from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

class FISA001(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereco do webapp e o nome do Browser
        inst.oHelper = Webapp()
        DateSystem = datetime.today()
        #Parametros de inicializacao
        inst.oHelper.Setup("SIGAFIS",DateSystem.strftime('%d/%m/%Y'),"T1","XIFIS26","09")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("FISA001")
        

    def FISA001_APURACAO(self):
      
        DateSystem = datetime.today()
        self.oHelper.ClickTree('Apuração EFD Contribuições > Processar Apuração da EFD Contribuições')
        self.oHelper.SetValue('Data Inicial: ?',DateSystem.strftime('%d/%m/%Y'))
        self.oHelper.SetValue('Data Final: ?',DateSystem.strftime('%d/%m/%Y'))
        self.oHelper.SetValue('Livro: ?','*')
        self.oHelper.SetValue('Seleciona Filial ?','2') 
        self.oHelper.SetValue('Tributos: ?','1')  
        self.oHelper.SetValue('Regime PIS/COFINS: ?','1')

        self.oHelper.SetValue('PIS Folha de Salario ?','2')
        self.oHelper.SetValue('Sociedade Cooperativa ?','2')
        self.oHelper.SetValue('Instituicao Financeira ?','2')
        self.oHelper.SetValue('Diferimento ?','2')
        self.oHelper.SetValue('Cupom Fiscal ?','2')
        self.oHelper.SetValue('Detalhamento Regime Caixa ?','4')

        self.oHelper.SetValue('Gera Titulo ?','2')
        self.oHelper.SetValue('Contabiliza ?','2')
        self.oHelper.SetValue('Opção Gravação ?','1')
        self.oHelper.SetValue('Cod. Receita Servico ?','')
        self.oHelper.SetValue('Cod. Receita Demais Operacoe ?','')
        self.oHelper.SetValue('Indicador Natureza PJ ?','')
        self.oHelper.SetValue('Processa Retenções - Saídas ?','1')
        self.oHelper.SetValue('Indicador Regime Cumulativo ? ','1')
        self.oHelper.SetButton('OK')

        self.oHelper.WaitShow('Apuração Processada com Sucesso')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Finalizar')
        self.oHelper.WaitShow('TOTVS - Filial: XIFIS26  - Filial SAO PAUL')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()

    def FISA001_DEMAISDOCS(self):

         #FONTE FISA048

        self.oHelper.ClickTree('Apuração EFD Contribuições > Demais Documentos PIS/COFINS')
       
        self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('CF8_TPREG','2')
        self.oHelper.SetValue('CF8_INDOPE','1')
        self.oHelper.SetValue('CF8_CLIFOR','SP0001')
        self.oHelper.SetValue('CF8_LOJA','01')
        self.oHelper.SetValue('CF8_DTOPER',DateSystem)
        self.oHelper.SetValue('CF8_VLOPER','1000,00')
        self.oHelper.SetValue('CF8_CSTPIS','01')
        self.oHelper.SetValue('CF8_CSTCOF','01')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        
        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('CF8_INDOPE','2')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        self.oHelper.SetButton('Fechar') 
        self.oHelper.SetButton('Fechar') 

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('Outras Ações', 'Excluir', 2)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

    def FISA001_DEDPISCOF(self):

        #FONTE FISA041

        self.oHelper.ClickTree('Apuração EFD Contribuições > Deduções Diversas PIS COFINS')
       
        self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('CF2_PER','102019')
        self.oHelper.SetValue('CF2_ORIDED','99')
        self.oHelper.SetValue('CF2_INDNAT','0')
        self.oHelper.SetValue('CF2_DEDPIS','16,50')
        self.oHelper.SetValue('CF2_DEDCOF','76,00')
        self.oHelper.SetValue('CF2_BASE','1000,00')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('CF2_DEDPIS','18,00')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('Outras Ações', 'Excluir', 2)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

    def FISA001_AJUSTEPISCOF(self):
        
        #FONTE FISA042
    
        self.oHelper.ClickTree('Apuração EFD Contribuições > Ajuste de PIS/COFINS e CPRB')
       
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('CF5_INDAJU','0')
        self.oHelper.SetValue('CF5_PISCOF','0')
        self.oHelper.SetValue('CF5_VALAJU','500,00')
        self.oHelper.SetValue('CF5_CODAJU','05')
        self.oHelper.SetValue('CF5_DTREF',DateSystem)
        self.oHelper.SetValue('CF5_TPAJST','2')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("000001 ")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('CF5_PISCOF','1')
        self.oHelper.SetValue('CF5_TPAJST','2')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("000001 ")
        self.oHelper.SetButton('Outras Ações', 'Excluir', 2)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

    def FISA001_AJUSBCPISCOF(self):
       
        #FONTE FISA210
        
        self.oHelper.ClickTree('Apuração EFD Contribuições > Ajustes Base de Cálculo de PIS e COFINS')
       
        self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('F2Z_TRIB','1')
        self.oHelper.SetValue('F2Z_INDAJU','1')
        self.oHelper.SetValue('F2Z_VALAJU','200,00')
        self.oHelper.SetValue('F2Z_CODAJU','02')
        self.oHelper.SetValue('F2Z_CODCON','01')
        self.oHelper.SetValue('F2Z_DTREF',DateSystem)
        self.oHelper.SetValue('F2Z_CNPJ','86845790000121')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('F2Z_CODAJU','41')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('Outras Ações', 'Excluir', 2)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()
    
    def FISA001_CONTCREDPIS(self):
       
        #FONTE FISA044
        
        self.oHelper.ClickTree('Apuração EFD Contribuições > Controle de saldo de Crédito de PIS')
       
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('Período','102019')
        self.oHelper.SetValue('Cod Cred','101')
        self.oHelper.SetValue('Tot. Cred','500,00')
        self.oHelper.SetValue('Cred. Utiliz','300,00')
        self.oHelper.SetValue('Cred. Disp','200,00')
        self.oHelper.SetValue('Ano.Origem','2019')
        self.oHelper.SetValue('Mes.Origem','10')
        self.oHelper.SetValue('Origem Créd','01')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("102019 ")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('Cred. Utiliz','400,00')
        self.oHelper.SetValue('Cred. Disp','100,00')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("102019 ")
        self.oHelper.SetButton('Outras Ações', 'Excluir', 2)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()


    def FISA001_CONTCREDCOF(self):
       
        #FONTE FISA045
        
        self.oHelper.ClickTree('Apuração EFD Contribuições > Controle de saldo de Crédito da COFINS')
       
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('Período','102019')
        self.oHelper.SetValue('Cod Cred','101')
        self.oHelper.SetValue('Tot. Cred','1500,00')
        self.oHelper.SetValue('Cred. Utiliz','800,00')
        self.oHelper.SetValue('Cred. Disp','700,00')
        self.oHelper.SetValue('Ano.Origem','2019')
        self.oHelper.SetValue('Mes.Origem','10')
        self.oHelper.SetValue('Origem Créd','01')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("102019 ")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('Cred. Utiliz','1000,00')
        self.oHelper.SetValue('Cred. Disp','500,00')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("102019 ")
        self.oHelper.SetButton('Outras Ações', 'Excluir', 2)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()



    def FISA001_RESCREDPISCOF(self):
       
        #FONTE FISA050
        
        self.oHelper.ClickTree('Apuração EFD Contribuições > Ressarcimento de crédito de PIS e COFINS ')
       
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('PIS/COF','0')
        self.oHelper.SetValue('Período','102019')
        self.oHelper.SetValue('Origem','012019')
        self.oHelper.SetValue('Codigo','101')
        self.oHelper.SetValue('Vlr Ress','700,00')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("0 ")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('Vlr Comp','1000,00')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("0 ")
        self.oHelper.SetButton('Outras Ações', 'Excluir', 2)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()


    def FISA001_DEMAISRETENCOES(self):
       
        #FONTE FISA006
        
        self.oHelper.ClickTree('Apuração EFD Contribuições > Demais Retenções')
       
        self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('Dt.retenção',DateSystem)
        self.oHelper.SetValue('Ind.Nat.Ret','03')
        self.oHelper.SetValue('Base Ret','200,00')
        self.oHelper.SetValue('Tot.Retido','1,30')
        self.oHelper.SetValue('Regime','1')
        self.oHelper.SetValue('CNPJ','86845790000121')
        self.oHelper.SetValue('Indic.Ret.','0')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('Indic.Ret.','1')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('Outras Ações', 'Excluir', 2)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

    def FISA001_PERDISPEFDPC(self):
       
        #FONTE FISA089
        
        self.oHelper.ClickTree('Apuração EFD Contribuições > Período Dispensado da EFD-Contribuições')
       
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('Mês EFD','02')
        self.oHelper.SetValue('Ano EFD.','2019')
        self.oHelper.SetValue('Mês Disp.','01')
        self.oHelper.SetValue('Ano Disp.','2019')
        self.oHelper.SetValue('Motivo','04')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("02 ")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('Motivo','99')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("02 ")
        self.oHelper.SetButton('Outras Ações', 'Excluir', 2)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()
  
    def FISA001_RECTRANSMISSAO(self):
       
        #FONTE FISA211
        
        self.oHelper.ClickTree('Apuração EFD Contribuições > Recibos de Transmissão do SPED')
       
        self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('Mês','02')
        self.oHelper.SetValue('Ano','2019')
        self.oHelper.SetValue('Num Recibo','2019120390901940149103KAKDNXL9348928W912O')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('Mês','03')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()
        
        self.oHelper.SearchBrowse("XIFIS26 ")
        self.oHelper.SetButton('Outras Ações', 'Excluir', 2)
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar') 
        
        self.oHelper.AssertTrue()
  
        self.oHelper.SetButton('Sair da página') 
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

        
          
if __name__ == '__main__':
    unittest.main()