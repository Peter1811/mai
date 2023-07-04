import numpy as np
import json
import copy
from constants import STRING_FOR_OUTPUT
import sys


class Rotation:

    def __init__(self):
        pass

    def read(self, file):
        with open(file, 'r') as input_file:
            data = json.loads(input_file.read())
        self.matrix = np.array(data['A'], dtype='float64')
        self.eps = data['eps']
        self.dim = self.matrix.shape[0]
        for i in range(self.dim):
            for j in range(self.dim):
                if self.matrix[i][j] != self.matrix[j][i]:
                    print(self.matrix[i][j], self.matrix[j][i])
                    print('Matrix should be symmetric!')
                    sys.exit(0)

    def find_max_upper_element(self, A):
        n = A.shape[0]
        i_max, j_max = 0, 1
        max_elem = abs(A[0][1])
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > max_elem:
                    max_elem = abs(A[i][j])
                    i_max = i
                    j_max = j
        return i_max, j_max

    def matrix_norm(self, matrix):
        n = matrix.shape[0]
        norm = 0
        for i in range(n):
            for j in range(i + 1, n):
                norm += matrix[i][j] * matrix[i][j]
        return np.sqrt(norm)

    def rotation(self):
        n = self.matrix.shape[0]
        A_i = np.copy(self.matrix)
        eigen_vectors = np.eye(n)
        iterations = 0
        while self.matrix_norm(A_i) > self.eps:
            i_max, j_max = self.find_max_upper_element(A_i)
            if A_i[i_max][i_max] - A_i[j_max][j_max] == 0:
                phi = np.pi / 4
            else:
                phi = 0.5 * np.arctan(2 * A_i[i_max][j_max] / (A_i[i_max][i_max] -
                                                            A_i[j_max][j_max]))
            U = np.eye(n)
            U[i_max][j_max] = -np.sin(phi)
            U[j_max][i_max] = np.sin(phi)
            U[i_max][i_max] = np.cos(phi)
            U[j_max][j_max] = np.cos(phi)
            A_i = U.T @ A_i @ U
            eigen_vectors = eigen_vectors @ U
            iterations += 1
        eigen_values = np.array([A_i[i][i] for i in range(n)])
        return eigen_values, np.transpose(eigen_vectors), iterations
    
    def run(self):
        self.read('input/input4.json')
        result = self.rotation()
        eigen_values = result[0]
        eigen_vectors = result[1]
        print('\nEigen values of matrix: \n')
        for value in eigen_values:
            print(STRING_FOR_OUTPUT.format(value), end=' ')
        print('\n')
        print('Eigen vectors of matrix: \n')
        for i in range(len(eigen_vectors)):
            print(f'{i + 1} vector: ')
            for j in range(len(eigen_vectors[i])):
                print(STRING_FOR_OUTPUT.format(eigen_vectors[i][j]), end=' ')
            print()


if __name__ == '__main__':
    task4 = Rotation()
    task4.run()
