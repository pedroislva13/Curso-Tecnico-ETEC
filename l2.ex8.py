import math

area = float(input("Digite o tamanho em metros quadrados (m²) da área a ser pintada: "))

litros_necessarios = area / 3.0

capacidade_lata = 18.0
preco_lata = 80.00

quantidade_latas = math.ceil(litros_necessarios / capacidade_lata)

preco_total = quantidade_latas * preco_lata

print(f"\nPara pintar {area} m², você precisará de {litros_necessarios:.2f} litros de tinta.")
print(f"Quantidade de latas a comprar: {quantidade_latas}")
print(f"Preço total: R$ {preco_total:.2f}")
