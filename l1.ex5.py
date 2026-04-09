preco = float(input("Digite o preço da mercadoria: R$ "))
desconto_perc = float(input("Digite o percentual de desconto: "))

valor_desconto = preco * (desconto_perc / 100)
preco_pagar = preco - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final a pagar: R$ {preco_pagar:.2f}")
