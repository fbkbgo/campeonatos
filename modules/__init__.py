"""
Funções uteis para o correto funcionamento dos campeonatos.

Name: Modules

Language: pt_BR.utf-8

OS: Ubuntu 20.04

IDE: Pycharm Community 2020.3 and Geany

Python Version: 3.8

Date: May 29 2021

Author: Fabio Santos
 """
import os
import sqlite3
from time import sleep


def tabela(campeonato, ano, caminho_rodada, equipes_participantes, qnt_rodadas,
           rebaixados, turno_n, caminho_criterio, turno):
    """tabela printa a tabela do campeonato
       campeonato = seleciona o campeonato à ser mostrado na tabela
       ano = ano do inicio da temporada
       caminho_rodada = O caminho_rodada do arquivo rodada.txt do campeonato
       equipes_participantes = lista das equipes participantes do campeonato
       qnt_rodadas = número de rodadas do campeonato
       rebaixados = número de rebaixados que o cmpeonato terá
       turno_n = Nome do turno do campeonato (se houver) mostrado abaixo do none
       caminho_criterio = Critério de desempate do campeonato
       turno = Turno do campeonato (se houver)
       return = Sem retorno
    """

    try:
        os.system('clear')
        con = sqlite3.connect('campeonatos.db')
        cur = con.cursor()
        if os.path.isfile(caminho_criterio):
            with open(caminho_criterio) as a:
                criterio = a.read()
        else:
            criterio = '1'
        if criterio == '1':
            cur.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, Vitórias DESC, SG DESC, GP DESC')
        elif criterio == '2':
            cur.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, Vitórias DESC, SG DESC, GP DESC, GC ASC')
        elif criterio == '3':
            cur.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, SG DESC, GP DESC')
        result = cur.fetchall()
        if os.path.isfile(caminho_rodada):
            with open(caminho_rodada) as a:
                r = a.read()
            rodada = int(r)

            # Cabeçalho da tabela
            print('*' * 75)
            print('*', f'\033[1;32m{campeonato} {ano} \033[33m({rodada - 1}ª Rodada)\033[m'.center(85), ' *')
            if turno:
                print('*', f'\033[1;32m{turno_n}\033[m'.center(81), '*')
            else:
                print('*', ' '.center(71), '*')
            print('*\033[0m' * 75)
            print('\033[0m*|\033[m', '\033[1;33mPº|'.rjust(1), 'Equipes'.center(14), '|'.center(3), 'J'.center(1),
                  '|'.center(3), 'P'.center(1), '|'.center(3), 'V'.center(1), '|'.center(3), 'D'.center(1),
                  '|'.center(3), 'E'.center(1), ' |'.center(2), 'SG'.center(3), ' |'.center(2), 'GP'.center(3),
                  ' |'.center(2), 'GC', ' |\033[m*')
            print('\033[4m*\033[m' * 75)
            # Corpo da tabela
            if campeonato == 'Brasileirão':
                for c, lin in enumerate(result):
                    print((f'*|\033[1;33m {str(c + 1).center(2)}-\033[m' if (c + 1) < 10 else
                           f'*|\033[1;33m{str(c + 1).ljust(1)} -\033[m'),
                          (f'\033[32m{lin[0].center(15)}\033[m' if 1 != (c + 1) <= 4 else
                           f'\033[36m{lin[0].center(15)}\033[m' if 4 < (c + 1) <= 6 else
                           f'\033[33m{lin[0].center(15)}\033[m' if 6 < (c + 1) <= 12 else
                           f'\033[1;31m{lin[0].center(15)}\033[m' if (c + 1) > len(
                               equipes_participantes) - rebaixados else
                           f'\033[1;32m{lin[0].center(15)}\033[m' if (c + 1) == 1 and rodada == qnt_rodadas else
                           f'\033[32m{lin[0].center(15)}\033[m' if (c + 1) == 1 else lin[0].center(15)),
                          '\033[4m|'.center(3), str(lin[1]).center(1),
                          ' |'.center(3) if int(lin[1]) < 10 else ' |'.center(2), str(lin[2]).center(1),
                          ' |'.center(3) if int(lin[2]) < 10 else ' |'.center(2), str(lin[3]).center(1),
                          ' |'.center(3) if int(lin[3]) < 10 else ' |'.center(2), str(lin[4]).center(1),
                          ' |'.center(3) if int(lin[4]) < 10 else ' |'.center(2), str(lin[5]).center(1),
                          ' |'.center(3) if int(lin[5]) < 10 else ' |'.center(2), str(lin[6]).center(2),
                          ' |'.center(3) if int(lin[6]) < 10 else ' |'.center(2), str(lin[7]).center(2),
                          ' |'.center(3) if int(lin[7]) < 10 else ' |'.center(2), str(lin[8]).center(3), '|*\033[m')

                # Rodapé da tabela
                print('*' * 75)
                print('*', '\033[1;7;32m  \033[m - Campeão              *')
                print('*', '\033[7;32m  \033[m - Libertadores         *')
                print('*', '\033[7;36m  \033[m - Pré-Libertadores     *')
                print('*', '\033[7;33m  \033[m - Sulamericana         *')
                print('*', '\033[7;31m  \033[m - Zona de rebaixamento *')
                print('*' * 29)
            else:
                for c, lin in enumerate(result):
                    print((f'*|\033[1;33m {str(c + 1).center(2)}-\033[m' if (c + 1) < 10 else
                           f'*|\033[1;33m{str(c + 1).ljust(1)} -\033[m'),
                          (f'\033[32m{lin[0].center(15)}\033[m' if 1 != (c + 1) <= 4 else
                           f'\033[31m{lin[0].center(15)}\033[m' if (c + 1) > len(equipes_participantes) - rebaixados
                           else f'\033[33m{lin[0].center(15)}\033[m' if (c + 1) == 1 and rodada == qnt_rodadas else
                           f'\033[32m{lin[0].center(15)}\033[m' if (c + 1) == 1 else lin[0].center(15)),
                          '\033[4m|'.center(3), str(lin[1]).center(1),
                          ' |'.center(3) if int(lin[1]) < 10 else ' |'.center(2), str(lin[2]).center(1),
                          ' |'.center(3) if int(lin[2]) < 10 else ' |'.center(2), str(lin[3]).center(1),
                          ' |'.center(3) if int(lin[3]) < 10 else ' |'.center(2), str(lin[4]).center(1),
                          ' |'.center(3) if int(lin[4]) < 10 else ' |'.center(2), str(lin[5]).center(1),
                          ' |'.center(3) if int(lin[5]) < 10 else ' |'.center(2), str(lin[6]).center(2),
                          ' |'.center(3) if int(lin[6]) < 10 else ' |'.center(2), str(lin[7]).center(2),
                          ' |'.center(3) if int(lin[7]) < 10 else ' |'.center(2), str(lin[8]).center(3), '|*\033[m')
                # Rodapé da tabela
                print('*' * 75)
                print('*', '\033[7;33m  \033[m - Campeão              *')
                print('*', '\033[7;32m  \033[m - Classificados        *')
                print('*', '\033[7;31m  \033[m - Zona de rebaixamento *')
                print('*' * 29)
            print()
            # Infos adicionais ao fim do campeonato
            if rodada == qnt_rodadas + 1:  # Imprimindo o CAMPEÃO
                campeao = result[0][0]
                print('\033[33m+\033[m' * 45)
                print('\033[33m+\033[m', ' ' * 41, '\033[33m+\033[m')
                print(f'  \033[1;33m{campeao} CAMPEÃO!!!\033[m'.center(45))
                print('\033[33m+\033[m', ' ' * 41, '\033[33m+\033[m')
                print('\033[33m+\033[m' * 45)
        else:
            print(f'{caminho_rodada} não existe!\n\033[31mAdicione uma rodada completa primeiro!\033[m')

    except Exception as e:
        print(f'\033[31mO erro ocorrido foi -> {e}.')
        print('Não foi encontrado tabelas salvas\nTente adicionar uma rodada primeiro.\033[m')


