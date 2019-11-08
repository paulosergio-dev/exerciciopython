# 10. Tendo como dados de entrada a altura e o sexo de uma pessoa (M - masculino e F - feminino), 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:  
#- para homens: (72.7*h)-58
#- para mulheres: (62.1*h)-44.7


sexo = int(input('Digite seu sexo: (1) Para Homem (2) Para Mulher: '))

if sexo == 1:
    alturaHomem = float(input('Digite sua altura:'))
    pesoHomem = 72.7 * alturaHomem
    pesoRealHomem = pesoHomem - 58  
    print('Seu peso ideal é : {:.1f} Quilos'.format(pesoRealHomem,))

if sexo == 2:
    alturaMulher = float(input('Digite sua altura:'))
    pesoMulher = 62.1 * alturaMulher
    pesoRealMulher = pesoMulher - 44.7 
    print('Seu peso ideal é : {:.1f} Quilos'.format(pesoRealMulher))   