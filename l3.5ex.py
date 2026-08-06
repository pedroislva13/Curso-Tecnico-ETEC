num1 = int(input("Informe o primeiro número inteiro positivo: "))
num2 = int(input("Informe o segundo número inteiro positivo: "))

# Guarda os valores originais para exibir no print final
a, b = num1, num2 

# Algoritmo de Euclides
while num2 != 0:
    resto = num1 % num2
    num1 = num2
    num2 = resto

print(f"O Máximo Divisor Comum (MDC) entre {a} e {b} é: {num1}")
