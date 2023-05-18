from utils.dados_contrato import Ap, Locatario, Fiador, Data
from configuration.configuration import Contrato
from utils.cpf_cnpj import Documentos

# Instanciando objetos e obtendo informações da janela
contrato = Contrato()  # Instância da classe Contrato
ap = Ap()  # Instância da classe Ap
locatario = Locatario()  # Instância da classe Locatario
fiador = Fiador()  # Instância da classe Fiador
data = Data()  # Instância da classe Data

# Verifica se o botão do fiador foi acionado para determinar o caminho do modelo de contrato
if fiador.botao:
    caminho = "docs\modelo_edit.docx"
    vaidador_cpf_locatario = Documentos.Valida_doc(locatario.cpf)
    referencia = {
        # Dicionário com os códigos e valores a serem substituídos no contrato
    }
else:
    caminho = 'docs\modelo_edit - fiador.docx'
    vaidador_cpf_fiador = Documentos.Valida_doc(fiador.cpf)
    vaidador_cpf_locatario = Documentos.Valida_doc(locatario.cpf)
    referencia = {
        # Dicionário com os códigos e valores a serem substituídos no contrato
    }

# Lê o documento de contrato existente
contrato.read_doc(caminho)

# Itera sobre os parágrafos do contrato
for paragrafo in contrato.documento.paragraphs:
    for codigo in referencia:
        valor = referencia[codigo]
        # Substitui os códigos pelos valores correspondentes no parágrafo atual
        paragrafo.text = paragrafo.text.replace(codigo, valor)

# Salva o documento do contrato
contrato.save_doc(ap.ap, locatario.nome, ap.ap)

# Converte o documento do contrato para PDF
contrato.convert_to_pdf(ap.ap, locatario.nome, ap.ap)
