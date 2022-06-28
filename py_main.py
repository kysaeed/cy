import numpy as np

def func(n):
    theta = np.pi/2
    cos = np.cos(theta)
    sin = np.sin(theta)
    A = np.array([[1.0, 2.0], [1.0, 2.0]])
    mat = np.array([[cos, -sin], [sin, cos]])
    for i in range(n):
        A *= mat

    sum = 0
    return sum

