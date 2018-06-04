

import numpy as np
import datetime as date
import time as time

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
    print(" Arquivo da Matriz: \t", file)

    if symetric == None or symetric == False:
        texto = NONSYMETRIC
    else:
        texto = YESSYMETRIC

    print(" Matriz Simetrica: \t", symetric, texto)

    return (t2 - t1)


def reverse_cuthill_mckee(data, symetric):

    cdef np.npy_intp N = 0, N_old, level_start, level_end, temp
    cdef np.npy_intp zz, ii, jj, kk, ll, level_len
    cdef np.ndarray[int32_or_int64] order = np.zeros(num_rows, dtype=ind.dtype)
    cdef np.ndarray[int32_or_int64] degree = _node_degrees(ind, ptr, num_rows)
    cdef np.ndarray[np.npy_intp] inds = np.argsort(degree)
    cdef np.ndarray[np.npy_intp] rev_inds = np.argsort(inds)
    cdef np.ndarray[ITYPE_t] temp_degrees = np.zeros(np.max(degree), dtype=ITYPE)
    cdef int32_or_int64 i, j, seed, temp2

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
                    for jj in range(ptr[i], ptr[i + 1]):
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


cdef _node_degrees(
    np.ndarray[int32_or_int64, ndim = 1, mode = "c"] ind,
    np.ndarray[int32_or_int64, ndim = 1, mode = "c"] ptr,
    np.npy_intp num_rows):

    cdef np.npy_intp ii, jj
    cdef np.ndarray[int32_or_int64]
    degree = np.zeros(num_rows, dtype=ind.dtype)

    for ii in range(num_rows):
        degree[ii] = ptr[ii + 1] - ptr[ii]
        for jj in range(ptr[ii], ptr[ii + 1]):
            if ind[jj] == ii:
                # add one if the diagonal is in row ii
                degree[ii] += 1
                break

    return degree
