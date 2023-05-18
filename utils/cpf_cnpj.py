from validate_docbr import CPF, CNPJ

class Documentos:
    # O decorator @staticmethod é usado para definir um método estático dentro da classe.
    # Métodos estáticos não exigem uma referência à instância da classe (self) como o primeiro argumento.
    # Eles são semelhantes a funções comuns, mas residem no escopo da classe.
    @staticmethod
    def Valida_doc(documento):
        # Verifica o comprimento do documento para determinar se é CPF ou CNPJ.
        if len(documento) == 11:
            return DocCpf(documento)
        if len(documento) == 14:
            return  DocCnpj(documento)
        else:
            raise ValueError('Documento inexistente!')

class DocCpf:
    def __init__(self, documento):
        # Verifica se o CPF fornecido é válido usando o método 'valida'
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido')  # Levanta uma exceção de valor inválido se o CPF não for válido

    def valida(self, cpf):
        validador = CPF()  # Instancia um objeto da classe 'CPF' do módulo 'validate_docbr'
        return validador.validate(cpf)  # Utiliza o método 'validate' para validar o CPF fornecido

    def format(self):
        mascara = CPF()  # Instancia um objeto da classe 'CPF' do módulo 'validate_docbr'
        return mascara.mask(self.cpf)  # Utiliza o método 'mask' para aplicar uma máscara ao CPF e retornar uma representação formatada

    def __str__(self):
        return self.format()  # Retorna o CPF formatado ao converter o objeto para uma string


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido')

    def valida(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format()
