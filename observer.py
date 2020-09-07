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
                print(f'A operação {observador.__name__}, com as variaveis {self.__x} e {self.__y}, retornou {observador(self.__x, self.__y)}')
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

def soma(x, y):
    return x + y

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

variaveis = Variaveis(65, 12)
variaveis.notify_observers()

variaveis.register_observer(soma)
variaveis.notify_observers()

variaveis.register_observer(subtrai)

variaveis.x = 23

variaveis.register_observer(multiplica)
variaveis.register_observer(divide)

variaveis.y = 45

variaveis.unregister_observer(multiplica)

variaveis.x = 1

variaveis.register_observer(power)

variaveis.x = 6
