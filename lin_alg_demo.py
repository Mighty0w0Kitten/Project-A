# lin_alg_demo.py
import numpy as np

# Векторы (как строки, shape=(5,))
a = np.array([7, -4, 0, 3, 2], dtype=float)
b = np.array([-5, 1, 6, -2, 4], dtype=float)

# При как столбцы (shape=(5,1))
a_col = a.reshape(-1, 1)
b_col = b.reshape(-1, 1)

# Матрицы
E = np.array([[2, -1, 0, 3],
              [1, 4, -2, 5],
              [0, -3, 1, 2]], dtype=float)

F = np.array([[1, 2],
              [-2, 0],
              [3, 1],
              [0, -1]], dtype=float)

