# -*- coding: utf-8 -*-
"""
Jogo da velha - python funcional
Alunas:
    Ana Paula Fidelis
    Bárbara Marquez
"""
def criarQuadro():
    quadro = {};
    linhas = ['S','M','I']
    colunas = ['E','M','D']
    for linha in linhas:
        for coluna in colunas:
            key = str(linha) + '-' + str(coluna)
            quadro.setdefault(key,False)
    
    return quadro

def escreverCelula(celula):
    if celula: 
        return ' '+str(celula)+' '
    else:
        return '   '

def mostrarQuadro(quadro):
    print(escreverCelula(quadro['S-E'])+'|'+escreverCelula(quadro['S-M'])+'|'+escreverCelula(quadro['S-D']))
    print('-----------')
    print(escreverCelula(quadro['M-E'])+'|'+escreverCelula(quadro['M-M'])+'|'+escreverCelula(quadro['M-D']))
    print('-----------')
    print(escreverCelula(quadro['I-E'])+'|'+escreverCelula(quadro['I-M'])+'|'+escreverCelula(quadro['I-D']))

def verificarVitoria(quadro):
    linhas = ['S','M','I']
    colunas = ['E','M','D']
    #se uma linha tiver todas as colunas iguais é vitoria
    for linha in linhas:
        col1 = str(linha)+'-E'
        col2 = str(linha)+'-M'
        col3 = str(linha)+'-D'
        if quadro[col1] == quadro[col2] == quadro[col3] and bool(quadro[col1]):
            return quadro[col3]
    #se uma coluna tiver todas as linhas iguais é vitoria
    for coluna in colunas:
        lin1 = 'S-'+str(coluna)
        lin2 = 'M-'+str(coluna)
        lin3 = 'I-'+str(coluna)
        if quadro[lin1] == quadro[lin2] == quadro[lin3] and bool(quadro[lin1]):
            return quadro[lin3]
    #se houver uma diagonal com todas iguais então é vitoria
    middle = 'M-M';
    sel1, sel2 = str(linhas[0]+'-'+colunas[2]), str(linhas[2]+'-'+colunas[0])
    if quadro[middle] == quadro[sel1] == quadro[sel2]:
       return quadro[middle]
    sel1, sel2 = str(linhas[0]+'-'+colunas[0]), str(linhas[2]+'-'+colunas[2])
    if quadro[middle] == quadro[sel1] == quadro[sel2]:
       return quadro[middle]
    return False

def verificarMovimentosDisponiveis(quadro):
    linhas = ['S','M','I']
    colunas = ['E','M','D']
    possuiMovimentos = False
    #verifica se posicão escolhida é válida
    for linha in linhas:
        for coluna in colunas:
            key = str(linha) + '-' + str(coluna)
            if not bool(quadro[key]):
                return True
    return possuiMovimentos

def processaEntrada(quadro, jogador):
    linhas = ['S','M','I']
    colunas = ['E','M','D']
    print('Para fazer um movimento, digite uma linha (S [superior], M [meio], I [inferior]), seguido por um traço (-) e uma coluna (E [esquerda], M [meio], D [direita]), como exemplo: S-M')
    posicao = input()
    valida = False
    
    # verifica se posicão escolhida é válida
    for r in linhas:
        for c in colunas:
            key = str(r) + '-' + str(c)
            if key == posicao:
                valida = True
    
    try:
        if valida & bool(quadro[posicao]):
            print('Essa posição já está ocupada!:( Vamos tentar mais uma vez?');
            return False
        elif valida:
            quadro[posicao] = jogador
            return True
    except:
        print('Posição inválida! Vamos tentar de novo? :D')
        return False

def mudarJogador(jogador):
    if jogador == 'X':
        print('Jogador O, sua vez! :D ')
        return 'O'
    else:
        print('Jogador X, sua vez! ;) ')
        return 'X'

def formatarCamposMap(a, b):
  return a + '-' + b

def imprimirInstrucoes():
    linhas = ['S','M','I']
    colunas = ['E','M','D']
    result = zip(linhas, colunas)
    
    print('JOGO DA VELHA')
    print('As regras são extremamente simples: o vencedor é quem conseguir fechar primeiro uma sequencia de 3 símbolos iguais, em uma linha, coluna ou diagonal.')
    print('E se empatar? É velha ;) ')
    print('Ainda não sabe como jogar? Aí vai um exemplo de combinação possível:')
    for x, y in result:
        print(set(map(formatarCamposMap, x, y)))
    print('É isso aí! Vamos jogar? Jogador X, você começa ;) ')

def jogarJogoDaVelha():
    imprimirInstrucoes();
    #inicializa com o jogador X
    jogador = 'X'
    #cria o quadro
    quadro = criarQuadro();
    while True:
        #mostra o quadro
        mostrarQuadro(quadro);
        #obtem movimento
        while True: 
            move = processaEntrada(quadro, jogador)
            if move:
                break
        #verifica se movimento implica em finalização do jogo
        if verificarVitoria(quadro):
            mostrarQuadro(quadro);
            print('Jogador '+jogador+' é o vencedor!!! :D ')
            return True
        #verifica se ainda há movimentos possíveis
        if not verificarMovimentosDisponiveis(quadro):
            print('E não é que deu velha? ;) ')
            return True
        #caso não tenha vencido então muda jogador e segue o jogo
        jogador = mudarJogador(jogador)
        
#bora jogar essa coisa maravilhosa
jogarJogoDaVelha();