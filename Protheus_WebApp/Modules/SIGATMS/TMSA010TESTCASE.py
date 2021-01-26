from tir import Webapp
import unittest

class TMSA010(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMS','15/10/2020','T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA010') 

        inst.oHelper.AddParameter("MV_TMSTFO","",".T.",".T.",".T.") 
        inst.oHelper.SetParameters() 		

    #Inclusão de registro
    def test_TMA010_CT001(self):		

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 03')

        self.oHelper.ClickBox("Descricao", "TABELA DE FRETE A RECEBER TMS", grid_number=1)

        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('DT0_CDRORI','Q57204')
        self.oHelper.SetValue('DT0_CDRDES','Q57204')
        self.oHelper.SetValue('DT0_TABTAR','0001')
        self.oHelper.SetValue('DT0_CODPRO','TMS-001-PERIGOSO')

        self.oHelper.ClickFolder("TDA a Receber ")
        self.oHelper.SetValue('Ate                   (Dificuldade de acesso com base no total do frete sem imposto.)','999.999.999,9999',grid=True)
        self.oHelper.SetValue('Valor','17,00',grid=True, grid_number=1, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Outras Ações', 'Base TDA')
        self.oHelper.WaitShow('Tabela de Frete - INCLUIR')    
        self.oHelper.SetKey("DELETE", grid=True)
        self.oHelper.SetValue('DVY_VLBASE','140,00',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Outras Ações', 'Comp.Tab.')
        self.oHelper.WaitShow('Tabela de Frete - INCLUIR')
        self.oHelper.SetKey("DELETE", grid=True)
        self.oHelper.SetValue('DTK_EXCMIN','10,0000',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTK_VALMIN','101,33',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTK_VALMAX','200,19',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()
    
    #Copia de registro
    def test_TMA010_CT002(self):
        self.oHelper.SearchBrowse("M SP    R00101Q57204")

        self.oHelper.SetButton("Outras Ações", "Copiar")

        self.oHelper.ClickLabel('Para o Destino')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetValue('Para o Destino','Q57154') 
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Confirma")

        self.oHelper.SearchBrowse("M SP    R00101Q57204Q57154")
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
                       
        self.oHelper.AssertTrue()

    #Exclusão de registro
    def test_TMA010_CT003(self):
        self.oHelper.SearchBrowse("M SP    R00101Q57204")

        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
                       
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

