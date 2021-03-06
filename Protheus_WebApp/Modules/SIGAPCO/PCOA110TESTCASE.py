from tir import Webapp
import unittest
from datetime import datetime


class PCOA110(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper =  Webapp()
        inst.oHelper.Setup('SIGAPCO', '30/08/2019', 'T1', 'D MG 01 ')
        inst.oHelper.Program('PCOA110')
        
    #Inclusao
    
    def test_PCOA110_CT001(self):

        cCodigo     = 'MYPLNPCO0000001'
        cContaPai   = 'PCOR0'
        
        #Posicionar no registro
        self.oHelper.SearchBrowse(f'D MG 01 {cCodigo}0001')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.WaitShow('Controle de Usuarios da Planilha Orcamentaria - VISUALIZAR')
        #Abrir item pesquisar conta orçamentária
        self.oHelper.SetButton('Outras Ações', 'Pesquisar')
        self.oHelper.WaitShow('Controle de Usuarios da Planilha Orcamentaria - VISUALIZAR')
        self.oHelper.SetValue("MV_PAR01",cContaPai    )
        self.oHelper.ClickCheckBox("Utilizar Pesquisa Exata",1)
        self.oHelper.ClickCheckBox("Pesquisar Proxima Ocorrencia",1)
        self.oHelper.SetButton('Ok')  
        #Fim Pesquisar
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SearchBrowse(f'D MG 01 {cCodigo}0001')
        self.oHelper.AssertTrue()
    
    #Alteração
    
    def test_PCOA110_CT002(self):

        cCodigo     = 'MYPLNPCO0000001'
        cContaPai   = 'PCOR0'
        cUsuario1   = '000005'
        cUsuario2   = '000006'
        cUsuario3   = '000063'

        
        #Posicionar no registro
        self.oHelper.SearchBrowse(f'D MG 01 {cCodigo}0001')
        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Controle de Usuarios da Planilha Orcamentaria - ALTERAR')

        #Abrir item pesquisar conta orçamentária
        self.oHelper.SetButton('Outras Ações', 'Pesquisar')
        self.oHelper.WaitShow('Controle de Usuarios da Planilha Orcamentaria - ALTERAR')
        self.oHelper.SetValue("MV_PAR01",cContaPai    )
        self.oHelper.ClickCheckBox("Utilizar Pesquisa Exata",1)
        self.oHelper.ClickCheckBox("Pesquisar Proxima Ocorrencia",1)
        self.oHelper.SetButton('Ok')  
        #Fim Pesquisar
        
        #primeiro usuário
        self.oHelper.SetButton('Outras Ações', 'Usuarios')
        self.oHelper.ClickMenuPopUpItem("Incluir Usuario")
        
        self.oHelper.ClickFolder('Propriedades do Usuario')
        self.oHelper.SetValue('AKG_USER', cUsuario1)
        self.oHelper.SetValue('AKG_ESTRUT', '1'    )#1- Bloqueado 2- Visualizar 3-Alterar 4-Controle Total
        self.oHelper.SetValue('AKG_ITENS' , '2'    )
        self.oHelper.SetValue('AKG_CNTUSU', '2'    )

        self.oHelper.ClickFolder('Outros')
        self.oHelper.SetValue('AKG_REVISA', '3') # 1- bloqueado 2-revisar 3- Iniciar/Revisar/Finalizar
        self.oHelper.SetValue('AKG_ITMCTB', '2') # 1-Restricao Acesso IC  2-Controle Total
        self.oHelper.SetValue('AKG_CCUSTO', '2') # 1- Restricao Acesso CC  2-Controle Total
        self.oHelper.SetValue('AKG_CLAVLR', '2')  # 1- Restrical Acesso Cl. Vlr 2-Controle Total
        self.oHelper.SetValue('AKG_ENTIDA', '2')  # 1-Restricao Acesso Entidades - 2 Controle Total
        self.oHelper.SetButton('Salvar')
        
        self.oHelper.WaitShow('Controle de Usuarios da Planilha Orcamentaria - ALTERAR')

        ## Inclusão do segundo usuário
        self.oHelper.SetButton('Outras Ações', 'Usuarios')
        self.oHelper.ClickMenuPopUpItem("Incluir Usuario")
        
        self.oHelper.ClickFolder('Propriedades do Usuario')
        self.oHelper.SetValue('AKG_USER', cUsuario2)
        self.oHelper.SetValue('AKG_ESTRUT', '1'    )#1- Bloqueado 2- Visualizar 3-Alterar 4-Controle Total
        self.oHelper.SetValue('AKG_ITENS' , '4'    )
        self.oHelper.SetValue('AKG_CNTUSU', '4'    )

        self.oHelper.ClickFolder('Outros')
        self.oHelper.SetValue('AKG_REVISA', '3') # 1- bloqueado 2-revisar 3- Iniciar/Revisar/Finalizar
        self.oHelper.SetValue('AKG_ITMCTB', '2') # 1-Restricao Acesso IC  2-Controle Total
        self.oHelper.SetValue('AKG_CCUSTO', '2') # 1- Restricao Acesso CC  2-Controle Total
        self.oHelper.SetValue('AKG_CLAVLR', '2')  # 1- Restrical Acesso Cl. Vlr 2-Controle Total
        self.oHelper.SetValue('AKG_ENTIDA', '2')  # 1-Restricao Acesso Entidades - 2 Controle Total
        self.oHelper.SetButton('Salvar')
        
        self.oHelper.WaitShow('Controle de Usuarios da Planilha Orcamentaria - ALTERAR')

        ## Inclusão do terceiro usuário
        self.oHelper.SetButton('Outras Ações', 'Usuarios')
        self.oHelper.ClickMenuPopUpItem("Incluir Usuario")
        
        self.oHelper.ClickFolder('Propriedades do Usuario')
        self.oHelper.SetValue('AKG_USER', cUsuario3)
        self.oHelper.SetValue('AKG_ESTRUT', '1'    )#1- Bloqueado 2- Visualizar 3-Alterar 4-Controle Total
        self.oHelper.SetValue('AKG_ITENS' , '4'    )
        self.oHelper.SetValue('AKG_CNTUSU', '4'    )

        self.oHelper.ClickFolder('Outros')
        self.oHelper.SetValue('AKG_REVISA', '3') # 1- bloqueado 2-revisar 3- Iniciar/Revisar/Finalizar
        self.oHelper.SetValue('AKG_ITMCTB', '2') # 1-Restricao Acesso IC  2-Controle Total
        self.oHelper.SetValue('AKG_CCUSTO', '2') # 1- Restricao Acesso CC  2-Controle Total
        self.oHelper.SetValue('AKG_CLAVLR', '2')  # 1- Restrical Acesso Cl. Vlr 2-Controle Total
        self.oHelper.SetValue('AKG_ENTIDA', '2')  # 1-Restricao Acesso Entidades - 2 Controle Total
        self.oHelper.SetButton('Salvar')

        self.oHelper.WaitShow('Controle de Usuarios da Planilha Orcamentaria - ALTERAR')

        #posicionar no primeiro usuário
        self.oHelper.ClickGridCell("Descricao", 2)

        ## Alterar propriedades do usuário
        self.oHelper.SetButton('Outras Ações', 'Usuarios')
        self.oHelper.ClickMenuPopUpItem("Alterar Propriedades")

        self.oHelper.ClickFolder('Propriedades do Usuario')
        self.oHelper.SetValue('AKG_ESTRUT', '2'    )#1- Bloqueado 2- Visualizar 3-Alterar 4-Controle Total
        self.oHelper.SetValue('AKG_ITENS' , '2'    )
        self.oHelper.SetValue('AKG_CNTUSU', '2'    )
        
        self.oHelper.ClickFolder('Outros')
        self.oHelper.SetValue('AKG_REVISA', '1') # 1- bloqueado 2-revisar 3- Iniciar/Revisar/Finalizar
        self.oHelper.SetButton('Salvar')

        self.oHelper.WaitShow('Controle de Usuarios da Planilha Orcamentaria - ALTERAR')

        ## Excluir usuário
        self.oHelper.SetButton('Outras Ações', 'Usuarios')
        self.oHelper.ClickMenuPopUpItem("Excluir Usuario")
        self.oHelper.SetButton('Confirmar')

        
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'D MG 01 {cCodigo}0001')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()    