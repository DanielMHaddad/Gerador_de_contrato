from datetime import datetime
from utils.window import Window
from num2words import num2words

janela = Window()

# Classe Ap
class Ap:
    def __init__(self):
        # Obtém o número do apartamento e remove espaços em branco
        self.ap = janela.values['ap_num'].replace(" ", "")
        # Obtém o valor do apartamento e substitui ',' por '.' para lidar com decimais
        self.valor = janela.values['ap_valor'].replace(',', '.')
        # Converte o valor para extenso usando a biblioteca num2words
        self.valor_ext = num2words(float(self.valor), lang='pt-br')

# Classe Locatario
class Locatario:
    def __init__(self, nome=None, cpf=None, rg=None, cel=None, nacionalidade=None):
        # Obtém as informações do locatário da janela e as armazena nos atributos correspondentes
        self.nome = janela.values['nome_loc'].title()
        self.cpf = janela.values['cpf_loc']
        self.rg = janela.values['rg_loc']
        self.cel = janela.values['nacionalidade_loc'].title()
        self.nacionaliade = janela.values['cel_loc']

# Classe Fiador
class Fiador:
    def __init__(self, nome=None, cpf=None, rg=None, cel=None, end=None, estado_civil=None, nacionalidade=None):
        # Obtém as informações do fiador da janela e as armazena nos atributos correspondentes
        self.nome = janela.values['nome_fiador'].title()
        self.cpf = janela.values['cpf_fiador']
        self.rg = janela.values['rg_fiador']
        self.cel = janela.values['cel_fiador']
        self.end = janela.values['end_fiador'].title()
        self.estado_civil = janela.values['estado_civil_fiador']
        self.nacionalidade = janela.values['nacionalidade_fiador'].title()
        self.botao = janela.values['botao']

# Classe Data
class Data:
    meses_do_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    def __init__(self):
        # Obtém a data atual e extrai dia, mês e ano
        self.dia = str(datetime.now().day)
        self.mes = str(datetime.now().month)
        # Obtém o nome do mês correspondente
        self.mes_ext = self.meses_do_ano[datetime.now().month - 1]
        self.ano = str(datetime.now().year)
        # Calcula o ano de vencimento (3 anos a partir do ano atual)
        self.ano_venc = str(int(self.ano) + 3)


