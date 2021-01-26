from tir import Webapp
import unittest

class TMSA011(unittest.TestCase): 

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMS','15/10/2020','T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA011') 

    #Inclusão de registro
    def test_TMA011_CT001(self):		

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 03')

        self.oHelper.ClickBox("Descricao", "TABELA DE FRETE A RECEBER TMS", grid_number=1)

        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('DVC_CDRORI','BRASIL')
        self.oHelper.SetValue('DVC_CDRDES','BRASIL')
        self.oHelper.SetValue('DVC_TIPFRE','1')

        self.oHelper.SetValue('DVO_PERMIN','10,77000000',grid=True, grid_number=1, row=1)
        self.oHelper.SetValue('DVO_PERAJU','10,69000000',grid=True, grid_number=1, row=1)
        self.oHelper.SetValue('DVO_VLRMAX','200,00',grid=True, grid_number=1, row=1)
        self.oHelper.SetValue('DVO_PERMAX','5,0410000',grid=True, grid_number=1, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetValue('DVO_PERMIN','11,77000000',grid=True, grid_number=1, row=2)
        self.oHelper.SetValue('DVO_PERAJU','11,69000000',grid=True, grid_number=1, row=2)
        self.oHelper.SetValue('DVO_VLRMAX','210,00',grid=True, grid_number=1, row=2)
        self.oHelper.SetValue('DVO_PERMAX','6,0410000',grid=True, grid_number=1, row=2)
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetValue('DVC_CODCLI','TMSAJU')
        self.oHelper.SetValue('DVC_LOJCLI','ST')
        self.oHelper.SetValue('DVC_CODNEG','01')

        self.oHelper.ClickBox("Serviço", "309", grid_number=1)

        self.oHelper.SetButton('Outras Ações', 'Obs.Com.')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações', 'Comp.Aju.')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Outras Ações', 'Reg.Des')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações', 'Contrato')
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('Outras Ações', 'Destinos')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.ClickFolder("TDA a Receber ")
        self.oHelper.SetButton('Outras Ações', 'Base TDA')
        self.oHelper.WaitShow('Ajuste da Tabela de Frete - INCLUIR')    
        self.oHelper.SetKey("DELETE", grid=True)
        self.oHelper.SetValue('DWZ_VLAJUS','140,00',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()
    
    #Estrutura e Visualização
    def test_TMA011_CT002(self):
        self.oHelper.SearchBrowse(f"M SP    02TMSAJUSTR001BRASIL    ", "Filial+sequencia + Cod.cliente + Loja Cliente + Tab Frete + Cod.reg.ori. + Co")

        self.oHelper.SetButton("Outras Ações", "Estrutura")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"M SP    02TMSAJUSTR001BRASIL    ", "Filial+sequencia + Cod.cliente + Loja Cliente + Tab Frete + Cod.reg.ori. + Co")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Cancelar") 
                       
        self.oHelper.AssertTrue()

    #Excluir
    def test_TMA011_CT003(self):
        self.oHelper.SearchBrowse(f"M SP    02TMSAJUSTR001BRASIL    ", "Filial+sequencia + Cod.cliente + Loja Cliente + Tab Frete + Cod.reg.ori. + Co")

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.WaitShow('Ajuste da Tabela de Frete - EXCLUIR')
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse(f"M SP    02TMSAJUSTR001BRASIL    ", "Filial+sequencia + Cod.cliente + Loja Cliente + Tab Frete + Cod.reg.ori. + Co")                       
        self.oHelper.AssertFalse()
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

