import time
import os

def Iniciar():
    os.system('cls')
    Tempo = int(input('\nDigite quanto tempo o temporizador vai ter: '))
    while Tempo > 60 and Tempo < 0:
        Tempo = int(input('\nValor invalido!\nDigite outro valor!\nR: '))

    Tipo = str(input('\nEsse valor será em\nH- Horas\nM- Minutos\nS- Segundos\nCS- Centesimos\nR: '))
    while Tipo != ('h' or 'H') and Tipo != ('m' or 'M') and Tipo != ('s' or 'S') and Tipo != ('cs' or 'CS'):
        Tipo = str(input('\nOpção invalida!\nDigite outra opção!\nR:'))

    if Tipo == ('h' or 'H'):
        hh = Tempo - 1
        mm = 59
        ss = 59
        cs = 9
    elif Tipo == ('m' or 'M'):
        hh = 0
        mm = Tempo - 1
        ss = 59
        cs = 9
    elif Tipo == ('s' or 'S'):
        hh = 0
        mm = 0
        ss = Tempo - 1
        cs = 9
    else: 
        hh = 0
        mm = 0
        ss = 0
        cs = Tempo 


    for i in range(hh,-1,-1):
        for j in range(mm,-1,-1):
            for k in range(ss,-1,-1):
                for l in range(cs,-1,-1):
                    os.system('cls')
                    print('hh:mm:ss:m')
                    print(f'{i:02d}:{j:02d}:{k:02d}:{l:1d}')
                    time.sleep(0.1)
    
    Voltar = int(input('\nDigite "1" para voltar\nR: '))
    while Voltar != 1:
        Voltar = int(input('\nOpção invalida!\nDigite "1" para voltar\nR: '))

while True:
    os.system('cls')

    Menu = int(input(f'\n* Menu *\n1- Começar\n2- Sair\nR: '))
    while Menu != 1 and Menu != 2:
        Menu = int(input('\n* Menu *\nOpção invalida!\n1- Começar\n2- Sair\nR: '))

    if Menu == 1:
        Iniciar()
    else:
        print('\nPrograma finaliado!')
        break