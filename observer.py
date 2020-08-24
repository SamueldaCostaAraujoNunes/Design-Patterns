class Variaveis:
    def __init__(self, x, y, observers = []):
        self.x = x
        self.y = y
        for observador in observers:
            print(f'A operação {observador.__name__} retornou {observador(x, y)}')


class Operacoes:
    def soma(self, x, y):
        return x + y

    def subtrai(self, x, y):
        return x - y

    def multiplica(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def get_functions(self):
        return [self.soma, self.subtrai, self.multiplica, self.divide]

variaveis = Variaveis(1, 1 , Operacoes().get_functions())