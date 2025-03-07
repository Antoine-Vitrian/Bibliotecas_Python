# Programa Principal
import operacoes
# or from operacoes import fatorial, dobro, quadrado
# deste modo não é necessário escrever "operacoes.""

numero = int(input("Calcule o fatorial de um número: "))
operacoes.fatorial(numero)
operacoes.dobro(numero)
operacoes.quadrado(numero)