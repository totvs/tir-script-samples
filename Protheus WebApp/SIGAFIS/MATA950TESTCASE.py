from tir import Webapp
import unittest
from datetime import datetime

class MATA950(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''
        inst.oHelper = Webapp()

        DateSystem = datetime.today()
        
        inst.oHelper.Setup("SIGAFIS",DateSystem.strftime('%d/%m/%Y'),"T1","X FIS27","09")
        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA950")
    
    def test_MATA950_001(self):
        '''
        Test Case 001
        '''
        self.oHelper.SetButton('x')
        self.oHelper.SetButton('Param.')
        self.oHelper.SetValue('Data Inicial ?','01/08/2016')
        self.oHelper.SetValue('Data Final ?','31/08/2016')
        self.oHelper.SetValue('Instr.Normativa ?','DIMESC')
        self.oHelper.SetButton('Confirmar')        
        self.oHelper.SetValue('Diretorio ?',"C:\\")
        self.oHelper.SetValue('Seleciona filiais ?','Não')
        self.oHelper.SetValue('Aglutina Obrigação ?','Não')  
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('Cpf Contador','40259278882')      
        self.oHelper.SetValue('Nome Contador','FULANO DE TAL')  #campo não é acionado nem pelo nome da label
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('Nome Contribuinte','CONTRIBUINTE DE TAL')
        self.oHelper.SetValue('Tipo Declaracäo','Normal')
        self.oHelper.SetValue('Regime de Apuracäo','Normal')
        self.oHelper.SetValue('Porte da Empresa','Normal')
        self.oHelper.SetValue('Apuracäo Consolidada','Não é apuração consolidada')
        self.oHelper.SetValue('Transf. Cred. Periodo','Não apurou ou reservou nem recebeu créditos')
        self.oHelper.SetValue('Tem creditos presumidos','Não')
        self.oHelper.SetValue('Tem Creditos por incentivos fiscais','Não')
        self.oHelper.SetValue('Movimento','Sem movimento e com saldos')
        self.oHelper.SetValue('Substituto tributario','Sim')
        self.oHelper.SetValue('Tem escrita contabil','Sim é estab. principal')
        self.oHelper.SetValue('Tipo Apuracäo','Mensal')
        self.oHelper.SetValue('Quantidade Trabalhadores atividade','')
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('Gera Quadro 80?','Sim')
        self.oHelper.SetValue('Quadro 80 Zerado?','Sim')
        self.oHelper.SetValue('Data de Inicio do Exercicio','01/08/2016')
        self.oHelper.SetValue('Valor do Estoque no inicio do Exercício','10.000,00')
        self.oHelper.SetValue('Data Final do Exercício','31/08/2016')
        self.oHelper.SetValue('Valor do Estoque no final do Exercício','2.000,00')
        self.oHelper.SetValue('Receita Bruta Vendas/Servicos','0,00')
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('Disponibilidades','0,00')
        self.oHelper.SetValue('Contas a receber do circulante','0,00')
        self.oHelper.SetValue('Estoque de mercadorias e materia-prima','0,00')
        self.oHelper.SetValue('Outros estoques','0,00')
        self.oHelper.SetValue('Outras contas do ativo circulante','0,00')
        self.oHelper.SetValue('Contas a receber do realizavel','0,00')
        self.oHelper.SetValue('Outras Contas do realizavel','0,00')
        self.oHelper.SetValue('Investimentos','0,00')
        self.oHelper.SetValue('Imobilizado (Liquido)','0,00')
        self.oHelper.SetValue('Diferido','0,00')
        self.oHelper.SetValue('Intangivel','0,00')        
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('Fornecedores','0,00')
        self.oHelper.SetValue('Emprestimos e financiamentos','0,00')
        self.oHelper.SetValue('Outras contas do passivo circulante','0,00')
        self.oHelper.SetValue('- Exigivel a longo prazo','0,00')
        self.oHelper.SetValue('- Resultado de exercicios futuros','0,00')
        self.oHelper.SetValue('Capital social','0,00')
        self.oHelper.SetValue('Outras contas do patrimonio liquido','0,00')
        self.oHelper.SetValue('Outras patrimônio líquido (valor negativo)','0,00')  
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('Receita bruta vendas/servico','0,00')
        self.oHelper.SetValue('Devolucöes/Abatimentos e impostos','0,00')
        self.oHelper.SetValue('Custo da mercadoria vendida','0,00')
        self.oHelper.SetValue('- Outras Receitas operacionais','0,00')
        self.oHelper.SetValue('Despesas operacionais','0,00')
        self.oHelper.SetValue('Receitas näo operacionais','0,00')
        self.oHelper.SetValue('Despesas näo operacionais','0,00')
        self.oHelper.SetValue('Provisäo para o IR','0,00')  
        self.oHelper.SetValue('Provisão para o IR e para contribuição social','0,00')
        self.oHelper.SetValue('Participacöes e contribuicöes','0,00')        
        self.oHelper.SetButton('Avançar >>')
        
        #Informações para montagem dos registros Tipo 84/94 - Detalhamento das Despesas
        self.oHelper.SetValue('Pro-labore','0,00')
        self.oHelper.SetValue('Comissoes, salarios, ordenados','0,00')
        self.oHelper.SetValue('Combustiveis e  lubrificantes','0,00')
        self.oHelper.SetValue('Encargos sociais','0,00')
        self.oHelper.SetValue('Tributos federais','0,00')
        self.oHelper.SetValue('Tributos estaduais','0,00')
        self.oHelper.SetValue('Tributos municipais','0,00')
        self.oHelper.SetValue('Agua e telefone','0,00')
        self.oHelper.SetValue('Energia eletrica','0,00')
        self.oHelper.SetValue('Alugueis','0,00')
        self.oHelper.SetValue('Servicos profissionais','0,00')
        self.oHelper.SetValue('Seguros','0,00')  
        self.oHelper.SetValue('Fretes e carretos','0,00')
        self.oHelper.SetValue('Despesas financeiras','0,00')
        self.oHelper.SetValue('Outras despesas','0,00')       
        self.oHelper.SetButton('Avançar >>')
        
        #Informações para montagem do registro Tipo 41 - Demonstrativo de Créditos Acumulados
        self.oHelper.SetValue('Credito nas aquisicöes','0,00')
        self.oHelper.SetValue('Produtos Exportados no Mês','0,00')
        self.oHelper.SetValue('Saídas Isentas ou Não Tributadas','0,00')
        self.oHelper.SetValue('Saídas Diferidas ou Suspensas','0,00')
        self.oHelper.SetValue('Relativo à exportação','0,00')
        self.oHelper.SetValue('Relativo a saídas isentas','0,00')
        self.oHelper.SetValue('Relativo a saídas diferidas','0,00')
        self.oHelper.SetValue('Outros créditos não transferíveis','0,00')
        self.oHelper.SetValue('Exportação lançado em DCIP','0,00')  
        self.oHelper.SetValue('Saída isenta lançado em DCIP','0,00')
        self.oHelper.SetValue('Saídas diferidas lançado em DCIP','0,00')
        self.oHelper.SetValue('Rec. estabelecimentos consolidados','0,00')
        self.oHelper.SetValue('Crédito recebido por transferência','0,00')       
        self.oHelper.SetValue('Outras deduções do saldo credor','0,00') 
        self.oHelper.SetButton('Avançar >>')
        
        #Informações para montagem do registro Tipo 44 - Créditos Presumidos:
        self.oHelper.SetValue('Total pago no mes aos empregados','0,00')       
        self.oHelper.SetValue('Media no exercicio anterior','0,00') 
        self.oHelper.SetButton('Avançar >>')
        
        #Informações para montagem do registro Tipo 45 - Créditos Por Incentivos Fiscais
        self.oHelper.SetValue('Valor recibo (D. 3604/98)','0,00')
        self.oHelper.SetButton('Avançar >>')
        
        #Informações para montagem do registro Tipo 28 - Apuração Especial para Bares, Restaurantes e Similares
        self.oHelper.SetValue('Debito sobre o valor das entradas','0,00')
        self.oHelper.SetValue('Debito sobre a diferenca entre Entradas/Saidas','0,00')       
        self.oHelper.SetValue('Credito Aquisicäo atacadistas outras UF','0,00')
        self.oHelper.SetValue('Saldo credor Mes Anterior','0,00') 
        self.oHelper.SetButton('Avançar >>')
        
        #Informações para montagem do registro Tipo 51 - Exclusões do valor adicionado no mês (Entradas)
        self.oHelper.SetValue('Prestacäo de servico sujeita ao ISS','0,00')
        self.oHelper.SetValue('25% Transf. recebidas a preço de venda','0,00')       
        self.oHelper.SetValue('Tributo a recuperar incidente na entrada','0,00')
        self.oHelper.SetValue('IPI relativo aquisicäo de materias-primas','0,00') 
        self.oHelper.SetValue('Parcela do ICMS Retido','0,00')
        self.oHelper.SetValue('Subsidios concedidos por orgäos do governo','0,00')
        self.oHelper.SetButton('Avançar >>')
        
        #Informações para montagem do registro Tipo 51 - Exclusões do valor adicionado no mês (Saídas)
        self.oHelper.SetValue('Prestacäo de servico sujeita ao ISS','0,00') 
        self.oHelper.SetValue('25% Transf.recebidas a preço de venda','0,00') 
        self.oHelper.SetValue('IPI incidente','0,00')
        self.oHelper.SetValue('Parcela do ICMS Retido','0,00')
        self.oHelper.SetButton('Avançar >>')  
        
        #Informações para montagem do registro Tipo 32 - Informações Sobre Substituição Tributária      
        self.oHelper.SetValue('Valor dos produtos','0,00')
        self.oHelper.SetValue('Valor de IPI','0,00')
        self.oHelper.SetValue('Despesas acessorias','0,00')
        self.oHelper.SetValue('Base de calculo do ICMS Proprio','0,00')
        self.oHelper.SetValue('ICMS Proprio','0,00')
        self.oHelper.SetValue('Base calculo ICMS/ST','0,00')
        self.oHelper.SetValue('Débito por ocasião do fato gerador','0,00')
        self.oHelper.SetValue('Imposto Retido','0,00')
        self.oHelper.SetValue('Saldo Credor Periodo Anterior','0,00')
        self.oHelper.SetValue('Devolucäo e Desfazimento','0,00')
        self.oHelper.SetValue('Ressarcimento ICMS/ST','0,00')
        self.oHelper.SetValue('Outros creditos','0,00')
        self.oHelper.SetValue('Imposto 1. Decendio','0,00')  
        self.oHelper.SetValue('Imposto 2. Decendio','0,00')
        self.oHelper.SetValue('Antecip.Combustíveis Liquidos e Gasosos','0,00')
        self.oHelper.SetValue('transf Sld devedor ao estab consolidador','Nao')
        self.oHelper.SetValue('transf Sld credor ao estab consolidador','Nao')       
        self.oHelper.SetValue('Sld Dev Recebidos de estab consolidados','0,00')
        self.oHelper.SetValue('Créditos Declarados no DCIP','0,00') 
        self.oHelper.SetButton('Avançar >>')

        #Informações para montagem do registro Tipo 31 - Débitos Específicos
        self.oHelper.SetValue('Débito relativo a operações de importação','0,00')  
        self.oHelper.SetValue('Débito relativo a aquisição de outras UF','0,00')
        self.oHelper.SetValue('Débito por responsabilidade Tributária','0,00')
        self.oHelper.SetValue('Outros débitos por ocasião do Fat. Ger.','0,00')
        self.oHelper.SetValue('Outros débitos eventuais','0,00')       
        self.oHelper.SetValue('Numero GNRE Débitos específico','')
        self.oHelper.SetValue('Cod.Receita e Classe de Venc. Débitos Espec.','') 
        self.oHelper.SetButton('Avançar >>')
        
        # 
        #Informações para montagem do registro Tipo 30 - Cálculo do Imposto a Pagar ou Saldo Credor
        self.oHelper.SetValue('Imposto 1º decêndio ou 1ª parc. antecipa.','0,00')       
        self.oHelper.SetValue('Imposto 2º decêndio ou 2ª parc. antecipa.','0,00')
        self.oHelper.SetValue('Antecip.Combustíveis Liquidos e Gasosos','0,00') 
        self.oHelper.SetButton('Avançar >>')
        
        # Campos s
        #Informações para montagem do registro Tipo 90 (Encerramento Atividades) - Resumo Livro de Inventário e Receita Bruta
        self.oHelper.SetValue('Data de Inicio do Exercicio','')
        self.oHelper.SetValue('Valor do Estoque no inicio do Exercício','0,00')
        self.oHelper.SetValue('Data Final do Exercício','')       
        self.oHelper.SetValue('Valor do Estoque no final do Exercício','0,00')
        self.oHelper.SetValue('Receita Bruta Vendas/Servicos','0,00') 
        self.oHelper.SetButton('Avançar >>')

        # 
        # Informações para montagem do registro Tipo 91 (Encerramento Atividades) - Ativo:
        self.oHelper.SetValue('Disponibilidades','0,00')  
        self.oHelper.SetValue('Contas a receber do circulante','0,00')
        self.oHelper.SetValue('Estoque de mercadorias e materia-prima','0,00')
        self.oHelper.SetValue('Outros estoques','0,00')
        self.oHelper.SetValue('Outras contas do ativo circulante','0,00')       
        self.oHelper.SetValue('Contas a receber do realizavel','0,00')
        self.oHelper.SetValue('Outras Contas do realizavel','0,00')
        self.oHelper.SetValue('Investimentos','0,00')  
        self.oHelper.SetValue('Imobilizado (Liquido)','0,00')
        self.oHelper.SetValue('Diferido','0,00')
        self.oHelper.SetValue('Intangivel','0,00') 
        self.oHelper.SetButton('Avançar >>')

        # 
        #Informações para montagem do registro Tipo 92 - (Encerramento Atividades) - Passivo
        self.oHelper.SetValue('Fornecedores','0,00')  
        self.oHelper.SetValue('Emprestimos e financiamentos','0,00')
        self.oHelper.SetValue('Outras contas do passivo circulante','0,00')
        self.oHelper.SetValue('- Exigivel a longo prazo','0,00')
        self.oHelper.SetValue('- Resultado de exercicios futuros','0,00')       
        self.oHelper.SetValue('Capital social','0,00')
        self.oHelper.SetValue('Outras contas do patrimonio liquido','0,00')
        self.oHelper.SetValue('Outras patrimônio líquido (valor negativo)','0,00')  
        self.oHelper.SetButton('Avançar >>')

        # 
        #Informações para montagem do registro Tipo 93 (Encerramento Atividades) - Demonstração de Resultados
        self.oHelper.SetValue('Receita bruta vendas/servico','0,00')  
        self.oHelper.SetValue('Devolucöes/Abatimentos e impostos','0,00')
        self.oHelper.SetValue('Custo da mercadoria vendida','0,00')
        self.oHelper.SetValue('- Outras Receitas operacionais','0,00')
        self.oHelper.SetValue('Despesas operacionais','0,00')       
        self.oHelper.SetValue('Receitas näo operacionais','0,00')
        self.oHelper.SetValue('Despesas näo operacionais','0,00')
        self.oHelper.SetValue('Provisäo para o IR','0,00')
        self.oHelper.SetValue('Provisão para o IR e para contribuição social','0,00') 
        self.oHelper.SetValue('Participacöes e contribuicöes','0,00')         
        self.oHelper.SetButton('Avançar >>')

        # 
        #Informações para montagem do registro Tipo 94 (Encerramento Atividades) - Detalhamento das Despesas
        self.oHelper.SetValue('Pro-labore','0,00')  
        self.oHelper.SetValue('Comissoes, salarios, ordenados','0,00')
        self.oHelper.SetValue('Combustiveis e  lubrificantes','0,00') 
        self.oHelper.SetValue('Encargos sociais','0,00')
        self.oHelper.SetValue('Tributos federais','0,00')       
        self.oHelper.SetValue('Tributos estaduais','0,00')
        self.oHelper.SetValue('Tributos municipais','0,00')
        self.oHelper.SetValue('Agua e telefone','0,00')
        self.oHelper.SetValue('Energia eletrica','0,00') 
        self.oHelper.SetValue('Alugueis','0,00')   
        self.oHelper.SetValue('Servicos profissionais','0,00')
        self.oHelper.SetValue('Seguros','0,00')
        self.oHelper.SetValue('Fretes e carretos','0,00')
        self.oHelper.SetValue('Despesas financeiras','0,00') 
        self.oHelper.SetValue('Outras despesas','0,00')        
        self.oHelper.SetButton('Avançar >>')

        #Informações para montagem do registro Tipo 46 (Créditos por Regimes e Autorizações Especiais) Relativo ao crédito informado no DCIP
        self.oHelper.SetValue('Informa Protocolos?','Não')        
        self.oHelper.SetButton('Avançar >>')

        #Informações para montagem do registro Tipo 48 - Informações para rateio do valor adicionado
        self.oHelper.SetValue('Envia Informações para Reg. 48 em %?','Não')        
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('10- Valor da Base de Cálculo das Saídas','0,00')
        self.oHelper.SetValue('20- Déb. Rel. às Saídas com Créd. Presumido','0,00')
        self.oHelper.SetValue('30- Créd. Presumido Utilizado em Substituição','0,00')
        self.oHelper.SetValue('31- Créditos Permitidos para Compensar com','0,00')
        self.oHelper.SetValue('45- Déb. pela utilização do crédito presumido','0,00')
        self.oHelper.SetValue('50- Débito Apurado pela Apropriação','0,00')
        self.oHelper.SetValue('110- Saldo Credor das Antecipações para','0,00')
        self.oHelper.SetValue('120- Créd. decorrente do Pagto. Antecip. do','0,00')

        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('OK')

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()