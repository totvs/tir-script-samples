from tir import Webapp
import unittest

class PCOA490(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper =  Webapp()
        inst.oHelper.Setup('SIGAPCO', '26/02/2019', 'T1', 'M SP 01 ')
        inst.oHelper.Program('PCOA490')
    
    #Inclusao
    @classmethod
    def test_PCOA490_CT001(self):

        codigoCT001 = '000000000000003'

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 01')

        self.oHelper.SetValue('ALV_CODIGO', codigoCT001)
        self.oHelper.SetValue('ALV_DESCRI', '00PCO INCLUSAO')
        self.oHelper.SetValue('ALV_TPPERI', '6'             )
        self.oHelper.SetValue('ALV_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('ALV_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('ALV_CTRUSR', '1'             )

        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT001}0001')

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult('ALV_CODIGO', codigoCT001      )
        self.oHelper.CheckResult('ALV_DESCRI', '00PCO INCLUSAO' )
        self.oHelper.CheckResult('ALV_TPPERI','6'               )
        self.oHelper.CheckResult('ALV_INIPER','01/01/2019'      )
        self.oHelper.CheckResult('ALV_FIMPER','31/12/2019'      )
        self.oHelper.CheckResult('ALV_CTRUSR','1'               )

        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()
    
    #Alteração
    @classmethod
    def test_PCOA490_CT002(self):

        codigoCT002 = '000000000000004'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT002}0001')
        
        self.oHelper.SetButton('Outras ações', 'Alterar')

        self.oHelper.SetValue('ALV_DESCRI', '00PCO ALTERADO')
        self.oHelper.SetValue('ALV_TPPERI', '5'              )
        self.oHelper.SetValue('ALV_INIPER', '01/01/2019'     )
        self.oHelper.SetValue('ALV_FIMPER', '30/06/2019'     )
        self.oHelper.SetValue('ALV_CTRUSR', '1'              )

        self.oHelper.SetButton('Salvar')

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT002}0001')

        self.oHelper.SetButton('Visualizar')

        self.oHelper.CheckResult('ALV_CODIGO', codigoCT002      )
        self.oHelper.CheckResult('ALV_DESCRI', '00PCO ALTERADO' )
        self.oHelper.CheckResult('ALV_TPPERI','5'               )
        self.oHelper.CheckResult('ALV_INIPER','01/01/2019'      )
        self.oHelper.CheckResult('ALV_FIMPER','30/06/2019'      )
        self.oHelper.CheckResult('ALV_CTRUSR','1'               )

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    #Exclusao
    @classmethod
    def test_PCOA490_CT003(self):
        
        codigoCT003 = '000000000000005'
        
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT003}0001')

        self.oHelper.SetButton('Outras ações', 'Excluir')
        self.oHelper.SetButton('Sim')
        
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT003}0001')

        self.oHelper.AssertFalse

    #Mudança de grid, nas linhas e ao salvar
    @classmethod
    def test_PCOA490_CT004(self):

        codigoCT004 = '000000000000010'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')

        self.oHelper.SetValue('MV_PAR01','02-Despesas',name_attr=True)

        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('9001-DESP. AUTOMACAO')
        self.oHelper.ClickIcon('Editar')        

        ##Validando ao mudar de linha
        self.oHelper.SetValue("ALX_CLASSE","000001",grid=True,row=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("UP")
        self.oHelper.CheckResult("ALX_CLASSE","000001",grid=True,line=2)
        self.oHelper.LoadGrid()

        ##Validando ao mudar de linha e Confirmar
        self.oHelper.SetValue("ALX_CLASSE","000002",grid=True,row=2)
        self.oHelper.LoadGrid()
        self.oHelper.CheckResult("ALX_CLASSE","000002",grid=True,line=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("UP")

        self.oHelper.SetValue("ALX_CLASSE","000001",grid=True,row=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("UP")
        self.oHelper.CheckResult("ALX_CLASSE","000001",grid=True,line=2)
        self.oHelper.LoadGrid()

        #self.oHelper.WaitShow
        self.oHelper.SetButton("Confirmar")
        self.oHelper.LoadGrid()

        ###Aguardando automação
        ###self.oHelper.ClickIcon("X")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()    