import random
lista = []
for i in range(10):
    numero_sorteado = random.randint(1, 100)
    lista.append(numero_sorteado)
maior = lista[0]
menor = lista[0]
for numero in lista:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("A lista completa é: ", lista)
print("O maior número é: ", maior)
print("O menor número é: ", menor)
