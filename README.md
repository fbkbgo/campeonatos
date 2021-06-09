# campeonatos
Adiciona qualquer campeonato de futebol em pontos corridos, você pode atualizar a tabela e jogos realizaos apenas adicionando o campeonato e adicionando o resultado de cada partida em cada rodada.

# changelog
Versão 0.2 31/05/2021
* Corrigido vários pequenos bugs de apresentação;
* Adicionado campeonatos pré-configurados em adic menu;
* Adicionado o Brasileirão 2021 nos campeonatos pré-configurados;
* Adicionado em tabela para o Brasileirão, classificção para Libertadores, Pré-Libertadores e Sulamericana;

Versão 0.1 29/05/2021
* Você poderá adicionar qualquer campeonato de futebol de pontos corridos do mundo e admininstra-lo pelo terminal apenas adicionando os resultados de cada partida;
* Poderá cancelar partidas no meio, adiar e restaurar também;
* Poderá consultar a tabela do campeonato, equipes participantes, jogos por rodada ou todos os jogos realizados;
* Salva todos os jogos mais os resultados no banco de dados sqlite3. Jogos adiados serão especificados e terão "*" como resultado;
* Poderá adicionar uma arquivo.txt em campeonatos/ com todas as equipes participantes do campeonato (uma equipe por linha com uma linha em branco no final) e renomea-lo para (as três primeiras letras do campeonato, sendo a primeira letra maiúscula)+_equipes.txt, exemplo: Bra_equipes.txt para Brasileirão. Eu disponibilizei um exemplo no projeto;
* E mais...



# Bugs

* Campeonatos que tenham como primeiro critério de desempate "confrontos direto" não funcionarão corretamente;

# Instalação

- apt-get update
- apt-get install git
- apt-get install python3
- git clone https://github.com/fbkbgo/campeonatos.git
- cd campeonatos/
- python3 sql_camps.py
