

import numpy as np
import datetime as date
import time as time

from scipy.io.mmio import mmread
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import reverse_cuthill_mckee

# Constants
NONSYMETRIC = "==> Execucao menos otimizada. OBS.: Para otimizar, acrescente 'True' na execucao)"
YESSYMETRIC = "==> Execucao mais otimizada ;)"

def heuristica_bandwidth(file, symetric):
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

    # Carregando o arquivo de formao Matriz Market filename
    matriz = mmread(file)

    # Convertendo com CSR uma Matriz Esparsa
    G_sparse = csr_matrix(matriz)

    print(" Aplicando a Heuristica REVERSE-CUTHIL-MCKEE")
    t1 = time.time()
    print("\tInicio\t- ", date.datetime.fromtimestamp(t1))
    reverse_cuthill_mckee(G_sparse, symetric)
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
