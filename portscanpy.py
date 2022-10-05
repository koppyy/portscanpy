import socket
import os
# Contribuições:
# Ch4rse404
# Koppy404
#  ★★★


os.system('clear')
print('\033[1;91m    ____  ____  ____  ___________ _________    _   ________  __\033[m')
print('\033[1;91m   / __ \/ __ \/ __ \/_  __/ ___// ____/   |  / | / / __ \ \/ /\033[m')
print('\033[1;91m  / /_/ / / / / /_/ / / /  \__ \/ /   / /| | /  |/ / /_/ /\  /\033[m')
print('\033[1;92m / ____/ /_/ / _, _/ / /  ___/ / /___/ ___ |/ /|  / ____/ / /\033[m')
print('\033[1;92m/_/    \____/_/ |_| /_/  /____/\____/_/  |_/_/ |_/_/     /_/\033[m')
print('\n')
print('                https://github.com/koppyy')
print('''

by : \033[91mKoppy\033[0m and \033[92mCh4rse\033[0m

  [ 1 ]\033[91m Scanear portas\033[0m

  [ 2 ]\033[92m Sair\033[0m

        ''')
try:
    op = int(input('opção : '))

    if op == 1:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5555, 5900, 8080, 8888]
    elif op == 2:
        print("Saindo...")
        exit()
        
    target = str(input('\nALVO: '))
except:
    exit()
    print('[ ! ] - ERRO NA SELECAO DE OPÇÃO [ ! ]')
try:
    print('\tPORTA\tSTATUS')
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(0.6)
        code = s.connect_ex((target, port))
        if code == 0:
            print(f"\t{port}\tABERTA")
except:
    exit()
    print('[ ! ] IP OU SOCKET INVALIDO [ ! ]')
