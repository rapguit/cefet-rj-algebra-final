from modules.args_factory import create_parser
from modules.css_loader import load
from modules.conjugated_gradient import ConjugatedGradient

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    data = load(args.mtx_file)

    gradient = ConjugatedGradient(args.maxit, args.err)
    gradient.calculate(data)

    print(gradient.get_result())

