#12.	Fazer um algoritmo para calcular a contribuição ao INSS, IR e a associação 
# de funcionários a partir do salário bruto, que é dado de entrada. 
# As taxas sobre o salário bruto são as seguintes: 
#•	INSS - 10%
#•	IR - 25%
#•	Sindicato - 0.5 %
# O programa deve imprimir as contribuições e o valor do salário líquido.


salario = float(input('Qual é o seu salário ? - > '))
novoSalario = salario - (salario * 10/100) - (salario * 25/100) - (salario * 0.5/100)
print('Seu salário atualizado conforme as contribuições é {} : '.format(novoSalario))