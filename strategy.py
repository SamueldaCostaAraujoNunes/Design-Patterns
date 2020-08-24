'''
Definir uma família de algoritmos, encapsular cada uma delas e torná-las
intercambiáveis. Strategy permite que o algoritmo varie independentemente
dos clientes que o utilizam
'''

def calculadora(x, y, strategy):
    return strategy(x, y)

def soma(x, y):
    return x + y

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    return x / y

lista_de_funcoes = [soma, subtrai, multiplica, divide]
x, y = 8, 23


for operacao in lista_de_funcoes:
    resultado = calculadora(x, y, operacao)
    print(f'A operação {operacao.__name__} retornou {resultado}')