peso = float(input("Digite a quantidade de quilos de peixe pescados: "))
limite = 50.0
valor_multa_por_quilo = 4.00

if peso > limite:
    excesso = peso - limite
    multa = excesso * valor_multa_por_quilo
else:
    excesso = 0.0
    multa = 0.0

print(f"Excesso de peso: {excesso:.2f} kg")
print(f"Valor da multa a pagar: R$ {multa:.2f}")
