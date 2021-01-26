from tir import Webapp
import unittest

class PCOA050(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAPCO", "28/02/2019", "T1", "M SP 01 ", "57")

        inst.oHelper.Program("PCOA050")

    @classmethod
    def test_PCOA050_001(self):
		#TESTE DE INCLUSAO DE LANÇAMENTOS
        #gustavo.campos 15/03/2019
        cLote='0000000003'
        cStatus='1 - Aprovado'
        cItemPesq='0001'
        cValor1='1000000,00'
        cDescri='LANCAMENTO MANUAL SQUAD CONTROL'

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch("M SP 01 ")

        #Chegando cabeçalho
        self.oHelper.SetValue('AKD_LOTE',cLote)

        #Atribuição dos campos para inclusão na AKD - LANÇAMENTOS GRID
        self.oHelper.SetValue('C.O.','057000000001', grid=True, row=1)#AKD_CO
        self.oHelper.SetValue('Classe','000002', grid=True, row=1)#AKD_CLASSE
        self.oHelper.SetValue('Tp. Saldo','RE', grid=True, row=1)#AKD_TPSALD
        self.oHelper.SetValue('Tipo','1', grid=True, row=1)#AKD_TIPO
        self.oHelper.SetValue('Historico',cDescri, grid=True, row=1)#AKD_HIST
        self.oHelper.SetValue('Vlr.Lancto.',cValor1, grid=True, row=1)#AKD_VALOR1  Vlr.Lancto.
        self.oHelper.SetValue('Centro Custo','05700001 ', grid=True, row=1)#AKD_CC 
        self.oHelper.LoadGrid()

        #Operação efetuada Inclusão e apos cancelar para a tela apos incluir um registro 
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f"M SP 01 {cLote}{cItemPesq}","Filial+lote + item")
        self.oHelper.SetButton('Visualizar')

        #Verifica na tela( Cabeçalho ) os valores
        self.oHelper.CheckResult('AKD_LOTE',cLote) #checar COD registro
        self.oHelper.CheckResult('AKD_STATUS',cStatus) # Status da manutenção lançamentos
        
        #Verifica na tela os valores
        self.oHelper.CheckResult('AKD_CO','057000000001', grid=True, line=1, grid_number=1)
        self.oHelper.CheckResult('AKD_CLASSE','000002', grid=True, line=1, grid_number=1)
        self.oHelper.CheckResult('AKD_TPSALD','RE', grid=True, line=1, grid_number=1)
        self.oHelper.CheckResult('AKD_TIPO','Credito', grid=True, line=1, grid_number=1)
        self.oHelper.CheckResult('AKD_HIST',cDescri, grid=True, line=1, grid_number=1)
        self.oHelper.CheckResult('AKD_VALOR1',cValor1, grid=True, line=1, grid_number=1)
        self.oHelper.CheckResult('AKD_CC','05700001 ', grid=True, line=1, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Confirmar')
        self.oHelper.AssertTrue()

    @classmethod
    def test_PCOA050_002(self):
        #Teste de ALteração de lançamentos -
        
        #Variaveis
        cLote='0000000004'
        cItemPesq='0001'
        cValor1='1000000,00'
        cDescri='ALTERACAO MANUAL SQUAD CONTROL TT                               '

        self.oHelper.SearchBrowse(f"M SP 01 {cLote}{cItemPesq}","Filial+lote + item")
        self.oHelper.SetButton('Alterar')

        self.oHelper.SetValue('Vlr.Lancto.',cValor1, grid=True, row=1)# AKD_VALOR1
        self.oHelper.SetValue('Historico',  cDescri, grid=True, row=1)#AKD_HIST
        #Valores alterados acima e carregamento da grid para atualizar.
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Salvar')

        self.oHelper.SearchBrowse(f"M SP 01 {cLote}{cItemPesq}","Filial+lote + item")
        self.oHelper.SetButton('Visualizar')
        
        #Verifica na tela os valores
        self.oHelper.CheckResult('AKD_VALOR1',cValor1, grid=True, line=1, grid_number=1)# AKD_VALOR1
        self.oHelper.CheckResult('AKD_HIST',cDescri, grid=True, line=1, grid_number=1)# AKD_HIST
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Confirmar')
        self.oHelper.AssertTrue()

    @classmethod
    def test_PCOA050_003(self):
        #Estorno de um lançamento - OK
        cLote='0000000005'
        cStatus='3 - Estornado'
        cItemPesq='0001'

        self.oHelper.SearchBrowse(f"M SP 01 {cLote}{cItemPesq}","Filial+lote + item")
        self.oHelper.SetButton('Outras Ações', 'Estornar')
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SearchBrowse(f"M SP 01 {cLote}{cItemPesq}","Filial+lote + item")
        self.oHelper.SetButton('Visualizar')

        #Verifica na tela os valores
        self.oHelper.CheckResult('AKD_LOTE',cLote) #checar COD registro
        self.oHelper.CheckResult('AKD_STATUS',cStatus) # Status da manutenção lançamentos
        self.oHelper.SetButton('Confirmar')
        self.oHelper.AssertTrue()

    @classmethod
    def test_PCOA050_004(self):
        #Exclusão de um lançamento - OK
        cLote='0000000006'
        cItemPesq='0001'

        self.oHelper.SearchBrowse(f"M SP 01 {cLote}{cItemPesq}","Filial+lote + item")
        self.oHelper.SetButton('Outras Ações', 'Excluir')
        # self.oHelper.CheckResult('AKD_LOTE',cLote) #checar COD registro
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SearchBrowse(f"M SP 01 {cLote}{cItemPesq}","Filial+lote + item")
        self.oHelper.SetButton('Visualizar')
        self.oHelper.CheckResult('AKD_LOTE',cLote) #checar COD registros
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.AssertFalse()

    def test_PCOA050_005(self):
        #Teste de ALteração de lançamentos Verificar origem - falta kanoah
        #Variaveis
        cLote='0000000025'
        cItemPesq='0001'

        self.oHelper.SearchBrowse(f"D MG 01 {cLote}{cItemPesq}","Filial+lote + item")
        self.oHelper.SetButton('Alterar')

        self.oHelper.SetButton('Outras Ações','Origem')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    def test_PCOA050_006(self):
        #Teste de ALteração de lançamentos por linha - falta kanoah
        #Variaveis
        cLote='0000000025'
        cItemPesq='0001'

        self.oHelper.WaitShow('Manutenção de Lançamentos')

        self.oHelper.SetKey( key = "F12", wait_show="Parametros", step = 3)
        self.oHelper.SetValue("Alterar por ?","Linha")
        self.oHelper.SetButton("Ok")

        self.oHelper.SearchBrowse(f"D MG 01 {cLote}{cItemPesq}","Filial+lote + item")
        self.oHelper.SetButton('Alterar')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.WaitShow('Manutenção de Lançamentos')

        self.oHelper.SetKey( key = "F12", wait_show="Parametros", step = 3)
        self.oHelper.SetValue("Alterar por ?","Lote")
        self.oHelper.SetButton("Ok")

        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()