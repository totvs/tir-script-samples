from tir import Webapp
import unittest


class CTBA025(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "25/06/2020", "T1", "D MG 01 ", "34")

        inst.oHelper.Program("CTBA025")

        
     ###########################################################################################
    # Caso de teste 001 - Incluir Rateio                                                       #
    # 25/06/2020                                                                               #
    ###########################################################################################

    def test_CTBA025_001(self):
        #INCLUSÃO
        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01")
        
        self.oHelper.SetValue("CVN_CODPLA", "CBA025",name_attr=True)#Plano Ref.  
        self.oHelper.SetValue("CVN_DSCPLA", "PLANO REFERENCIAL CTBA025",name_attr=True)#Descr.P.Ref 
        self.oHelper.SetValue("CVN_DTVIGI", "01012020",name_attr=True)#Dt.Vig.Inic.
        self.oHelper.SetValue("CVN_DTVIGF", "31122020",name_attr=True)#Dt.Vig.Fim.
        self.oHelper.SetValue("CVN_ENTREF", "10",name_attr=True)#Entidade

        self.oHelper.SetValue("Conta Ref.", "1", grid=True, grid_number=1, row=1)
        self.oHelper.SetValue("Descr.C.Ref.","ATIVO", grid=True, grid_number=1, row=1)
        self.oHelper.SetValue("Tp.Utiliz.","A - Ambos", grid=True, grid_number=1, row=1)
        self.oHelper.SetValue("Classe","1 - Sintética", grid=True, grid_number=1, row=1)
        self.oHelper.SetValue("Nat.Conta","01 - Conta de Ativo", grid=True, grid_number=1, row=1)
        self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetValue("Conta Ref.", "1.01", grid=True, grid_number=1, row=2)
        self.oHelper.SetValue("Descr.C.Ref.","ATIVO CIRCULANTE", grid=True, grid_number=1, row=2)
        self.oHelper.SetValue("Tp.Utiliz.","A - Ambos", grid=True, grid_number=1, row=2)
        self.oHelper.SetValue("Classe","1 - Sintética", grid=True, grid_number=1, row=2)
        self.oHelper.SetValue("Nat.Conta","01 - Conta de Ativo", grid=True, grid_number=1, row=2)
        self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetValue("Conta Ref.", "1.01.01", grid=True, grid_number=1, row=3)
        self.oHelper.SetValue("Descr.C.Ref.","DISPONIBILIDADES", grid=True, grid_number=1, row=3)
        self.oHelper.SetValue("Tp.Utiliz.","A - Ambos", grid=True, grid_number=1, row=3)
        self.oHelper.SetValue("Classe","1 - Sintética", grid=True, grid_number=1, row=3)
        self.oHelper.SetValue("Nat.Conta","01 - Conta de Ativo", grid=True, grid_number=1, row=3)
        self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetValue("Conta Ref.", "1.01.01.01", grid=True, grid_number=1, row=4)
        self.oHelper.SetValue("Descr.C.Ref.","CAIXA GERAL", grid=True, grid_number=1, row=4)
        self.oHelper.SetValue("Tp.Utiliz.","A - Ambos", grid=True, grid_number=1, row=4)
        self.oHelper.SetValue("Classe","1 - Sintética", grid=True, grid_number=1, row=4)
        self.oHelper.SetValue("Nat.Conta","01 - Conta de Ativo", grid=True, grid_number=1, row=4)
        self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetValue("Conta Ref.", "1.01.01.01.01", grid=True, grid_number=1, row=5)
        self.oHelper.SetValue("Descr.C.Ref.","CAIXA MATRIZ", grid=True, grid_number=1, row=5)
        self.oHelper.SetValue("Tp.Utiliz.","A - Ambos", grid=True, grid_number=1, row=5)
        self.oHelper.SetValue("Classe","2 - Analítica", grid=True, grid_number=1, row=5)
        self.oHelper.SetValue("Nat.Conta","01 - Conta de Ativo", grid=True, grid_number=1, row=5)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG    CBA025 1 0001", "Filial+plano Ref. + Conta Ref. + Versão")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("Descr.C.Ref.","CAIXA MATRIZ", grid=True,grid_number=1, line=5)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_CTBA025_002(self):
        #ALTERAÇÃO
        self.oHelper.SearchBrowse(f"D MG    ALTERA 1 0001", "Filial+plano Ref. + Conta Ref. + Versão")

        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("CVN_DSCPLA", "PLANO REFERENCIAL ALTERADO",name_attr=True)#Descr.P.Ref
        self.oHelper.SetValue("Descr.C.Ref.","CAIXA GERAL ALTERADO", grid=True, grid_number=1, row=4) 
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.AssertTrue()



    def test_CTBA025_003(self):
        #EXCLUSÃO

        self.oHelper.SearchBrowse(f"D MG    EXCLUI 1 0001", "Filial+plano Ref. + Conta Ref. + Versão")

        self.oHelper.SetButton("Outras Ações", "Excluir")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("OK")

        self.oHelper.AssertTrue()

    def test_CTBA025_004(self):
        self.oHelper.SearchBrowse(f"D MG    1                             COPIAR0002", "Filial+conta Ref. + Plano Ref. + Versão")

        self.oHelper.SetButton("Outras Ações", "Revisão")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG    1                             COPIAR0002", "Filial+conta Ref. + Plano Ref. + Versão")

        self.oHelper.SetButton("Outras Ações", "Efetivar Revisão")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("x")

        self.oHelper.SetButton("Fechar")

        self.oHelper.WaitShow("Plano Referencial")

        self.oHelper.AssertTrue()

    def test_CTBA025_005(self):
        #COPIAR 

        self.oHelper.SearchBrowse(f"D MG    1                             COPIA20001", "Filial+conta Ref. + Plano Ref. + Versão")

        self.oHelper.SetButton("Outras Ações", "Incluir Versão , Copiar")

        self.oHelper.AssertTrue()

    def test_CTBA025_006(self):
        #EXPORTAR

        self.oHelper.SetButton("Outras Ações", "Exp.Plano.Ref.")

        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("MV_PAR01","\\baseline\\planoreferencialtir.cve",name_attr=True)

        self.oHelper.SetValue("MV_PAR02","TESTE",name_attr=True)

        self.oHelper.CheckHelp(text_help="REGNOIS", button="Fechar")
        
        self.oHelper.SetValue("MV_PAR02","ALTERA",name_attr=True)

        self.oHelper.SetButton("OK")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
