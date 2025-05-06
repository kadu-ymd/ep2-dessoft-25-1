import random


def rolar_dados(num: int) -> list:
    return [random.randint(1, 6) for i in range(num)]

def guardar_dado(
    dados_rolados: list, dados_no_estoque: list, dado_para_guardar: list
) -> list:
    dados_novos = dados_no_estoque.copy()
    dados_rolados_final = []

    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            dados_rolados_final.append(dados_rolados[i])

    dados_novos.append(dados_rolados[dado_para_guardar])

    return [dados_rolados_final, dados_novos]

def remover_dado(dados_rolados: list, dados_no_estoque: list, dado_para_remover: int):
    new_dados_no_estoque = []
    new_dados_rolados = dados_rolados

    new_dados_rolados.append(dados_no_estoque[dado_para_remover])

    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            new_dados_no_estoque.append(dados_no_estoque[i])

    return [new_dados_rolados, new_dados_no_estoque]

def calcula_pontos_regra_simples(lista_dados: list):
    dict_pontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for dado in lista_dados:
        dict_pontos[dado] += dado

    return dict_pontos

def calcula_pontos_soma(dados_rolados: list):
    soma = 0

    for dado in dados_rolados:
        soma += dado

    return soma

def calcula_pontos_sequencia_baixa(lista_int: list):
    lista_no_rep = []

    for val in lista_int:
        if val not in lista_no_rep:
            lista_no_rep.append(val)

    lista_aux = sorted(lista_no_rep)

    for i in range(len(lista_aux) - 3):
        if lista_aux[i + 1] == lista_aux[i] + 1 and \
            lista_aux[i + 2] == lista_aux[i] + 2 and \
            lista_aux[i + 3] == lista_aux[i] + 3:
            return 15
    
    return 0

def calcula_pontos_sequencia_alta(lista_int: list):
    lista_no_rep = []

    for val in lista_int:
        if val not in lista_no_rep:
            lista_no_rep.append(val)

    lista_aux = sorted(lista_no_rep)

    for i in range(len(lista_aux) - 4):
        if lista_aux[i + 1] == lista_aux[i] + 1 and \
            lista_aux[i + 2] == lista_aux[i] + 2 and \
            lista_aux[i + 3] == lista_aux[i] + 3 and \
            lista_aux[i + 4] == lista_aux[i] + 4:
            return 30
    
    return 0

def calcula_pontos_full_house(lista_int: list):
    soma = 0
    
    val_dict = {}

    for val in lista_int:
        soma += val

        if val not in val_dict:
            val_dict[val] = 1
        else:
            val_dict[val] += 1
        
    for qtde in val_dict.values():
        if qtde not in [2, 3]:
            return 0

    if len(val_dict) == 2:
        return soma
    
def calcula_pontos_quadra(lista_int: list):
    soma = 0
    
    val_dict = {}

    for val in lista_int:
        soma += val

        if val not in val_dict:
            val_dict[val] = 1
        else:
            val_dict[val] += 1

    for qtde in val_dict.values():
        if qtde >= 4:
            return soma
    
    return 0

def calcula_pontos_quina(lista_int: list):
    val_dict = {}

    for val in lista_int:
        if val not in val_dict:
            val_dict[val] = 1
        else:
            val_dict[val] += 1

    for qtde in val_dict.values():
        if qtde >= 5:
            return 50
    
    return 0

def calcula_pontos_regra_avancada(lista_int: list):
    return {
            'cinco_iguais': calcula_pontos_quina(lista_int),
            'full_house': calcula_pontos_full_house(lista_int),
            'quadra': calcula_pontos_quadra(lista_int),
            'sem_combinacao': calcula_pontos_soma(lista_int),
            'sequencia_alta': calcula_pontos_sequencia_alta(lista_int),
            'sequencia_baixa': calcula_pontos_sequencia_baixa(lista_int)
            }

def faz_jogada(lista_dados: list, categoria: str, cartela_dict: dict):
    cartela_copy = cartela_dict.copy()

    if categoria in ["1", "2", "3", "4", "5", "6"]:
        cartela_copy["regra_simples"][int(categoria)] = calcula_pontos_regra_simples(lista_dados)[int(categoria)]
    else:
        cartela_copy["regra_avancada"][categoria] = calcula_pontos_regra_avancada(lista_dados)[categoria]
   
    return cartela_copy

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)