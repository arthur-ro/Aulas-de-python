from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador 'PENSAR'
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente aidvinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensie? ')) # Jogaodr tenta adivinhar
print('PROCESSANDO...')
sleep(0)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Pensei no {} e não no {}.'.format(computador, jogador))


