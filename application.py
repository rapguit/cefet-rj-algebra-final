import datetime as date
import time as time

from modules.printer import print_stats
from modules.args_factory import create_parser
from modules.csr_loader import load
from modules.conjugated_gradient import ConjugatedGradient
from modules.heuristic_cuthillmckee import heuristica_bandwidth

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    print("\n============================ COMPARACAO DE DESEMPENHO: CG vs RCM ============================\n")

    # Carregando o arquivo de matriz
    data = load(args.filename)

    print("\n-------------------------------------------------------------------------------------------------")
    print(" [RELATORIO] - Descricao da Execucao")
    print("-------------------------------------------------------------------------------------------------")
    print("\n Aplicando o Metodo Iterativo GRADIENTE-CONJUGADO")
    t1 = time.time()
    print("\tInicio\t- ", date.datetime.fromtimestamp(t1))
    
    #Execucao do Gradiente Conjugado
    gradient = ConjugatedGradient(args.maxit, args.err)
    gradient.calculate(data)
    t2 = time.time()

    tGC = t2 - t1
    print("\tTermino\t- ", date.datetime.fromtimestamp(t2))
    print(" Tempo de Execucao do Metodo Iterativo GRADIENTE-CONJUGADO: ", tGC)
    print("\n")

    # Execucao da Heuristica de Reducao de Bandwidth RCM
    tRCM = heuristica_bandwidth(data)

    print("\n-------------------------------------------------------------------------------------------------")
    print(" [RESULTADO] - Avaliacao do Tempo de Execucao")
    print("-------------------------------------------------------------------------------------------------\n")

    if(tGC < tRCM):
        print(" GRADIENTE-CONJUGADO teve DESEMPENHO MELHOR que REVERSE-CUTHIL-MCKEE")
    elif (tGC > tRCM):
        print(" REVERSE-CUTHIL-MCKEE teve DESEMPENHO MELHOR que GRADIENTE-CONJUGADO")
    else:
        print(" REVERSE-CUTHIL-MCKEE e GRADIENTE-CONJUGADO tiveram DESEMPENHO SEMELHANTE")

    print("-------------------------------------------------------------------------------------------------")

    # Auxilio por help
    print("\n[Ajuda] Para conhecer os parametros, execute: 'python application.py -h'")
    print("[Exemplo] Para execucao padrao, execute: 'python application.py datasets/<FILE>.mtx' \n")

        