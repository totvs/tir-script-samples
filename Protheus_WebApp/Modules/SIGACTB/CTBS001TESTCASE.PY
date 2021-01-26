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
        # Layout 7  -   Diario Presumido
        if self.oHelper.GetRelease() > '12.1.025':

            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            # self.oHelper.ClickLabel("ECD")
            self.oHelper.ClickTree("ECD")
            self.oHelper.SetButton("Incluir")
            self.oHelper.SetValue("Leiaute 7", True)  # Disponiveis Leiaute 1 ao 7
            self.oHelper.SetButton("Ok")

            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Avançar")
            #-----------------------------------------------------------------------------
            ##   Informe os dados da empresa escolhida para escrituração  ##
            #-----------------------------------------------------------------------------

            self.oHelper.SetValue("Com Centralização", True)
            #self.oHelper.SetValue("Sem Centralização", True)

            # Situação Especial ?
            self.oHelper.SetValue("Z-Normal", True)
            # self.oHelper.SetValue("0-Abertura",True)
            # self.oHelper.SetValue("1-Cosão",True)
            # self.oHelper.SetValue("2-Fusão",True)
            # self.oHelper.SetValue("3-Incorporação",True)
            # self.oHelper.SetValue("4-Extinção",True)
            # self.oHelper.SetValue("5-Transformação",True)

            # Indicador início de Periodo ?
            self.oHelper.SetValue("0-Inicio no primeiro dia do ano", True)
            # self.oHelper.SetValue("1-Abertura",True)
            #self.oHelper.SetValue("2-Resultante Cisao/Fusao ou remanescente...",True)
            #self.oHelper.SetValue("3-Inicio Obrigatoriedade Entrega ECD",True)

            #Indicador de existência de NIRE ? 
            self.oHelper.SetValue("0-Empresa não possui NIRE",True)
            #self.oHelper.SetValue("1-Empresa possui NIRE",True)

            #Indicador de finalidade da escrituração ?
            self.oHelper.SetValue("0 - Original", True)
            ##self.oHelper.SetValue("1 - Substituta",True)

            # self.oHelper.SetValue("Hash da escrituração de finalidade da escrituração ?","")
            # self.oHelper.SetValue("NIRE da Escrituração Substituida ?","") ##Bloqueado

            # indicador Empr.Grande Porte ?
            self.oHelper.SetValue(
                "0  Empresa não é entidade sujeita a auditoria independente.", True)
            ##self.oHelper.SetValue("1 - Empresa é entidade sujeita a auditoria independente.",True)

            # Tipo da ECD (SCP) ?
            self.oHelper.SetValue(
                "0  ECD de empresa não participante de SCP como sócio ostensivo.", True)
            ##self.oHelper.SetValue("1 - ECD de empresa participante de SCP como sócio ostensivo.",True)
            ##self.oHelper.SetValue("1 - ECD da SCP",True)

            # Plano Contas Referencial ?
            self.oHelper.SetValue("1-PJ em Geral (L100A + L300A da ECF)", True)
            #self.oHelper.SetValue(
            #    "2-PJ em GeralLucro Presumido (P100 + P150 da ECF)", True)
            #self.oHelper.SetValue("3-Financeiras (L100B + L300B da ECF)", True)
            #self.oHelper.SetValue("4-Seguradoras (L100C + L300C da ECF)", True)
            #self.oHelper.SetValue(
            #    "5-Imunes e Isentas em Geral (U100A + U150A da ECF)", True)
            #self.oHelper.SetValue(
            #    "6-Financeiras-Imunes e Isentas (U100B + U150B da ECF)", True)
            #self.oHelper.SetValue(
            #    "7-Seguradoras-Imunes e Isentas (U100C + U150C da ECF)", True)
            #self.oHelper.SetValue(
            #    "8-Entidades Fechadas Prev Complementar (U100D + U150D da ECF)", True)
            #self.oHelper.SetValue(
            #    "9-Partidos Politicos (U100E + U150E da ECF)", True)
            #self.oHelper.SetValue(
            #    "10-Financeiras  Lucro Presumido (P100B + P150B da ECF)", True)

            # Moeda funcional diferente da nacional ?
            self.oHelper.SetValue("1-Sim", True, position=1)
            #self.oHelper.SetValue("2-Não", True,position=1)

            # Escrituração Contábeis consolidadas ?
            #self.oHelper.SetValue("1-Sim", True)
            self.oHelper.SetValue("2-Não", True,position=2)

            #self.oHelper.SetValue("Codigo Identif. Bloco K ?","")
            # Encerra dados da empresa para escrituração
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ##  Quais são as filiais que essa empresa centralizadora?   ##
            #-----------------------------------------------------------------------------
            #PASSO 03 FILIAIS
            self.oHelper.ClickBox("Empresa/Unidade/Filial", "M SP 02")
            self.oHelper.SetButton("Avançar")  # Encerra escolha de filiais

            ##  Informe neste passo, quais as incrições de sua empresa. ##
            # Outras Inscrições ?
            self.oHelper.SetValue("00-Não ha",True)
            #self.oHelper.SetValue("01-Bco Cent. do Brasil / BACEN",True)
            #self.oHelper.SetValue("02-Super. de Seg. Privados / SUSEP",True)
            #self.oHelper.SetValue("03-Comis. de Val. Mobiliários / CVM",True)
            #self.oHelper.SetValue("04-Agência Nacional de Transportes Terrestres (ANTT)",True)
            #self.oHelper.SetValue("UF-Secretarias de Estado",True)

            self.oHelper.SetValue("Unidade Federativa ?","SP")
            self.oHelper.SetValue("Inscrição ?","")

            #self.oHelper.SetValue("Codigo da SCP ?","")    #BLOQUEADO
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ##  Informe neste passo, quais os dados principais para a escrituração. PASSO 1/3   ##
            #-----------------------------------------------------------------------------
            #Indicação da Escrituracao ? 
            #self.oHelper.SetValue("G-Geral",True)
            self.oHelper.SetValue("R-Diário Resumido",True)
            ##self.oHelper.SetValue("A-Diário Auxiliar",True)
            ##self.oHelper.SetValue("B-Balancete Diário",True)

            self.oHelper.SetValue("Numero de Ordem do Livro ?","000007")
            self.oHelper.SetValue("Natureza do Livro ?","Livro R")
            self.oHelper.SetButton("Avançar") #Encerra dados principais da escrituração 1/3

            #-----------------------------------------------------------------------------
            ##  Informe neste passo, quais os dados principais para a escrituração. PASSO 2/3   ##
            #-----------------------------------------------------------------------------
            
            self.oHelper.SetValue("Periodo Inicial Lcto ?", "01/01/2018")
            self.oHelper.SetValue("Periodo Final Lcto ?",   "31/12/2018")
            self.oHelper.SetValue("Apuração do Exercicio(L/P) ?","31/12/2018")
            self.oHelper.SetValue("Calendario ?","218")
            self.oHelper.SetValue("Moeda ?","01")
            self.oHelper.SetValue("Tipo Saldo (Societario) ?","1")
            self.oHelper.SetValue("Conta De ?","")
            self.oHelper.SetValue("Conta Ate ?","ZZZZZZZZZZZZZZZZZZZZ")
            self.oHelper.SetValue("Plano Contas Referencial ?","000001") #Branco a nao ser que precise
            self.oHelper.SetValue("Versão ?","0001")                   #Branco a nao ser que precise

            #Arquivo Trimestral Unificado ? 
            #self.oHelper.SetValue("1-Sim",True)
            self.oHelper.SetValue("2-Não",True,position=3)
            self.oHelper.SetButton("Avançar")   #Encerra informações principais Passo 2/3
            #-----------------------------------------------------------------------------
            ##   Informe neste passo, quais os dados principais para a escrituração. PASSO 3/3   ##
            #-----------------------------------------------------------------------------
            self.oHelper.SetValue("Periodo Inicial Demons ?","01/01/2018")
            self.oHelper.SetValue("Periodo Final Demons ?","31/12/2018")
            self.oHelper.SetValue("Cod. Conf. Bal. Patrim ?","BP")
            self.oHelper.SetValue("Cod. Conf. DRE ?","DRE")

            #self.oHelper.SetValue("Outras Demonstracoes ?","")# BLOQUEADO

            #Processa C.Custo ? ? 
            self.oHelper.SetValue("1-Não",True)
            #self.oHelper.SetValue("2-Sim",True)

            #J210:Indicador do tipo de demostração ? ? 
            ##self.oHelper.SetValue("DLPA",True)
            self.oHelper.SetValue("DMPL",True)

            self.oHelper.SetValue("J210: Cod.Conf.Dem. ?","210")
            #self.oHelper.SetValue("J310: Cod.Conf.DFC ?","")   #BLOQUEADO
            #self.oHelper.SetValue("J410: Cod.Conf.DVA ?","")   #BLOQUEADO

            #J200:Historico Fato Contabil - Cadastrar ?                             #BLOQUEADO
            ##self.oHelper.SetValue("1-Sim",True)                                   #BLOQUEADO
            ##self.oHelper.SetValue("2-Não",True)                                   #BLOQUEADO

            #J215:Detalhar Fato Contabil - Detalhar ? 
            self.oHelper.SetValue("2-Não",True,position=5)  
            # self.oHelper.SetValue("2-Não",True,position=2)      

            ##self.oHelper.SetValue("001: Dem. Abrang. do Período ","")             #BLOQUEADO
            ##self.oHelper.SetValue("002: Dem. Fluxos de Caixa ? ","")              #BLOQUEADO
            ##self.oHelper.SetValue("003: Dem. do Valor Adicionado ?","")           #BLOQUEADO
            ##self.oHelper.SetValue("010: Notas Explicativas ? ","")                #BLOQUEADO
            ##self.oHelper.SetValue("011: Relatório da Administração ?","")         #BLOQUEADO
            ##self.oHelper.SetValue("012: Parecer dos Auditores ? ","")             #BLOQUEADO
            ##self.oHelper.SetValue("099: Outros ? ","")                            #BLOQUEADO

            ##self.oHelper.SetValue("Termo de Substituição da ECD ?","")            #BLOQUEADO

            #Motivo da Substituição ? 
            #self.oHelper.SetValue("000=Não se aplica",True)                       #BLOQUEADO
            ##self.oHelper.SetValue("001=Mudanças de saldos",True)                  #BLOQUEADO
            ##self.oHelper.SetValue("002=Alteração assinatura",True)                #BLOQUEADO
            ##self.oHelper.SetValue("003=Alteração Dem. contábil",True)             #BLOQUEADO
            ##self.oHelper.SetValue("004=Alteração Forma Escrit. contábil",True)    #BLOQUEADO
            ##self.oHelper.SetValue("005=Alteração do número do livro",True)        #BLOQUEADO
            ##self.oHelper.SetValue("099=Outros",True)  #BLOQUEADO

            self.oHelper.SetButton("Avançar")   #Encerra informações principais 3/3 
            self.oHelper.SetButton("Finalizar")
            
            ##tela de moeda funcional
            self.oHelper.SetValue("Moeda Nacional", "01")
            self.oHelper.SetValue("Codigo Leiaute", "01")
            self.oHelper.SetButton("Confirmar")




            ## colocar setbuton fechar nesse ponto esta aparecendo help intermitente de procedure
            ##Ponto de quebra no portal as vezes aparece o help as vezes não



            self.oHelper.SetButton("Fechar")



            #self.oHelper.WaitProcessing("Aguarde")
            #self.oHelper.WaitProcessing("gravando dados")
            
            #self.oHelper.CheckView("ECD")
            self.oHelper.WaitShow("Tipo de Escrituração")

            self.oHelper.ClickTree("ECD")
            self.oHelper.SetButton("Sair")
            self.oHelper.Program("CTBS001")
            self.oHelper.AssertTrue()

    #   Inclusão Layout 7  -   ECD
    def test_CTBS001_002(self):
        # Layout 7  -   ECD
        # self.oHelper.Program("CTBS001")
        if self.oHelper.GetRelease() > '12.1.025':

            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            self.oHelper.ClickTree("ECD")
            self.oHelper.SetButton("Incluir")
            self.oHelper.SetValue("Leiaute 7", True)  # Disponiveis Leiaute 1 ao 7
            self.oHelper.SetButton("Ok")

            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Avançar")
            #-----------------------------------------------------------------------------
            ##   Informe os dados da empresa escolhida para escrituração  ##
            #-----------------------------------------------------------------------------

            self.oHelper.SetValue("Com Centralização", True)
            #self.oHelper.SetValue("Sem Centralização", True)

            # Situação Especial ?
            self.oHelper.SetValue("Z-Normal", True)
            # self.oHelper.SetValue("0-Abertura",True)
            # self.oHelper.SetValue("1-Cosão",True)
            # self.oHelper.SetValue("2-Fusão",True)
            # self.oHelper.SetValue("3-Incorporação",True)
            # self.oHelper.SetValue("4-Extinção",True)
            # self.oHelper.SetValue("5-Transformação",True)

            # Indicador início de Periodo ?
            self.oHelper.SetValue("0-Inicio no primeiro dia do ano", True)
            # self.oHelper.SetValue("1-Abertura",True)
            #self.oHelper.SetValue("2-Resultante Cisao/Fusao ou remanescente...",True)
            #self.oHelper.SetValue("3-Inicio Obrigatoriedade Entrega ECD",True)

            #Indicador de existência de NIRE ? 
            self.oHelper.SetValue("0-Empresa não possui NIRE",True)
            #self.oHelper.SetValue("1-Empresa possui NIRE",True)

            #Indicador de finalidade da escrituração ?
            self.oHelper.SetValue("0 - Original", True)
            ##self.oHelper.SetValue("1 - Substituta",True)

            # self.oHelper.SetValue("Hash da escrituração de finalidade da escrituração ?","")
            # self.oHelper.SetValue("NIRE da Escrituração Substituida ?","") ##Bloqueado

            # indicador Empr.Grande Porte ?
            self.oHelper.SetValue(
                "0  Empresa não é entidade sujeita a auditoria independente.", True)
            ##self.oHelper.SetValue("1 - Empresa é entidade sujeita a auditoria independente.",True)

            # Tipo da ECD (SCP) ?
            self.oHelper.SetValue(
                "0  ECD de empresa não participante de SCP como sócio ostensivo.", True)
            ##self.oHelper.SetValue("1 - ECD de empresa participante de SCP como sócio ostensivo.",True)
            ##self.oHelper.SetValue("1 - ECD da SCP",True)

            # Plano Contas Referencial ?
            self.oHelper.SetValue("1-PJ em Geral (L100A + L300A da ECF)", True)
            #self.oHelper.SetValue(
            #    "2-PJ em GeralLucro Presumido (P100 + P150 da ECF)", True)
            #self.oHelper.SetValue("3-Financeiras (L100B + L300B da ECF)", True)
            #self.oHelper.SetValue("4-Seguradoras (L100C + L300C da ECF)", True)
            #self.oHelper.SetValue(
            #    "5-Imunes e Isentas em Geral (U100A + U150A da ECF)", True)
            #self.oHelper.SetValue(
            #    "6-Financeiras-Imunes e Isentas (U100B + U150B da ECF)", True)
            #self.oHelper.SetValue(
            #    "7-Seguradoras-Imunes e Isentas (U100C + U150C da ECF)", True)
            #self.oHelper.SetValue(
            #    "8-Entidades Fechadas Prev Complementar (U100D + U150D da ECF)", True)
            #self.oHelper.SetValue(
            #    "9-Partidos Politicos (U100E + U150E da ECF)", True)
            #self.oHelper.SetValue(
            #    "10-Financeiras  Lucro Presumido (P100B + P150B da ECF)", True)

            # Moeda funcional diferente da nacional ?
            #self.oHelper.SetValue("1-Sim", True)
            self.oHelper.SetValue("2-Não", True,position=1)

            # Escrituração Contábeis consolidadas ?
            #self.oHelper.SetValue("1-Sim", True)
            self.oHelper.SetValue("2-Não", True,position=2)

            #self.oHelper.SetValue("Codigo Identif. Bloco K ?","")
            # Encerra dados da empresa para escrituração
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ##  Quais são as filiais que essa empresa centralizadora?   ##
            #-----------------------------------------------------------------------------
            #PASSO 03 FILIAIS
            self.oHelper.ClickBox("Empresa/Unidade/Filial", "M SP 02")
            self.oHelper.SetButton("Avançar")  # Encerra escolha de filiais

            ##  Informe neste passo, quais as incrições de sua empresa. ##
            # Outras Inscrições ?
            self.oHelper.SetValue("00-Não ha",True)
            #self.oHelper.SetValue("01-Bco Cent. do Brasil / BACEN",True)
            #self.oHelper.SetValue("02-Super. de Seg. Privados / SUSEP",True)
            #self.oHelper.SetValue("03-Comis. de Val. Mobiliários / CVM",True)
            #self.oHelper.SetValue("04-Agência Nacional de Transportes Terrestres (ANTT)",True)
            #self.oHelper.SetValue("UF-Secretarias de Estado",True)

            self.oHelper.SetValue("Unidade Federativa ?","SP")
            self.oHelper.SetValue("Inscrição ?","")

            self.oHelper.CheckResult("Unidade Federativa ?","SP")

            #self.oHelper.SetValue("Codigo da SCP ?","")    #BLOQUEADO
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ##  Informe neste passo, quais os dados principais para a escrituração. PASSO 1/3   ##
            #-----------------------------------------------------------------------------
            #Indicação da Escrituracao ? 
            self.oHelper.SetValue("G-Geral",True)
            ##self.oHelper.SetValue("R-Diário Resumido",True)
            ##self.oHelper.SetValue("A-Diário Auxiliar",True)
            ##self.oHelper.SetValue("B-Balancete Diário",True)

            self.oHelper.SetValue("Numero de Ordem do Livro ?","000006")
            self.oHelper.SetValue("Natureza do Livro ?","Livro G")
            self.oHelper.SetButton("Avançar") #Encerra dados principais da escrituração 1/3

            #-----------------------------------------------------------------------------
            ##  Informe neste passo, quais os dados principais para a escrituração. PASSO 2/3   ##
            #-----------------------------------------------------------------------------
            
            self.oHelper.SetValue("Periodo Inicial Lcto ?", "01/01/2018")
            self.oHelper.SetValue("Periodo Final Lcto ?",   "31/12/2018")
            self.oHelper.SetValue("Apuração do Exercicio(L/P) ?","31/12/2018")
            self.oHelper.SetValue("Calendario ?","218")
            self.oHelper.SetValue("Moeda ?","01")
            self.oHelper.SetValue("Tipo Saldo (Societario) ?","1")
            self.oHelper.SetValue("Conta De ?","")
            self.oHelper.SetValue("Conta Ate ?","ZZZZZZZZZZZZZZZZZZZZ")
            self.oHelper.SetValue("Plano Contas Referencial ?","000001") #Branco a nao ser que precise
            self.oHelper.SetValue("Versão ?","0001")                   #Branco a nao ser que precise
            
            #Arquivo Trimestral Unificado ? 
            #self.oHelper.SetValue("1-Sim",True)
            self.oHelper.SetValue("2-Não",True,position=3)
            self.oHelper.SetButton("Avançar")   #Encerra informações principais Passo 2/3
            #-----------------------------------------------------------------------------
            ##   Informe neste passo, quais os dados principais para a escrituração. PASSO 3/3   ##
            #-----------------------------------------------------------------------------
            self.oHelper.SetValue("Periodo Inicial Demons ?","01/01/2018")
            self.oHelper.SetValue("Periodo Final Demons ?","31/12/2018")
            self.oHelper.SetValue("Cod. Conf. Bal. Patrim ?","BP")
            self.oHelper.SetValue("Cod. Conf. DRE ?","DRE")
            
            #self.oHelper.SetValue("Outras Demonstracoes ?","")# BLOQUEADO

            #Processa C.Custo ? ? 
            self.oHelper.SetValue("1-Não",True)
            #self.oHelper.SetValue("2-Sim",True)

            #J210:Indicador do tipo de demostração ? ? 
            ##self.oHelper.SetValue("DLPA",True)
            self.oHelper.SetValue("DMPL",True)

            self.oHelper.SetValue("J210: Cod.Conf.Dem. ?","210")
            #self.oHelper.SetValue("J310: Cod.Conf.DFC ?","")   #BLOQUEADO
            #self.oHelper.SetValue("J410: Cod.Conf.DVA ?","")   #BLOQUEADO

            #J200:Historico Fato Contabil - Cadastrar ?                             #BLOQUEADO
            ##self.oHelper.SetValue("1-Sim",True)                                   #BLOQUEADO
            ##self.oHelper.SetValue("2-Não",True)                                   #BLOQUEADO

            #J215:Detalhar Fato Contabil - Detalhar ? 
            #self.oHelper.SetValue("1-Sim",True)  
            self.oHelper.SetValue("2-Não",True,position=5)      

            ##self.oHelper.SetValue("001: Dem. Abrang. do Período ","")             #BLOQUEADO
            ##self.oHelper.SetValue("002: Dem. Fluxos de Caixa ? ","")              #BLOQUEADO
            ##self.oHelper.SetValue("003: Dem. do Valor Adicionado ?","")           #BLOQUEADO
            ##self.oHelper.SetValue("010: Notas Explicativas ? ","")                #BLOQUEADO
            ##self.oHelper.SetValue("011: Relatório da Administração ?","")         #BLOQUEADO
            ##self.oHelper.SetValue("012: Parecer dos Auditores ? ","")             #BLOQUEADO
            ##self.oHelper.SetValue("099: Outros ? ","")                            #BLOQUEADO

            ##self.oHelper.SetValue("Termo de Substituição da ECD ?","")            #BLOQUEADO

            #Motivo da Substituição ? 
            #self.oHelper.SetValue("000=Não se aplica",True)                       #BLOQUEADO
            ##self.oHelper.SetValue("001=Mudanças de saldos",True)                  #BLOQUEADO
            ##self.oHelper.SetValue("002=Alteração assinatura",True)                #BLOQUEADO
            ##self.oHelper.SetValue("003=Alteração Dem. contábil",True)             #BLOQUEADO
            ##self.oHelper.SetValue("004=Alteração Forma Escrit. contábil",True)    #BLOQUEADO
            ##self.oHelper.SetValue("005=Alteração do número do livro",True)        #BLOQUEADO
            ##self.oHelper.SetValue("099=Outros",True)  #BLOQUEADO
            self.oHelper.SetButton("Avançar")   #Encerra informações principais 3/3 
            self.oHelper.SetButton("Finalizar")

            ##tela de moeda funcional
            # self.oHelper.SetButton("Cancelar")

            # self.oHelper.SetButton("x")

            #self.oHelper.WaitProcessing("Aguarde")
            #self.oHelper.WaitProcessing("gravando dados")
            
            #self.oHelper.CheckView("ECD")
            self.oHelper.ClickTree("ECD")
            # self.oHelper.ClickLabel("Revisão - 000006 - G")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.AssertTrue()

    #   Inclusão Layout 7  -   Diario Presumido
    def test_CTBS001_003(self):
        # Layout 7  -   Diario Presumido
        # self.oHelper.Program("CTBS001")
        if self.oHelper.GetRelease() > '12.1.025':

            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            # self.oHelper.ClickLabel("ECD")
            self.oHelper.ClickTree("ECD")
            self.oHelper.SetButton("Incluir")
            self.oHelper.SetValue("Leiaute 7", True)  # Disponiveis Leiaute 1 ao 7
            self.oHelper.SetButton("Ok")

            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Avançar")
            #-----------------------------------------------------------------------------
            ##   Informe os dados da empresa escolhida para escrituração  ##
            #-----------------------------------------------------------------------------

            self.oHelper.SetValue("Com Centralização", True)
            #self.oHelper.SetValue("Sem Centralização", True)

            # Situação Especial ?
            self.oHelper.SetValue("Z-Normal", True)
            # self.oHelper.SetValue("0-Abertura",True)
            # self.oHelper.SetValue("1-Cosão",True)
            # self.oHelper.SetValue("2-Fusão",True)
            # self.oHelper.SetValue("3-Incorporação",True)
            # self.oHelper.SetValue("4-Extinção",True)
            # self.oHelper.SetValue("5-Transformação",True)

            # Indicador início de Periodo ?
            self.oHelper.SetValue("0-Inicio no primeiro dia do ano", True)
            # self.oHelper.SetValue("1-Abertura",True)
            #self.oHelper.SetValue("2-Resultante Cisao/Fusao ou remanescente...",True)
            #self.oHelper.SetValue("3-Inicio Obrigatoriedade Entrega ECD",True)

            #Indicador de existência de NIRE ? 
            self.oHelper.SetValue("0-Empresa não possui NIRE",True)
            #self.oHelper.SetValue("1-Empresa possui NIRE",True)

            #Indicador de finalidade da escrituração ?
            self.oHelper.SetValue("0 - Original", True)
            ##self.oHelper.SetValue("1 - Substituta",True)

            # self.oHelper.SetValue("Hash da escrituração de finalidade da escrituração ?","")
            # self.oHelper.SetValue("NIRE da Escrituração Substituida ?","") ##Bloqueado

            # indicador Empr.Grande Porte ?
            self.oHelper.SetValue(
                "0  Empresa não é entidade sujeita a auditoria independente.", True)
            ##self.oHelper.SetValue("1 - Empresa é entidade sujeita a auditoria independente.",True)

            # Tipo da ECD (SCP) ?
            self.oHelper.SetValue(
                "0  ECD de empresa não participante de SCP como sócio ostensivo.", True)
            ##self.oHelper.SetValue("1 - ECD de empresa participante de SCP como sócio ostensivo.",True)
            ##self.oHelper.SetValue("1 - ECD da SCP",True)

            # Plano Contas Referencial ?
            self.oHelper.SetValue("1-PJ em Geral (L100A + L300A da ECF)", True)
            #self.oHelper.SetValue(
            #    "2-PJ em GeralLucro Presumido (P100 + P150 da ECF)", True)
            #self.oHelper.SetValue("3-Financeiras (L100B + L300B da ECF)", True)
            #self.oHelper.SetValue("4-Seguradoras (L100C + L300C da ECF)", True)
            #self.oHelper.SetValue(
            #    "5-Imunes e Isentas em Geral (U100A + U150A da ECF)", True)
            #self.oHelper.SetValue(
            #    "6-Financeiras-Imunes e Isentas (U100B + U150B da ECF)", True)
            #self.oHelper.SetValue(
            #    "7-Seguradoras-Imunes e Isentas (U100C + U150C da ECF)", True)
            #self.oHelper.SetValue(
            #    "8-Entidades Fechadas Prev Complementar (U100D + U150D da ECF)", True)
            #self.oHelper.SetValue(
            #    "9-Partidos Politicos (U100E + U150E da ECF)", True)
            #self.oHelper.SetValue(
            #    "10-Financeiras  Lucro Presumido (P100B + P150B da ECF)", True)

            # Moeda funcional diferente da nacional ?
            #self.oHelper.SetValue("1-Sim", True)
            self.oHelper.SetValue("2-Não", True,position=1)

            # Escrituração Contábeis consolidadas ?
            #self.oHelper.SetValue("1-Sim", True)
            self.oHelper.SetValue("2-Não", True,position=2)

            #self.oHelper.SetValue("Codigo Identif. Bloco K ?","")
            # Encerra dados da empresa para escrituração
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ##  Quais são as filiais que essa empresa centralizadora?   ##
            #-----------------------------------------------------------------------------
            #PASSO 03 FILIAIS
            self.oHelper.ClickBox("Empresa/Unidade/Filial", "M SP 02")
            self.oHelper.SetButton("Avançar")  # Encerra escolha de filiais

            ##  Informe neste passo, quais as incrições de sua empresa. ##
            # Outras Inscrições ?
            self.oHelper.SetValue("00-Não ha",True)
            #self.oHelper.SetValue("01-Bco Cent. do Brasil / BACEN",True)
            #self.oHelper.SetValue("02-Super. de Seg. Privados / SUSEP",True)
            #self.oHelper.SetValue("03-Comis. de Val. Mobiliários / CVM",True)
            #self.oHelper.SetValue("04-Agência Nacional de Transportes Terrestres (ANTT)",True)
            #self.oHelper.SetValue("UF-Secretarias de Estado",True)

            self.oHelper.SetValue("Unidade Federativa ?","SP")
            self.oHelper.SetValue("Inscrição ?","")

            #self.oHelper.SetValue("Codigo da SCP ?","")    #BLOQUEADO
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ##  Informe neste passo, quais os dados principais para a escrituração. PASSO 1/3   ##
            #-----------------------------------------------------------------------------
            #Indicação da Escrituracao ? 
            #self.oHelper.SetValue("G-Geral",True)
            self.oHelper.SetValue("R-Diário Resumido",True)
            ##self.oHelper.SetValue("A-Diário Auxiliar",True)
            ##self.oHelper.SetValue("B-Balancete Diário",True)

            self.oHelper.SetValue("Numero de Ordem do Livro ?","000007")
            self.oHelper.SetValue("Natureza do Livro ?","Livro R")
            self.oHelper.SetButton("Avançar") #Encerra dados principais da escrituração 1/3

            #-----------------------------------------------------------------------------
            ##  Informe neste passo, quais os dados principais para a escrituração. PASSO 2/3   ##
            #-----------------------------------------------------------------------------
            
            self.oHelper.SetValue("Periodo Inicial Lcto ?", "01/01/2018")
            self.oHelper.SetValue("Periodo Final Lcto ?",   "31/12/2018")
            self.oHelper.SetValue("Apuração do Exercicio(L/P) ?","31/12/2018")
            self.oHelper.SetValue("Calendario ?","218")
            self.oHelper.SetValue("Moeda ?","01")
            self.oHelper.SetValue("Tipo Saldo (Societario) ?","1")
            self.oHelper.SetValue("Conta De ?","")
            self.oHelper.SetValue("Conta Ate ?","ZZZZZZZZZZZZZZZZZZZZ")
            self.oHelper.SetValue("Plano Contas Referencial ?","000001") #Branco a nao ser que precise
            self.oHelper.SetValue("Versão ?","0001")                   #Branco a nao ser que precise

            #Arquivo Trimestral Unificado ? 
            #self.oHelper.SetValue("1-Sim",True)
            self.oHelper.SetValue("2-Não",True,position=3)
            self.oHelper.SetButton("Avançar")   #Encerra informações principais Passo 2/3
            #-----------------------------------------------------------------------------
            ##   Informe neste passo, quais os dados principais para a escrituração. PASSO 3/3   ##
            #-----------------------------------------------------------------------------
            self.oHelper.SetValue("Periodo Inicial Demons ?","01/01/2018")
            self.oHelper.SetValue("Periodo Final Demons ?","31/12/2018")
            self.oHelper.SetValue("Cod. Conf. Bal. Patrim ?","BP")
            self.oHelper.SetValue("Cod. Conf. DRE ?","DRE")

            #self.oHelper.SetValue("Outras Demonstracoes ?","")# BLOQUEADO

            #Processa C.Custo ? ? 
            self.oHelper.SetValue("1-Não",True)
            #self.oHelper.SetValue("2-Sim",True)

            #J210:Indicador do tipo de demostração ? ? 
            ##self.oHelper.SetValue("DLPA",True)
            self.oHelper.SetValue("DMPL",True)

            self.oHelper.SetValue("J210: Cod.Conf.Dem. ?","210")
            #self.oHelper.SetValue("J310: Cod.Conf.DFC ?","")   #BLOQUEADO
            #self.oHelper.SetValue("J410: Cod.Conf.DVA ?","")   #BLOQUEADO

            #J200:Historico Fato Contabil - Cadastrar ?                             #BLOQUEADO
            ##self.oHelper.SetValue("1-Sim",True)                                   #BLOQUEADO
            ##self.oHelper.SetValue("2-Não",True)                                   #BLOQUEADO

            #J215:Detalhar Fato Contabil - Detalhar ? 
            self.oHelper.SetValue("1-Sim",True,position=5)  
            #self.oHelper.SetValue("2-Não",True)      

            ##self.oHelper.SetValue("001: Dem. Abrang. do Período ","")             #BLOQUEADO
            ##self.oHelper.SetValue("002: Dem. Fluxos de Caixa ? ","")              #BLOQUEADO
            ##self.oHelper.SetValue("003: Dem. do Valor Adicionado ?","")           #BLOQUEADO
            ##self.oHelper.SetValue("010: Notas Explicativas ? ","")                #BLOQUEADO
            ##self.oHelper.SetValue("011: Relatório da Administração ?","")         #BLOQUEADO
            ##self.oHelper.SetValue("012: Parecer dos Auditores ? ","")             #BLOQUEADO
            ##self.oHelper.SetValue("099: Outros ? ","")                            #BLOQUEADO

            ##self.oHelper.SetValue("Termo de Substituição da ECD ?","")            #BLOQUEADO

            #Motivo da Substituição ? 
            #self.oHelper.SetValue("000=Não se aplica",True)                       #BLOQUEADO
            ##self.oHelper.SetValue("001=Mudanças de saldos",True)                  #BLOQUEADO
            ##self.oHelper.SetValue("002=Alteração assinatura",True)                #BLOQUEADO
            ##self.oHelper.SetValue("003=Alteração Dem. contábil",True)             #BLOQUEADO
            ##self.oHelper.SetValue("004=Alteração Forma Escrit. contábil",True)    #BLOQUEADO
            ##self.oHelper.SetValue("005=Alteração do número do livro",True)        #BLOQUEADO
            ##self.oHelper.SetValue("099=Outros",True)  #BLOQUEADO

            self.oHelper.SetButton("Avançar")   #Encerra informações principais 3/3 
            self.oHelper.SetButton("Finalizar")
            
            ##tela de moeda funcional
            self.oHelper.SetButton("Cancelar")
            
            #-----------------------------------------------------------------------------
            ##   Tela detalhe Contabil - Cadastro   ##
            #-----------------------------------------------------------------------------
            self.oHelper.SetButton("Incluir")

            self.oHelper.SetValue("Cod. Aglut.","21002")
            self.oHelper.SetValue("Cod.Fato Ctb","01")
            self.oHelper.SetValue("Desc.Fato","FATO 01")
            self.oHelper.SetValue("Valor","10,00")
            self.oHelper.SetValue("Ind Valor","D - Devedor")

            self.oHelper.SetButton("Salvar")
            self.oHelper.SetButton("Cancelar")
            self.oHelper.SetButton("x")

            # self.oHelper.SetButton("Fechar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            #self.oHelper.WaitProcessing("Aguarde")
            #self.oHelper.WaitProcessing("gravando dados")
            
            #self.oHelper.CheckView("ECD")
            self.oHelper.ClickTree("ECD")
            # self.oHelper.ClickLabel("Revisão - 000007 - R")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.AssertTrue()

    #   Inclusão ECD GERAL COM DRE e BP
    def test_CTBS001_004(self):
        #ECD GERAL COM DRE e BP
        # self.oHelper.Program("CTBS001")
        if self.oHelper.GetRelease() > '12.1.025':
        
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            # self.oHelper.ClickLabel("ECD")
            self.oHelper.ClickTree("ECD")
            self.oHelper.SetButton("Incluir")
            self.oHelper.SetValue("Leiaute 7", True)  # Disponiveis Leiaute 1 ao 7
            self.oHelper.SetButton("Ok")

            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Avançar")
            #-----------------------------------------------------------------------------
            ##   Informe os dados da empresa escolhida para escrituração  ##
            #-----------------------------------------------------------------------------

            self.oHelper.SetValue("Com Centralização", True)
            #self.oHelper.SetValue("Sem Centralização", True)

            # Situação Especial ?
            self.oHelper.SetValue("Z-Normal", True)
            # self.oHelper.SetValue("0-Abertura",True)
            # self.oHelper.SetValue("1-Cosão",True)
            # self.oHelper.SetValue("2-Fusão",True)
            # self.oHelper.SetValue("3-Incorporação",True)
            # self.oHelper.SetValue("4-Extinção",True)
            # self.oHelper.SetValue("5-Transformação",True)

            # Indicador início de Periodo ?
            self.oHelper.SetValue("0-Inicio no primeiro dia do ano", True)
            # self.oHelper.SetValue("1-Abertura",True)
            #self.oHelper.SetValue("2-Resultante Cisao/Fusao ou remanescente...",True)
            #self.oHelper.SetValue("3-Inicio Obrigatoriedade Entrega ECD",True)

            #Indicador de existência de NIRE ? 
            self.oHelper.SetValue("0-Empresa não possui NIRE",True)
            #self.oHelper.SetValue("1-Empresa possui NIRE",True)

            #Indicador de finalidade da escrituração ?
            self.oHelper.SetValue("0 - Original", True)
            ##self.oHelper.SetValue("1 - Substituta",True)

            # self.oHelper.SetValue("Hash da escrituração de finalidade da escrituração ?","")
            # self.oHelper.SetValue("NIRE da Escrituração Substituida ?","") ##Bloqueado

            # indicador Empr.Grande Porte ?
            self.oHelper.SetValue(
                "0  Empresa não é entidade sujeita a auditoria independente.", True)
            ##self.oHelper.SetValue("1 - Empresa é entidade sujeita a auditoria independente.",True)

            # Tipo da ECD (SCP) ?
            self.oHelper.SetValue(
                "0  ECD de empresa não participante de SCP como sócio ostensivo.", True)
            ##self.oHelper.SetValue("1 - ECD de empresa participante de SCP como sócio ostensivo.",True)
            ##self.oHelper.SetValue("1 - ECD da SCP",True)

            # Plano Contas Referencial ?
            self.oHelper.SetValue("1-PJ em Geral (L100A + L300A da ECF)", True)
            #self.oHelper.SetValue(
            #    "2-PJ em GeralLucro Presumido (P100 + P150 da ECF)", True)
            #self.oHelper.SetValue("3-Financeiras (L100B + L300B da ECF)", True)
            #self.oHelper.SetValue("4-Seguradoras (L100C + L300C da ECF)", True)
            #self.oHelper.SetValue(
            #    "5-Imunes e Isentas em Geral (U100A + U150A da ECF)", True)
            #self.oHelper.SetValue(
            #    "6-Financeiras-Imunes e Isentas (U100B + U150B da ECF)", True)
            #self.oHelper.SetValue(
            #    "7-Seguradoras-Imunes e Isentas (U100C + U150C da ECF)", True)
            #self.oHelper.SetValue(
            #    "8-Entidades Fechadas Prev Complementar (U100D + U150D da ECF)", True)
            #self.oHelper.SetValue(
            #    "9-Partidos Politicos (U100E + U150E da ECF)", True)
            #self.oHelper.SetValue(
            #    "10-Financeiras  Lucro Presumido (P100B + P150B da ECF)", True)

            # Moeda funcional diferente da nacional ?
            self.oHelper.SetValue("1-Sim", True,position=1)
            #self.oHelper.SetValue("2-Não", True)

            # Escrituração Contábeis consolidadas ?
            #self.oHelper.SetValue("1-Sim", True)
            self.oHelper.SetValue("2-Não", True,position=2)

            #self.oHelper.SetValue("Codigo Identif. Bloco K ?","")
            # Encerra dados da empresa para escrituração
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ##  Quais são as filiais que essa empresa centralizadora?   ##
            #-----------------------------------------------------------------------------
            #PASSO 03 FILIAIS
            self.oHelper.ClickBox("Empresa/Unidade/Filial", "M SP 02")
            self.oHelper.SetButton("Avançar")  # Encerra escolha de filiais


            ##  Informe neste passo, quais as incrições de sua empresa. ##
            # Outras Inscrições ?
            self.oHelper.SetValue("00-Não ha",True)
            #self.oHelper.SetValue("01-Bco Cent. do Brasil / BACEN",True)
            #self.oHelper.SetValue("02-Super. de Seg. Privados / SUSEP",True)
            #self.oHelper.SetValue("03-Comis. de Val. Mobiliários / CVM",True)
            #self.oHelper.SetValue("04-Agência Nacional de Transportes Terrestres (ANTT)",True)
            #self.oHelper.SetValue("UF-Secretarias de Estado",True)

            self.oHelper.SetValue("Unidade Federativa ?","SP")
            self.oHelper.SetValue("Inscrição ?","")

            #self.oHelper.SetValue("Codigo da SCP ?","")    #BLOQUEADO
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ##  Informe neste passo, quais os dados principais para a escrituração. PASSO 1/3   ##
            #-----------------------------------------------------------------------------
            #Indicação da Escrituracao ? 
            self.oHelper.SetValue("G-Geral",True)
            ##self.oHelper.SetValue("R-Diário Resumido",True)
            ##self.oHelper.SetValue("A-Diário Auxiliar",True)
            ##self.oHelper.SetValue("B-Balancete Diário",True)

            self.oHelper.SetValue("Numero de Ordem do Livro ?","000003")
            self.oHelper.SetValue("Natureza do Livro ?","Livro G")
            self.oHelper.SetButton("Avançar") #Encerra dados principais da escrituração 1/3

            #-----------------------------------------------------------------------------
            ##  Informe neste passo, quais os dados principais para a escrituração. PASSO 2/3   ##
            #-----------------------------------------------------------------------------
            
            self.oHelper.SetValue("Periodo Inicial Lcto ?", "01/01/2018")
            self.oHelper.SetValue("Periodo Final Lcto ?",   "31/12/2018")
            self.oHelper.SetValue("Apuração do Exercicio(L/P) ?","31/12/2018")
            self.oHelper.SetValue("Calendario ?","218")
            self.oHelper.SetValue("Moeda ?","01")
            self.oHelper.SetValue("Tipo Saldo (Societario) ?","1")
            self.oHelper.SetValue("Conta De ?","")
            self.oHelper.SetValue("Conta Ate ?","ZZZZZZZZZZZZZZZZZZZZ")
            self.oHelper.SetValue("Plano Contas Referencial ?","000001") #Branco a nao ser que precise
            self.oHelper.SetValue("Versão ?","0001")                    #Branco a nao ser que precise

            #Arquivo Trimestral Unificado ? 
            #self.oHelper.SetValue("1-Sim",True)
            self.oHelper.SetValue("2-Não",True,position=3)
            self.oHelper.SetButton("Avançar")   #Encerra informações principais Passo 2/3
            #-----------------------------------------------------------------------------
            ##   Informe neste passo, quais os dados principais para a escrituração. PASSO 3/3   ##
            #-----------------------------------------------------------------------------
            self.oHelper.SetValue("Periodo Inicial Demons ?","01/01/2018")
            self.oHelper.SetValue("Periodo Final Demons ?","31/12/2018")
            self.oHelper.SetValue("Cod. Conf. Bal. Patrim ?","BP")
            self.oHelper.SetValue("Cod. Conf. DRE ?","DRE")

            #self.oHelper.SetValue("Outras Demonstracoes ?","")# BLOQUEADO

            #Processa C.Custo ? ? 
            self.oHelper.SetValue("1-Não",True)
            #self.oHelper.SetValue("2-Sim",True)

            #J210:Indicador do tipo de demostração ? ? 
            ##self.oHelper.SetValue("DLPA",True)
            self.oHelper.SetValue("DMPL",True)

            self.oHelper.SetValue("J210: Cod.Conf.Dem. ?","210")
            #self.oHelper.SetValue("J310: Cod.Conf.DFC ?","")   #BLOQUEADO
            #self.oHelper.SetValue("J410: Cod.Conf.DVA ?","")   #BLOQUEADO

            #J200:Historico Fato Contabil - Cadastrar ?                             #BLOQUEADO
            ##self.oHelper.SetValue("1-Sim",True)                                   #BLOQUEADO
            ##self.oHelper.SetValue("2-Não",True)                                   #BLOQUEADO

            #J215:Detalhar Fato Contabil - Detalhar ? 
            self.oHelper.SetValue("1-Sim",True,position=5)  
            #self.oHelper.SetValue("2-Não",True)      

            ##self.oHelper.SetValue("001: Dem. Abrang. do Período ","")             #BLOQUEADO
            ##self.oHelper.SetValue("002: Dem. Fluxos de Caixa ? ","")              #BLOQUEADO
            ##self.oHelper.SetValue("003: Dem. do Valor Adicionado ?","")           #BLOQUEADO
            ##self.oHelper.SetValue("010: Notas Explicativas ? ","")                #BLOQUEADO
            ##self.oHelper.SetValue("011: Relatório da Administração ?","")         #BLOQUEADO
            ##self.oHelper.SetValue("012: Parecer dos Auditores ? ","")             #BLOQUEADO
            ##self.oHelper.SetValue("099: Outros ? ","")                            #BLOQUEADO

            ##self.oHelper.SetValue("Termo de Substituição da ECD ?","")            #BLOQUEADO

            #Motivo da Substituição ? 
            #self.oHelper.SetValue("000=Não se aplica",True)                       #BLOQUEADO
            ##self.oHelper.SetValue("001=Mudanças de saldos",True)                  #BLOQUEADO
            ##self.oHelper.SetValue("002=Alteração assinatura",True)                #BLOQUEADO
            ##self.oHelper.SetValue("003=Alteração Dem. contábil",True)             #BLOQUEADO
            ##self.oHelper.SetValue("004=Alteração Forma Escrit. contábil",True)    #BLOQUEADO
            ##self.oHelper.SetValue("005=Alteração do número do livro",True)        #BLOQUEADO
            ##self.oHelper.SetValue("099=Outros",True)  #BLOQUEADO
            self.oHelper.SetButton("Avançar")   #Encerra informações principais 3/3 
            self.oHelper.SetButton("Finalizar")
            
            ##tela de moeda funcional
            self.oHelper.SetButton("Cancelar")
            self.oHelper.SetButton("Fechar")
            #-----------------------------------------------------------------------------
            ## Detalhe Fato Contabil      ##
            #-----------------------------------------------------------------------------
            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Finalizar")

            #-----------------------------------------------------------------------------
            ##   Tela detalhe Contabil - Cadastro   ##
            #-----------------------------------------------------------------------------
            self.oHelper.SetButton("Incluir")

            self.oHelper.SetValue("Cod. Aglut.","21002")
            self.oHelper.SetValue("Cod.Fato Ctb","01")
            self.oHelper.SetValue("Desc.Fato","FATO 01")
            self.oHelper.SetValue("Valor","10,00")
            self.oHelper.SetValue("Ind Valor","D - Devedor")

            self.oHelper.SetButton("Salvar")
            self.oHelper.SetButton("Cancelar")
            self.oHelper.SetButton("x")
            
            #self.oHelper.CheckView("ECD")
            self.oHelper.ClickTree("ECD")
            #self.oHelper.ClickLabel("Revisão - 000008 - G")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.AssertTrue()
    
       # Dados CS0 REVISÃO
    def test_CTBS001_005(self):
        #ECD VERIFICANDO tabela visualizando CS0
        # self.oHelper.Program("CTBS001")
        if self.oHelper.GetRelease() > '12.1.025':
        
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            self.oHelper.ClickTree("ECD")
            self.oHelper.ClickLabel("Revisão - 000001 - G")

            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Buscar")

            self.oHelper.ClickGridCell("Tabelas de Consulta")
            self.oHelper.SetButton("Ok")
            self.oHelper.SetButton("Visualizar")
            self.oHelper.WaitShow("Consulta dados ECD - Revisão")
                    
            self.oHelper.CheckResult("CS0_CODREV","000001",name_attr=True)
            self.oHelper.CheckResult("CS0_CODEMP","T1",name_attr=True)
            self.oHelper.CheckResult("CS0_CODFIL","M SP 02",name_attr=True)
            self.oHelper.CheckResult("CS0_NUMLIV","000001",name_attr=True)
            self.oHelper.CheckResult("CS0_TPESC","1 - Com Centralização",name_attr=True)
            self.oHelper.CheckResult("CS0_UPDATE","01/01/2018",name_attr=True)
            self.oHelper.CheckResult("CS0_DTINI","01/01/2018",name_attr=True)
            self.oHelper.CheckResult("CS0_DTFIM","31/12/2018",name_attr=True)
            self.oHelper.CheckResult("CS0_NATLIV","LIVRO G",name_attr=True)
            self.oHelper.CheckResult("CS0_TIPLIV","G - Geral",name_attr=True)
            self.oHelper.CheckResult("CS0_ECDREV","ECD - SPED",name_attr=True)
            self.oHelper.CheckResult("CS0_SITPER","0 - Inicio do Ano",name_attr=True)
            self.oHelper.CheckResult("CS0_LEIAUT","7.00",name_attr=True)
            self.oHelper.CheckResult("CS0_INNIRE","0 - Empresa sem NIRE",name_attr=True)
            self.oHelper.CheckResult("CS0_FINESC","0 - Origin",name_attr=True)

            self.oHelper.CheckResult("CS0_HASHSB","")
            self.oHelper.CheckResult("CS0_NIRESB","")

            self.oHelper.CheckResult("CS0_DATALP","31/12/2018")
            self.oHelper.CheckResult("CS0_GDEPOR","0 - Nao sujeita a auditoria")
            self.oHelper.CheckResult("CS0_TIPECD","0 - ECD de nao participante de SCP")#Verificar opção selecionada
            self.oHelper.CheckResult("CS0_PLAREF","1")#numerico
            self.oHelper.CheckResult("CS0_CODPLA","000001")#codigo
            self.oHelper.CheckResult("CS0_VERPLA","")
            self.oHelper.CheckResult("CS0_MOEFUN","")
            self.oHelper.CheckResult("CS0_CONGEC","N")
            self.oHelper.CheckResult("CS0_IDBLK","")
            self.oHelper.CheckResult("CS0_CALEND","218")

            self.oHelper.SetButton("Confirmar")
            self.oHelper.SetButton("Sair")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.AssertTrue()

    #Inclusão Livro Z
    def test_CTBS001_006(self):
        #Inclusão (IMPORTA RAZAO ECD - Livro Z)
        # self.oHelper.Program("CTBS001")
        if self.oHelper.GetRelease() > '12.1.025':

            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            self.oHelper.ClickTree("ECD")
            self.oHelper.SetButton("Imp. Razao")
            self.oHelper.SetValue("Leiaute 7",True)
            self.oHelper.SetButton("Ok")
            self.oHelper.SetButton("Avançar")
            self.oHelper.ClickBox("Filial","M SP 02")
            self.oHelper.SetButton("Avançar")   


            #self.oHelper.SetButton("Procurar")
            #self.oHelper.SetFilePath(r"C:\ProtheusT\BC25\totvs\protheus\protheus_data\UnitTest\LIVROZ.txt")                                                                 
            self.oHelper.SetValue("Qual arquivo ?","BASELINE\\LIVROZ.txt")                                                                 
            self.oHelper.SetValue("Periodo Inicial Lcto ?","01/01/2018")
            self.oHelper.SetValue("Periodo Final Lcto ?","31/12/2018")
            self.oHelper.SetValue("Layout ?","01")
            self.oHelper.SetValue("Numero de Ordem do Livro ?","00008") 
            self.oHelper.SetValue("Natureza do Livro ?","LIVRO Z")

            #Indicador Inicio de Periodo ? 
            self.oHelper.SetValue("0-Inicio no primeiro dia do ano",True)
            #self.oHelper.SetValue("1-Abertura",True)
            #self.oHelper.SetValue("2-Resultante Cisao/Fusao ou remanescente...",True)
            #self.oHelper.SetValue("3-Inicio Obrigatoriedade Entrega",True)


            #Indicador de existência de NIRE ? 
            self.oHelper.SetValue("0-Empresa não possui NIRE",True)
            #self.oHelper.SetValue("1-Empresa possui NIRE",True)
            
            #Indicador de finalidade da escrituração ? 
            self.oHelper.SetValue("0 - Original",True)
            #self.oHelper.SetValue("1 - Substituta",True)

            #self.oHelper.SetValue("Hash da Escrituração Substituida ?",True)
            #self.oHelper.SetValue("NIRE da Escrituração Substituida ?",True)
            
            #Indicador Empr.Grande Porte ? 
            self.oHelper.SetValue("0  Empresa não é entidade sujeita a auditoria independente.",True)
            #self.oHelper.SetValue("1  Empresa é entidade sujeita a auditoria independente.",True)
            
            #Tipo da ECD (SCP) ? 
            self.oHelper.SetValue("0  ECD de empresa não participante de SCP como sócio ostensivo.",True)
            #self.oHelper.SetValue("1  ECD de empresa participante de SCP como sócio ostensivo.",True)
            #self.oHelper.SetValue("2  ECD da SCP.",True)
            
            #Plano Contas Referencial ? 
            self.oHelper.SetValue("1-PJ em Geral (L100A + L300A da ECF)",True)
            #self.oHelper.SetValue("2-PJ em GeralLucro Presumido (P100 + P150 da ECF)",True)
            #self.oHelper.SetValue("3-Financeiras (L100B + L300B da ECF)",True)
            #self.oHelper.SetValue("4-Seguradoras (L100C + L300C da ECF)",True)
            #self.oHelper.SetValue("5-Imunes e Isentas em Geral (U100A + U150A da ECF)",True)
            #self.oHelper.SetValue("6-Financeiras-Imunes e Isentas (U100B + U150B da ECF)",True)
            #self.oHelper.SetValue("7-Seguradoras-Imunes e Isentas (U100C + U150C da ECF)",True)
            #self.oHelper.SetValue("8-Entidades Fechadas de Previdencia Complementar (U100D + U150D da ECF)",True)
            #self.oHelper.SetValue("9-Partidos Politicos (U100E + U150E da ECF)",True)
            #self.oHelper.SetValue("10-Financeiras  Lucro Presumido (P100B + P150B da ECF)",True)
            
            self.oHelper.SetValue("Plan. Conta Ref. ?","000001")

            #Moeda funcional diferente da nacional? ? 
            #self.oHelper.SetValue("Sim",True)
            self.oHelper.SetValue("Não",True)
            
            self.oHelper.SetValue("Data de Apuração ?","31/12/2018")

            ##self.oHelper.SetValue("Termo de Substituição da ECD ?",True)    #BLOQUEADO
            ##self.oHelper.SetValue("Termo de Substituição da ECD ?",True)    #BLOQUEADO
            
            #self.oHelper.SetValue("Termo de Substituição da ECD ?","")
            
            #Motivo de Substituição ? 
            self.oHelper.SetValue("000=Não se aplica",True)
            #self.oHelper.SetValue("001=Mudanças de saldos",True)
            #self.oHelper.SetValue("002=Alteração assinatura",True)
            #self.oHelper.SetValue("003=Alteração Dem. contábil",True)
            #self.oHelper.SetValue("004=Alteração Forma Escrit. contábil",True)
            #self.oHelper.SetValue("005=Alteração do número do livro",True)
            #self.oHelper.SetValue("099=Outros",True)
            
            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Finalizar")

            self.oHelper.WaitShow("Importação finalizada.")
            self.oHelper.CheckView("Importação finalizada.")
            self.oHelper.SetButton("Fechar")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.AssertTrue()

    #Seleciona conta Livro Z
    def test_CTBS001_007(self):
        #SELECIONA CONTA LIVRO Z
        # self.oHelper.Program("CTBS001")
        if self.oHelper.GetRelease() > '12.1.025':

            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            self.oHelper.ClickTree("ECD")
            self.oHelper.ClickLabel("Revisão - 000002 - Z")
            ##Selecionando uma conta ao livro incluido Z
            self.oHelper.SetButton("Sel. Conta")
            self.oHelper.SetButton("Avançar")

            self.oHelper.LoadGrid()
            self.oHelper.SetValue("Código"," 1110210",grid=True)
            self.oHelper.SetValue("Descrição","CONTA NOVA",grid=True)
            self.oHelper.LoadGrid()
            self.oHelper.CheckResult("Código"," 1110210 ",grid=True)
            self.oHelper.CheckResult("Descrição","CONTA NOVA",grid=True)
            self.oHelper.LoadGrid()

            self.oHelper.SetButton("Finalizar")
            # self.oHelper.CheckView("ECD")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.AssertTrue()

    #Notas Explicativas BP(Balanço Patrimonial)
    def test_CTBS001_008(self):
        ## Nota explicativa BALANÇO PATRIMONIAL(BP) ECD L7

        # self.oHelper.Program("CTBS001")
        #self.oHelper.CheckView("ECD")
        if self.oHelper.GetRelease() > '12.1.025':
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            self.oHelper.ClickTree("ECD")
            self.oHelper.ClickLabel("Revisão - 000005 - G")
            
            self.oHelper.SetButton("Notas Explicativas")
            self.oHelper.SetValue("J100 - Balanço Patrimonial",True)
            self.oHelper.SetButton("Ok")
            #self.oHelper.SetValue("J150 - Demonstração dos Resultados",True)
            #self.oHelper.SetValue("J210 - DLPA/DMPL",True)
            
            self.oHelper.WaitShow("Cadastro Notas Explicativas")
            chave = "000005BP                            BP 00000000000000002318       "
            #self.oHelper.SearchBrowse(f"{chave}", "Cod. Revisão + Cod. Visao + Cod. Aglut.")
            self.oHelper.SearchBrowse(chave)

            self.oHelper.SetButton("Alterar")
            self.oHelper.SetValue("Nota Explic.","BP11")
            self.oHelper.CheckResult("Nota Explic.","BP11")

            self.oHelper.SetButton("Confirmar")
            self.oHelper.SetButton("Fechar")
            self.oHelper.SetButton("x")
            self.oHelper.SetButton("Cancelar")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.AssertTrue()

    #Outras Informações
    def test_CTBS001_009(self):
        ##Outras Informações
        if self.oHelper.GetRelease() > '12.1.025':
            # self.oHelper.Program("CTBS001")
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")
        
            self.oHelper.ClickTree("ECD")
            self.oHelper.ClickLabel("Revisão - 000003 - G")

            self.oHelper.SetButton("Outras informações")
            self.oHelper.WaitShow("Cadastro de Outras Informações")
            self.oHelper.SetButton("Incluir")

            self.oHelper.CheckResult("Cod. Registr","J800 - Outras Informações")
            
            self.oHelper.SetValue("Tip. Doc.","099 - Outros")
            self.oHelper.SetValue("Nome Demonst","ECD INFO")
            self.oHelper.SetValue("Arq. RTF","BASELINE\\NOTAS EXPLICATIVAS_J800 - 010.RTF")
            self.oHelper.SetValue("Período","")

            self.oHelper.CheckResult("Tip. Doc.","099 - Outros")
            self.oHelper.CheckResult("Nome Demonst","ECD INFO")
            self.oHelper.CheckResult("Arq. RTF","BASELINE\\NOTAS EXPLICATIVAS_J800 - 010.RTF")
            self.oHelper.CheckResult("Período","")

            self.oHelper.SetButton("Confirmar")
            self.oHelper.SetButton("Fechar")
            self.oHelper.SetButton("X")
            self.oHelper.ClickLabel("Revisão - 000003 - G")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.AssertTrue()
    
    #Notas Explicativas DRE(Demostrativo dos resultados)
    def test_CTBS001_010(self):
        ## Nota explicativa Demostrativo dos resultados(DRE) ECD L7
        # self.oHelper.Program("CTBS001")
        if self.oHelper.GetRelease() > '12.1.025':
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            self.oHelper.ClickTree("ECD")
            self.oHelper.ClickLabel("Revisão - 000005 - G")
            
            self.oHelper.SetButton("Notas Explicativas")
            #self.oHelper.SetValue("J100 - Balanço Patrimonial",True)
            self.oHelper.SetValue("J150 - Demonstração dos Resultados",True)
            #self.oHelper.SetValue("J210 - DLPA/DMPL",True)
            self.oHelper.SetButton("Ok")

            self.oHelper.WaitShow("Cadastro Notas Explicativas")
            chave = "000005DRE                           DRE00000000000000002318       "
            #self.oHelper.SearchBrowse(f"{chave}", "Cod. Revisão + Cod. Visao + Cod. Aglut.")
            self.oHelper.SearchBrowse(chave)

            self.oHelper.SetButton("Alterar")
            self.oHelper.SetValue("Nota Explic.","DRE11")
            self.oHelper.CheckResult("Nota Explic.","DRE11")

            self.oHelper.SetButton("Confirmar")
            self.oHelper.SetButton("Fechar")
            self.oHelper.SetButton("x")
            self.oHelper.SetButton("Cancelar")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.AssertTrue()     

    #Cod Hash 
    def test_CTBS001_011(self):
        #Cod hash 
        if self.oHelper.GetRelease() > '12.1.025':
            # self.oHelper.Program("CTBS001")
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            self.oHelper.ClickTree("ECD")
            self.oHelper.ClickLabel("Revisão - 000004 - R") #Coloque seu registro aqui

            self.oHelper.SetButton("Cod HASH")
            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Avançar")
            
            self.oHelper.LoadGrid()
            self.oHelper.SetValue("Num do Livro","000002",grid=True)
            self.oHelper.SetValue("Nat. do Livr","Livro R",grid=True)
            self.oHelper.SetValue("Cod. Hash","B123456789",grid=True)
            self.oHelper.LoadGrid()

            self.oHelper.CheckResult("Num do Livro","000002",grid=True)
            self.oHelper.CheckResult("Nat. do Livr","Livro R",grid=True)
            self.oHelper.CheckResult("Cod. Hash","B123456789",grid=True)
            self.oHelper.LoadGrid()

            self.oHelper.SetButton("Finalizar")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.AssertTrue()


    #-----------------------------------------------------------------------------
    #ECD - ESCRITURAÇÃO CONTABIL DIGITAL
    #-----------------------------------------------------------------------------
    #ECF LUCRO REAL
    def test_CTBS001_012(self):
       # Layout 5 ECF Lucro Real
        # self.oHelper.Program("CTBS001")
        if self.oHelper.GetRelease() > '12.1.025':
            
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            self.oHelper.ClickTree("ECF")
            # self.oHelper.ClickLabel("ECF")
            self.oHelper.SetButton("Incluir")
            self.oHelper.SetButton("Avançar")

            # Tipo da Escrituração
            #self.oHelper.SetValue("Com Centralização", True)
            self.oHelper.SetValue("Sem Centralização", True)

            #Qual o Tipo de Escriturtação ? BLOQUEADO padrão
            #self.oHelper.SetValue("",True)# ECD , FCONT ou ECF 
            
            #-----------------------------------------------------------------------------
            #PASSO 02   -   Tipo da escrituração
            #-----------------------------------------------------------------------------
            #Informe o leiaute da ECF
            self.oHelper.SetValue("Leiaute 5", True)
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            #PASSO 03   -   Filiais 
            #-----------------------------------------------------------------------------
            self.oHelper.ClickBox("Filial", "M SP 02")
            self.oHelper.SetValue("Matriz", "")    #Filial Matriz
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            #PASSO 04   -   Dados da empresa para escrituração
            #-----------------------------------------------------------------------------
            #Indicador Inicio de Periodo ? 
            self.oHelper.SetValue("0 - Regular",True)
            #self.oHelper.SetValue("1 - Abertura",True)
            #self.oHelper.SetValue("2 - Resultante Cisao/Fusao ou remanescente...",True)
            #self.oHelper.SetValue("3 - Resultante de Transformação",True)
            #self.oHelper.SetValue("4 - Início de obrigatoriedade da entrega no curso do ano calendário",True)

            #Indicador de Situação Especial ? 
            self.oHelper.SetValue("0 - Normal",True)
            #self.oHelper.SetValue("1 - Extinção",True)
            #self.oHelper.SetValue("2 - Fusão",True)
            #self.oHelper.SetValue("3 - Incorporada",True)
            #self.oHelper.SetValue("4 - Incorporadora",True)
            #self.oHelper.SetValue("5 - Cisão Total",True)
            #self.oHelper.SetValue("6 - Cisão Parcial",True)
            #self.oHelper.SetValue("7 - Transformação - OBSOLETO",True)
            #self.oHelper.SetValue("8 - Isenta",True)
            #self.oHelper.SetValue("9 - Inclusão Simples Nacional",True)

            #Patr. Remanescente de Cisão(%) ? *
            self.oHelper.SetValue("Patr. Remanescente de Cisão(%) ?","00000")

            #Retificadora ? 
            #self.oHelper.SetValue("S - ECF Retificadora",True)
            self.oHelper.SetValue("N - ECF Original",True)
            #self.oHelper.SetValue("F - ECF Original com mudança de forma de tributação",True)

            #Número do Recibo Anterior ?
            #self.oHelper.SetValue("Número do Recibo Anterior ?","")

            #Tipo da ECF ? 
            self.oHelper.SetValue("0 - ECF de empresa não participante como sócio Ostensivo",True)
            #self.oHelper.SetValue("1 - ECF de empresa participante como sócio Ostensivo",True)
            #self.oHelper.SetValue("2 - ECF da SCP",True)

            #Identificação da SCP ?
            self.oHelper.SetValue("Identificação da SCP ?","")

            #Data Situação Especial/Evento ? SÓ SE NECESSARIO
            #self.oHelper.SetValue("Data Situação Especial/Evento ?","") #data

            #Método de Avalição de Estoque Final ? 
            #self.oHelper.SetValue("1 - Custo Médio Ponderado",True)
            #self.oHelper.SetValue("2 - PEPS",True)
            #self.oHelper.SetValue("3 - Arbitramento",True)
            #self.oHelper.SetValue("4 - Custo Específico",True)
            #self.oHelper.SetValue("5  Valor Realizável Líquido",True)
            #self.oHelper.SetValue("6 - Inventário Periódico",True)
            #self.oHelper.SetValue("7 - Outros",True)
            self.oHelper.SetValue("8 - Não há",True)
            self.oHelper.SetButton("Avançar")   #ENCERRA PASSO 04
            
            #-----------------------------------------------------------------------------
            #PASSO 05 - Parâmetros de Tributação
            #-----------------------------------------------------------------------------
            #Indicador de Optante pelo Refis ? 
            #self.oHelper.SetValue("S - Sim",True)
            self.oHelper.SetValue("N - Não",True)

            #Indicador de Optante pelo Paes ? 
            #self.oHelper.SetValue("S - Sim",True)
            self.oHelper.SetValue("N - Não",True)

            #Forma de Tributação do Lucro ? 
            self.oHelper.SetValue("1 - Lucro Real",True)
            #self.oHelper.SetValue("2 - Lucro Real/Arbitrado",True)
            #self.oHelper.SetValue("3 - Lucro Presumido/Real",True)
            #self.oHelper.SetValue("4 - Lucro Presumido/Real/Arbitrado",True)
            #self.oHelper.SetValue("5 - Lucro Presumido",True)
            #self.oHelper.SetValue("6 - Lucro Arbitrado",True)
            #self.oHelper.SetValue("7 - Lucro Presumido/Arbitrado",True)
            #self.oHelper.SetValue("8 - Imune de IRPJ",True)
            #self.oHelper.SetValue("9 - Isento de IRPJ",True)

            #Período de Apuração do IRPJ e CSLL ? 
            #self.oHelper.SetValue("T - Trimestral",True)
            self.oHelper.SetValue("A - Anual",True)

            #Qualificação da Pessoa Jurídica ? 
            self.oHelper.SetValue("01 - PJ em Geral",True)
            #self.oHelper.SetValue("02 - PJ Componente do Sistema Financeiro",True)
            #self.oHelper.SetValue("03 - Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar",True)

            #Forma de Trib. no Período ? 
            self.oHelper.SetValue("Forma de Trib. no Período ? ","RRRR")

            #Forma de Apur. da Estimativa ?
            self.oHelper.SetValue("Forma de Apur. da Estimativa ?","BBBBBBBBBBBB")

            #Tipo de Escrituração ?  SOMENTE PRESUMIDO
            #self.oHelper.SetValue("L - Livro Caixa",True)
            #self.oHelper.SetValue("C - Contábil",True)

            #Tipo de Pessoa Jur. Imune ou Isenta ? SOMENTE IMUNES E ISENTAS
            #self.oHelper.SetValue("01 - Assistencia Social",True)
            #self.oHelper.SetValue("02 - Educacional",True)
            #self.oHelper.SetValue("03 - Sindicato de Trabalhadores",True)
            #self.oHelper.SetValue("04 - Associação Civil",True)
            #self.oHelper.SetValue("05 - Cultural",True)
            #self.oHelper.SetValue("06 - Entidade Fechada de Prêvidencia Complementar",True)
            #self.oHelper.SetValue("07 - Filantrópica",True)
            #self.oHelper.SetValue("08 - Sindicato",True)
            #self.oHelper.SetValue("09 - Recreativa",True)
            #self.oHelper.SetValue("10 - Científica",True)
            #self.oHelper.SetValue("11 - Associação de Poupanã e Empréstimo",True)
            #self.oHelper.SetValue("12 - Entidade Aberta de Provência Complementar}",True)
            #self.oHelper.SetValue("13 - FIFA e Entidades Relacionadas",True)
            #self.oHelper.SetValue("14 - CIO e Entidades Relacionadas",True)
            #self.oHelper.SetValue("15  Partidos Políticos",True)
            #self.oHelper.SetValue("99 - Outras",True)

            #Apuração do IRPJ para Imunes ou Isentas ? #SÓ PARA IMUNES E ISENTAS
            #self.oHelper.SetValue("A - Anual",True)
            #self.oHelper.SetValue("T - Trimestral",True)
            #self.oHelper.SetValue("D - Desobrigada",True)

            #Apuração da CSLL para Imunes e Isentas ?   #SÓ PARA IMUNES E ISENTAS
            #self.oHelper.SetValue("A - Anual",True)
            #self.oHelper.SetValue("T - Trimestral",True)
            #self.oHelper.SetValue("D - Desobrigada",True)

            #Optante pela Extinção do RTT em 2014 ?  BLOQUEADO
            #self.oHelper.SetValue("S - Sim",True)  #BLOQUEADO
            #self.oHelper.SetValue("N - Não",True)  #BLOQUEADO

            #Dif. entre Contabilidade Societaria e FCONT ?  BLOQUEADO
            #self.oHelper.SetValue("S - Sim",True)          #BLOQUEADO
            #self.oHelper.SetValue("N - Não",True)          #BLOQUEADO

            #Critério de reconhecimento de receitas ? 
            #self.oHelper.SetValue("1 - Regime de Caixa",True)
            self.oHelper.SetValue("2 - Regime de Competencia",True)

            #Declaração País a País ?  
            #self.oHelper.SetValue("S - Sim",True)
            self.oHelper.SetValue("N - Não",True)

            #Codigo Identif. Bloco W ?
            #self.oHelper.SetValue("Codigo Identif. Bloco W ?","") #Caso necessario

            #DEREX ?  
            #self.oHelper.SetValue("S - Sim",True)
            self.oHelper.SetValue("N - Não",True)
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            #PASSO 06   -   Parâmetros de tributação
            #-----------------------------------------------------------------------------
            #PJ Sujeita a Aliquota de CSLL ? 
            self.oHelper.SetValue("09%",True)
            ##self.oHelper.SetValue("17%",True)
            ##self.oHelper.SetValue("20%",True)

            self.oHelper.SetValue("Quantidade de SCP da PJ ? ","000")

            #Administradora de Fundos e Clubes de Investimento ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Participações em Consórcios de Empresas ? 
            #self.oHelper.SetValue("S - Sim",True)
            ##self.oHelper.SetValue("N - Não",True)
            
            #Operações com o Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Operações com pessoa Vinculada/Interposta Pessoa/Pais com Tributação Favorecida ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #PJ Enquadrada nos artigos 48 ou 49 da Instrução Normativa RFB nº 1.312/2012 ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Participações no Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Atividade Rural ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Lucro da Exploração ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Isenção e Redução do Imposto para Lucro Presumido ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #FINOR/FINAM/FUNRES ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Doações a Campanhas Eleitorais ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Participação Permanente em Coligadas ou Controladas ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #PJ Efetuou Vendas a Empresa Comercial Exportadora com Fim Expecífico de Exportação ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Recebimentos do Exterior ou de Não Residentes ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Ativos no Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #PJ Comercial Exportadora ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Pagamentos ao Exterior ou não Residentes ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Comércio Eletronico e Tecnologia da Informação ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Royalties Recebidos do Brasil e do Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Royalties Pagos a beneficiários do Brasil e do Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Pagamentos ou Remessas a Titulos de Serviços, Juros e Dividendos a Beneficiarios do Brasil e do Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Inovação Tenológica e Desenvolvimento Tecnológico ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Capitação de Infomática e Inclusão Digital ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #PJ Habilitada ?
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Pólo INdustrial de Manaus e Amazônia Ocidental ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Zonas de Processamento de Exportação ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Áreas de Livre Comércio ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)

            #Codigo Identif. Registro 0021 ?
            self.oHelper.SetValue("Codigo Identif. Registro 0021 ?","")

            #Cod.Identif. Bloco V - DEREX ? BLOQUEADO
            #self.oHelper.SetValue("Cod.Identif. Bloco V - DEREX ?","")
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ## PASSO 07 -   Parâmetros de Filtro
            #-----------------------------------------------------------------------------

            self.oHelper.SetValue("Data Inicial ?","01/01/2018")
            self.oHelper.SetValue("Data Final ?","31/12/2018")
            self.oHelper.SetValue("Apuração do Exercicio(L/P) ?","31/12/2018")
            self.oHelper.SetValue("Calendário ?","215")
            self.oHelper.SetValue("Moeda ?","01")
            self.oHelper.SetValue("Tipo de Saldo ?","1")
            self.oHelper.SetValue("Plano de Contas De ?","")
            self.oHelper.SetValue("Plano de Contas Até ?","ZZZZZZZZZZZZZZZZZZZZ")
            self.oHelper.SetValue("Conta Patrimonio De ?","1")
            self.oHelper.SetValue("Conta Patrimonio Até ?","29999999999999999999")
            self.oHelper.SetValue("Conta Resultado De ?","3")
            self.oHelper.SetValue("Conta Resultado Até ?","49999999999999999999")

            ##Considera Vis. p/ Bal. Patrim. e DRE ? 
            #self.oHelper.SetValue("1 = Sim",True)
            self.oHelper.SetValue("2 = Não",True)

            #Cod. Conf. Bal. Patrim ?
            self.oHelper.SetValue("Cod. Conf. Bal. Patrim ?","")

            #Cod. Conf. Dem. Resul ?
            self.oHelper.SetValue("Cod. Conf. Dem. Resul ?","")

            #Processa C. Custo ? ? 
            #self.oHelper.SetValue("1 = Sim",True)
            self.oHelper.SetValue("2 = Não",True)

            #Plan. Conta Ref. ?
            self.oHelper.SetValue("Plan. Conta Ref. ?","000001")

            #Versão ?
            self.oHelper.SetValue("Versão ?","0001")
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ## PASSO 08 -   Parâmetros de Filtro
            #-----------------------------------------------------------------------------

            #self.oHelper.SetValue("L210 - Informa. Comp.Custos ?",True )
            #self.oHelper.SetValue("P130 - Dem. Receitas Incent. ?",True )  
            #self.oHelper.SetValue("P200 - Apur. da Base Cálculo ?",True )  
            #self.oHelper.SetValue("P230 - Calc. Isenção e Redu. ?",True ) 
            #self.oHelper.SetValue("P300 - Cálculo do IRPJ ?",True ) 
            #self.oHelper.SetValue("P400 - Apur Base de Calc.CSLL ?",True )
            #self.oHelper.SetValue("P500 - Calculo do CSLL ?",True ) 
            #self.oHelper.SetValue("T120 - Apur. da Base Cálculo ?",True )
            #self.oHelper.SetValue("T150 - Cálculo do IRPJ ?",True ) 
            #self.oHelper.SetValue("T170 - Apur Base de Calc.CSLL ?",True )
            #self.oHelper.SetValue("T181 - Calculo do CSLL ?",True )
            #self.oHelper.SetValue("U180 - Cálculo do IRPJ ?",True )
            #self.oHelper.SetValue("U182 - Cálculo do CSLL ?",True )
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ## PASSO 09 -   Informações Economicas/Gerais.
            #-----------------------------------------------------------------------------

            #Posição Anterior L/P ? 
            #self.oHelper.SetValue("S - Sim",True)
            self.oHelper.SetValue("N - Não",True,position=0)

            #self.oHelper.SetValue("Reg X390 ?",True) 
            #self.oHelper.SetValue("Reg X400 ?",True) 
            #self.oHelper.SetValue("Reg X460 ?",True) 
            #self.oHelper.SetValue("Reg X470 ?",True) 
            #self.oHelper.SetValue("Reg X480 ?",True) 
            #self.oHelper.SetValue("Reg X490 ?",True) 
            #self.oHelper.SetValue("Reg X500 ?",True) 
            #self.oHelper.SetValue("Reg X510 ?",True) 
            #self.oHelper.SetValue("Reg Y671 ?",True) 
            #self.oHelper.SetValue("Reg Y672 ?",True) 
            #self.oHelper.SetValue("Reg Y681 ?",True) 
            #self.oHelper.SetValue("Reg Y800 ?",True)
            self.oHelper.SetButton("Avançar")

            self.oHelper.SetButton("Finalizar") #cONFIGURAÇÃO EFETUADA
            #self.oHelper.WaitProcessing("Aguarde") #Processamento contabil
            self.oHelper.WaitShow("Deseja exportar dados para o DIPJ?")
            self.oHelper.SetButton("Não") #DIPJ
            

            #-----------------------------------------------------------------------------
            #Inicio da Exportação ao TAF
            #-----------------------------------------------------------------------------
            
            #Verificação do tipo, filial, empresa e codigo da empresa
            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Finalizar")

            #arrrumar aqui 

            self.oHelper.WaitShow("Atenção")
        
            # self.oHelper.SetButton("Não")#  Não #Sim    

            self.oHelper.SetButton("Não")#  Não #Sim

            self.oHelper.SetButton("Fechar")

            #Clicando no registro para verificação de sua criação
            #self.oHelper.WaitShow("ECF")
            self.oHelper.ClickTree("ECF")
            #self.oHelper.ClickLabel("Revisão - 000011 - E")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.AssertTrue()

    ###
     #ECF IMUNES IRPJ
    def test_CTBS001_013(self):
       # Layout 5 ECF Lucro Real
        # self.oHelper.Program("CTBS001")
        if self.oHelper.GetRelease() > '12.1.025':

            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            
            self.oHelper.ClickTree("ECF")
            self.oHelper.SetButton("Incluir")
            self.oHelper.SetButton("Avançar")

            # Tipo da Escrituração
            #self.oHelper.SetValue("Com Centralização", True)
            self.oHelper.SetValue("Sem Centralização", True)

            #Qual o Tipo de Escriturtação ? BLOQUEADO padrão
            #self.oHelper.SetValue("",True)# ECD , FCONT ou ECF 
            
            #-----------------------------------------------------------------------------
            #PASSO 02   -   Tipo da escrituração
            #-----------------------------------------------------------------------------
            #Informe o leiaute da ECF
            self.oHelper.SetValue("Leiaute 5", True)
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            #PASSO 03   -   Filiais 
            #-----------------------------------------------------------------------------
            self.oHelper.ClickBox("Filial", "M SP 02")
            self.oHelper.SetValue("Matriz", "")    #Filial Matriz
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            #PASSO 04   -   Dados da empresa para escrituração
            #-----------------------------------------------------------------------------
            #Indicador Inicio de Periodo ? 
            self.oHelper.SetValue("0 - Regular",True)
            #self.oHelper.SetValue("1 - Abertura",True)
            #self.oHelper.SetValue("2 - Resultante Cisao/Fusao ou remanescente...",True)
            #self.oHelper.SetValue("3 - Resultante de Transformação",True)
            #self.oHelper.SetValue("4 - Início de obrigatoriedade da entrega no curso do ano calendário",True)

            #Indicador de Situação Especial ? 
            self.oHelper.SetValue("0 - Normal",True)
            #self.oHelper.SetValue("1 - Extinção",True)
            #self.oHelper.SetValue("2 - Fusão",True)
            #self.oHelper.SetValue("3 - Incorporada",True)
            #self.oHelper.SetValue("4 - Incorporadora",True)
            #self.oHelper.SetValue("5 - Cisão Total",True)
            #self.oHelper.SetValue("6 - Cisão Parcial",True)
            #self.oHelper.SetValue("7 - Transformação - OBSOLETO",True)
            #self.oHelper.SetValue("8 - Isenta",True)
            #self.oHelper.SetValue("9 - Inclusão Simples Nacional",True)

            #Patr. Remanescente de Cisão(%) ? *
            self.oHelper.SetValue("Patr. Remanescente de Cisão(%) ?","00000")

            #Retificadora ? 
            #self.oHelper.SetValue("S - ECF Retificadora",True)
            self.oHelper.SetValue("N - ECF Original",True)
            #self.oHelper.SetValue("F - ECF Original com mudança de forma de tributação",True)

            #Número do Recibo Anterior ?
            #self.oHelper.SetValue("Número do Recibo Anterior ?","")

            #Tipo da ECF ? 
            self.oHelper.SetValue("0 - ECF de empresa não participante como sócio Ostensivo",True)
            #self.oHelper.SetValue("1 - ECF de empresa participante como sócio Ostensivo",True)
            #self.oHelper.SetValue("2 - ECF da SCP",True)

            #Identificação da SCP ?
            self.oHelper.SetValue("Identificação da SCP ?","")

            #Data Situação Especial/Evento ? SÓ SE NECESSARIO
            #self.oHelper.SetValue("Data Situação Especial/Evento ?","") #data

            #Método de Avalição de Estoque Final ? 
            #self.oHelper.SetValue("1 - Custo Médio Ponderado",True)
            #self.oHelper.SetValue("2 - PEPS",True)
            #self.oHelper.SetValue("3 - Arbitramento",True)
            #self.oHelper.SetValue("4 - Custo Específico",True)
            #self.oHelper.SetValue("5  Valor Realizável Líquido",True)
            #self.oHelper.SetValue("6 - Inventário Periódico",True)
            #self.oHelper.SetValue("7 - Outros",True)
            self.oHelper.SetValue("8 - Não há",True)
            self.oHelper.SetButton("Avançar")   #ENCERRA PASSO 04
            
            #-----------------------------------------------------------------------------
            #PASSO 05 - Parâmetros de Tributação
            #-----------------------------------------------------------------------------
            #Indicador de Optante pelo Refis ? 
            #self.oHelper.SetValue("S - Sim",True)
            self.oHelper.SetValue("N - Não",True)

            #Indicador de Optante pelo Paes ? 
            #self.oHelper.SetValue("S - Sim",True)
            self.oHelper.SetValue("N - Não",True)

            #Forma de Tributação do Lucro ? 
            #self.oHelper.SetValue("1 - Lucro Real",True)
            #self.oHelper.SetValue("2 - Lucro Real/Arbitrado",True)
            #self.oHelper.SetValue("3 - Lucro Presumido/Real",True)
            #self.oHelper.SetValue("4 - Lucro Presumido/Real/Arbitrado",True)
            #self.oHelper.SetValue("5 - Lucro Presumido",True)
            #self.oHelper.SetValue("6 - Lucro Arbitrado",True)
            #self.oHelper.SetValue("7 - Lucro Presumido/Arbitrado",True)
            self.oHelper.SetValue("8 - Imune de IRPJ",True)
            #self.oHelper.SetValue("9 - Isento de IRPJ",True)

            #Período de Apuração do IRPJ e CSLL ? 
            #self.oHelper.SetValue("T - Trimestral",True)
            self.oHelper.SetValue("A - Anual",True)

            #Qualificação da Pessoa Jurídica ? 
            self.oHelper.SetValue("01 - PJ em Geral",True)
            #self.oHelper.SetValue("02 - PJ Componente do Sistema Financeiro",True)
            #self.oHelper.SetValue("03 - Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar",True)

            #Forma de Trib. no Período ? 
            self.oHelper.SetValue("Forma de Trib. no Período ? ","")

            #Forma de Apur. da Estimativa ?
            self.oHelper.SetValue("Forma de Apur. da Estimativa ?","")

            #Tipo de Escrituração ?  SOMENTE PRESUMIDO
            #self.oHelper.SetValue("L - Livro Caixa",True)
            #self.oHelper.SetValue("C - Contábil",True)

            #Tipo de Pessoa Jur. Imune ou Isenta ? SOMENTE IMUNES E ISENTAS
            #self.oHelper.SetValue("01 - Assistencia Social",True)
            #self.oHelper.SetValue("02 - Educacional",True)
            #self.oHelper.SetValue("03 - Sindicato de Trabalhadores",True)
            #self.oHelper.SetValue("04 - Associação Civil",True)
            #self.oHelper.SetValue("05 - Cultural",True)
            #self.oHelper.SetValue("06 - Entidade Fechada de Prêvidencia Complementar",True)
            #self.oHelper.SetValue("07 - Filantrópica",True)
            #self.oHelper.SetValue("08 - Sindicato",True)
            #self.oHelper.SetValue("09 - Recreativa",True)
            #self.oHelper.SetValue("10 - Científica",True)
            #self.oHelper.SetValue("11 - Associação de Poupanã e Empréstimo",True)
            #self.oHelper.SetValue("12 - Entidade Aberta de Provência Complementar}",True)
            #self.oHelper.SetValue("13 - FIFA e Entidades Relacionadas",True)
            #self.oHelper.SetValue("14 - CIO e Entidades Relacionadas",True)
            #self.oHelper.SetValue("15  Partidos Políticos",True)
            #self.oHelper.SetValue("99 - Outras",True)

            #Apuração do IRPJ para Imunes ou Isentas ? #SÓ PARA IMUNES E ISENTAS
            #self.oHelper.SetValue("A - Anual",True)
            #self.oHelper.SetValue("T - Trimestral",True)
            self.oHelper.SetValue("D - Desobrigada",True)

            #Apuração da CSLL para Imunes e Isentas ?   #SÓ PARA IMUNES E ISENTAS
            #self.oHelper.SetValue("A - Anual",True)
            #self.oHelper.SetValue("T - Trimestral",True)
            self.oHelper.SetValue("D - Desobrigada",True)

            #Optante pela Extinção do RTT em 2014 ?  BLOQUEADO
            #self.oHelper.SetValue("S - Sim",True)  #BLOQUEADO
            #self.oHelper.SetValue("N - Não",True)  #BLOQUEADO

            #Dif. entre Contabilidade Societaria e FCONT ?  BLOQUEADO
            #self.oHelper.SetValue("S - Sim",True)          #BLOQUEADO
            #self.oHelper.SetValue("N - Não",True)          #BLOQUEADO

            #Critério de reconhecimento de receitas ? 
            #self.oHelper.SetValue("1 - Regime de Caixa",True)
            self.oHelper.SetValue("2 - Regime de Competencia",True)

            #Declaração País a País ?  
            #self.oHelper.SetValue("S - Sim",True)
            self.oHelper.SetValue("N - Não",True)

            #Codigo Identif. Bloco W ?
            #self.oHelper.SetValue("Codigo Identif. Bloco W ?","") #Caso necessario

            #DEREX ?  
            #self.oHelper.SetValue("S - Sim",True)
            self.oHelper.SetValue("N - Não",True)
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            #PASSO 06   -   Parâmetros de tributação
            #-----------------------------------------------------------------------------
            #PJ Sujeita a Aliquota de CSLL ? 
            self.oHelper.SetValue("09%",True)
            ##self.oHelper.SetValue("17%",True)
            ##self.oHelper.SetValue("20%",True)

            self.oHelper.SetValue("Quantidade de SCP da PJ ? ","000")

            #Administradora de Fundos e Clubes de Investimento ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Participações em Consórcios de Empresas ? 
            #self.oHelper.SetValue("S - Sim",True)
            ##self.oHelper.SetValue("N - Não",True)
            
            #Operações com o Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Operações com pessoa Vinculada/Interposta Pessoa/Pais com Tributação Favorecida ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #PJ Enquadrada nos artigos 48 ou 49 da Instrução Normativa RFB nº 1.312/2012 ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Participações no Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Atividade Rural ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Lucro da Exploração ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Isenção e Redução do Imposto para Lucro Presumido ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #FINOR/FINAM/FUNRES ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Doações a Campanhas Eleitorais ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Participação Permanente em Coligadas ou Controladas ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #PJ Efetuou Vendas a Empresa Comercial Exportadora com Fim Expecífico de Exportação ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Recebimentos do Exterior ou de Não Residentes ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Ativos no Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #PJ Comercial Exportadora ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Pagamentos ao Exterior ou não Residentes ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Comércio Eletronico e Tecnologia da Informação ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Royalties Recebidos do Brasil e do Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Royalties Pagos a beneficiários do Brasil e do Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Pagamentos ou Remessas a Titulos de Serviços, Juros e Dividendos a Beneficiarios do Brasil e do Exterior ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Inovação Tenológica e Desenvolvimento Tecnológico ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Capitação de Infomática e Inclusão Digital ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #PJ Habilitada ?
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Pólo INdustrial de Manaus e Amazônia Ocidental ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Zonas de Processamento de Exportação ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)
            
            #Áreas de Livre Comércio ? 
            #self.oHelper.SetValue("S - Sim",True)
            #self.oHelper.SetValue("N - Não",True)

            #Codigo Identif. Registro 0021 ?
            self.oHelper.SetValue("Codigo Identif. Registro 0021 ?","")

            #Cod.Identif. Bloco V - DEREX ? BLOQUEADO
            #self.oHelper.SetValue("Cod.Identif. Bloco V - DEREX ?","")
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ## PASSO 07 -   Parâmetros de Filtro
            #-----------------------------------------------------------------------------

            self.oHelper.SetValue("Data Inicial ?","01/01/2018")
            self.oHelper.SetValue("Data Final ?","31/12/2018")
            self.oHelper.SetValue("Apuração do Exercicio(L/P) ?","31/12/2018")
            self.oHelper.SetValue("Calendário ?","215")
            self.oHelper.SetValue("Moeda ?","01")
            self.oHelper.SetValue("Tipo de Saldo ?","1")
            self.oHelper.SetValue("Plano de Contas De ?","")
            self.oHelper.SetValue("Plano de Contas Até ?","ZZZZZZZZZZZZZZZZZZZZ")
            self.oHelper.SetValue("Conta Patrimonio De ?","1")
            self.oHelper.SetValue("Conta Patrimonio Até ?","29999999999999999999")
            self.oHelper.SetValue("Conta Resultado De ?","3")
            self.oHelper.SetValue("Conta Resultado Até ?","49999999999999999999")

            ##Considera Vis. p/ Bal. Patrim. e DRE ? 
            #self.oHelper.SetValue("1 = Sim",True)
            self.oHelper.SetValue("2 = Não",True)

            #Cod. Conf. Bal. Patrim ?
            self.oHelper.SetValue("Cod. Conf. Bal. Patrim ?","")

            #Cod. Conf. Dem. Resul ?
            self.oHelper.SetValue("Cod. Conf. Dem. Resul ?","")

            #Processa C. Custo ? ? 
            #self.oHelper.SetValue("1 = Sim",True)
            self.oHelper.SetValue("2 = Não",True)

            #Plan. Conta Ref. ?
            self.oHelper.SetValue("Plan. Conta Ref. ?","000001")

            #Versão ?
            self.oHelper.SetValue("Versão ?","0001")
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ## PASSO 08 -   Parâmetros de Filtro
            #-----------------------------------------------------------------------------

            #self.oHelper.SetValue("L210 - Informa. Comp.Custos ?",True )
            #self.oHelper.SetValue("P130 - Dem. Receitas Incent. ?",True )  
            #self.oHelper.SetValue("P200 - Apur. da Base Cálculo ?",True )  
            #self.oHelper.SetValue("P230 - Calc. Isenção e Redu. ?",True ) 
            #self.oHelper.SetValue("P300 - Cálculo do IRPJ ?",True ) 
            #self.oHelper.SetValue("P400 - Apur Base de Calc.CSLL ?",True )
            #self.oHelper.SetValue("P500 - Calculo do CSLL ?",True ) 
            #self.oHelper.SetValue("T120 - Apur. da Base Cálculo ?",True )
            #self.oHelper.SetValue("T150 - Cálculo do IRPJ ?",True ) 
            #self.oHelper.SetValue("T170 - Apur Base de Calc.CSLL ?",True )
            #self.oHelper.SetValue("T181 - Calculo do CSLL ?",True )
            #self.oHelper.SetValue("U180 - Cálculo do IRPJ ?",True )
            #self.oHelper.SetValue("U182 - Cálculo do CSLL ?",True )
            self.oHelper.SetButton("Avançar")

            #-----------------------------------------------------------------------------
            ## PASSO 09 -   Informações Economicas/Gerais.
            #-----------------------------------------------------------------------------

            #Posição Anterior L/P ? 
            #self.oHelper.SetValue("S - Sim",True)
            self.oHelper.SetValue("N - Não",True,position=0)

            #self.oHelper.SetValue("Reg X390 ?",True) 
            #self.oHelper.SetValue("Reg X400 ?",True) 
            #self.oHelper.SetValue("Reg X460 ?",True) 
            #self.oHelper.SetValue("Reg X470 ?",True) 
            #self.oHelper.SetValue("Reg X480 ?",True) 
            #self.oHelper.SetValue("Reg X490 ?",True) 
            #self.oHelper.SetValue("Reg X500 ?",True) 
            #self.oHelper.SetValue("Reg X510 ?",True) 
            #self.oHelper.SetValue("Reg Y671 ?",True) 
            #self.oHelper.SetValue("Reg Y672 ?",True) 
            #self.oHelper.SetValue("Reg Y681 ?",True) 
            #self.oHelper.SetValue("Reg Y800 ?",True)
            self.oHelper.SetButton("Avançar")

            self.oHelper.SetButton("Finalizar") #cONFIGURAÇÃO EFETUADA
            #self.oHelper.WaitProcessing("Aguarde") #Processamento contabil
            self.oHelper.WaitShow("Deseja exportar dados para o DIPJ?")
            self.oHelper.SetButton("Não") #DIPJ
            

            #-----------------------------------------------------------------------------
            #Inicio da Exportação ao TAF
            #-----------------------------------------------------------------------------
            
            #Verificação do tipo, filial, empresa e codigo da empresa
            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Finalizar") 

            self.oHelper.WaitShow("Atenção")

            self.oHelper.SetButton("Não")#  Não #Sim    

            self.oHelper.SetButton("Não")#  Não #Sim  

            self.oHelper.SetButton("Fechar")

            #Clicando no registro para verificação de sua criação
            #self.oHelper.WaitShow("ECF")
            self.oHelper.ClickTree("ECF")
            # self.oHelper.ClickLabel("Revisão - 000012 - E")
            self.oHelper.SetButton("Sair")

            self.oHelper.Program("CTBS001")
            self.oHelper.AssertTrue()

    

    def test_CTBS001_044(self):

        if self.oHelper.GetRelease() > '12.1.025':
        
            self.oHelper.ChangeEnvironment(date="31/12/2019",group="T1",branch="X CT101",module="34")
            # Layout 8  -  Geral
            self.oHelper.Program("CTBS001")

            self.oHelper.WaitShow("Bem-vindo...")
            self.oHelper.SetButton("Avançar")
            self.oHelper.WaitShow("Escolha a Empresa para exibição na central de escrituração.")
            self.oHelper.SetButton("Finalizar")
            self.oHelper.WaitShow("Tipo de Escrituração")

            self.oHelper.ClickTree("ECD")
            self.oHelper.SetButton("Incluir")
            self.oHelper.SetValue("Leiaute 8", True)  # Disponiveis Leiaute 1 ao 7
            self.oHelper.SetButton("Ok")

            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Avançar")
            #-----------------------------------------------------------------------------
            ##   Informe os dados da empresa escolhida para escrituração  ##
            #-----------------------------------------------------------------------------

            self.oHelper.SetValue("Com Centralização", True)
            #self.oHelper.SetValue("Sem Centralização", True)

            # Situação Especial ?
            self.oHelper.SetValue("Z-Normal", True)
            # self.oHelper.SetValue("0-Abertura",True)
            # self.oHelper.SetValue("1-Cosão",True)
            # self.oHelper.SetValue("2-Fusão",True)
            # self.oHelper.SetValue("3-Incorporação",True)
            # self.oHelper.SetValue("4-Extinção",True)
            # self.oHelper.SetValue("5-Transformação",True)

            # Indicador início de Periodo ?
            self.oHelper.SetValue("0-Inicio no primeiro dia do ano", True)
            # self.oHelper.SetValue("1-Abertura",True)
            #self.oHelper.SetValue("2-Resultante Cisao/Fusao ou remanescente...",True)
            #self.oHelper.SetValue("3-Inicio Obrigatoriedade Entrega ECD",True)

            #Indicador de existência de NIRE ? 
            self.oHelper.SetValue("0-Empresa não possui NIRE",True)
            #self.oHelper.SetValue("1-Empresa possui NIRE",True)

            #Indicador de finalidade da escrituração ?
            self.oHelper.SetValue("0 - Original", True)
            ##self.oHelper.SetValue("1 - Substituta",True)

            # self.oHelper.SetValue("Hash da escrituração de finalidade da escrituração ?","")
            # self.oHelper.SetValue("NIRE da Escrituração Substituida ?","") ##Bloqueado

            # indicador Empr.Grande Porte ?
            self.oHelper.SetValue(
                "0  Empresa não é entidade sujeita a auditoria independente.", True)
            ##self.oHelper.SetValue("1 - Empresa é entidade sujeita a auditoria independente.",True)

            # Tipo da ECD (SCP) ?
            self.oHelper.SetValue(
                "0  ECD de empresa não participante de SCP como sócio ostensivo.", True)
            ##self.oHelper.SetValue("1 - ECD de empresa participante de SCP como sócio ostensivo.",True)
            ##self.oHelper.SetValue("1 - ECD da SCP",True)

            # Plano Contas Referencial ?
            self.oHelper.SetValue("1-PJ em Geral (L100A + L300A da ECF)", True)
            #self.oHelper.SetValue(
            #    "2-PJ em GeralLucro Presumido (P100 + P150 da ECF)", True)
            #self.oHelper.SetValue("3-Financeiras (L100B + L300B da ECF)", True)
            #self.oHelper.SetValue("4-Seguradoras (L100C + L300C da ECF)", True)
            #self.oHelper.SetValue(
            #    "5-Imunes e Isentas em Geral (U100A + U150A da ECF)", True)
            #self.oHelper.SetValue(
            #    "6-Financeiras-Imunes e Isentas (U100B + U150B da ECF)", True)
            #self.oHelper.SetValue(
            #    "7-Seguradoras-Imunes e Isentas (U100C + U150C da ECF)", True)
            #self.oHelper.SetValue(
            #    "8-Entidades Fechadas Prev Complementar (U100D + U150D da ECF)", True)
            #self.oHelper.SetValue(
            #    "9-Partidos Politicos (U100E + U150E da ECF)", True)
            #self.oHelper.SetValue(
            #    "10-Financeiras  Lucro Presumido (P100B + P150B da ECF)", True)

            # Moeda funcional diferente da nacional ?
            # self.oHelper.SetValue("1-Sim", True, position=1)
            self.oHelper.SetValue("2-Não", True,position=1)

            # Escrituração Contábeis consolidadas ?
            #self.oHelper.SetValue("1-Sim", True)
            self.oHelper.SetValue("2-Não", True,position=2)

            #self.oHelper.SetValue("Codigo Identif. Bloco K ?","")
            
            ###Novas perguntas Leiaute 8
            #Ocorreu mudança no Plano de Contas ? 
            #self.oHelper.SetValue("1-Sim", True)
            self.oHelper.SetValue("2-Não", True,position=3)

            #Existe amarração com Plano Referencial ? 
            self.oHelper.SetValue("1-Sim", True)
            # self.oHelper.SetValue("2-Não", True,position=3)

            # Encerra dados da empresa para escrituração
            self.oHelper.SetButton("Avançar")
            #-----------------------------------------------------------------------------
            ##  Quais são as filiais que essa empresa centralizadora?   ##
            #-----------------------------------------------------------------------------
            #PASSO 03 FILIAIS
            # self.oHelper.WaitShow("Quais são as filiais que essa empresa centralizadora?")
            # self.oHelper.ClickBox("Empresa/Unidade/Filial", "M SP 04") #X CT102
            self.oHelper.ClickBox("Empresa/Unidade/Filial", "X CT101") #X CT101
            # self.oHelper.SetKey("DOWN")
            # self.oHelper.SetKey("DOWN")
            # self.oHelper.SetKey("DOWN")
            # self.oHelper.SetKey("ENTER")
            # self.oHelper.ClickGridCell("Empresa/Unidade/Filial",row=11)
            # self.oHelper.
            
            self.oHelper.SetButton("Avançar")  # Encerra escolha de filiais

            ##  Informe neste passo, quais as incrições de sua empresa. ##
            # Outras Inscrições ?
            # self.oHelper.SetValue("00-Não ha",True)
            #self.oHelper.SetValue("01-Bco Cent. do Brasil / BACEN",True)
            #self.oHelper.SetValue("02-Super. de Seg. Privados / SUSEP",True)
            #self.oHelper.SetValue("03-Comis. de Val. Mobiliários / CVM",True)
            #self.oHelper.SetValue("04-Agência Nacional de Transportes Terrestres (ANTT)",True)
            #self.oHelper.SetValue("UF-Secretarias de Estado",True)
            self.oHelper.SetValue("MI-Múltiplas Inscrições",True)

            self.oHelper.SetButton("Avançar") ## Abrir tela de multiplas inscricoes
            self.oHelper.WaitShow("Múltiplas inscrições cadastrais da pessoa jurídica")
            self.oHelper.SetButton("Incluir") ## Abrir tela de multiplas inscricoes

            #PREENCHENDO CAMPOS
            
            ## Primeira instituicao
            self.oHelper.WaitShow("Múltiplas inscrições cadastrais da pessoa jurídica - INCLUIR")
        
            RevisaoAtual = self.oHelper.GetValue("CSS_CODREV")
            CodigoInstituicao = self.oHelper.GetValue("CSS_INSTIT")
            self.oHelper.SetValue("CSS_INSTIT", "PR") ## 
            self.oHelper.SetValue("CSS_CODIGO", "1100002511") ## 
            self.oHelper.SetButton("Salvar") ## 
            self.oHelper.SetButton("Cancelar") ## 
            
            self.oHelper.SearchBrowse(RevisaoAtual + CodigoInstituicao) ## 
        
            ## Segunda instituicao
            self.oHelper.SetButton("Incluir") ##

            self.oHelper.WaitHide("Múltiplas inscrições cadastrais da pessoa jurídica - INCLUIR")
            self.oHelper.WaitShow("Múltiplas inscrições cadastrais da pessoa jurídica - INCLUIR")
        
            CodigoInstituicao2 = self.oHelper.GetValue("CSS_INSTIT")
            self.oHelper.SetValue("CSS_INSTIT", "SP") ## 
            self.oHelper.SetValue("CSS_CODIGO", "535054653118") ## 
            self.oHelper.SetButton("Salvar") ## 
            self.oHelper.SetButton("Cancelar") ## 
            self.oHelper.SearchBrowse(RevisaoAtual + CodigoInstituicao2) ## 

            self.oHelper.SetButton("X") ## 
            
            # self.oHelper.SetValue("Unidade Federativa ?","SP")
            # self.oHelper.SetValue("Inscrição ?","")
            #self.oHelper.SetValue("Codigo da SCP ?","")    #BLOQUEADO
            # self.oHelper.SetButton("Avançar") ##somente se for uma inscrição, pula todas inclusões acima

            #-----------------------------------------------------------------------------
            ##  Informe neste passo, quais os dados principais para a escrituração. PASSO 1/3   ##
            #-----------------------------------------------------------------------------
            #Indicação da Escrituracao ? 
            self.oHelper.SetValue("G-Geral",True)
            # self.oHelper.SetValue("R-Diário Resumido",True)
            ##self.oHelper.SetValue("A-Diário Auxiliar",True)
            ##self.oHelper.SetValue("B-Balancete Diário",True)

            self.oHelper.SetValue("Numero de Ordem do Livro ?","000020")
            self.oHelper.SetValue("Natureza do Livro ?","Livro G")
            self.oHelper.SetButton("Avançar") #Encerra dados principais da escrituração 1/3

            #-----------------------------------------------------------------------------
            ##  Informe neste passo, quais os dados principais para a escrituração. PASSO 2/3   ##
            #-----------------------------------------------------------------------------
            
            self.oHelper.SetValue("Periodo Inicial Lcto ?", "01/01/2019")
            self.oHelper.SetValue("Periodo Final Lcto ?",   "31/12/2019")
            self.oHelper.SetValue("Apuração do Exercicio(L/P) ?","31/12/2019")
            self.oHelper.SetValue("Calendario ?","219")
            self.oHelper.SetValue("Moeda ?","01")
            self.oHelper.SetValue("Tipo Saldo (Societario) ?","1")
            self.oHelper.SetValue("Conta De ?","")
            self.oHelper.SetValue("Conta Ate ?","ZZZZZZZZZZZZZZZZZZZZ")
            self.oHelper.SetValue("Plano Contas Referencial ?","000010") #Branco a nao ser que precise
            self.oHelper.SetValue("Versão ?","0001")                   #Branco a nao ser que precise

            #Arquivo Trimestral Unificado ? 
            #self.oHelper.SetValue("1-Sim",True)
            self.oHelper.SetValue("2-Não",True,position=3)
            self.oHelper.SetButton("Avançar")   #Encerra informações principais Passo 2/3
            #-----------------------------------------------------------------------------
            ##   Informe neste passo, quais os dados principais para a escrituração. PASSO 3/3   ##
            #-----------------------------------------------------------------------------
            self.oHelper.SetValue("Periodo Inicial Demons ?","01/01/2019")
            self.oHelper.SetValue("Periodo Final Demons ?","31/12/2019")
            self.oHelper.SetValue("Cod. Conf. Bal. Patrim ?","L10")
            self.oHelper.SetValue("Cod. Conf. DRE ?","L30")

            #self.oHelper.SetValue("Outras Demonstracoes ?","")# BLOQUEADO

            #Processa C.Custo ? ? 
            self.oHelper.SetValue("1-Não",True)
            #self.oHelper.SetValue("2-Sim",True)

            #J210:Indicador do tipo de demostração ? ? 
            ##self.oHelper.SetValue("DLPA",True)
            self.oHelper.SetValue("DMPL",True)

            # self.oHelper.SetValue("J210: Cod.Conf.Dem. ?","")
            #self.oHelper.SetValue("J310: Cod.Conf.DFC ?","")   #BLOQUEADO
            #self.oHelper.SetValue("J410: Cod.Conf.DVA ?","")   #BLOQUEADO

            #J200:Historico Fato Contabil - Cadastrar ?                             #BLOQUEADO
            ##self.oHelper.SetValue("1-Sim",True)                                   #BLOQUEADO
            ##self.oHelper.SetValue("2-Não",True)                                   #BLOQUEADO

            #J215:Detalhar Fato Contabil - Detalhar ? 
            # self.oHelper.SetValue("1-Sim",True)  
            self.oHelper.SetValue("2-Não",True,position=5)      

            ##self.oHelper.SetValue("001: Dem. Abrang. do Período ","")             #BLOQUEADO
            ##self.oHelper.SetValue("002: Dem. Fluxos de Caixa ? ","")              #BLOQUEADO
            ##self.oHelper.SetValue("003: Dem. do Valor Adicionado ?","")           #BLOQUEADO
            ##self.oHelper.SetValue("010: Notas Explicativas ? ","")                #BLOQUEADO
            ##self.oHelper.SetValue("011: Relatório da Administração ?","")         #BLOQUEADO
            ##self.oHelper.SetValue("012: Parecer dos Auditores ? ","")             #BLOQUEADO
            ##self.oHelper.SetValue("099: Outros ? ","")                            #BLOQUEADO

            ##self.oHelper.SetValue("Termo de Substituição da ECD ?","")            #BLOQUEADO

            #Motivo da Substituição ? 
            #self.oHelper.SetValue("000=Não se aplica",True)                       #BLOQUEADO
            ##self.oHelper.SetValue("001=Mudanças de saldos",True)                  #BLOQUEADO
            ##self.oHelper.SetValue("002=Alteração assinatura",True)                #BLOQUEADO
            ##self.oHelper.SetValue("003=Alteração Dem. contábil",True)             #BLOQUEADO
            ##self.oHelper.SetValue("004=Alteração Forma Escrit. contábil",True)    #BLOQUEADO
            ##self.oHelper.SetValue("005=Alteração do número do livro",True)        #BLOQUEADO
            ##self.oHelper.SetValue("099=Outros",True)  #BLOQUEADO

            self.oHelper.SetButton("Avançar")   #Encerra informações principais 3/3 
            self.oHelper.SetButton("Finalizar")
            
            # ##tela de moeda funcional - NÃO UTILIZA NESSE CASO
            # self.oHelper.SetValue("Moeda Nacional", "01")
            # self.oHelper.SetValue("Codigo Leiaute", "01")
            # self.oHelper.SetButton("Confirmar")
            

            #self.oHelper.WaitProcessing("Aguarde")
            #self.oHelper.WaitProcessing("gravando dados")
            
            #self.oHelper.CheckView("ECD")
            #self.oHelper.ClickTree("ECD")
            ##self.oHelper.SetButton("Sair")
            self.oHelper.AssertTrue()    



    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
