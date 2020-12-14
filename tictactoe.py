table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turn = 0
player1 = 'X'
player2 = 'O'

def grade():
    print('%s | %s | %s' % (table[0], table[1], table[2]))
    print('--+---+--')
    print('%s | %s | %s' % (table[3], table[4], table[5]))
    print('--+---+--')
    print('%s | %s | %s' % (table[6], table[7], table[8]))

def jogador1():
    escolha = input('Player 1, escolha uma casa: ')
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha not in table:
            print("Escolha outro número!")
            jogador1()
        if escolha <= 10:
            table[escolha - 1] = player1
            grade()
            print('\nTurno: ' + str(turn))
            vencer()
            turno()
            jogador2()
        else:
            print('Escolha um número de 1 a 9')
            jogador1()
    elif escolha.isalnum or escolha.isspace:
        print('Escolha um número de 1 a 9')
        jogador1()

def jogador2():
    escolha = input('Player 2, escolha uma casa: ')
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha not in table:
            print("Escolha outro numero!")
            jogador2()
        table[escolha - 1] = player2
        grade()
        print('\nTurno: ' + str(turn))
        vencer()
        turno()
        jogador1()
    elif escolha.isalnum or escolha.isspace():
        print('Escolha um número de 1 a 9')
        jogador2()

def vencer():
    if (table[0] == player1 and table[1] == player1 and table[2] == player1) or (table[3] == player1 and table[4] == player1 and table[5] == player1)\
    or (table[6] == player1 and table[7] == player1 and table[8] == player1) or (table[0] == player1 and table[3] == player1 and table[6] == player1)\
    or (table[1] == player1 and table[4] == player1 and table[7] == player1) or (table[2] == player1 and table[5] == player1 and table[8] == player1)\
    or (table[2] == player1 and table[4] == player1 and table[6] == player1) or (table[0] == player1 and table[4] == player1 and table[8] == player1):
        print("Player 1 venceu!")
        exit()
    if (table[0] == player2 and table[1] == player2 and table[2] == player2) or (table[3] == player2 and table[4] == player2 and table[5] == player2)\
    or (table[6] == player2 and table[7] == player2 and table[8] == player2) or (table[0] == player2 and table[3] == player2 and table[6] == player2)\
    or (table[1] == player2 and table[4] == player2 and table[7] == player2) or (table[2] == player2 and table[5] == player2 and table[8] == player2)\
    or (table[2] == player2 and table[4] == player2 and table[6] == player2) or (table[0] == player2 and table[4] == player2 and table[8] == player2):
        print("PLayer 2 venceu!")
        exit()
    elif turn == 9:
        print("\nEmpate!")
        exit()

def turno():
    global turn
    turn = turn + 1

grade()
print('\nTurno: ' + str(turn))
turno()
jogador1()