# noinspection PyUnboundLocalVariable
def dados(equipes_participantes, campeonato, caminho_rodada, caminho_partidas, qnt_rodadas, qnt_partidas, ano,
          caminho_criterio, turno_n, turno):
    """
    Modulo dados
    :param equipes_participantes: Lista de equipes participantees no campeonato
    :param campeonato: Nome do campeonato
    :param caminho_rodada: Caminho do arquivo rodadas
    :param caminho_partidas: Caminho do arquivo partidas
    :param qnt_rodadas:  Quantidade de rodadas que o campeonato terá
    :param qnt_partidas:  Quantidade de partidas que cada rodada terá
    :param ano: Ano que começou o campeonato
    :param caminho_criterio: Critério de desempate caso duas ou mais equipes acebem empatadas
    :param turno_n: Nome do turno do campeonato, caso tenha
    :param turno: Boleano do turno para especificar caso tenha turno o campeonato
    :return: Śem retorno
    """
    os.system('clear')
    pts_cs = pts_fr = emp_cs = emp_fr = der_cs = der_fr = vit_cs = vit_fr = saldo_cs = saldo_fr = gp_cs = gp_fr = \
        gc_cs = gc_fr = 0
    vitoria = 3
    empate = 1
    mandante = []
    visitante = []
    if os.path.isfile(caminho_rodada):
        with open(caminho_rodada) as arq:
            r = arq.read()
        rodada = int(r)
    else:
        rodada = 1

    while rodada < qnt_rodadas + 1:  # Rodadas
        conn = sqlite3.connect('campeonatos.db')
        cursor = conn.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {campeonato}(
        Time STRING PRIMARY KEY NOT NULL,
        Jogos INTEGER NOT NULL,
        Pontos INTEGER NOT NULL,
        Vitórias INTEGER NOT NULL,
        Derrotas INTEGER NOT NULL,
        Empates INTTEGER NOT NULL,
        SG INTEGER NOT NULL,
        GP INTEGER NOT NULL,
        GC INTEGER NOT NULL);
        ''')

        if not os.path.isfile(campeonato+'/adiado.txt'):
            with open(campeonato+'/adiado.txt', 'w') as a:
                a.write('')
        if os.path.isfile(caminho_partidas):
            with open(caminho_partidas) as a:
                r = a.read()
            partida = int(r)
        else:
            partida = 1

        if rodada > 1 == partida:
            opcao = input(f'Deseja adicionar a {rodada}ª rodada? (ENTER N PARA SAIR) ').strip()
            if opcao.upper() == 'N':
                print('\033[1;32mBYE BYE!!!\033[m')
                break
            else:
                print('\033[1mOK! Vamos lá...\033[m')
                sleep(1)
            os.system('clear')

        time_casa = ''
        time_fora = ''
        part_ad = 0
        part = 1
        while True:  # Rodada
            if os.path.isfile(campeonato + '/adiado.txt'):
                with open(campeonato+'/adiado.txt') as a:
                    adiados = a.read().splitlines()
            else:
                adiados = []
            rdd = ' '
            conn = sqlite3.connect('campeonatos.db')
            cursor = conn.cursor()
            while True:  # Partida
                print()
                print('-' * 50)
                print(f'\033[32m{partida}ª partida da {rodada}ª rodada\033[m'.center(56))

                if os.path.isfile(campeonato + '/jogos.txt'):
                    with open(campeonato + '/jogos.txt') as a:
                        partidas = a.read().splitlines()
                        print('-' * 50)
                        print(f'\033[1mJOGOS REALIZADOS NA {rodada}ª RODADA\033[m'.center(56))
                        print('*' * 50)
                        for c, time in enumerate(partidas):
                            if '-' in time:
                                print('[ADIADO]' if c == 0 or c % 2 == 0 else '', end=' ')
                                print(f'{time} x ' if c % 2 == 0 else f'{time}', end='' if c % 2 == 0 else '\n')
                            else:
                                print(f'{time} x ' if c % 2 == 0 else f'{time}', end='' if c % 2 == 0 else '\n')
                if os.path.isfile(campeonato + '/jogos1.txt'):
                    with open(campeonato + '/jogos1.txt') as a:
                        jogados = a.read().split('\n')
                else:
                    jogados = ' '
                print('*' * 50)
                eqps_parts = set(equipes_participantes)
                eqps_jgds = set(jogados)
                if len(eqps_jgds) == 1:
                    eqps_jgds.pop()
                eqps_falt = eqps_parts.symmetric_difference(eqps_jgds)
                print('\033[1;4mEquipes que ainda não jogaram\033[m'.center(56))
                cont = 1
                for eqps in eqps_falt:
                    print(f'{eqps.center(15)} ' if cont != len(eqps_falt) else f'{eqps.center(15)}', end='\n'
                          if cont % 3 == 0 else '')
                    cont += 1
                print()
                print('*' * 50)
                if len(adiados) > 0:
                    print('Jogos adiados'.center(50))
                    print('-' * 50)
                    for jg in adiados:
                        print(f'{jg}'.center(50))
                else:
                    print('Não temos jogos adiados'.center(50))
                print('*' * 50)

                print('\033[33mVocê pode cancelar a partida entrando CTRL+C \nou o botão STOP à qualquer '
                      'momento.\033[m')
                try:  # Tratando os inputs do jogo
                    while True:
                        try:
                            time_casa = input('Time mandante: ').title().strip()
                        except Exception as erro:
                            print(f'Algo ocorreu de errado: {erro}')
                        else:
                            break
                    while True:
                        try:
                            time_fora = input('Time visitante: ').title().strip()
                        except Exception as erro:
                            print(f'Algo ocorreu de errado: {erro}')
                        else:
                            break
                    adia = False
                    recupera = False
                    saia = False
                    while True:  # Opções da partida
                        opcoes = input("A partida foi adiada, quer recuperar partida adiada ou continuar?\n"
                                       "[A] - Adiar partida\n"
                                       "[C] - Complementar partida\n"
                                       "[R] - Recuperar partida adiada\n"
                                       "[E] - Voltar ao menu anterior\n"
                                       "Sua opção: ").strip().upper()
                        if opcoes == "A":
                            adia = True
                            break
                        elif opcoes == "C":
                            break
                        elif opcoes == "R":
                            while True:
                                try:
                                    jg_rodada = int(input('Em qual rodada o jogo foi adiado? Nº'))
                                except (ValueError, TypeError):
                                    print('\033[31mDigite um numero inteiro.\033[m')
                                else:
                                    break
                            while True:
                                try:
                                    jg_partida = int(input('Qual partida? Nº'))
                                except (ValueError, TypeError):
                                    print('\033[31mDigite um numero inteiro.\033[m')
                                else:
                                    break
                            part_adiada = f'{str(jg_rodada)}ªR {str(jg_partida)}ªP {time_casa} - x - {time_fora}'
                            for adiado in adiados:
                                if part_adiada == adiado:
                                    recupera = True
                                    break
                            if recupera:
                                break
                            else:
                                print(f'\033[31mERRO:{jg_rodada}ª rodada -> {jg_partida}ª partida - {time_casa} x '
                                      f'{time_fora} não é uma partida atrasada.\033[m')
                                sleep(2)
                        elif opcoes == "E":
                            saia = True
                            break
                        else:
                            print("\033[31mOpção invalida.\nTente novamente!\033[m")
                except Exception as e:
                    print(f'\033[31mHouve o seguinte erro: {e}\033[m')
                if (time_casa in equipes_participantes and time_fora in equipes_participantes) and \
                        (time_casa not in jogados and time_fora not in jogados) and time_casa != time_fora:
                    break
                os.system('clear')
                print(f'\033[31mERRO: {time_casa} x {time_fora}\033[m')
                print(
                    f"\033[31mUma das equipes (ou as duas) não participa(m) do {campeonato} \n{ano}, "
                    f"já jogaram na rodada ou são a mesma equipe.\nTente novamente!\033[m\n")

            if adia:  # Sai das opções da partida e volta ao menu anterior
                with open(campeonato + "/adiado.txt", 'a') as a:
                    a.write(f'{str(rodada)}ªR {str(partida)}ªP {time_casa} - x - {time_fora}\n')
                man = [(time_casa, part_ad, pts_cs, vit_cs, der_cs, emp_cs, saldo_cs, gp_cs, gc_cs)]
                vis = [(time_fora, part_ad, pts_fr, vit_fr, der_fr, emp_fr, saldo_fr, gp_fr, gc_fr)]

            elif recupera:  # Trata a recuperaçã de uma partida anteriormente adiada
                with open(campeonato + '/adiado.txt', '+w') as a:
                    ads = a.read().splitlines()
                    for jg in ads:
                        if jg != part_adiada:
                            a.write(jg + '\n')
                        elif len(ads) == 1:
                            a.write('')
                while True:
                    try:
                        gols_cs = int(input(f'Gols do \033[4m{time_casa}\033[m na partida: '))
                    except (ValueError, TypeError):
                        print('\033[31mERRO: Digite apenas números inteiros.\nTente novamente!\033[m')
                    else:
                        break
                while True:
                    try:
                        gols_fr = int(input(f'Gols do \033[4m{time_fora}\033[m na partida: '))
                    except (ValueError, TypeError):
                        print('\033[31mERRO: Digite apenas números inteiros.\nTente novamente!\033[m')
                    else:
                        break
                word = 'Gooll'
                os.system('clear')
                for c, letra in enumerate(word):
                    print(f'\033[5;33m{letra}' if c == 0 else f'{" " * c}\033[5;33m{letra}\033[m', flush=True, end='')
                    sleep(0.2)
                    os.system('clear')
                print(f'\033[5;33m{word}\033[m')

                saldo_cs += (gols_cs - gols_fr)
                saldo_fr += (gols_fr - gols_cs)
                gp_cs += gols_cs
                gp_fr += gols_fr
                gc_cs += gols_fr
                gc_fr += gols_cs
                if gols_cs > gols_fr:
                    print(f'\033[1;33m{time_casa}\033[m \033[1m{gols_cs} x {gols_fr} {time_fora}\033[m')
                    vit_cs += 1
                    der_fr += 1
                    pts_cs += vitoria
                elif gols_cs < gols_fr:
                    print(f'\033[1m{time_casa} {gols_cs} x {gols_fr} \033[33m{time_fora}\033[m')
                    vit_fr += 1
                    der_cs += 1
                    pts_fr += vitoria
                elif gols_cs == gols_fr:
                    print(f'\033[1m{time_casa} {gols_cs} x {gols_fr} {time_fora}\033[m')
                    emp_cs += 1
                    emp_fr += 1
                    pts_cs += 1
                    pts_fr += empate
                man = [(time_casa, part, pts_cs, vit_cs, der_cs, emp_cs, saldo_cs,
                        gp_cs, gc_cs)]
                vis = [(time_fora, part, pts_fr, vit_fr, der_fr, emp_fr, saldo_fr,
                        gp_fr, gc_fr)]

            elif saia:  # Sai das opções da partida e vota ao menu anterior
                break

            else:  # Se não quer sair, recuperar ou adiar a partida, trata a partida atual
                while True:
                    try:
                        gols_cs = int(input(f'Gols do \033[4m{time_casa}\033[m na partida: '))
                    except (ValueError, TypeError):
                        print('\033[31mERRO: Digite apenas números inteiros.\nTente novamente!\033[m')
                    else:
                        break
                while True:
                    try:
                        gols_fr = int(input(f'Gols do \033[4m{time_fora}\033[m na partida: '))
                    except (ValueError, TypeError):
                        print('\033[31mERRO: Digite apenas números inteiros.\nTente novamente!\033[m')
                    else:
                        break
                word = 'Gooll'
                os.system('clear')
                for c, letra in enumerate(word):
                    print(f'\033[5;33m{letra}' if c == 0 else f'{" " * c}\033[5;33m{letra}\033[m', flush=True, end='')
                    sleep(0.2)
                    os.system('clear')
                print(f'\033[5;33m{word}\033[m')

                saldo_cs += (gols_cs - gols_fr)
                saldo_fr += (gols_fr - gols_cs)
                gp_cs += gols_cs
                gp_fr += gols_fr
                gc_cs += gols_fr
                gc_fr += gols_cs
                if gols_cs > gols_fr:
                    print(f'\033[1;33m{time_casa}\033[m \033[1m{gols_cs} x {gols_fr} {time_fora}\033[m')
                    vit_cs += 1
                    der_fr += 1
                    pts_cs += vitoria
                elif gols_cs < gols_fr:
                    print(f'\033[1m{time_casa} {gols_cs} x {gols_fr} \033[33m{time_fora}\033[m')
                    vit_fr += 1
                    der_cs += 1
                    pts_fr += vitoria
                elif gols_cs == gols_fr:
                    print(f'\033[1m{time_casa} {gols_cs} x {gols_fr} {time_fora}\033[m')
                    emp_cs += 1
                    emp_fr += 1
                    pts_cs += 1
                    pts_fr += empate
                for resultado in adiados:
                    if str(rodada) in resultado:
                        rdd = resultado
                man = [(time_casa, part_ad if time_casa in adiados and str(rodada) in rdd else part, pts_cs,
                        vit_cs, der_cs, emp_cs, saldo_cs, gp_cs, gc_cs)]
                vis = [(time_fora, part_ad if time_fora in adiados and str(rodada) in rdd else part, pts_fr,
                        vit_fr, der_fr, emp_fr, saldo_fr, gp_fr, gc_fr)]

            if saia:  # Sai das opções da partida e volta ao menu anterior
                break

            mandante.clear()
            visitante.clear()

            if rodada == 1:  # Preenchendo a tabela do campeonato de acordo com os resultados da primeira rodada.

                for item in man:
                    mandante.append(item)
                for item in vis:
                    visitante.append(item)

                cursor.executemany(f'INSERT INTO {campeonato}'
                                   '(Time, '
                                   'Jogos, '
                                   'Pontos, '
                                   'Vitórias, '
                                   'Derrotas, '
                                   'Empates, '
                                   'SG, '
                                   'GP, '
                                   'GC) '
                                   'VALUES(?,?,?,?,?,?,?,?,?)', mandante)
                cursor.executemany(f'INSERT INTO {campeonato}'
                                   '(Time, '
                                   'Jogos, '
                                   'Pontos, '
                                   'Vitórias, '
                                   'Derrotas, '
                                   'Empates, '
                                   'SG, '
                                   'GP, '
                                   'GC) '
                                   'VALUES(?,?,?,?,?,?,?,?,?)', visitante)

            elif rodada > 1:  # Atualizando a tabela do campeonato de acordo com os resultados das rodadas seguintes.
                for resultado in adiados:
                    if str(rodada) in resultado:
                        rdd = resultado
                update_list = []

                cursor.execute(f'SELECT * FROM {campeonato}')
                result = cursor.fetchall()
                for cont, linha in enumerate(result):
                    if linha[0] == time_casa:
                        if (time_casa in adiados and str(rodada) in rdd and not recupera) or adia:
                            prtd = part_ad + linha[1]
                        else:
                            prtd = part + linha[1]
                        pts_cs += linha[2]
                        vit_cs += linha[3]
                        der_cs += linha[4]
                        emp_cs += linha[5]
                        if not adia:
                            saldo_cs += linha[6]
                            gp_cs += linha[7]
                            gc_cs += linha[8]
                        else:
                            saldo_cs = linha[6]
                            gp_cs = linha[7]
                            gc_cs = linha[8]
                        update_tuple = (prtd, pts_cs, vit_cs, der_cs, emp_cs,
                                        saldo_cs, gp_cs, gc_cs, time_casa)
                        update_list.insert(0, update_tuple)
                    elif linha[0] == time_fora:
                        if (time_fora in adiados and str(rodada) in rdd and not recupera) or adia:
                            prtd = part_ad + linha[1]
                        else:
                            prtd = part + linha[1]
                        pts_fr += linha[2]
                        vit_fr += linha[3]
                        der_fr += linha[4]
                        emp_fr += linha[5]
                        if not adia:
                            saldo_fr += linha[6]
                            gp_fr += linha[7]
                            gc_fr += linha[8]
                        else:
                            saldo_fr = linha[6]
                            gp_fr = linha[7]
                            gc_fr = linha[8]
                        update_tuple = (prtd, pts_fr, vit_fr, der_fr, emp_fr,
                                        saldo_fr, gp_fr, gc_fr, time_fora)
                        update_list.insert(1, update_tuple)
                if os.path.isfile(caminho_criterio):  # Critério de desempate
                    with open(caminho_criterio) as a:
                        criterio = a.read()
                else:
                    criterio = '1'
                if criterio == '1':
                    cursor.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, Vitórias DESC, SG DESC, GP DESC')
                elif criterio == '2':
                    cursor.execute(
                        f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, Vitórias DESC, SG DESC, GP DESC, GC ASC')
                elif criterio == '3':
                    cursor.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, SG DESC, GP DESC')
                    # Atualizando a tabela
                cursor.executemany(f'''UPDATE {campeonato} SET
                Jogos=?, 
                Pontos=?,
                Vitórias=?,
                Derrotas=?,
                Empates=?,
                SG=?,
                GP=?,
                GC=?
                WHERE Time=?''', update_list)
                update_list.clear()
            conn.commit()
            cursor.close()
            conn.close()

            conn1 = sqlite3.connect(f"{campeonato}/jogos_realizados.db")  # Salvando os jogos realizados
            cursor1 = conn1.cursor()
            cursor1.execute(f'''CREATE TABLE IF NOT EXISTS Rodada{rodada}
                    (Partidas PRIMARY KEY,
                    Mandantes VARCHAR(20),
                    GC VARCHAR(2),
                    Vs VARCHAR(1),
                    GF VARCHAR(2),
                    Visitantes VARCHAR(20));
                    ''')
            if recupera:
                part_realzd = [f'{jg_partida}ª', time_casa, gols_cs, 'X', gols_fr, time_fora, '*']
                cursor1.execute(f'SELECT * FROM Rodada{jg_rodada} ORDER BY Partidas ASC')
                cursor1.execute(f'''UPDATE Rodada{jg_rodada} SET 
                                    Partidas= ?,
                                    Mandantes = ?,
                                    GC = ?,
                                    Vs = ?,
                                    GF = ?,
                                    Visitantes = ? WHERE GC = ?''', part_realzd)

            else:
                part_realzd = [f'{partida}ª[Adiada]' if adia else f'{partida}ª', time_casa,
                               '*' if adia else gols_cs, 'X', '*' if adia else gols_fr, time_fora]
                cursor1.execute(f'INSERT INTO Rodada{rodada}'
                                '(Partidas,'
                                'Mandantes,'
                                'GC,'
                                'Vs,'
                                'GF,'
                                'Visitantes)'
                                'VALUES(?,?,?,?,?,?)', part_realzd)

            conn1.commit()
            cursor1.close()
            conn1.close()
            pts_cs = pts_fr = emp_cs = emp_fr = der_cs = der_fr = vit_cs = vit_fr = saldo_cs = saldo_fr = gp_cs = \
                gp_fr = gc_cs = gc_fr = 0  # Zerando as variaveis com resultados salvos da rodada anterior.

            if adia:
                print(f'\n\033[1mA partida entre {time_casa} x {time_fora} foi adiada.\033[m')
            else:
                conn = sqlite3.connect('campeonatos.db')
                cursor = conn.cursor()
                if os.path.isfile(caminho_criterio):
                    with open(caminho_criterio) as a:
                        criterio = a.read()
                else:
                    criterio = '1'
                if criterio == '1':
                    cursor.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, Vitórias DESC, SG DESC, GP DESC')
                elif criterio == '2':
                    cursor.execute(
                        f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, Vitórias DESC, SG DESC, GP DESC, GC ASC')
                elif criterio == '3':
                    cursor.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, SG DESC, GP DESC')
                result = cursor.fetchall()
                print('\033[4mPOS', 'Time'.center(13), '|  J  P   V   D   E   SG  GP  GC\033[m')
                # Imprimindo situação atual do time
                for c, lin in enumerate(result):
                    if lin[0] == time_casa:
                        print(f'{c + 1}º ', lin[0].center(13),
                              f' {str(lin[1]).center(3)} {str(lin[2]).center(3)} '
                              f'{str(lin[3]).center(3)} {str(lin[4]).center(3)} {str(lin[5]).center(3)} '
                              f'{str(lin[6]).center(3)} {str(lin[7]).center(3)} {str(lin[8]).center(3)}')
                    elif lin[0] == time_fora:
                        print(f'{c + 1}º ', lin[0].center(13),
                              f' {str(lin[1]).center(3)} {str(lin[2]).center(3)} {str(lin[3]).center(3)} '
                              f'{str(lin[4]).center(3)} {str(lin[5]).center(3)} {str(lin[6]).center(3)} '
                              f'{str(lin[7]).center(3)} {str(lin[8]).center(3)}')
            if not recupera:
                if partida == 1:
                    with open(campeonato + '/jogos.txt', 'wt') as a:
                        a.write(f'{time_casa} {"-" if adia else str(gols_cs)}' + '\n')
                        a.write(f'{"-" if adia else str(gols_fr)} {time_fora}' + '\n')
                    with open(campeonato + '/jogos1.txt', 'wt') as a:
                        a.write(f'{time_casa}' + '\n')
                        a.write(f'{time_fora}' + '\n')
                else:
                    with open(campeonato + '/jogos.txt', 'at') as a:
                        a.write(f'{time_casa} {"-" if adia else str(gols_cs)}' + '\n')
                        a.write(f'{str("-" if adia else gols_fr)} {time_fora}' + '\n')
                    with open(campeonato + '/jogos1.txt', 'at') as a:
                        a.write(f'{time_casa}' + '\n')
                        a.write(f'{time_fora}' + '\n')

                if adia:
                    print('\n\033[32mAtualização da partida adiada no banco de dados concluída com sucesso!\033[m')
                else:
                    print(f'\n\033[32mAtualização da {partida}ª partida no banco de dados concluída com sucesso!\033[m')
                partida += 1
                with open(caminho_partidas, 'wt') as a:
                    if partida >= qnt_partidas + 1:
                        a.write('1')
                        break
                    else:
                        a.write(str(partida))
            else:
                print(f'\n\033[32mAtualização da {jg_partida}ª partida da {jg_rodada}ª rodada, recuperada no banco de '
                      f'dados concluída com sucesso!\033[m')

        if saia:
            break

        os.remove(campeonato + '/jogos.txt')
        os.remove(campeonato + '/jogos1.txt')
        print(f'\n\033[32mAtualização da {rodada}ª rodada no banco de dados concluída com sucesso!\033[m\n')

        if rodada == qnt_rodadas:
            conn = sqlite3.connect('campeonatos.db')
            cursor = conn.cursor()
            if os.path.isfile(caminho_criterio):
                with open(caminho_criterio) as a:
                    criterio = a.read()
            else:
                criterio = '1'
            if criterio == '1':
                cursor.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, Vitórias DESC, SG DESC, GP DESC')
            elif criterio == '2':
                cursor.execute(
                    f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, Vitórias DESC, SG DESC, GP DESC, GC ASC')
            elif criterio == '3':
                cursor.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, SG DESC, GP DESC')
            result = cursor.fetchall()
            campeao = result[0][0]
            while True:  # Imprimindo o campeão após a última rodada
                print('\033[33m+\033[m' * 45)
                print('\033[33m+\033[m', ' ' * 41, '\033[33m+\033[m')
                print(f'  \033[1;33m{campeao} CAMPEÃO!!!\033[m'.center(45))
                print('\033[33m+\033[m', ' ' * 41, '\033[33m+\033[m')
                print('\033[33m+\033[m' * 45)
                back = input('\033[1;5mTecle ENTER para voltar ao menu anterior.\033[m').strip()
                if back == '':
                    break

        rodada += 1
        with open(caminho_rodada, 'wt') as a:
            a.write(str(rodada))  # Criando arquivo rodada com o número da rodada seguinte.

    else:
        os.system('clear')
        conn = sqlite3.connect('campeonatos.db')
        cursor = conn.cursor()
        if os.path.isfile(caminho_criterio):
            with open(caminho_criterio) as a:
                criterio = a.read()
        else:
            criterio = '1'
        if criterio == '1':
            cursor.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, Vitórias DESC, SG DESC, GP DESC')
        elif criterio == '2':
            cursor.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, Vitórias DESC, SG DESC, GP DESC, GC ASC')
        elif criterio == '3':
            cursor.execute(f'SELECT * FROM {campeonato} ORDER BY Pontos DESC, SG DESC, GP DESC')
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        pontuacao = result[0][2]
        campeao = result[0][0]
        print(f'\033[1mÚLTIMA RODADA DO {campeonato.upper()} JÁ CONCLUÍDA!!!\033[m')
        while True:
            print('\033[33m+\033[m' * 61)
            print('\033[33m+\033[m', ' ' * 57, '\033[33m+\033[m')
            if turno:
                print(f'  \033[1;33m{campeao.upper()} CAMPEÃO ({turno_n}) COM {pontuacao} PONTOS!!!\033[m'.center(50))
            else:
                print(f'  \033[1;33m{campeao.upper()} CAMPEÃO COM {pontuacao} PONTOS!!!\033[m'.center(50))
            print('\033[33m+\033[m', ' ' * 57, '\033[33m+\033[m')
            print('\033[33m+\033[m' * 61)
            back = input('\033[1;5mTecle ENTER para voltar ao menu anterior.\033[m').strip()
            if back == '':
                break


def jogos_realizados(campeonato, rodada, r, p):
    """
    jogos_realizados mostra os jogos realizados em uma rodada do campeonato
    :param campeonato: campeonato no qual foi realizado os jogos
    :param rodada: rodada do campeonato à ser mostrada
    :param r: Rodada atual do campeonato
    :param p: Número de partidas que aconteceu na rodada
    :return: sem retorno
    """
    os.system('clear')
    try:
        print('*' * 50)
        print(f'Jogos realizados na {rodada}ª Rodada'.center(50) if rodada != '' else
              'Todos os jogos realizados até o momento'.center(50))
        print('*' * 50)
        if rodada != '':
            print('Partidas'.center(11)+' |', 'Resultados'.center(39))
        else:
            print('Resultados'.center(50))
        print('-' * 50)
        conn = sqlite3.connect(f'{campeonato}/jogos_realizados.db')
        cursor = conn.cursor()
        if rodada == '':
            rd = 1  # Primeira rodada
            for rdd in range(rd, r if p == 1 else r+1):  # rdd: Rodada
                cursor.execute(f'SELECT * FROM Rodada{rdd}')
                jogos = cursor.fetchall()
                for jogo in jogos:
                    for results in jogo:
                        if results != jogo[0]:
                            print(
                              f'\033[32m{str(results).center(22)}\033[m' if results == jogo[1] or results == jogo[-1]
                              else str(results).center(2), end='')
                    print()
        else:
            cursor.execute(f'SELECT * FROM Rodada{rodada}')
            jogos = cursor.fetchall()
            for jogo in jogos:
                for results in jogo:
                    print(f'\033[33m{str(results).center(11)}\033[m |' if results == jogo[0] else
                          f'\033[32m{str(results).center(17)}\033[m' if results == jogo[1] or results == jogo[-1] else
                          str(results).center(2), end='')
                print()
        print('*' * 50)
    except Exception as e:
        print(f'\033[31mHouve o seguinte erro: {e}\nTalvez você tenha que adicionar uma rodada ao '
              f'"{campeonato}" primeiro.')
        sleep(12)
    else:
        while True:
            fechar = input('Tecle ENTER para sair...')
            if fechar == '':
                break
            else:
                pass
