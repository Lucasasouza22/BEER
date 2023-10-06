from beesnew.biblioteca.interface import *
from beesnew.biblioteca.dados import *

arq = 'produtosnortebeer'
leiaarquivo(arq)

if not existearquivo(arq):
    criaarquivo(arq)

while True:
    sleep(2)
    cabecalho(f'{"NORTE BEER"}')
    resp = menu(['Listar produtos', 'Cadastrar prodruto', 'Sair do sistema'])
    if resp == 1:
        cabecalho('Produtos')
        a = open(arq, 'rt')
        print(a.read())
        a.close()
    elif resp == 2:
        cabecalho('Novo Produto')
        produto = str(input('Produto: '))
        valor = input('Valor R$ ')
        cadastrar(arq,produto, valor)
    elif resp == 3:
        cabecalho('Até logo! Obrigado!')
        break
    else:
        print(f'{cores[1]}ERRO!Opção invalida!.{cores[0]}')

