import numpy as np
from copy import copy
import json
from constants import STRING_FOR_OUTPUT
import math

class QR_decomposition:

    def __init__(self) -> None:
        self.dim = 0

    def read(self, file):
        with open(file, 'r') as input_file:
            data = json.loads(input_file.read())
        self.matrix = np.array(data["A"])
        self.eps = data["eps"]
        self.dim = self.matrix.shape[0]
    
    def norm(self, X):
        n = X.shape[0]
        res = 0
        for x in X:
            res += x ** 2
        return math.sqrt(res)
    
    def sign(self, x):
        return x / abs(x) if x else 0


    def get_householder_matrix(self, A, col_num):
        n = A.shape[0]
        v = np.zeros(n)
        a = A[:, col_num]
        v[col_num] = a[col_num] + self.sign(a[col_num]) * self.norm(a[col_num:])
        for i in range(col_num + 1, n):
            v[i] = a[i]
        v = v[:, np.newaxis]
        H = np.eye(n) - (2 / (v.T @ v)) * (v @ v.T)
        return H


    def qr_decompose(self, A):
        """
        A = QR
        :return: Q, R
        """
        n = A.shape[0]
        Q = np.eye(n)
        A_i = np.copy(A)
        for i in range(n - 1):
            H = self.get_householder_matrix(A_i, i)
            Q = Q @ H
            A_i = H @ A_i
        return Q, A_i


    def get_roots(self, A, i):
        n = A.shape[0]
        a11 = A[i][i]
        a12 = A[i][i + 1] if i + 1 < n else 0
        a21 = A[i + 1][i] if i + 1 < n else 0
        a22 = A[i + 1][i + 1] if i + 1 < n else 0
        return np.roots((1, -a11 - a22, a11 * a22 - a12 * a21))


    def is_complex(self, A, i, eps):
        Q, R = self.qr_decompose(A)
        A_next = self.prod_matrix(R, Q)
        lambda1 = self.get_roots(A, i)
        lambda2 = self.get_roots(A_next, i)
        return abs(lambda1[0] - lambda2[0]) <= eps and \
            abs(lambda1[1] - lambda2[1]) <= eps

    @staticmethod
    def prod_matrix(matrix1, matrix2):
        l = matrix1.shape[0]
        res_matrix = np.zeros((l, l))
        for i in range(l):
            for j in range(l):
                for k in range(l):
                    res_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

        return res_matrix


    def get_eigen_value(self, A, i, eps):
        A_i = np.copy(A)
        while True:
            Q, R = self.qr_decompose(A_i)
            A_i = self.prod_matrix(R, Q)
            if self.norm(A_i[i + 1:, i]) <= eps:
                return A_i[i][i], A_i
            elif self.norm(A_i[i + 2:, i]) <= eps and self.is_complex(A_i, i, eps):
                return self.get_roots(A_i, i), A_i


    def qr_eigen_values(self, A, eps):
        n = A.shape[0]
        A_i = np.copy(A)
        eigen_values = []
        i = 0
        while i < n:
            cur_eigen_values, A_i_plus_1 = self.get_eigen_value(A_i, i, eps)
            if isinstance(cur_eigen_values, np.ndarray):
                eigen_values.extend(cur_eigen_values)
                i += 2
            else:
                eigen_values.append(cur_eigen_values)
                i += 1
            A_i = A_i_plus_1
        return eigen_values
    
    def run(self):
        self.read('input/input5.json')
        values = self.qr_eigen_values(self.matrix, self.eps)
        print('Eigen values:')
        for value in values:
            print(STRING_FOR_OUTPUT.format(value), end=' ')
        print()


if __name__ == '__main__':
    task5 = QR_decomposition()
    task5.run()