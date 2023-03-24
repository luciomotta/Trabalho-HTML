from signal import pause


class Pessoa:
    #----> Fora de def, p\ não da erro e iniciar fora da class de inicialização
    def __init__(self, nome, endereco, telefone):
        self.registrado = True
        self._nome = nome.title()  # Tornar o atributo privado __ # Tittle torna letyraas aiscula
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome
        pass

    @nome.setter
    def set_nome(self, nome):
        self._nome = nome.title()  # Garantir fiar maisula tanto na hr que for craida..
        pass

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def set_endereco(self, endereco):
        self._endereco = endereco

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def set_telefone(self, telefone):
        self._telefone = telefone

class PessoaFisica(Pessoa):

    def __init__(self, nome, endereco, cpf, telefone):
        super().__init__(nome, endereco, telefone)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def set_cpf(self, cpf):
        self.__cpf = cpf

marcelo = PessoaFisica("Marcelo Soares", "Rua 20", "056.938.331-51", "61993517017")
print("_"*80,"!")
print(f"Úsuario: {marcelo.nome}\nCPF: {marcelo.cpf} Está registrado -->{marcelo.registrado}")
print("_" * 80, "!")

#--------------------
print("$"*25,"Pessoa Fisica e cima - Pessoa Juricia e baixo", "$"*25 )
#--------------------

class PessoaJuridica(Pessoa):

    def __init__(self, nome, endereco, cnpj, telefone):
        super().__init__(nome, endereco, telefone)
        self.__cnpj = cnpj

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj

marcelo = PessoaJuridica("Tulio Silva", "NULL", "38.708.851-0001", "61993517017")
print("_" * 80, "!")
print(marcelo.nome,"------\CNPJ/---> ", marcelo.cnpj)
print(f"Endereço de Entrega:{marcelo.endereco}")
print("_" * 80, "!")

#APLICAÇÃO WEB dJANGO
#Data Base PostL ----> Ter contato com outro banco de dados
