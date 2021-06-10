"""
Name= sql_camps
Language= pt_BR.utf-8
OS: Ubuntu 20.04
IDE= Pycharm Community 2020.3 and Geany
Python version= 3.8
Date= May 29 2021
Author= Fabio Santos
"""
from datetime import datetime
from shutil import rmtree
from modules import *

ano_hj = datetime.today().year

while True:
    camps = []
    if os.path.isfile('campeonatos.txt'):
        with open('campeonatos.txt') as a:
            camp_list = a.read().split()
        for camp in camp_list:
            camps.append(camp.capitalize())
    campeonato = ' '
    
    while True:
        os.system('clear')
        print("\033[7m \033[m" * 60)
        print('\033[7m ' * 60)
        print(f'\033[1mCAMPEONATOS {ano_hj}'.center(64))
        print('\033[7m \033[m' * 60)
        print('\033[7m \033[m' * 60)
        if len(camps) == 0:
            print('\033[31mNão há campeonatos disponíveis.\nPor favor, use a opção adic para adicionar.\033[m')
        for c, camp in enumerate(camps):
            print(f'\033[1;6;33m{camp.center(11)}\033[m')
        campeonato = input('[\033[32mremove\033[m] - Para remover um campeonato salvo\n[\033[32madic\033[m] - Para '
                           'adicionar um campeonato a lista existente\n[\033[32msair\033[m] - para sair\n\n\033['
                           '1mInforme o nome do \033[33mcampeonato\033[m ou uma das \033[32mopções\033[m:\033[m '
                           '').capitalize().strip()
        if campeonato in camps and campeonato.upper() not in ('ADIC', 'REMOVE', 'SAIR'):
            caminho_rodadas: str = campeonato + '/rodadas.txt'
            caminho_partidas = campeonato + '/partidas.txt'
            caminho_equipes = campeonato + '/equipes.txt'
            caminho_criterio = campeonato + '/criterio.txt'
            if os.path.isfile(campeonato+'/turno.txt'):
                with open(campeonato+'/turno.txt') as a:
                    turno = True
                    turno_n = a.read()
            else:
                turno = False
                turno_n = ''
            if os.path.isfile(campeonato+'/qnt_rodadas.txt'):
                with open(campeonato+'/qnt_rodadas.txt') as a:
                    r = a.read()
                qnt_rodadas = int(r)
            with open(campeonato+'/qnt_rebaixados.txt') as a:
                r = a.read()
            qnt_rebaixados = int(r)
            with open(caminho_equipes) as a:
                equipes = a.read().splitlines()
            qnt_partidas = int(len(equipes) / 2)
            if not os.path.isfile(campeonato+'/ano.txt'):
                with open(campeonato+'/ano.txt', 'wt') as a:
                    a.write(str(ano_hj))
            with open(campeonato+'/ano.txt') as a:
                ano = a.read()
        break

    if os.path.isdir(campeonato):
        if campeonato in camps:   # Trabalhar com o campeonato
            while True:
                os.system('clear')
                print('\033[7m \033[m' * 60)
                print('\033[7m ' * 60)
                print(f'\033[1m{campeonato} {ano}'.center(64))
                print('\033[7m \033[m' * 60)
                print('\033[7m \033[m' * 60)
                opcao = input("[1] - Mostrar tabela\n"
                              "[2] - Adicionar/complementar/recuperar rodada/partida\n"
                              "[3] - Mostrar equipes participantes\n"
                              f"[4] - Mostrar jogos realizados em uma rodada do {campeonato}\n"
                              f"[5] - Mostrar todos os jogos de uma equipe no {campeonato}\n"
                              "[6] - Sair\n"
                              "Sua opção: ").strip()
                if opcao == '1':   # Mostrar tabela
                    while True:
                        # noinspection PyUnboundLocalVariable
                        tabela(campeonato, ano, caminho_rodadas, equipes, qnt_rodadas, qnt_rebaixados, turno_n,
                               caminho_criterio, turno)
                        sair = input('\n\033[1mTecle ENTER para sair\033[m')
                        if sair == "":
                            break
                elif opcao == "2":  # Adicionar Rodada
                    try:
                        # noinspection PyUnboundLocalVariable
                        dados(equipes, campeonato, caminho_rodadas, caminho_partidas,
                              qnt_rodadas, qnt_partidas, ano, caminho_criterio, turno_n, turno)
                    except KeyboardInterrupt:
                        os.system('clear')
                        print('\033[33mCancelando...\033[m')
                        sleep(1)
                        pass
                elif opcao == "3":  # Mostrar equipes participantes
                    while True:
                        print("*" * 40)
                        print("EQUIPES PARTICIPANTES".center(40))
                        print("*" * 40)
                        equipes.sort()
                        for c, equipe in enumerate(equipes):
                            if c % 2 == 0:
                                print(equipe.center(15), end=' ')
                            else:
                                print(equipe.center(15), end='\n')
                        print("*" * 40)
                        op = input('Tecle ENTER para voltar...')
                        if op == '':
                            break
                    
                elif opcao == "4":  # Mostrar jogos realizados em uma rodada
                    if os.path.isfile(caminho_rodadas):
                        with open(caminho_rodadas) as a:
                            r = int(a.read())
                    else:
                        r = 0
                    if os.path.isfile(caminho_partidas):
                        with open(caminho_partidas) as a:
                            p = int(a.read())
                    else:
                        p = 0
                    while True:
                        try:
                            rodada = input('Informe a rodada (Nº) que queira mostrar os jogos ou tecle ENTER\n'
                                           'para mostrar todos os jogos realizados até o momento '
                                           '[0 para sair]: ').strip()
                        except (ValueError, TypeError):
                            print('\033[31mErro: \033[m')
                        else:
                            if rodada.isdigit():
                                if int(rodada) in range(0, r+1):
                                    break
                                print('\033[31mEsta rodada não existe!\033[m')
                            elif rodada == '':
                                break
                            else:
                                print('\033[31mEsta rodada não existe!\033[m')
                    jogos_realizados(campeonato, rodada, r, p) if r != 0 else ''
                elif opcao == '5':
                    os.system('clear')
                    if os.path.isfile(caminho_rodadas):
                        with open(caminho_rodadas) as a:
                            atual_rodada = int(a.read())
                    else:
                        atual_rodada = 1
                    if os.path.isfile(caminho_partidas):
                        with open(caminho_partidas) as a:
                            partida = int(a.read())
                    else:
                        partida = 0
                    show_jogos(campeonato, equipes, atual_rodada, partida)

                elif opcao == "6":   # Voltar ao menu inicial
                    os.system('clear')
                    print('Voltando ao menu inicial...')
                    sleep(1)
                    break            
                else:
                    os.system('clear')
                    print('\033[31mOpção inválida!\033[m')
                    sleep(1)

    elif campeonato.upper() == 'REMOVE':   # Remover campeonatos
        os.system('clear')
        n_camp = input('Informe o nome do campronato que você deseja remover: ').strip().capitalize()
        if os.path.isdir(n_camp):
            conn = sqlite3.connect('campeonatos.db')
            cursor = conn.cursor()
            cursor.execute(f'DROP TABLE IF EXISTS {n_camp}')
            conn.commit()
            cursor.close()
            conn.close()
            rmtree(n_camp)
            with open('campeonatos.txt') as a:
                r = a.read().split()
            os.remove('campeonatos.txt')
            for time in r:
                if time.capitalize() != n_camp:
                    if not os.path.isfile('campeonatos.txt'):
                        with open('campeonatos.txt', 'wt') as a:
                            a.write(time+'\n')
                    elif os.path.isfile('campeonatos.txt'):
                        with open('campeonatos.txt', 'at') as a:
                            a.write(time+'\n')
                else:
                    pass
            print(f'\033[32mCampeonato {n_camp} removido com sucesso!\033[m')
            sleep(2)
        else:
            print(f'\033[31mO campeonato {n_camp} não existe!\033[m')
            sleep(2)

    elif campeonato.upper() == 'ADIC':   # Adicionar campeonatos
        os.system('clear')
        print('\033[33m*OBSERVAÇÕES:')
        print('Os \033[4;33mcritérios de desempate\033[m',
              "\033[33mnão funcionarão corretamente em \ncampeonatos onde",
              '\033[4;33messes\033[m \033[33mcomecem com \033[4;33mconfrontos direto\033[m',
              "\033[33m.Como \no Espanhol ou Italiano por exemplo, no momento.\033[m\n")
        print('\033[33mVocê também pode adicionar um arquivo.txt com as equipes participantes do\n'
              'campeonato \033[4;33m(uma equipe por linha com uma linha em branco no final)\033[m'
              '\033[33m na pasta campeonatos\ne renomear este arquivo para \033[1;33m"(as três primeiras letras '
              'do seu\ncampeonato, sendo a primeira maiúscula)+_equipes.txt ex: Bra_equipes.txt para\n'
              'Brasileirão"\033[m\033[33m, antes de adiciona-lo. Caso não queira, adicione por aqui mesmo\n,'
              'manualmente, mais à frente.\033[m\n')
        pre_camps = ['Brasileirão']
        print('Campeonatos pré_configurados'.center(40))
        print('+' * 40)
        for c, ca in enumerate(pre_camps):
            print(f'[{c + 1}] - {ca}')
        print('+' * 40)
        camp_name = input('Informe o nome do novo campeonato ou o número de um \ncampeonato pré_configurado:'
                          ' ').capitalize().strip()
        if camp_name == '1' and (int(camp_name)-1) == pre_camps.index('Brasileirão'):
            os.system('clear')
            print(f'Adicionando {pre_camps[0]} a lista de campeonatos...')
            sleep(1)
            if os.path.isfile('campeonatos.txt'):
                with open('campeonatos.txt', 'at') as a:
                    a.write(pre_camps[0]+'\n')
            else:
                with open('campeonatos.txt', 'wt') as a:
                    a.write(pre_camps[0]+'\n')
            os.system('clear')
            print(f'Criando a pasta do {pre_camps[0]}...')
            sleep(1)
            os.mkdir(pre_camps[0])
            os.system('clear')
            print(f'Configurando a quantidade de rodadas do {pre_camps[0]}...')
            sleep(1)
            with open('Brasileirão/qnt_rodadas.txt', 'wt') as a:
                a.write('38')
            os.system('clear')
            print(f'Configurando a quantidade de rebaixados do {pre_camps[0]}...')
            sleep(1)
            with open('Brasileirão/qnt_rebaixados.txt', 'wt') as a:
                a.write('4')
            os.system('clear')
            print(f'Configurando o critério de desempate do {pre_camps[0]}...')
            sleep(1)
            with open('Brasileirão/criterio.txt', 'wt') as a:
                a.write('1')
            os.system('clear')
            print('Configurando quantidade de equipes...')
            sleep(1)
            qnt_equipes = 20
            print('\033[33mConfigurando equipes participantes...\033[m')
            print('*' * 50)
            sleep(1)
            with open('Bra_equipes.txt') as a:
                eqps = a.read().splitlines()
            if qnt_equipes == len(eqps):
                with open('Brasileirão/equipes.txt', 'w') as a:
                    for c, eqp in enumerate(eqps):
                        a.write(eqp + '\n')
                        print(eqp.center(15), flush=True, end='\n' if c == 0 else '' if c % 3 != 0 else '\n')
                        sleep(0.5)
                    print()
                print('*' * 50)
                sleep(1)

        else:
            confirme = ' '
            while camp_name != confirme:  # Nome do camp
                confirme = input('Confirme o nome do campeonato: ').capitalize().strip()
                if camp_name != confirme:
                    print('\033[31mOs nomes não conferem.\ntente novamente!\033[m')
            if os.path.isfile('campeonatos.txt'):
                with open('campeonatos.txt', 'at') as a:
                    a.write(camp_name+'\n')
            else:
                with open('campeonatos.txt', 'wt') as a:
                    a.write(camp_name+'\n')

            os.mkdir(camp_name)

            while True:           # Se o camp terá turno ou não
                turno_opc = input(f'O {camp_name} terá turno? (S/N) ').strip().upper()
                if turno_opc == 'S':
                    turno_name = input('Informe o nome do turno: ').strip().title()
                    with open(camp_name+'/turno.txt', 'wt') as a:
                        a.write(turno_name)
                    print('\033[32mTurno adicionado com sucesso!!\033[m')
                    break
                elif turno_opc == 'N':
                    print(f'\033[1mO {camp_name} {ano_hj} não terá turno.\033[m')
                    break
                else:
                    print('\033[31mOPÇÃO INVÁLIDA\nTENTE NOVAMENTE!!!\033[m')

            while True:   # Quantidade de rodadas do camp
                try:
                    qnt_rodadas = int(input(f'Quantidade de rodadas que o {camp_name} {ano_hj} terá: '))
                except (ValueError, TypeError):
                    print('\033[31mERROR: Você não entrou com um número inteiro.\nTente novamente!\033[m')
                else:
                    with open(camp_name+'/qnt_rodadas.txt', 'wt') as a:
                        a.write(str(qnt_rodadas))
                    break

            while True:      # Número de equipes rebaixadas no camp
                try:
                    qnt_rebaixados = int(input(f'Quantas equipes será(ão) rebaixada(s) no {camp_name} {ano_hj}? '))
                except (ValueError, TypeError):
                    print('\033[31mERROR: Informe apenas número interiro!\nTente novamente!\033[m')
                else:
                    with open(camp_name+'/qnt_rebaixados.txt', 'wt') as a:
                        a.write(str(qnt_rebaixados))
                    break

            while True:   # Critérios de desempate
                criterio = input('''\n\033[1mEscolha um critŕio de desempate para caso duas ou
    mais equipes acabem empatadas em número de pontos.\033[m\033[36m
    [1] - (vitórias, saldo de gols, gols marcados)
    [2] - (vitórias, saldo de gols, gols marcados, gols sofridos)
    [3] - (saldo de gols, gols marcados)\033[m
    
    \033[1mSua escolha:\033[m ''').strip()
                if criterio == '1':
                    with open(camp_name+'/criterio.txt', 'wt') as a:
                        a.write('1')
                    break
                elif criterio == '2':
                    with open(camp_name+'/criterio.txt', 'wt') as a:
                        a.write('2')
                    break
                elif criterio == '3':
                    with open(camp_name+'/criterio.txt', 'wt') as a:
                        a.write('3')
                    break
                else:
                    print('\033[31mOPÇÃO INVÁLIDA!\nTENTE NOVAMENTE!!\033[m')

            while True:     # Quantidade de equipes participantes
                try:
                    qnt_equipes = int(input(f'Quantas equipes participarão do {camp_name} {ano_hj}? '))
                except (ValueError, TypeError):
                    print('\033[31mERROR: Informe apenas número interiro!\nTente novamente!\033[m')
                else:
                    break
            c = 1

            while c <= qnt_equipes:   # Equipes participantes
                if not os.path.isfile(camp_name+'/equipes.txt') and not os.path.isfile(camp_name[0:3]+'_equipes.txt'):
                    eqp = input(f'{c}ª Equipe: ').title().strip()
                    with open(camp_name+'/equipes.txt', 'wt') as a:
                        a.write(eqp+'\n')
                elif os.path.isfile(camp_name+'/equipes.txt') and not os.path.isfile(camp_name[0:3]+'_equipes.txt'):
                    eqp = input(f'{c}ª Equipe: ').title().strip()
                    with open(camp_name+'/equipes.txt', 'at') as a:
                        a.write(eqp+'\n')
                else:
                    # if os.path.isfile(camp_name[0:3]+'equipes.txt'):
                    print('\033[33mEquipes existentes\033[m'.center(54))
                    print('*' * 50)
                    with open(camp_name[0:3]+'_equipes.txt') as a:
                        eqps = a.read().splitlines()
                    if qnt_equipes == len(eqps):
                        with open(camp_name+'/equipes.txt', 'w') as a:
                            for c, eqp in enumerate(eqps):
                                a.write(eqp+'\n')
                                print(eqp.center(15), flush=True, end='\n' if c == 0 else '' if c % 3 != 0 else '\n')
                                sleep(0.5)
                            print()
                        print('*' * 50)
                        sleep(2)
                    else:
                        print('\033[31mO número de equipes da sua lista não é igual ao\n'
                              'número de equipes participantes informado.\033[m')
                    break
                c += 1
        os.system('clear')
        print(f'\n\033[32m{camp_name if not camp_name.isdigit() else pre_camps[int(camp_name)-1]} {ano_hj} '
              f'adicionado com sucesso!')
        sleep(3)

    elif campeonato.upper() == 'SAIR':   # Fechar o programa
        os.system('clear')
        print('\033[1mTCHAUUU!\033[m')
        break

    else:
        os.system('clear')
        print('\033[31mOpção inválida!\033[m')
        sleep(1)
