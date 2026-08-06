n = int(input("Qual termo de Fibonacci você deseja calcular? "))

if n <= 0:
    print("Por favor, insira um número inteiro positivo.")
elif n == 1 or n == 2:
    resultado = 1
    print(f"O termo F{n} da sequência de Fibonacci é: {resultado}")
else:
    a = 1  # Representa F(n-2)
    b = 1  # Representa F(n-1)
    
    for i in range(3, n + 1):
        resultado = a + b
        a = b
        b = resultado
        
    print(f"O termo F{n} da sequência de Fibonacci é: {resultado}")
