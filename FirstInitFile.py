import numpy as np

"""
E = np.array([[2, -1, 0, 3],
              [1, 4, -2, 5],
              [0, -3, 1, 2]], dtype=float)#/
"""

u = np.array([2, -1, 4, 0], dtype=float)
v = np.array([-3, 5, -2, 1], dtype=float)

E = np.array([[2, -1, 0, 3],
              [1, 4, -2, 5],
              [0, -3, 1, 2]], dtype=float)

F = np.array([[1, 2],
              [-2, 0],
              [3, 1],
              [0, -1]], dtype=float)

answer = E.T @ E

print(answer)