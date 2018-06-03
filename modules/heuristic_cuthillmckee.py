

import argparse
import numpy as np
import datetime as date
import time as time

from scipy.io.mmio import mmread
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import reverse_cuthill_mckee

def heuristica_bandwidth(file, symetric):
    """
    Descrição
    -----------
    Reduz a largura de banda de uma Matriz grandes com a Heurística Reverse-Cuthill-Mckee.
    Paramêtros
    ----------
    Symetric_mode: True (ou False), se a Matriz for simetrica (ou nao simetrica)\n
    filename: O nome do arquivo da matriz (extensoes .mtx, .mtz.gz)
    Retorno
    -------
    O tempo de execução da heurística de redução de largura de banda.
    Para acessar a coleção de matrizes esparsas: https://sparse.tamu.edu
    -------------------------------------------------------------------- 
    """

    # Carregando o arquivo de formao Matriz Market filename
    matriz = mmread(file)
    print("\nApresentando a Matriz:")
    print("\tDimensao (M): ", matriz.shape)
    print("\tElementos NONZERO: ", matriz.nnz)
    print("\tArquivo da Matriz: ", file)

    # Convertendo com CSR uma Matriz Esparsa
    G_sparse = csr_matrix(matriz)

    print("\nAplicando a Heuristica REVERSE-CUTHIL-MCKEE")
    t1 = time.time()
    print("\tInicio\t- ", date.datetime.fromtimestamp(t1))
    reverse_cuthill_mckee(G_sparse, symetric)
    t2 = time.time()
    print("\tTermino\t- ", date.datetime.fromtimestamp(t2))
    print("Tempo de Execucao da Heuristica REVERSE-CUTHIL-MCKEE: ", t2 - t1)
    print("\n")


if __name__ == '__main__':
    
    # Definição dos argumentos de execução
    parser = argparse.ArgumentParser(description="Tempo de Execucao da Heuristica para Reducao de Largura de Banda")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verboso", help="Execucao em tela", action="store_true")
    group.add_argument("-q", "--silencioso", help="(Default) Execucao em background", action="store_true")
    parser.add_argument("symetric_mode", type=bool, help=": True (ou False), se a Matriz for simetrica (ou nao)")
    parser.add_argument("filename", type=str, help=": O nome do arquivo da matriz (extensoes .mtx, .mtz.gz)")
    args = parser.parse_args()

    if args.silencioso:
        print("Estao faltando argumentos")
    elif args.verboso:
        print("A Reducao de Largura de Banda vai ser aplicada na Matriz (*.mtx) {} com forma SIMETRICA = {}.".format(args.filename, args.symetric_mode))

    # Executa a heuristica
    heuristica_bandwidth(args.filename, args.symetric_mode)
