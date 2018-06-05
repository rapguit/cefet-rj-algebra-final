

import numpy as np
import datetime as date
import time as time
from modules.csr_matriz import csr_matrix

# Constants
NONSYMETRIC = "==> Execucao menos otimizada. OBS.: Para otimizar, acrescente 'True' na execucao)"
YESSYMETRIC = "==> Execucao mais otimizada ;)"

def heuristica_bandwidth(data, symetric):
    """
    Descricao
    -----------
    Reduz a largura de banda de uma Matriz grandes com a Heuristica RCM (Reverse-Cuthill-Mckee).
    Parametros
    ----------
    Symetric_mode: True (ou False), se a Matriz for simetrica (ou nao simetrica)\n
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
    reverse_cuthill_mckee(data, symetric)
    t2 = time.time()
    print("\tTermino\t- ", date.datetime.fromtimestamp(t2))
    print(" Tempo de Execucao da Heuristica REVERSE-CUTHIL-MCKEE: ", t2 - t1)

    # Sumarizando o Dataset da Matriz
    print("\n-------------------------------------------------------------------------------------------------")
    print(" [SUMARIO] - Apresentando a Matriz")
    print("-------------------------------------------------------------------------------------------------\n")
    #print(" Dimensao (NxN): \t", matriz.shape)
    #print(" Elementos NONZERO: \t", matriz.nnz)
    print(" Arquivo da Matriz: \t", data.file)

    if symetric == None or symetric == False:
        texto = NONSYMETRIC
    else:
        texto = YESSYMETRIC

    print(" Matriz Simetrica: \t", symetric, texto)

    return (t2 - t1)


def reverse_cuthill_mckee(data, symetric):

    #np.npy_intp N = 0, N_old, level_start, level_end, temp
    #zz, ii, jj, kk, ll, level_len
    N = 0
    num_rows = data.get_size()['n']
    ind = data.get_ia_values()
    ptr = data.get_ja_values()   # Precisa ser revisto!!!!!!! Aqui tem que receber uma lista de indices
    order = np.zeros(num_rows)
    degree = _node_degrees(ind, ptr, num_rows)
    print(degree)

    inds = np.argsort(degree)
    print(inds)

    rev_inds = np.argsort(inds)
    print(rev_inds)

    temp_degrees = np.zeros(int(np.max(degree)))
    print(temp_degrees)                 # Funcionando até aqui

    #def int32_or_int64 i, j, seed, temp2

    # loop over zz takes into account possible disconnected graph.
    for zz in range(num_rows):
        if inds[zz] != -1:  # Do BFS with seed=inds[zz]
            seed = inds[zz]
            order[N] = seed
            N += 1
            inds[rev_inds[seed]] = -1
            level_start = N - 1
            level_end = N

            while level_start < level_end:
                for ii in range(level_start, level_end):
                    i = order[ii]
                    N_old = N

                    # add unvisited neighbors
                    for jj in range(ptr[i], ptr[i + 1]):   # ERRO AQUI: list indices must be integers or slices, not numpy.float64
                        # j is node number connected to i
                        j = ind[jj]
                        if inds[rev_inds[j]] != -1:
                            inds[rev_inds[j]] = -1
                            order[N] = j
                            N += 1

                    # Add values to temp_degrees array for insertion sort
                    level_len = 0
                    for kk in range(N_old, N):
                        temp_degrees[level_len] = degree[order[kk]]
                        level_len += 1

                    # Do insertion sort for nodes from lowest to highest degree
                    for kk in range(1, level_len):
                        temp = temp_degrees[kk]
                        temp2 = order[N_old + kk]
                        ll = kk
                        while (ll > 0) and (temp < temp_degrees[ll - 1]):
                            temp_degrees[ll] = temp_degrees[ll - 1]
                            order[N_old + ll] = order[N_old + ll - 1]
                            ll -= 1
                        temp_degrees[ll] = temp
                        order[N_old + ll] = temp2

                # set next level start and end ranges
                level_start = level_end
                level_end = N

        if N == num_rows:
            break

    # return reversed order for RCM ordering
    return order[::-1]


def _node_degrees(ind, ptr, num_rows):
    #ii, jj
    degree = np.zeros(num_rows)

    for ii in range(num_rows):
        degree[ii] = ptr[ii + 1] - ptr[ii]
        for jj in range(ptr[ii], ptr[ii + 1]):
            if ind[jj] == ii:
                # add one if the diagonal is in row ii
                degree[ii] += 1
                break

    return degree
