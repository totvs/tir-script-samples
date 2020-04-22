from tir import Webapp
import unittest

class TAFA261(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATAF','29/04/2019','T1','D MG 01 ','84')
        #inst.oHelper.Program('TAFA261') chama a rotina pelo campo de pesquisa
        inst.oHelper.SetLateralMenu('Atualizações > Eventos Esocial > Não-periódicos > Afastamento Temp.') #navega pelos menus laterais

    def test_TAFA261_CT001(self):

        #-------------------------Incluir-----------------------------------------------------------------

        # Grid Informações do Afastamento
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01')
        self.oHelper.ClickFolder('Informações do Afastamento')
        self.oHelper.SetValue('CM6_FUNC', '000001')
        self.oHelper.SetValue('CM6_DTAFAS','20032019')
        self.oHelper.SetValue('CM6_MOTVAF','000001')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
     
       #--------------------------Alterar-----------------------------------------------------------
        
        self.oHelper.SearchBrowse('D MG 01 000001', key='Filial+id.func. + Reg. Ativo?')
        self.oHelper.SetButton('Alterar', 'Retificar / Alterar Evento')
        self.oHelper.ClickFolder('Informações do Afastamento')
        self.oHelper.SetValue('CM6_OBSERV', 'Teste alteracao')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')

        #--------------------------Visualizar-----------------------------------------------------------

        self.oHelper.SearchBrowse('D MG 01 000001', key='Filial+id.func. + Reg. Ativo?')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Fechar')

        #--------------------------Termino Afastamento---------------------------------------------------

        self.oHelper.SearchBrowse('D MG 01 000001', key='Filial+id.func. + Reg. Ativo?')
        self.oHelper.SetButton('Alterar', 'Término do Afastamento')
        self.oHelper.SetValue('CM6_DTFAFA', '05042019')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')

         #--------------------------Filtro CPF / Pesquisa por CPF------------------------------------------

        self.oHelper.SearchBrowse('D MG 01 000001', key='Filial+id.func. + Reg. Ativo?')
        self.oHelper.SetButton('Filtro CPF/Nome')
        self.oHelper.SetValue('CPF', '07185885094')
        self.oHelper.SetButton('Ok')

        #--------------------------Filtro CPF / Pesquisa por Nome------------------------------------------

        self.oHelper.SearchBrowse('D MG 01 000001', key='Filial+id.func. + Reg. Ativo?')
        self.oHelper.SetButton('Filtro CPF/Nome')
        self.oHelper.SetValue('Nome', 'JOSE SILVA')
        self.oHelper.SetButton('Ok')
        
        #--------------------------Filtro CPF / Pesquisa por Data Inicio e Data Termino---------------------

        self.oHelper.SearchBrowse('D MG 01 000001', key='Filial+id.func. + Reg. Ativo?')
        self.oHelper.SetButton('Filtro CPF/Nome')
        self.oHelper.SetValue('Data Início', '20032019')
        self.oHelper.SetValue('Data Término', '05042019')
        self.oHelper.SetButton('Ok')

          #--------------------------Gerar XML em Lote-------------------------------------------------------

        self.oHelper.SetButton('Gerar XML em Lote')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')

        #--------------------------Exclusão-----------------------------------------------------------------

        self.oHelper.SearchBrowse('D MG 01 000001', key='Filial+id.func. + Reg. Ativo?')
        self.oHelper.SetButton('Excluir Registro')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')      

                
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()