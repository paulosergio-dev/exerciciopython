# 3.	Construir um programa que leia as 2 notas de um aluno e que calcule, 
# armazene e imprima a média. Se a média for maior ou igual a 7, imprimir “Aprovado”, 
# caso contrário, realizar a leitura de uma terceira nota, 
# que terá peso 2 e calcular, armazenar e imprimir uma nova média. 
# Se a nova média for maior ou igual a 6, imprimir “Aprovado”, caso contrário, imprimir “Reprovado”.

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua 2° nota: '))

media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

if media > 7:
  print('Aluno Aprovado')
elif media <= 6.9:
    nota3 = float(input('Digite sua 3° nota: '))
    novamedia = (nota1 + nota2) + (nota3 * 2) / 2 
    
    if novamedia > 7:
      print('O aluno está APROVADO!')
    else:
      print('O aluno está REPROVADO')