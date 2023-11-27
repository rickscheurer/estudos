import random
from time import sleep

print('-=-' * 8)
print('Jogo da adivinhação')
print('-=-' * 8)

numeros = random.randint(0, 21)
chances = 3
rodadas = 1

while rodadas <= 3: 
    print('Rodada', rodadas, 'de', chances)
    tentativa_str = input('Escolha um numero de 1 a 20: ')
    tentativa = int(tentativa_str)
    print('Você digitou..')
    sleep(1)
    print(tentativa)
    if tentativa == numeros:
        print('Você acertou')

    else:
        if tentativa > numeros:
            print('Você errou!')

        elif tentativa < numeros:
            print('Você errou!')

    if tentativa == numeros:
        rodadas = rodadas + 5
    else: 
        rodadas = rodadas + 1
    
print('Obrigado por jogar nosso jogo!')
