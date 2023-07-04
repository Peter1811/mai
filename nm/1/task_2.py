import numpy as np
from constants import STRING_FOR_OUTPUT
import sys
import json
            
class RunThrough:
    

    def __init__(self):
        self.dim = 0

    def read(self, file):
        conditions = 0
        with open(file, 'r') as input_file:
            data = json.loads(input_file.read())
        self.matrix = list(data['A'])
        self.matrix[0].append(0)
        self.matrix[-1].append(0)
        self.matrix = np.array(self.matrix)
        self.dim = self.matrix.shape[0]
        self.free_members = np.array(data['b'])
        self.eps = data['eps']

        for i in range(self.dim):
            if abs(self.matrix[i][1]) >= abs(self.matrix[i][0]) + abs(self.matrix[i][2]):
                conditions += 1
            
            elif i >= 1 and i < self.dim - 1 and self.matrix[i][0] != 0 and self.matrix[i][2] != 0:
                conditions += 1

        if conditions:
            print('\nSufficient condition is not met\n')
            
    def run_through_method(self):
        p_1 = -self.matrix[0][1] / self.matrix[0][0]
        q_1 = self.free_members[0] / self.matrix[0][0]
        current_p = p_1
        current_q = q_1
        print('Current p and q:', end=' ')
        print(STRING_FOR_OUTPUT.format(current_p), STRING_FOR_OUTPUT.format(current_q))
        print()
        self.coefficients = []
        self.coefficients.append((p_1, q_1))
        for i in range(1, self.dim):
            p_i = -self.matrix[i][2] / (self.matrix[i][1] + self.matrix[i][0] * current_p)
            q_i = (self.free_members[i] - self.matrix[i][0] * current_q) / (self.matrix[i][1] + self.matrix[i][0] * current_p)
            current_p = p_i
            current_q = q_i
            self.coefficients.append((current_p, current_q))
            print('Current p and q:', end=' ')
            print(STRING_FOR_OUTPUT.format(current_p), STRING_FOR_OUTPUT.format(current_q))
            print()

    def reserve_course(self):
        self.solutions = [0] * self.matrix.shape[0]
        self.solutions[-1] = self.coefficients[-1][1]
        for j in range(self.dim - 2, -1, -1):
            self.solutions[j] = self.coefficients[j][0] * self.solutions[j + 1] + self.coefficients[j][1]

    def check(self):
        number_of_correct = 0
        if self.solutions[0] * self.matrix[0][0] + self.solutions[1] * self.matrix[0][1] - self.free_members[0] < self.eps:
            number_of_correct += 1
        for i in range(1, self.dim - 1):
            if np.dot(self.matrix[i], self.solutions[i - 1 : i + 2]) - self.free_members[i] < self.eps:
                number_of_correct += 1
        
        if self.solutions[-2] * self.matrix[-1][0] + self.solutions[-1] * self.matrix[-1][1] - self.free_members[-1] < self.eps:
            number_of_correct += 1
        if number_of_correct == self.dim:
            print('Solution is true')
        else:
            print('Error!')

    def run(self):
        self.read('input/input2.json')
        self.run_through_method()
        self.reserve_course()
        print('Solutions of the system: \n')
        for sol in self.solutions:
            print(STRING_FOR_OUTPUT.format(sol), end=' ')

        print('\n')
        self.check()

            
if __name__ == '__main__':
    task2 = RunThrough()
    task2.run()

