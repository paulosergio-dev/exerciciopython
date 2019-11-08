    #programa1
    #Escreva um programa que calcule a quantidade de litros de combustível gastos em uma
    #viagem, considerando que o automóvel consome 1 litro a cada 12 Km. Para obter o consumo, o
    #usuário deve fornecer o tempo gasto na viagem e a velocidade média durante a mesma. Desta
    #forma, será possível obter a distância percorrida com a seguinte fórmula DISTÂNCIA = TEMPO
    #* VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros com a fórmula
    #LITROS_USADOS = DISTÂNCIA/12. Deve ser fornecido como resposta: a velocidade média, o
    #tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.

kml = 12 
tempoGasto = int(input("Tempo gasto na viagem: "))
velMedia = int(input("Velocidade média: "))

distancia = tempoGasto * velMedia
consumo = distancia/kml

print("O velocidade média foi de: {} KM/H".format(velMedia))
print("O tempo gasto na viagem foi de: {} horas".format(tempoGasto))
print("A distância percorrida foi de: {} KM".format(distancia))
print("Quantidade de litros de combustível gastos: {} KM/L".format(consumo))
