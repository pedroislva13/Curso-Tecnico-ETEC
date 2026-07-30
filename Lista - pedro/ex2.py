import random
lista_geral = []
lista_par = []
lista_impar = []
for i in range(20):
    numero = random.randint(1, 100)
    lista_geral.append(numero)
for numero in lista_geral:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
print("Geral misturado:", lista_geral)
print("Só os Pares:", lista_par)
print("Só os Ímpares:", lista_impar)
