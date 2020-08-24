class Carro:
    def __init__(self, nome, marca, modelo, cor, preço):
        self.__nome = nome
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__preço = preço

    def __str__(self):
        return (f" \
            Nome:{self.__nome}\n \
            Marca:{self.__marca}\n \
            Modelo:{self.__modelo}\n \
            Cor:{self.__cor}\n \
            Preço:{self.__preço}" 
        )

class BuilderCarro:
    def __init__(self):
        self.__nome = None
        self.__marca = None
        self.__modelo = None
        self.__cor = None
        self.__preço = None

    def com_nome(self, nome):
        self.__nome = nome
        return self

    def com_marca(self, marca):
        self.__marca = marca
        return self
    
    def com_modelo(self, modelo):
        self.__modelo = modelo
        return self

    def com_cor(self, cor):
        self.__cor = cor
        return self

    def com_preço(self, preço):
        self.__preço = preço
        return self

    def construa(self):
        if self.__nome == None:
            raise Exception("Precisa de um nome!")
        if self.__marca == None:
            raise Exception("Precisa de uma marca!")
        if self.__modelo == None:
            raise Exception("Precisa de um modelo!")
        if self.__cor == None:
            self.__cor = "Preto"
        if self.__preço == None:
            self.__preço = 0.0

        return Carro(nome = self.__nome, marca = self.__marca, modelo = self.__modelo, cor = self.__cor, preço = self.__preço)
    
if __name__ == "__main__":
    carro = Carro("Celta", "Chevrolet", "Ret", "Azul-Marinho", 10.000)
    print(carro)

    carro2 = (BuilderCarro()
            .com_nome("Onix")
            .com_marca("Chevrolet")
            .com_modelo("Sedan")
            .com_preço(1000.0)
            .construa())
    print(carro2)