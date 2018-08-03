from random import randint
print('\033[35m-='*30)
print('\033[1;35;43m{:=^60}\033[m'.format('Truco'))
print('\033[35m-=\033[m'*30)  # Tudo enfeites
placarjogador = placarmaquina = 0  # Placar total(de 0 a 12)
while placarjogador < 12 or placarmaquina < 12:
    n1 = {1: randint(1,10), 2: randint(1,10), 3: randint(1,10)}  # Cartas do jogador
    n2 = {1: randint(1,10), 2: randint(1,10), 3: randint(1,10)}  # Cartas da maquina
    vira = randint(1,10)  # Seleçao da vira
    for c in range(1, 4):  # Nesse for sera selecionado o nipe das manilhas.
        if n1[c]+1 == vira or vira == 1 and n1[c] == 10:
            n1[c] = randint(-4, -1)
        if n2[c]+1 == vira or vira == 1 and n2[c] == 10:
            n2[c] = randint(-4, -1)
    n1n2 = (n1[1], n1[2], n1[3], n2[1], n2[2], n2[3])
    while n1n2.count(-4) > 1 and n1n2.count(-3) > 1 and n1n2.count(-2) > 1 and n1n2.count(-1) > 1:
        if n1[1] < 0:              # Todos os comandos desse while são para evitar que aja duas manilhas de mesmo nipe
            n1[1] = randint(-4, -1)
        if n1[2] < 0:
            n1[2] = randint(-4, -1)
        if n1[3] < 0:
            n1[3] = randint(-4, -1)
        if n2[1] < 0:
            n2[1] = randint(-4, -1)
        if n2[2] < 0:
            n2[2] = randint(-4, -1)
        if n2[3] < 0:
            n2[3] = randint(-4, -1)
    lista = {-4: 'Zap', -3: 'Copas', -2: 'Espada', -1: 'Ouros', 1: 'Três', 2: 'Dois', 3: 'Ás',
             4: 'Reis', 5: 'Valete', 6: 'Dama', 7: 'Sete', 8: 'Seis', 9: 'Cinco', 10: 'Quatro'}  # Traduzindo as Cartas
    cp = cm = p1 = p2 = 0  # Contagem da rodada (de 0 a 3)
    print(f'A vira é: {lista[vira]}')
    while cp+cm < 3:
        p1a = p1
        p2a = p2
        print(f'Suas cartas são: {lista[n1[1]]}[ 1 ], {lista[n1[2]]}[ 2 ], {lista[n1[3]]}[ 3 ]')
        while p1a == p1:
            p1 = int(input('Digite o numero equivalente ao da carta que deseja jogar: '))
        while p2a == p2:
            p2 = randint(1, 3)  # Qual carta a maquina vai escolher?
        print(f'\033[1;36mVoce jogou um {lista[n1[p1]]}')
        print(f'\033[1;35mMaquina jogou um {lista[n2[p2]]}\033[m')
        if n1[p1] < n2[p2]:  # Jogador vence
            print('\033[1;32mVenceu')
            cp += 1
        elif n1[p1] == n2[p2]:  # Criterios de desempate nesse if
            print('\033[1;33mEmpate')
            cp += 1
            cm += 1
            if cp+cm == 4 and n1[p1a] < n2[p2a]:
                cm += 1
            elif cp+cm == 4 and n2[p2a] < n1[p1a]:
                cp += 1
        else:  # Jogador perde
            print('\033[1;31mPerdeu')
            cm += 1
        print('\033[36m--\033[m'*30)
    if cm > cp:
            placarmaquina += 1
    elif cp > cm:
            placarjogador += 1
    print(f'\033[1;36mVoce: {placarjogador}\n\033[1;35mComputador: {placarmaquina}\033[m')
