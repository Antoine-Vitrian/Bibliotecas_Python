# print("Hello World")

# x = input("Digite seu nome: ")

# print("Olá", x)

# Criar uma função que calcula o fatorial de um numero

def fatorial(numero):
    fatorial = 1
    for i in range(1, numero+1):
        fatorial = fatorial * i
    return print(fatorial)

def dobro(numero):
    return print(numero*2)

def quadrado(numero):
    return print("O quadrado é igual a", numero ** 2)

numero = int(input("Calcule o fatorial de um número: "))
fatorial(numero)
dobro(numero)
quadrado(numero)