from calculadora import Soma, Subtrai, Multiplica, Divide, Potencia

class Variaveis:
    def __init__(self, x, y, observers = []):
        self.__x = x
        self.__y = y
        self.__observers = observers

    def register_observer(self, function):
        self.__observers.append(function)

    def unregister_observer(self, function):
        self.__observers.remove(function)

    def notify_observers(self):
        if self.__observers:
            for observador in self.__observers:
                print(f'A operação {observador.__name__}, com as variaveis {self.__x} e {self.__y}, retornou {observador(self.__x, self.__y).calcular()}')
            print("")
        else:
            print("Ainda não existem observers!!")

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x
        self.notify_observers()
    
    @y.setter
    def y(self, y):
        self.__y = y
        self.notify_observers()


if __name__ == "__main__":
    variaveis = Variaveis(65, 12)
    variaveis.notify_observers()

    variaveis.register_observer(Soma)
    variaveis.notify_observers()

    variaveis.register_observer(Subtrai)

    variaveis.x = 23

    variaveis.register_observer(Multiplica)
    variaveis.register_observer(Divide)

    variaveis.y = 45

    variaveis.unregister_observer(Multiplica)

    variaveis.x = 1

    variaveis.register_observer(Potencia)

    variaveis.x = 6
