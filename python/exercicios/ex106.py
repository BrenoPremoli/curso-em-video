from time import sleep
c = ['\033[m',  # 0 - transparente
    '\033[0;30;41m',  # 1 - vermelho
    '\033[0;30;42m',  # 2 - verde
    '\033[0;30;43m',  # 3 - amarelo
    '\033[0;30;44m',  # 4 - roxo
    '\033[0;30;45m',  # 5 - rosa
    '\033[0;30;47m' # 6 - cinza
    ]
def ajuda(comand):
    titulo(f'Manual do comando \'{comand}\'', 5)
    print(c[6], end='')
    help(comand)
    print(c[0], end='')
    sleep(2)
def titulo(msg, cor=0):
    tam = len(msg) + 6
    print(c[cor], end='')
    print('='*tam)
    print(f'   {msg}')
    print('='*tam)
    print(c[0], end='')
    sleep(1)
comando = ''
while True:
    titulo('SISTEMA DE AJUDA DO PYTHON', 1)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ MAIS :)', 2)