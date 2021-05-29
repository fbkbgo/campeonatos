# campeonatos

* Você poderá adicionar qual campeonato de futebol de pontos corridos do mundo e admininstra-lo pelo terminal apenas adicionando os resultados de cada partida;
* Poderá cancelar partidas no meio, adiar e restaurar também;
* Poderá consultar a tabela do campeonato, equipes participantes, jogos por rodada ou todos os jogos realizados;
* Salva todos os jogos mais os resultados no banco de dados sqlite3. Jogos adiados serão especificados e terão "*" como resultado;
* Poderá adicionar uma arquivo.txt em campeonatos/ com todas as equipes participantes do campeonato (uma equipe por linha cm uma linha em branco no final) e renomea-lo para (as três primeiras letras do campeonato, sendo a primeira letra maiúscula)+_equipes.txt, exemplo: Bra_equipes.txt para Brasileirão. Eu disponibilizei um exemplo no projeto;
* E mais...

# Bugs

* Campeonatos que tenham como primero critério de desempate "confrontos direto" não funcionarão corretamente;

# Instalação

- apt-get update
- apt-get install git
- apt-get install python3
- git clone https://github.com/fbkbgo/campeonatos.git
- cd campeonatos/
- python3 sql_camps.py
