# 5.	Construir um programa que leia o salário bruto e o sexo de um funcionário. 
# Se o sexo for “M” (masculino), calcular, armazenar e imprimir um desconto de 5% e o 
# salário líquido, caso contrário, calcular, 
# armazenar e imprimir um desconto de 3% e o salário líquido.

nome = input('Qual seu nome:')
sexo = input('(M) ou (F)')
salario_bruto = float(input('Digite seu salario bruto : '))

desc_5 = salario_bruto * 5/100
desc_3 = salario_bruto * 3/100

if sexo =='M' or 'm':
    salario_liquido = salario_bruto - desc_5
    print('O salario final é {}'.format(salario_liquido))

elif sexo == 'F' or 'f' :
    salario_liquido = salario_bruto - desc_3
    print('O salario final é {}'.format(salario_liquido))   
else:
    print('Valor Invalido!')    