class Usuario:

    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha

    def autenticar(self):
        return self.__nome == "Samuel" and self.__senha == "mypassword"

class UsuarioFactory():
    def criar_user(self):
        return Usuario("Samuel", "mypassword")

print(UsuarioFactory().criar_user().autenticar())