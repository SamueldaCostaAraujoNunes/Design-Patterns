from abc import ABC, abstractmethod
 
class Calculo(ABC):
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()
    
    @abstractmethod
    def calcular(self):
        pass

class Soma(Calculo):
    def calcular(self):
        return self.x + self.y

class Subtrai(Calculo):
    def calcular(self):
        return self.x - self.y

class Multiplica(Calculo):
    def calcular(self):
        return self.x * self.y

class Divide(Calculo):
    def calcular(self):
        return self.x / self.y

class Potencia(Calculo):
    def calcular(self):
        return self.x ** self.y
