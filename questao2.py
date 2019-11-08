#    programa 2 Construir um programa que leia a quantidade de alunos do sexo masculino, do sexo feminino e
#    a quantidade de alunos aprovados de uma turma e calcule, armazene e imprima o total de
 #   alunos e a porcentagem de alunos do sexo masculino, do sexo feminino e a porcentagem de
  #  alunos aprovados.
#

qtdalunoM = int(input("Quantidade de alunos do sexo masculino: "))
qtdalunoF = int(input("Quantidade de alunos do sexo feminino: "))

qtdalunoAprovados = int(input("Quantidade de alunos aprovados: "))

totalAlunos = qtdalunoF + qtdalunoM

porcentagemM = ((qtdalunoM * 100)/totalAlunos)
porcentagemF = ((qtdalunoF * 100)/totalAlunos)
porcentagemAprovados = (totalAlunos * qtdalunoAprovados/100)

print("O total de alunos da turma é: {}".format(totalAlunos))
print("Porcentagem de alunos do sexo masculino: {:.2f}%".format(porcentagemM))
print("Porcentagem de alunos do sexo feminino: {:.2f}%".format(porcentagemF))
print("Porcentagem de alunos aprovados na turma: {:.2f}%".format(porcentagemAprovados))
