'''
O método atual para transformar funções e métodos (por exemplo, declarando-os
como classes ou métodos estáticos) é complicado e pode levar a código que é
difícil de entender. Idealmente, essas transformações devem ser feitas no
mesmo ponto do código onde a própria declaração é feita. Esta PEP introduz
uma nova sintaxe para transformações de uma função ou declaração de métodos.
'''

def decorator(funcao):
    def wrapper():
        print ("Estou antes da execução da função passada como argumento")
        funcao()
        print ("Estou depois da execução da função passada como argumento")

    return wrapper

def outra_funcao():
    print ("Sou um belo argumento!")

funcao_decorada = decorator(outra_funcao)
funcao_decorada()