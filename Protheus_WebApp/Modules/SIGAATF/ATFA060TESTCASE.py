# coding: UTF-8
from tir import Webapp
import unittest

class ATFA060(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAATF", "01/06/2015", "T1", "M SP 01 ", "01")
        inst.oHelper.Program("ATFA060")

        inst.oHelper.AddParameter("MV_ATFCATR","","1")

        inst.oHelper.AddParameter("M SP 01 MV_ULTDEPR","","20150531")
        inst.oHelper.AddParameter("M SP 02 MV_ULTDEPR","","20150531")
        inst.oHelper.AddParameter("D MG 01 MV_ULTDEPR","","20200531")
        inst.oHelper.AddParameter("D RJ 01 MV_ULTDEPR","","20200531")

        inst.oHelper.SetParameters()

    def test_ATFA060_001(self):

        chave = "M SP 01 ATF02"
        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)

        self.oHelper.SetButton("Outras Ações", "Canc. Transf.")
        self.oHelper.SetBranch("M SP 01 ")

        # Parâmetros de perguntes
        self.oHelper.SetValue("MV_PAR01", "ATF02", name_attr=True)  # Código Base de
        self.oHelper.SetValue("MV_PAR02", "001", name_attr=True)  # Item de

        self.oHelper.SetValue("MV_PAR03", "ATF02", name_attr=True)  # Código Base Ate
        self.oHelper.SetValue("MV_PAR04", "001", name_attr=True)  # Item Ate

        self.oHelper.SetValue("MV_PAR05", "", name_attr=True)  # Grupo de
        self.oHelper.SetValue("MV_PAR06", "ZZZZ", name_attr=True)  # Grupo ate

        self.oHelper.SetValue("Mostra Lanc Contab ?","Não")  # Mostra Lanc Contab
        self.oHelper.SetValue("Aglut Lancamentos ?","Não")  # Aglut Lancamentos
        self.oHelper.SetValue("Cancelamento ?", "Filial")  # Cancelamento
        self.oHelper.SetButton("OK")

        self.oHelper.WaitShow("Transferencia de Ativos - Cancelar")

        self.oHelper.ClickBox("Cod Base Bem", "ATF02")
        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.SetButton("Sair")

        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)

        self.oHelper.AssertTrue()

    def test_ATFA060_039(self): #Visualizar Transferencia de um bem que foi tranferido FILIAL ORIGEM 

        chave = "M SP 02 ATF02"
        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)

        self.oHelper.SetButton("Outras Ações", "Visualizar Transferencia")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()
    

    def test_ATFA060_040(self): #Visualizar Transferencia de um bem que foi tranferido FILIAL DESTINO

        chave = "M SP 01 ATF02"
        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)

        self.oHelper.SetButton("Outras Ações", "Visualizar Transferencia")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_ATFA060_041(self): #Visualizar Ativo

        chave = "M SP 01 ATF02"
        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)

        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
    def test_ATFA060_029(self): #Transferir entre filiais com geração de nota fiscal

        chave = "D MG 01 TRANSF060"
        self.oHelper.WaitShow('Transferencia de Ativos')
        self.oHelper.SetButton('X')
        self.oHelper.ChangeEnvironment("15/06/2020","T1", "D MG 01 ","01")
        self.oHelper.Program('ATFA060')
        self.oHelper.WaitShow('Transferencia de Ativos')
        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)
        self.oHelper.SetButton("Transferir")

        self.oHelper.SetValue('Contabiliza Online ?', 'Sim')
        self.oHelper.SetValue("Mostra Lanc Contab ?","Sim")  # Mostra Lanc Contab Nao / Sim
        self.oHelper.SetValue("Aglut Lançamentos ?","Sim")  # Aglut Lancamentos
        self.oHelper.SetValue('Botão Filtrar ?', 'Marcar')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('Filial Dest.','D RJ 01')
        self.oHelper.SetValue('Local Dest.','03')
        self.oHelper.CheckHelp(text='ATFBLQLOC',button='Fechar')
        self.oHelper.SetValue('Local Dest.','05')
        self.oHelper.SetValue('CC Desp Dest','CCDESPDES')
        self.oHelper.SetValue('Quant. Dest.','1,000')

        self.oHelper.ClickFolder('Conta Contábil')
        self.oHelper.SetValue('Ct Bem Dest','ATFA060CTBEMDEST')
        self.oHelper.SetValue('Ct Cor Mon D','ATFA060CTACORMOND')
        self.oHelper.SetValue('Ct Des Dep D','ATFA060CTDESDEPD')
        self.oHelper.SetValue('Ct Dep Acu D','ATFA060CTDEPACUD')
        self.oHelper.SetValue('Ct Cor Dep D','ATFA060CTCORDEPD')

        self.oHelper.ClickFolder('Centro de Custo')
        self.oHelper.SetValue('CC Bem Dest','CCBEMDEST')
        self.oHelper.SetValue('CC Cor Mon D','CCCORMOND')
        self.oHelper.SetValue('CC Des Dep D','CCDESDEPD')
        self.oHelper.SetValue('CC Dep Acu D','CCDEPACUD')
        self.oHelper.SetValue('CC Cor Dep D','CCCORDEPD')

        self.oHelper.ClickFolder('Item Contábil')
        self.oHelper.SetValue('It Bem Dest','ITBEMDEST')
        self.oHelper.SetValue('It Cor Mon D','ITCORMOND')
        self.oHelper.SetValue('It Des Dep D','ITDESDEPD')
        self.oHelper.SetValue('It Dep Acu D','ITDEPACUD')
        self.oHelper.SetValue('It Cor Dep D','ITCORDEPD')

        self.oHelper.ClickFolder('Classe de Valor')
        self.oHelper.SetValue('CV Bem Dest','CVBEMDEST')
        self.oHelper.SetValue('CV Cor Mon D','CVCORMOND')
        self.oHelper.SetValue('CV Des Dep D','CVDESDEPD')
        self.oHelper.SetValue('CV Dep Acu D','CVDEPACUD')
        self.oHelper.SetValue('CV Cor Dep D','CVCORDEPD')

        self.oHelper.ClickFolder('Nota Fiscal')
        self.oHelper.SetValue('Gera NF','1 - Sim')
        self.oHelper.SetValue('Serie','UNI')
        self.oHelper.SetValue('Class NF','2 - Classificada')
        self.oHelper.SetValue('TES Saída','547')
        self.oHelper.SetValue('TES Entrada','010')
        self.oHelper.SetValue('Valor da NF','9.000,00')
        self.oHelper.SetValue('Espécie NF','SPED')

        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow('Transferencia de Ativos - TRANSFERIR')
        self.oHelper.ClickGridCell('Hist Lanc',row=3)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.ClickGridCell('Hist Lanc',row=4)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.ClickGridCell('Hist Lanc',row=5)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.ClickGridCell('Hist Lanc',row=6)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Sair')
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()

    def test_ATFA060_042(self):

        self.oHelper.WaitShow('Transferencia de Ativos')

        self.oHelper.SetButton('X')
        self.oHelper.ChangeEnvironment("01/08/2020","T1", "D MG 02 ","01")
        self.oHelper.Program('ATFA060')

        self.oHelper.AddParameter("D MG 01 MV_ULTDEPR","","20200731")
        self.oHelper.AddParameter("D MG 02 MV_ULTDEPR","","20200731")
        self.oHelper.SetParameters()

        self.oHelper.WaitShow('Transferencia de Ativos')

        chave = "D MG 02 NFE000002V"
        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)

        self.oHelper.SetButton("Outras Ações", "Canc. Transf.")
        self.oHelper.SetBranch("D MG 02 ")

        # Parâmetros de perguntes
        self.oHelper.SetValue("MV_PAR01", "NFE000002V", name_attr=True)  # Código Base de
        self.oHelper.SetValue("MV_PAR02", "0001", name_attr=True)  # Item de

        self.oHelper.SetValue("MV_PAR03", "NFE000002V", name_attr=True)  # Código Base Ate
        self.oHelper.SetValue("MV_PAR04", "0001", name_attr=True)  # Item Ate

        self.oHelper.SetValue("MV_PAR05", "", name_attr=True)  # Grupo de
        self.oHelper.SetValue("MV_PAR06", "ZZZZ", name_attr=True)  # Grupo ate

        self.oHelper.SetValue("Mostra Lanc Contab ?","Não")  # Mostra Lanc Contab
        self.oHelper.SetValue("Aglut Lancamentos ?","Não")  # Aglut Lancamentos
        self.oHelper.SetValue("Cancelamento ?", "Filial")  # Cancelamento
        self.oHelper.SetButton("OK")

        self.oHelper.WaitShow("Transferencia de Ativos - Cancelar")

        self.oHelper.ClickBox("Cod Base Bem", "NFE000002V")
        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.SetButton('Sair')

        self.oHelper.AssertTrue()
    
    def test_ATFA060_043(self):

        self.oHelper.WaitShow('Transferencia de Ativos')

        chave = "D MG 01 ATFA060"
        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)

        self.oHelper.SetButton("Transferir")

        self.oHelper.SetValue('Contabiliza Online ?', 'Nao')
        self.oHelper.SetValue("Mostra Lanc Contab ?","Nao")  # Mostra Lanc Contab Nao / Sim
        self.oHelper.SetValue("Aglut Lançamentos ?","Nao")  # Aglut Lancamentos
        self.oHelper.SetValue('Botão Filtrar ?', 'Marcar')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('Grupo Dest.','1000')
        self.oHelper.SetButton('Espelhar')
        self.oHelper.SetButton('Sim')
        
        self.oHelper.SetFocus('Local Dest.')
        self.oHelper.SetKey('F3')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetValue('Local Dest.','05')
        self.oHelper.SetValue('Local Dest.','05')

        self.oHelper.SetValue('Quant. Dest.','1,000')

        self.oHelper.ClickGridCell('CC Bem Dest',row=1,grid_number=2)
        self.oHelper.SetKey('F3',grid=True)
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetValue('CC Bem Dest', 'CCBEMDEST',grid=True, grid_number=2,row=1 )
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Confirmar')

        self.oHelper.SetButton('Fechar')
      
        self.oHelper.AssertTrue()

    def test_ATFA060_044(self):

        chave = "D RJ 01 TRANSF060"
        self.oHelper.SetButton('X')
        self.oHelper.ChangeEnvironment("20/06/2020","T1", "D MG 01 ","01")
        self.oHelper.Program('ATFA060')
        self.oHelper.WaitShow('Transferencia de Ativos')
        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)
        self.oHelper.SetButton("Transferir")

        self.oHelper.SetValue('Contabiliza Online ?', 'Sim')
        self.oHelper.SetValue("Mostra Lanc Contab ?","Sim")  # Mostra Lanc Contab Nao / Sim
        self.oHelper.SetValue("Aglut Lançamentos ?","Sim")  # Aglut Lancamentos
        self.oHelper.SetValue('Botão Filtrar ?', 'Marcar')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('Filial Dest.','D MG 01')
        self.oHelper.SetValue('Quant. Dest.','1,000')

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    
    
    def test_ATFA060_060(self):  ### TEM QUE ABRIR TASK NO PORTAL PARA ENTENDIMENTO SOBRE AS DATAS DO TIR

        self.oHelper.WaitShow('Transferencia de Ativos')

        self.oHelper.SetButton('X')
        self.oHelper.ChangeEnvironment("10/06/2015","T1", "M SP 01 ","01")
        self.oHelper.Program('ATFA060')

        self.oHelper.WaitShow('Transferencia de Ativos')

        chave = "M SP 01 ATF060TRLT"
        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)

        
        self.oHelper.SetButton("Automatico")

        self.oHelper.SetBranch("M SP 01 ")

        self.oHelper.CheckHelp(text='A060DTAQUI',button='Fechar') ### esse help nao deveria aparecer

        ####Erro na ferramenta nao esta sendo possivel fazer o automatico com o tir erro referente as datas

        # self.oHelper.SetValue('Contabiliza Online ?', 'Não')
        # self.oHelper.SetValue("Mostra Lanc Contab ?","Não")  # Mostra Lanc Contab Nao / Sim
        # self.oHelper.SetValue("Aglut Lançamentos ?","Não")  # Aglut Lancamentos
        # self.oHelper.SetValue('Filtro Personalizado ?', 'Não')
        # self.oHelper.SetValue('Do bem ?', 'ATF060TRLT')
        # self.oHelper.SetValue('Até o Bem ?', 'ATF060TRLT')
        # self.oHelper.SetValue('Do Item ?', '0001')
        # self.oHelper.SetValue('Até o Item ?', '0003')
        # self.oHelper.SetButton('Ok')


        # self.oHelper.SetValue('Quant. Dest.','1,000')

        # self.oHelper.SetButton('Confirmar')
      
        self.oHelper.AssertTrue()

        


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
