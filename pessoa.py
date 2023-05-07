class Pessoa:
    def __init__(self, nome, email, senha, idade):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

    def get_idade(self):
        return  self.__idade

    def __str__(self):
        pass


cadastros = {}
