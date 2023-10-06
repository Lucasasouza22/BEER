from beesnew.biblioteca.interface import *
from time import sleep

def leiaarquivo(arq):
    try:
        print(f'Carregando...')
        sleep(2)
        a = open(arq, 'rt')
    except:
        print(f'ERRO! Não foi possivel abrir o arquivo.')
    finally:
        a.close()



def criaarquivo(arq):
    try:
        a = open(arq, 'wt+')
    except:
        print(f'Não foi possivel criar o arquivo!')
    else:
        print(f'Arquivo criado com sucesso!')


def existearquivo(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        print('Falha na leitura do arquivo')
        return False
    else:
        return True


def cadastrar(arq, produto='desconhecido',valor=float(0)):
    try:
        a = open(arq, 'a')
    except:
        print(f'Houve algum erro na abertura no arquivo!')
    else:
        try:
            a.write(f'{str(produto).upper():<15}{"R$":>8}{float(valor):>7.2f}\n')
        except Exception as e:
            print(f'Houve um erro: {e}')
        else:
            print(f'{str(produto).upper()} cadastrados com sucesso.')
            a.close()