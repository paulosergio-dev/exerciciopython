# 13.	Faça um programa que leia três números diferentes e informe o maior deles. 
# Se os números digitados não forem diferentes o programa deve gerar a mensagem: 
# “Os valores digitados não são diferentes”.

n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
n3 = int(input('Terceiro valor:'))

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
  

print('O maior valor digitado é: {}'.format(maior))