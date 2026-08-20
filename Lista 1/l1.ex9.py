km_percorridos = float(input("Quantidade de km percorridos: "))
dias_alugados = int(input("Quantidade de dias alugados: "))

preco_dias = dias_alugados * 60.00
preco_km = km_percorridos * 0.15
total_pagar = preco_dias + preco_km

print(f"O preço total a pagar é: R$ {total_pagar:.2f}")
