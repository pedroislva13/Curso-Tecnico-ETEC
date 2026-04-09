d = int(input("Quantidade de dias: "))
h = int(input("Quantidade de horas: "))
m = int(input("Quantidade de minutos: "))
s = int(input("Quantidade de segundos: "))

# 1 dia = 24h, 1h = 60min, 1min = 60seg
total_segundos = (d * 24 * 3600) + (h * 3600) + (m * 60) + s
