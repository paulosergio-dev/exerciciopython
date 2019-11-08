'''
    Elabore um programa que leia o salário de um empregado e com base na tabela abaixo calcule
    e informe sua gratificação e seu salário líquido.
'''

salario = float(input("Informe o salário: "))

if salario < 2000:
    aumento = 5
    resultado = salario + (salario * aumento/100)
    print("Sua gratificação é de 5%")
    print("Seu salário líquido é de: {}".format(resultado))
elif salario > 2000 and salario < 2500:
    aumento = 10
    resultado = salario + (salario * aumento/100)
    print("Sua gratificação é de 10%")
    print("Seu salário líquido é de: {}".format(resultado))
elif salario > 2500 and salario < 3000:
    aumento = 15
    resultado = salario + (salario * aumento/100)
    print("Sua gratificação é de 15%")
    print("Seu salário líquido é de: {}".format(resultado))
else:
    aumento = 20
    resultado = salario + (salario * aumento/100)
    print("Sua gratificação é de 20%")
    print("Seu salário líquido é de: {}".format(resultado))