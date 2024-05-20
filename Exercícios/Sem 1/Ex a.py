import random
import time

Rodada = 1
Jogadas = ('pedra', 'papel', 'tesoura')
Placar_Jog = 0
Placar_PC = 0
Placar = f'{Placar_Jog}x{Placar_PC}'

print('Pedra, Papel ou Tesoura: Melhor de 5')
time.sleep(1)

while Rodada <= 5:
    if Placar_Jog >= 3 or Placar_PC>= 3:
        break
    #Qual a rodada e quantas ganhou de 5:
    print()
    print(f'Rodada {Rodada}   Placar: {Placar}')
    time.sleep(1)

    #Jogador:
    Jogador = input('Escolha pedra, papel ou tesoura: ')
    if Jogador != 'pedra' and Jogador != 'papel' and Jogador != 'tesoura':
        time.sleep(1)
        print()
        print('Jogada não identificada, tente de novo. Obs: as jogadas são "case sensitive" e não precisam de pontuação.')
        time.sleep(1)
        print()
        continue
    else:
        print(f'Jogador: {Jogador}')
    time.sleep(.5)

    #Computador:
    Computador = random.choice(Jogadas)
    print(f'Computador = {Computador}')
    print()

    #Rodada zerada:
    if Jogador == Computador:
        time.sleep(1)
        print('Empate, rodada zerada.')
        time.sleep(1)
        print()
        continue

    #Placar e Próxima Rodada:
    if Jogador == 'pedra':
        if Computador == 'papel':
            time.sleep(1)
            print('Ponto para o computador!')
            Rodada += 1
            Placar_PC += 1
        elif Computador == 'tesoura':
            time.sleep(1)
            print('Ponto para o jogador!')
            Rodada += 1
            Placar_Jog += 1
    
    elif Jogador == 'papel':
        if Computador == 'pedra':
            time.sleep(1)
            print('Ponto para o jogador!')
            Rodada += 1
            Placar_Jog += 1
        elif Computador == 'tesoura':
            time.sleep(1)
            print('Ponto para o computador!')
            Rodada += 1
            Placar_PC += 1

    elif Jogador == 'tesoura':
        if Computador == 'pedra':
            time.sleep(1)
            print('Ponto para o computador!')
            Rodada += 1
            Placar_PC += 1
        elif Computador == 'papel':
            time.sleep(1)
            print('Ponto para o jogador!')
            Rodada += 1
            Placar_Jog += 1
    
    Placar = f'{Placar_Jog}x{Placar_PC}'

    time.sleep(1)
    print()

print()

print(f'Placar final: {Placar}')
time.sleep(1)

print()

if Placar_Jog >=3:
    print('Parabéns!! Você Ganhou >D')

else:
    print('Não foi dessa vez :\'(')