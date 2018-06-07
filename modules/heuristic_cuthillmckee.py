import datetime as date
import time as time
from modules.util import init_array

#REMOVER
import numpy as np

def heuristica_bandwidth(data):
    """
    Descricao
    -----------
    Reduz a largura de banda de uma matriz grande com a Heuristica RCM (Reverse-Cuthill-Mckee).
    Parametros
    ----------
    filename: O nome do arquivo da matriz (extensoes .mtx, .mtz.gz)
    Retorno
    -------
    O tempo de execucao da heuristica de reducao de largura de banda.

    Para maiores detalhes sobre a heuristica desta classe:
    --------------------------------------------------------------
    Gonzaga de Oliveira, Sanderson L., "INTRODUCAO A HEURISTICAS PARA REDUCAO DE LARGURA DE BANDA DE MATRIZES", \
    Notas em Matematica Aplicada, Volume 75, (2014). E-ISSN 2236-5915.
    Para obter novas matrizes:
    --------------------------
    https://sparse.tamu.edu
    """

    print(" Aplicando a Heuristica REVERSE-CUTHIL-MCKEE")
    t1 = time.time()
    print("\tInicio\t- ", date.datetime.fromtimestamp(t1))
    reverse_cuthill_mckee(data)
    t2 = time.time()
    print("\tTermino\t- ", date.datetime.fromtimestamp(t2))
    print(" Tempo de Execucao da Heuristica REVERSE-CUTHIL-MCKEE: ", t2 - t1)

    return (t2 - t1)


def reverse_cuthill_mckee(data):
    N = 0
    num_rows = data.get_size()['n']
    ind = data.get_ia_values()
    ptr = data.get_ja_values()
    order = init_array(num_rows)
    degree = node_degrees(ind, ptr, num_rows)

    indices = np.argsort(degree)   #SUBSTITUIR argsort
    rev_indices = np.argsort(indices) #SUBSTITUIR argsort 
    temp_degrees = init_array(max(degree)) 

    # Iniciando o Grafo
    for pos in range(num_rows):
        if indices[pos] != -1:  
            seed = indices[pos]
            order[N] = seed
            N += 1
            indices[rev_indices[seed]] = -1
            level_start = N - 1
            level_end = N

            while level_start < level_end:
                for it in range(level_start, level_end):
                    i = order[it]
                    N_old = N

                    # Adicionando vértices vizinhos
                    for idx in range(ptr[i], ptr[i + 1]): 
                        j = ind[idx]
                        if indices[rev_indices[j]] != -1:
                            indices[rev_indices[j]] = -1
                            order[N] = j
                            N += 1

                    # Adiciona valores já ordenados na lista temp_degrees
                    level_len = 0
                    for k in range(N_old, N):
                        temp_degrees[level_len] = degree[order[k]]
                        level_len += 1

                    # Insere os vértices já ordenados de forma crescente
                    for k in range(1, level_len):
                        temp = temp_degrees[k]
                        temp2 = order[N_old + k]
                        vertex = k
                        while (vertex > 0) and (temp < temp_degrees[vertex - 1]):
                            temp_degrees[vertex] = temp_degrees[vertex - 1]
                            order[N_old + vertex] = order[N_old + vertex - 1]
                            vertex -= 1
                        temp_degrees[vertex] = temp
                        order[N_old + vertex] = temp2

                # Atualiza o início e fim do próximo nível
                level_start = level_end
                level_end = N

        if N == num_rows:
            break

    # reordena o grafo
    return order[::-1]


def node_degrees(idx, ptr, num_rows):
    degree = init_array(num_rows) # criando novos vértices

    for i in range(num_rows):
        degree[i] = ptr[i + 1] - ptr[i]
        for j in range(ptr[i], ptr[i + 1]):
            if idx[j] == i:
                degree[i] += 1    # adiciona novo vértice na diagonal
                break

    return degree
