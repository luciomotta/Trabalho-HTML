class PessoaFisica:

    def ___init___(self, nome, endereco, cpf, telefone):
        self.__nome = nome.captalize.title()  # Tornar o atributo privado #Deixas as 1º letras MAIUSC
        self.__endereco = endereco
        self.__cpf = cpf
        self.__telefone = telefone

    @property
    def get_nome(self):
        return self.__nome.title()

    @nome.setter
    def set_nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def set_endereco(self, endereco):
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__endereco

    @cpf.setter
    def set_cpf(self, cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def set_cpf(self, telefone):
        self.__telefone = telefone


marcelo = PessoaFisica("Marcelo Soares", "Rua 20", "056.938.331-51", "61993517017")
print(marcelo.telefone)
marcelo.set_nome("Lucio")
