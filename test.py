import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import dia_matrix


a = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [0, 0, 0, 0], [-1, -1, -1, -1], [-2, -2, -2, -2], [-3, -3, -3, -3], [-4, -4, -4, -4]]
aa = [3, 2, 1, 0, -1, -2, -3, -4]
matr = dia_matrix((a, aa), shape=(8, 4))
print(matr.toarray())
