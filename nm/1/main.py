import sys
from task_1 import LUDecomposition
from task_2 import RunThrough
from task_3 import Iteration
from task_4 import Rotation
from task_5 import QR_decomposition

if sys.argv[1] == '1':
    task = LUDecomposition()

elif sys.argv[1] == '2':
    task = RunThrough() 

elif sys.argv[1] == '3':
    task = Iteration()

elif sys.argv[1] == '4':
    task = Rotation()

elif sys.argv[1] == '5':
    task = QR_decomposition()

try:
    task.run()
except NameError:
    print('Error')
