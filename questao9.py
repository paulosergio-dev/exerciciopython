#9.	O cardápio de uma lanchonete é o seguinte: 
#Especificação	 Código	Preço
#Cachorro quente	100	5,20
#Hambúrguer	        101	5,20
#Cheeseburguer   	102	7,30
#Refrigerante	    103	5,00
#Escrever um algoritmo que leia o código do item pedido,
#  a quantidade e calcule o valor a ser pago por aquele lanche. 
# Considere que a cada execução somente será calculado um item.


cont = 1

while cont <= 4:
    CodigoPedido = int(input("Digite o código do pedido: "))        
    qtdPedido = int(input("Digite a quantidade: "))
    if CodigoPedido == 100:
        valorPedido = qtdPedido * 5.20
        print('Pedido : Cachorro Quente')
        print('Qauntidade {}'.format(qtdPedido))
        print('Preço: {:.2f}'.format(valorPedido))
    elif CodigoPedido == 101:    
        valorPedido = qtdPedido * 5.20
        print('Pedido : Hamburguer')
        print('Qauntidade {}'.format(qtdPedido))
        print('Preço: {:.2f}'.format(valorPedido))
    elif CodigoPedido == 102:    
        valorPedido = qtdPedido * 7.30
        print('Pedido : Cheeseburguer')
        print('Qauntidade {}'.format(qtdPedido))
        print('Preço: {:.2f}'.format(valorPedido))
    elif CodigoPedido == 103:    
        valorPedido = qtdPedido * 5.00
        print('Pedido : Refrigerante')
        print('Qauntidade {}'.format(qtdPedido))
        print('Preço: {:.2f}'.format(valorPedido))    
    else:
        print('Codigo não existente!')    