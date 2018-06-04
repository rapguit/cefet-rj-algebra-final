

import numpy as np
import datetime as date
import time as time

from scipy.io.mmio import mmread
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import reverse_cuthill_mckee

# Constants
NONSYMETRIC = "==> Execução menos otimizada. OBS.: Para otimizar, acrescente 'True' na execucao)"
YESSYMETRIC = "==> Execução mais otimizada ;)"

def heuristica_bandwidth(file, symetric):
    """
    Descrição
    -----------
    Reduz a largura de banda de uma Matriz grandes com a Heurística RCM (Reverse-Cuthill-Mckee).
    Paramêtros
    ----------
    Symetric_mode: True (ou False), se a Matriz for simetrica (ou nao simetrica)\n
    filename: O nome do arquivo da matriz (extensoes .mtx, .mtz.gz)
    Retorno
    -------
    O tempo de execução da heurística de redução de largura de banda.

    Para maiores detalhes sobre a heurística desta classe:
    --------------------------------------------------------------
    Gonzaga de Oliveira, Sanderson L., "INTRODUÇÃO A HEURÍSTICAS PARA REDUÇÃO DE LARGURA DE BANDA DE MATRIZES", \
    Notas em Matemática Aplicada, Volume 75, (2014). E-ISSN 2236-5915.
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
    print(" Dimensao (NxN): \t", matriz.shape)
    print(" Elementos NONZERO: \t", matriz.nnz)
    print(" Arquivo da Matriz: \t", file)

    if symetric == None or symetric == False:
        texto = NONSYMETRIC
    else:
        texto = YESSYMETRIC

    print(" Matriz Simétrica: \t", symetric, texto)

    return (t2 - t1)