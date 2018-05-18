from modules.util import copy

class Result:

    def __init__(self):
        self.__iteration_vectors = {}

    def register_iteration_vector(self, vector, iteration, label):
        key = label+'_'+str(iteration)
        self.__iteration_vectors[key] = copy(vector)

    def set_solution(self, sol):
        self.__solution = sol

    def get_solution(self):
        return self.__solution

    def get_iteration_vectors(self):
        return self.__iteration_vectors

    def set_execution_time(self, time):
        self.__exec_time = time

    def get_execution_time(self):
        return self.__exec_time
