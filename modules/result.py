from modules.util import copy

class Result:

    def __init__(self):
        self.__iteration_vectors = {}
        self.__iteration_vectors = []

    def registerIterationVector(self, vector, iteration, label):
        self.__iteration_vectors[label+'_'+str(iteration)] = copy(vector)

    def set_solution(self, sol):
        self.__solution = sol

    def get_solution(self):
        return self.__solution