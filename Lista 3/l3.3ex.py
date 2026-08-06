populacao_A = 80000
taxa_A = 0.03  # 3% de crescimento
populacao_B = 200000
taxa_B = 0.015 # 1.5% de crescimento
anos = 0

while populacao_A < populacao_B:
    # Adiciona o crescimento do ano atual à população existente
    populacao_A += populacao_A * taxa_A
    populacao_B += populacao_B * taxa_B
    anos += 1

print(f"Serão necessários {anos} anos para a população do país A ultrapassar ou igualar a população do país B.")
