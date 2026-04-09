m = int(input('Digite a quantidade de minutos: '))
if m<200:
    v1 = m*0.20
    print (f'O valor é R${v1}')
elif m<=400:
     v2 = m*0.18
     print (f'O valor é R${v2}')
else:
    v3 = m*0.15
    print (f'O valor é R${v3}') 
