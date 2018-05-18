from pprint import pprint
from datetime import datetime

def print_stats(method):
    print('[ ' + type(method).__name__ + ' ]')
    print('[ Iteractions ]')
    pprint(method.get_result().get_iteration_vectors())
    print('[ Solution ]')
    pprint(method.get_result().get_solution())
    print('[ Summary ]')
    date = datetime.fromtimestamp(method.get_result().get_execution_time())
    print('\t Exec Time {:%S:%fs}'.format(date))
    print('\t Iteractions {}'.format(len(method.get_result().get_iteration_vectors())))
