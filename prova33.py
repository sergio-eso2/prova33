numero_secreto = 9
tentativas_maximo = 3
tentativas_jogador = 0

while tentativas_jogador != numero_secreto and tentativas_maximo > 0:
    tentativas_jogador = int(input('Adivinhe o numero de 1 a 10: '))
    tentativas_maximo -= 1
    if tentativas_jogador != numero_secreto:
        print('Ainda nao, resposta incorreta, tente novamente: ')

if tentativas_jogador == numero_secreto:
    print('Parabens, resposta correta!!!') 
else:
    print(f'Suas tentativas acabaram, o numero secreto era: {numero_secreto}')           


    
    

        
        


    