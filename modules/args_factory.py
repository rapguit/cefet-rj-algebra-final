import argparse


def create_parser():
    
    parser = argparse.ArgumentParser(description='Processamento de Matrizes com Avaliacao de Desempenho')
    parser.add_argument("maxit", nargs='?', type=int, default=100, help=': Iteracao maxima do metodo gradiente (default: max 100)')
    parser.add_argument("err", nargs='?', type=float, default=0.01, help=': Limite do erro para a convergencia (default: 0.01)')
    parser.add_argument("symetric_mode", nargs='?', type=bool, default=False, help=": True, se a Matriz for simetrica (default: False)")
    parser.add_argument("filename", type=str, help=": O nome do arquivo da matriz (extensoes .mtx, .mtz.gz)")

    return parser
