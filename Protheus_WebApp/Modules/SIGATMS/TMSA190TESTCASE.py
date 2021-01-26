from tir import Webapp
import unittest
import datetime

class TMSA190(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        dataAtual = str(datetime.datetime.now().strftime("%d/%m,%Y"))
        inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 04 ','43')
        inst.oHelper.Program('TMSA190')

        inst.oHelper.AddParameter("MV_SERMAN"   ,"","555")
        inst.oHelper.SetParameters()

    def test_TMSA190_CT001(self):

        self.oHelper.SetButton('Manifestar')
        self.oHelper.SetBranch('M SP 04')
        self.oHelper.SetValue("Tipo do Manifesto ?", "Normal")
        self.oHelper.SetButton('OK')
        self.oHelper.AssertTrue()

        self.oHelper.SetValue("Filial Origem", "M SP 04")
        self.oHelper.SetValue("Viagem","000052")
        self.oHelper.SetValue("Separar por filial ?", "Não separa")
        self.oHelper.SetValue("Separar por filial de origem ?", "Não")
        self.oHelper.SetValue("Separar por estado ?", "Não")
        self.oHelper.SetValue("Separar regiões isentas ?", "Não")
        self.oHelper.SetValue("Separar por carga perigosa ?", "Não")
        self.oHelper.SetValue("Imprime manifesto ?", "Não")
        self.oHelper.SetValue("Separar região destino ?", "Não")
        self.oHelper.SetValue("Quantidade de documentos ?", "1")    
        self.oHelper.SetButton("OK")
        self.oHelper.AssertTrue()

    def test_TMSA190_CT002(self):

        self.oHelper.SearchBrowse(f'M SP    888100002555')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Outras Ações','Imp.Cad.')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Viagem')
        self.oHelper.SetButton('Outras Ações','Comp.Via.')
        self.oHelper.SetButton('Outras Ações','Imp.Cad.')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Mot.Viag.')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Outras Ações','Aju.Viag.')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Outras Ações','Lac.Veic.')
        self.oHelper.SetButton('Cancelar')        
        self.oHelper.SetButton('Outras Ações','Adiantam./Desp.')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Outras Ações','Val. Inf.')
        self.oHelper.SetButton('Cancelar')        
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Outras Ações','Obs.')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Outras Ações','Id.Ope.Vge.')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Outras Ações','Leg. Doc.')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Leg. Agd. Entrega (A)')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Limite')
        self.oHelper.SetButton('Cancelar')    
        self.oHelper.SetButton('Outras Ações','Rota')
        self.oHelper.SetButton('Fechar')   
        self.oHelper.SetButton('Outras Ações','Docto.')
        self.oHelper.SetButton('Cancelar')         
        self.oHelper.SetButton('Outras Ações','Fornecedores Adicionais')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Prd. Doc.')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Outras Ações','Configurar')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Outras Ações','Legenda')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Histórico do MDF-e')
        self.oHelper.SetButton('Outras Ações','Leg. Documentos')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Leg. Viagens')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Vis.Manifesto')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Outras Ações','Configurar')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Fechar') 
        self.oHelper.SetButton('Outras Ações','MDF-e Consulta')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    def test_TMSA190_CT003(self):

        self.oHelper.SearchBrowse(f'M SP    888100003555')
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton('Sim')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()