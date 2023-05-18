import PySimpleGUI as sg



class Window:
    def __init__(self):
        sg.theme('Black')
        #CRIA O LAY OUT DA JANELA, CADA LISTA É IGUAL A UMA LINHA NA JANELA 
        layout = [
            [sg.Text("DADOS APARTAMENTO")],
            [sg.Text("Número:", size=7), sg.InputText(size=10, key='ap_num')],
            [sg.Text("Valor: R$", size=7), sg.InputText(size=10, key='ap_valor')],
                

            [sg.Text("DADOS LOCATARIO")],
            [sg.Text("Nome:", size=10), sg.InputText(size=30, key='nome_loc')],
            [sg.Text("RG:", size=10), sg.InputText(size=30, key='rg_loc')],
            [sg.Text("CPF:", size=10), sg.InputText(size=30, key='cpf_loc')],
            [sg.Text("Nacionalidade:", size=10), sg.InputText(size=30, key='nacionalidade_loc')],
            [sg.Text("Cel:", size=10), sg.InputText(size=30, key='cel_loc')],

            [sg.Text("DADOS FIADOR")],
            [sg.Checkbox("Não foi necessário",key='botao')],
            [sg.Text("Nome:", size=10), sg.InputText(size=30, key='nome_fiador')],
            [sg.Text("RG:", size=10), sg.InputText(size=30, key='rg_fiador')],
            [sg.Text("CPF:", size=10), sg.InputText(size=30, key='cpf_fiador')],
            [sg.Text("Endereço:", size=10), sg.InputText(size=30, key='end_fiador')],
            [sg.Text("Estado Civil:", size=10), sg.InputText(size=30, key='estado_civil_fiador')],
            [sg.Text("Nacionalidade:", size=10), sg.InputText(size=30, key='nacionalidade_fiador')],
            [sg.Text("Cel:", size=10), sg.InputText(size=30, key='cel_fiador')],

            [sg.Button("CRIAR CONTARTO",button_color='Green')]
        ]
        #CRIA A JANELA COM BASE NO LAYOT 
        janela = sg.Window("DADOS CONTARTO", layout,)

        #DEIXA A JANELA ABERTA PARA A INTERAÇÃO COM O USUARIO 
        self.buttn, self.values = janela.Read()


