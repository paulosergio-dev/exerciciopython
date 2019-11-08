# 4 Construir um programa leia um número inteiro entre 1 e 7 e 
# imprima o nome do dia da semana correspondente ao número, 
# caso o número esteja fora do intervalo entre 1 e 7, imprimir “Dia Inválido”.


dia1 = ("Domingo");
dia2 = ("SegundaFeira");
dia3 = ("TerçaFeira");
dia4 = ("QuartaFeira");
dia5 = ("QuintaFeira");
dia6 = ("SextaFeira");
dia7 = ("Sabado");
diainv = ("Dia Inválido");

num = int(input('Digite um numero:'))

if num == 1:
    print('Hoje é {}'.format(dia1))
elif num == 2:
    print('Hoje é {}'.format(dia2))
elif num == 3:
    print('Hoje é {}'.format(dia3))    
elif num == 4:
    print('Hoje é {}'.format(dia4))
elif num == 5:
    print('Hoje é {}'.format(dia5)) 
elif num == 6: 
    print('Hoje é {}'.format(dia6))
elif num == 7:
    print('Hoje é {}'.format(dia7))   
else: 
    num <0 and num >7
    print('{}'.format(diainv)) 

