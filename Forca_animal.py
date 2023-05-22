'''
import random

#Palavra oculta
animais = ['maritaca','cachorro', 'gato', 'papagaio', 'coelho', 'hamster']

animais = random.choice(animais)

palavra_oculta = ''

for letra in animais:
    palavra_oculta += '*'

palavra_oculta = str (input('Advinhe o animal da forca: '))

if animais == palavra_oculta:
    print('voce acertou o animal e: ', animais)
else:
    print('vc errou')
    '''

import random

# lista de palavras
animais = ['maritaca', 'cachorro', 'gato', 'papagaio', 'coelho', 'hamster']

# escolhe uma palavra aleatoriamente
palavra_original = random.choice(animais)

# converte a palavra original em uma palavra oculta
palavra_oculta = '*' * len(palavra_original)

# número máximo de tentativas
max_tentativas = 6

# lista de letras já usadas
letras_usadas = []

# loop principal do jogo
while max_tentativas > 0 and palavra_oculta != palavra_original:
    # exibe a palavra oculta e as letras já usadas
    print('Palavra:', palavra_oculta)
    print('Letras usadas:', letras_usadas)

    # pede ao usuário para adivinhar uma letra
    letra = input('Digite uma letra: ')

    # verifica se a letra já foi usada
    if letra in letras_usadas:
        print('Você já usou essa letra. Tente novamente.')
    else:
        # adiciona a letra à lista de letras usadas
        letras_usadas.append(letra)

        # verifica se a letra está na palavra original
        if letra in palavra_original:
            # atualiza a palavra oculta com a letra adivinhada
            nova_palavra_oculta = ''
            for i in range(len(palavra_original)):
                if palavra_original[i] == letra:
                    nova_palavra_oculta += letra
                else:
                    nova_palavra_oculta += palavra_oculta[i]
            palavra_oculta = nova_palavra_oculta
            print('Boa! A letra', letra, 'está na palavra.')
        else:
            print('Ops! A letra', letra, 'não está na palavra.')
            max_tentativas -= 1

# verifica se o jogador ganhou ou perdeu o jogo
if palavra_oculta == palavra_original:
    print('Parabéns! Você acertou a palavra ', palavra_original)
else:
    print('Que pena! A palavra era ', palavra_original)


