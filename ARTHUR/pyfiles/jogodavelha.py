
placeholder = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def verifyWinner():
    
    for i in range(1, 2):
        for j in range(2, 3):
            for c in range(0, 3):
                if placeholder[c][0] + placeholder[c][i] + placeholder[c][j] == 'xxx':
                    print('Jogador I venceu!')
                    exit()
                elif placeholder[c][0] + placeholder[c][i] + placeholder[c][j] == 'ooo':
                    print('Jogador II venceu!')
                    exit()
                elif placeholder[c][c] + placeholder[i][c] + placeholder[j][c] == 'xxx':
                    print('Jogador I venceu!')
                    exit()
                elif placeholder[c][c] + placeholder[i][c] + placeholder[j][c] == 'ooo':
                    print('Jogador II venceu!')
                    exit()
                elif placeholder[c][c] + placeholder[i][i] + placeholder[j][j] == 'xxx':
                    print('Jogador I venceu!')
                    exit()
                elif placeholder[c][c] + placeholder[i][i] + placeholder[j][j] == 'ooo':
                    print('Jogador I venceu!')
                    exit()
                elif placeholder[c][j] + placeholder[i][i] + placeholder[j][c] == 'xxx':
                    print('Jogador I venceu!')
                    exit()
                elif placeholder[c][j] + placeholder[i][i] + placeholder[j][c] == 'ooo':
                    print('Jogador II venceu!')
                    exit()
                
    a = placeholder[0][0]
    b = placeholder[0][1]
    c = placeholder[0][2]
    d = placeholder[1][0]
    e = placeholder[1][1]
    f = placeholder[1][2]
    g = placeholder[2][0]
    h = placeholder[2][1]
    i = placeholder[2][2]

def player1():
    try:
        player_select = 'x' 
        print('Vez do Jogador I')
        column = int(input('Digite a coluna desejada: '))
        line = int(input('Digite a linha desejada: '))
        if column >= 4:
            print('O número inserido é maior que 3. Tente novamente.')
            player1()
        if line >= 4:
            print('O número inserido é maior que 3. Tente novamente.')
            player1()
        if placeholder[line-1][column-1] == ' ':
            placeholder[line-1][column-1] = player_select
        else:
            print('Campo já ocupado. Tente novamente.')
            player1()
        showing()
        verifyWinner()
        player2()
    except ValueError:
        print('Algo deu errado. Tente novamente.')
        player1()

def player2():
    try:
        player_select = 'o'
        print('Vez do Jogador II')
        column = int(input('Digite a coluna desejada: '))
        line = int(input('Digite a linha desejada: '))
        if column >= 4:
            print('O número inserido é maior que 3. Tente novamente.')
            player2()
        if line >= 4:
            print('O número inserido é maior que 3. Tente novamente.')
            player2()
        if placeholder[line-1][column-1] == ' ':
            placeholder[line-1][column-1] = player_select
        else:
            print('Campo já ocupado. Tente novamente.')
            player2()
        showing()
        verifyWinner()
        player1()
    except ValueError:
        print('Algo deu errado. Tente novamente.')
        player2()

def showing():
    for line in placeholder:
        for column in line:
            print(f'│{column}', end="")
        print('│')
    return

player1()






    
