 area = float(input("Digite o tamanho em metros quadrados (m²) da área a ser pintada: "))

litros = area / 3.0

lata = 18.0
preco = 80.00

quantidade = (litros / lata)

preco = quantidade * preco

print(f"Para pintar {area} m², você precisará de {litros} litros de tinta.")
print(f"Quantidade de latas a comprar: {quantidade}")
print(f"Preço total: R$ {preco}")
