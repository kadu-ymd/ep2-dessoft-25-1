from funcoes import *

dados = [3, 3, 1, 2, 3]
categoria = "3"
cartela_de_pontos = {
    'regra_simples':  {
        1:3,
        2:2,
        3:-1,
        4:-1,
        5:20,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': 6,
        'full_house': -1,
        'sequencia_baixa': 15,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

print(faz_jogada(dados, categoria, cartela_de_pontos))