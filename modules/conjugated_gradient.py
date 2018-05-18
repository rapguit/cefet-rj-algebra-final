import sys

from time import time
from modules.result import Result
from modules.util import *


class ConjugatedGradient:
    def __init__(self, max_iterations, err):
        self.__max_iterations = max_iterations if max_iterations > 0 else sys.maxsize
        self.__err = err if err else 0.0
        self.__result = Result()

    def calculate(self, data, b = []):
        start = time()
        self.__execute(data, b)
        end = time()
        self.__result.set_execution_time(end - start)

    def __execute(self, data, b):
        n = data.get_size()['n']
        if len(b) == 0:
            b = init_array(n, 1.0)

        a = data
        iterative_r = init_array(n)
        previous_r = init_array(n)
        older_r = init_array(n)
        iterative_v = init_array(n)
        previous_v = init_array(n)
        iterative_p = init_array(n)
        previous_p = init_array(n)
        iterative_q = 0.0
        previous_q = iterative_q

        iteration = 0

        while iteration < self.__max_iterations:
            if iteration == 0:
                iterative_r = minus(mult_mtx(a, iterative_v), b)
                iterative_q = mult(iterative_r, iterative_r) / mult(mult_mtx(a, iterative_r), iterative_r)

            if iteration > 0:
                if iteration == 1:
                    iterative_v = minus(previous_v, mult_scalar(previous_q, previous_r))
                    iterative_p = mult_scalar(-1, iterative_r)
                    iterative_r = minus(previous_r, mult_scalar(previous_q, mult_mtx(a, previous_r)))


                if iteration > 1:
                    alpha = mult(previous_r, previous_r) / mult(older_r, older_r)
                    iterative_p = plus(mult_scalar(-1, iterative_r), mult_scalar(alpha, previous_p))

                    ap = mult_mtx(a, iterative_p)
                    iterative_q = mult(iterative_r, iterative_r) / mult(ap, iterative_p)
                    iterative_v = plus(previous_v, mult_scalar(iterative_q, iterative_p))
                    iterative_r = plus(previous_r, mult_scalar(iterative_q, ap))

                self.__result.register_iteration_vector(iterative_v, iteration, "V")

                if self.__err >= self.__calculate_err(iterative_v, previous_v):
                    break

            older_r = copy(previous_r)
            previous_r = copy(iterative_r)
            previous_q= iterative_q
            previous_v = copy(iterative_v)
            previous_p = iterative_p

            iteration += 1

        self.__result.set_solution(iterative_v)

    def __calculate_err(self, actual, previous):
        return minModOf(minus(actual, previous)) / maxModOf(actual)

    def get_result(self):
        return self.__result
    