# -*- coding: utf-8 -*-
"""
Jogo da velha
"""
def makeBoard() :
    theBoard = {};
    rows = ['S','M','I']
    cols = ['E','M','D']
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            theBoard.setdefault(key,False)
    
    return theBoard

def printCell(cell) :
    if cell : 
        return ' '+str(cell)+' '
    else :
        return '   '

def showBoard(board) : 
    print(printCell(board['S-E'])+'|'+printCell(board['S-M'])+'|'+printCell(board['S-D']))
    print('-----------')
    print(printCell(board['M-E'])+'|'+printCell(board['M-M'])+'|'+printCell(board['M-D']))
    print('-----------')
    print(printCell(board['I-E'])+'|'+printCell(board['I-M'])+'|'+printCell(board['I-D']))

def determineVictory(board):
    rows = ['S','M','I']
    cols = ['E','M','D']
    #se uma linha tiver todas as colunas iguais é vitoria
    for r in rows :
        col1 = str(r)+'-E'
        col2 = str(r)+'-M'
        col3 = str(r)+'-D'
        if board[col1] == board[col2] == board[col3] and bool(board[col1]) :
            return board[col3]
    #se uma coluna tiver todas as linhas iguais é vitoria
    for c in cols :
        row1 = 'S-'+str(c)
        row2 = 'M-'+str(c)
        row3 = 'I-'+str(c)
        if board[row1] == board[row2] == board[row3] and bool(board[row1]) :
            return board[row3]
    #se houver uma diagonal com todas iguais então é vitoria
    middle = 'M-M';
    sel1, sel2 = str(rows[0]+'-'+cols[2]), str(rows[2]+'-'+cols[0])
    if board[middle] == board[sel1] == board[sel2] :
       return board[middle]
    sel1, sel2 = str(rows[0]+'-'+cols[0]), str(rows[2]+'-'+cols[2])
    if board[middle] == board[sel1] == board[sel2] :
       return board[middle]
    return False

def determineAvailableMoves(board) :
    rows = ['S','M','I']
    cols = ['E','M','D']
    hasMoves = False
    #verifica se posicão escolhida é válida
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            if not bool(board[key]) :
                return True
    return hasMoves

def readInputAndTryToPutOnBoard(board, player) :
    rows = ['S','M','I']
    cols = ['E','M','D']
    print('Para fazer um movimento, digite uma linha (S [superior], M [meio], I [inferior]), seguido por um dash (-) e uma coluna (E [esquerda], M [meio], D [direita]), como exemplo: S-M')
    move = input()
    valida = False
    # verifica se posicão escolhida é válida
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            if key == move:
                valida = True

    if valida & bool(board[move]):
        print('Essa posição já está ocupada! :( Vamos tentar mais uma vez?');
        return False
    elif valida:
        board[move] = player
        return True
    else:
        print('Posição inválida!');
        return False

def changePlayer(player) :
    if player == 'X':
        print('Jogador O, sua vez! :D ')
        return 'O'
    else:
        print('Jogador X, sua vez! ;) ')
        return 'X'
    
def game():
    print('Vamos jogar! Jogador X, você começa ;) ')
    player = 'X'
    board = makeBoard();
    while True :
        showBoard(board);
        #obtem movimento
        while True : 
            move = readInputAndTryToPutOnBoard(board, player)
            if move :
                break
        #verifica se movimento concedeu vitoria
        if determineVictory(board) :
            showBoard(board);
            print('Jogador '+player+' é o vencedor!!! :D ')
            return True
        #verifica se ainda há movimentos possíveis
        if not determineAvailableMoves(board) :
            print('E não é que deu velha? ;) ')
            return True
        #caso não tenha vencido então muda jogador e tenta denovo
        player = changePlayer(player)
        
game();