import numpy as np
import json
from constants import ACCURACY, STRING_FOR_OUTPUT
import sys
import math
from copy import copy

class Iteration:

    def __init__(self):
        self.dim = 0

    def read(self, file):
        with open(file, 'r') as input_file:
            data = json.loads(input_file.read())
        self.matrix = np.array(data['A'], dtype='float64')
        self.free_members = np.array(data['b'], dtype='float64')
        self.eps = data['eps']
        self.dim = self.matrix.shape[0]

        lines = 0
        column = 0
        for i in range(self.dim):
            without_diag_lines = [self.matrix[i][j] for j in range(self.dim) if i != j]
            without_diag_columns = [self.matrix[j][i] for j in range(self.dim) if i != j]
            if abs(self.matrix[i][i]) >= sum([abs(i) for i in without_diag_lines]):
                lines += 1
            if abs(self.matrix[i][i]) >= sum([abs(i) for i in without_diag_columns]):
                column += 1

        if column != self.dim or lines != self.dim:
            print('Sufficient conditions doesn\'t met!')
        else:
            print('All good')
            

    def jacoby(self):
        self.free_members = self.free_members / np.diagonal(self.matrix)
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    self.matrix[i][j] = -self.matrix[i][j] / self.matrix[i][i]
            self.matrix[i][i] = 0

    def norm_of_matrix(self):
        matrix_norm = np.max([np.abs(np.sum(line)) for line in self.matrix])
        return np.round(matrix_norm, ACCURACY)

    
    def current_eps(self, x1, x2):
        amount = 0
        for i in range(len(x1)):
            amount += (x1[i] - x2[i]) ** 2
        
        return np.round((self.norm_of_matrix() / (1 - self.norm_of_matrix())) * math.sqrt(amount), ACCURACY)

    def prod_matrix_to_column(self, matrix, column):
        result = []
        for i in range(self.dim):
            current = 0
            for j in range(self.dim):
                current += matrix[i][j] * column[j]
            result.append(current)

        return result
    
    def iterations_method(self):
        x_prev = self.free_members
        x_curr = self.free_members + self.prod_matrix_to_column(self.matrix, self.free_members) 
        eps = self.current_eps(x_curr, x_prev)
        iterations = 0
        while eps >= self.eps:
            iterations += 1
            print(f'eps: {eps} ------ {self.eps}')
            x_prev = x_curr
            x_curr = self.free_members + self.prod_matrix_to_column(self.matrix, x_prev)
            eps = self.current_eps(x_curr, x_prev)

        print(f'\nNumber of iterations: {iterations}')
        return x_curr
    
    def iterations_method_zeidel(self):
        x_prev = self.free_members
        x_curr = copy(x_prev)

        for i in range(len(x_curr)):
            x_curr[i] += np.dot(self.matrix[i], x_curr)
        eps = self.current_eps(x_curr, x_prev)
        iterations = 0
        while eps >= self.eps:
            iterations += 1
            print(f'eps: {eps} ------ {self.eps}')
            x_prev = copy(x_curr)
            for i in range(len(x_curr)):
                x_curr[i] = self.free_members[i] + np.dot(self.matrix[i], x_curr)
            eps = self.current_eps(x_curr, x_prev)
            

        print(f'\nNumber of iterations: {iterations}')
        return x_curr
    
    def run(self):
        self.read('input/input3.json')
        self.jacoby()
        print('Iterations: \n')
        result_iter = self.iterations_method()
        print('\n' + 'Solutions of system: ')
        for i in result_iter:
            print(STRING_FOR_OUTPUT.format(i), end=' ')
        print('\n')   
        print('Zeildel: \n')
        result_zeidel = self.iterations_method_zeidel()
        print('\n' + 'Solutions of system: ')
        for i in result_zeidel:
            print(STRING_FOR_OUTPUT.format(i), end=' ')
        print()   
    
if __name__ == '__main__':
    task3 = Iteration()
    task3.run()
