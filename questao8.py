# 8.	Sejam P(x1,y1) e Q(x2,y2) dois pontos quaisquer do plano. 
# A sua distância é dada por: 
#D =    (x2 – x1)2 + (y2 – y1)2
# Elabore um programa que leia as coordenadas dos pontos “P” e “Q”, 
# calcule e escreva sua distância.

import math

x1 = int(input("Na coordenada P, qual a posição de X1? "))
y1 = int(input("Na coordenada P, qual a posição de Y1? "))

x2 = int(input("Na coordenada Q, qual a posição de X2? "))
y2 = int(input("Na coordenada Q, qual a posição de Y2? "))

d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print("A distância é: {:.1f}".format(d))
