import numpy as np
from constants import ACCURACY, STRING_FOR_OUTPUT
import sys
import json

class LUDecomposition:

    def __init__(self):
        self.dim = 0
        self.matrix = np.array([], dtype='float64')
        self.free_members = np.array([], dtype='float64')
        self.inversed_matrix = np.array([], dtype='float64') 

    def read(self, file):

        with open(file, 'r') as input_file:
            data = json.loads(input_file.read())
        self.matrix = np.array(data['A'], dtype='float64')
        self.free_members = np.array(data['b'], dtype='float64')
        self.eps = data['eps']

        self.inversed_matrix = np.zeros((self.dim, self.dim), dtype='float64')
        self.dim = self.matrix.shape[0]
        
        print()
        print('Source matrix: \n')
        self.print_matrix(self.matrix)

    def decomposite(self, matrix):
        result = np.zeros((matrix.shape[0], matrix.shape[1]), dtype='float64')
        result[0] = matrix[0]
        for i in range(1, self.dim):
            result[i] = matrix[i] + (- matrix[i][0] / result[0][0]) * result[0]
            result[i][0] = matrix[i][0] / result[0][0]        

        for k in range(1, self.dim - 1):
            for i in range(k + 1, self.dim):
                result[i][k + 1:] = result[i][k + 1:] + (- result[i][k] / result[k][k]) * result[k][k + 1:]
                result[i][k] = result[i][k] / result[k][k]

        return np.round(result, ACCURACY)

    def prod_matrix(self, matrix1, matrix2):
        size = matrix1.shape[0]
        result_matrix = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        return result_matrix            

    def print_matrix(self, matrix):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                print(STRING_FOR_OUTPUT.format(matrix[i][j]), end=' ')
            print()
        print()

    def reverse_course(self, matrix, b):
        size = matrix.shape[0]
        solutions = np.array([0] * size, dtype='float64')
        solutions[-1] = b[-1] / matrix[-1][-1]
        for i in range(size - 2, -1, -1):
            solutions[i] = b[i]
            for j in range(i + 1, size):
                solutions[i] -= matrix[i][j] * solutions[j]
            solutions[i] = round(solutions[i] / matrix[i][i], ACCURACY)
        solutions = np.round(solutions, ACCURACY)
        return np.reshape(solutions, (1, solutions.shape[0]))

    def determinant(self, matrix):
        return round(matrix.diagonal().prod(), ACCURACY)
    
    def find_reverse_matrix(self, matrix):
        size = matrix.shape[0]
        reversed_matrix = np.array([], dtype='float64')
        matrix_for_reversing = np.c_[matrix, np.eye(size)]
        matrix_for_reversing = self.decomposite(matrix_for_reversing)
        for column in np.transpose(matrix_for_reversing[:, matrix_for_reversing.shape[0]:]):
            sol = self.reverse_course(np.triu(matrix_for_reversing[:, :matrix_for_reversing.shape[0]]), column)
            reversed_matrix = np.append(reversed_matrix, sol)
        self.inversed_matrix = np.transpose(np.reshape(reversed_matrix, (size, size)))
    
    def check_prod(self):
        standard = np.eye(self.dim, self.dim)
        if np.count_nonzero(standard - np.eye(self.dim, self.dim) < self.eps) == self.dim ** 2:
            print('Inversed matrix is correct\n')
        else:
            print('Error!')
    
    def check_solution(self, solutions):
        solutions = solutions[0]
        if np.count_nonzero(np.array([abs(np.dot(self.matrix[i], solutions) - self.free_members[i]) < self.eps for i in range(self.dim)])):
            print('Solution is correct\n')
        else:
            print('Error!')

    def run(self):
        self.read('input/input1.json')
        arg_matrix = self.matrix
        size = arg_matrix.shape[0]
        arg_matrix = np.c_[arg_matrix, self.free_members]
        LU = self.decomposite(arg_matrix)
        U_matrix = np.triu(LU[:, :-1])
        L_matrix = np.tril(LU[:, :-1])
        np.fill_diagonal(L_matrix, 1)
        print('L-matrix: ', end='\n\n')
        self.print_matrix(L_matrix)
        print('U-matrix: ', end='\n\n')
        self.print_matrix(U_matrix)
        print('Solutions of system: \n')
        sol = self.reverse_course(U_matrix, LU[:, -1])
        self.print_matrix(sol)
        self.check_solution(sol)
        print('Determinant of matrix:\n')
        print(STRING_FOR_OUTPUT.format(self.determinant(U_matrix)))

        self.find_reverse_matrix(self.matrix)
        print('\nInversed matrix: \n')
        self.print_matrix(self.inversed_matrix)

        self.check_prod()


if __name__ == '__main__':
    task1 = LUDecomposition()
    task1.run()
