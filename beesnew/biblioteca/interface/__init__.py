

cores = ('\33[m',#0-quebra de cor
         '\033[0:31m',#1-vermelho
         '\033[0:32m',#2-verde
         '\033[0:33m',#3-amarelo
         '\033[0:34m',#4-azul
         '\033[0:35m',#5-roxo
         )

def linha():
    print('-'*30)


def cabecalho(msg):
    linha()
    print(f'{cores[5]}{msg}{cores[0]}'.center(40))
    linha()


def menu(lista):
    c = 1#contador
    for item in lista:
        print(f'{c} - {cores[4]}{item}{cores[0]}')
        c += 1#soma contador em cada lupim
    linha()
    resp = leiainteiro('Opção:')
    return resp

def leiainteiro(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
                valor = int(n)
                ok = True
        else:
            print(f'{cores[1]}ERRO! Digite um valor valido!!{cores[0]}')
        if ok:
            break
    return valor