# coding: UTF-8
from tir import Webapp
import unittest

class CTBS001(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "01/01/2015", "T1", "M SP 02", "34")
        inst.oHelper.Program("CTBS001")

    def test_CTBS001_001(self):
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Finalizar")
        self.oHelper.ClickLabel("ECD")
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetValue("Leiaute 7", True)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Com Centralização", True)
        self.oHelper.SetValue("Z-Normal", True)
        self.oHelper.SetValue("0-Inicio no primeiro dia do ano", True)
        self.oHelper.SetValue("0-Empresa não possui NIRE",True)
        self.oHelper.SetValue("0 - Original", True)
        self.oHelper.SetValue("0  Empresa não é entidade sujeita a auditoria independente.", True)
        self.oHelper.SetValue("0  ECD de empresa não participante de SCP como sócio ostensivo.", True)
        self.oHelper.SetValue("1-PJ em Geral (L100A + L300A da ECF)", True)
        self.oHelper.SetValue("2-Não", True,position=1)
        self.oHelper.SetValue("2-Não", True,position=2)
        self.oHelper.SetButton("Avançar")
        self.oHelper.ClickBox("Empresa/Unidade/Filial", "M SP 02")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("00-Não ha",True)
        self.oHelper.SetValue("Unidade Federativa ?","SP")
        self.oHelper.SetValue("Inscrição ?","")
        self.oHelper.CheckResult("Unidade Federativa ?","SP")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("G-Geral",True)
        self.oHelper.SetValue("Numero de Ordem do Livro ?","000006")
        self.oHelper.SetValue("Natureza do Livro ?","Livro G")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Periodo Inicial Lcto ?", "01/01/2018")
        self.oHelper.SetValue("Periodo Final Lcto ?",   "31/12/2018")
        self.oHelper.SetValue("Apuração do Exercicio(L/P) ?","31/12/2018")
        self.oHelper.SetValue("Calendario ?","218")
        self.oHelper.SetValue("Moeda ?","01")
        self.oHelper.SetValue("Tipo Saldo (Societario) ?","1")
        self.oHelper.SetValue("Conta De ?","")
        self.oHelper.SetValue("Conta Ate ?","ZZZZZZZZZZZZZZZZZZZZ")
        self.oHelper.SetValue("Plano Contas Referencial ?","000001")
        self.oHelper.SetValue("Versão ?","0001")        
        self.oHelper.SetValue("2-Não",True,position=3)
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Periodo Inicial Demons ?","01/01/2018")
        self.oHelper.SetValue("Periodo Final Demons ?","31/12/2018")
        self.oHelper.SetValue("Cod. Conf. Bal. Patrim ?","BP")
        self.oHelper.SetValue("Cod. Conf. DRE ?","DRE")
        self.oHelper.SetValue("1-Não",True)
        self.oHelper.SetValue("DMPL",True)
        self.oHelper.SetValue("J210: Cod.Conf.Dem. ?","210")
        self.oHelper.SetValue("2-Não",True)      
        self.oHelper.SetButton("Avançar") 
        self.oHelper.SetButton("Finalizar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("x")
        self.oHelper.ClickTree("ECD")
        self.oHelper.ClickLabel("Revisão - 000006 - G")
        self.oHelper.SetButton("Sair")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
