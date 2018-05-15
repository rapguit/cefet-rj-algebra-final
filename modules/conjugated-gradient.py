import sys

from modules.result import Result
from modules.util import copy
from modules.util import mult
from modules.util import mult_mtx
from modules.util import mult_scalar
from modules.util import minModOf
from modules.util import maxModOf
from modules.util import minus
from modules.util import plus


class ConjugatedGradient:
    def __init__(self, max_iterations, err):
        self.__max_iterations = max_iterations if max_iterations > 0 else sys.maxsize
        self.__err = err if err else 0.0
        self.__result = Result()

    def calculate(self):
        a = [[]]
        b = []
        iterative_r = []
        previous_r = []
        older_r = []
        iterative_v = []
        previous_v = []
        iterative_p = []
        previous_p = []
        iterative_q = 0.0
        previous_q = iterative_q

        iteration = 0

        while (iteration < max):
            iterative_r = minus(mult_mtx(a, iterative_v), b)
            iterative_q = mult(iterative_r, iterative_r) / mult(mult_mtx(a, iterative_r), iterative_r)

            if iteration > 0:
                if iteration == 1:
                    iterative_v = minus(previous_v, mult_scalar(previous_q, previous_r))
                    iterative_p = mult(-1, iterative_r)
                    iterative_r = minus(previous_r, mult_scalar(previous_q, mult_mtx(a, previous_r)))


                if iteration > 1:
                    alpha = mult(previous_r, previous_r) / mult(older_r, older_r)
                    iterative_p = plus(mult(-1, iterative_r), mult_scalar(alpha, previous_p))

                    ap = mult_mtx(a, iterative_p)
                    iterative_q = mult(iterative_r, iterative_r) / mult(ap, iterative_p)
                    iterative_v = plus(previous_v, mult_scalar(iterative_q, iterative_p))
                    iterative_r = plus(previous_r, mult_scalar(iterative_q, ap))

                self.__result.registerIterationVector(iterative_v, iteration, "V")

                if self.__err >= self.__calculate_err(iterative_v, previous_v):
                    break

            olderR = copy(previous_r)
            previousR = copy(iterative_r)
            previousQ = iterative_q
            previousV = copy(iterative_v)
            previousP = iterative_p

            iteration += 1

        self.__result.setSolution(iterative_v)

    def __calculate_err(self, actual, previous):
        return minModOf(minus(actual, previous)) / maxModOf(actual)

    def get_result(self):
        return self.__result