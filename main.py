#DESAFIO 58

'''
    MELHORE O JOGO DO DESAFIO 028, ONDE O COMPUTADOR VAI 'PENSAR' EM UM NUMERO ENTRE 0 E 10.
    SÓ QUE AGORA O JOGADOR VAI TENTAR ADVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES
    FORAM NECESSÁRIOS PRA VENCER!
'''
import time
from random import randint

computador = randint(0, 10)

print('=-=' * 20)
print('Vou pensar em um número entre 0 e 10! Tente adivinhar...')
print('=-=' * 20)

time.sleep(1)

tentativas = 0
acertou = False

while not acertou:
    jogador = int(input('Em que número você pensou? '))
    tentativas += 1

    if jogador == computador:
        acertou = True
        print(f'🎉 Acertou! O número era {computador}')
    else:
        if jogador < computador:
            print(f'Um pouquinho a mais... Você disse {jogador} e errou ❌! Tente novamente!')
        else:
            print(f'Um pouquinho a menos... Você disse {jogador} e errou ❌! Tente novamente!')

    time.sleep(1)

print(f'Você precisou de {tentativas} tentativas para vencer!')
