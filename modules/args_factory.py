import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Processamento de matrizes. Comparativo do Gradiente Conjugado x ????')
    parser.add_argument('--maxit', metavar='MAX', default=sys.maxsize, type=int, help='iteracao maxima do metodo gradiente (default: max int)')
    parser.add_argument('--err', metavar='E', default=0.0, type=float, help='limite do erro para a convergencia do metodo (default: 0.0)')
    parser.add_argument('mtx_file', metavar='FILE', type=str, help='the mtx file location')

    return parser
