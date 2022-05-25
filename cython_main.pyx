## coding: UTF-8
# cython test
cimport cython
import numpy as np
cimport numpy as cnp
import math

ctypedef cnp.float64_t DTYPE_t

def main(int n):
    cdef int i,j
    cdef float theta = np.pi/2
    cdef float cos = np.cos(theta)
    cdef float sin = np.sin(theta)
    cdef cnp.ndarray[DTYPE_t, ndim=2] x = np.array([1.0,0.0]).reshape(-1,1)
    cdef cnp.ndarray[DTYPE_t, ndim=2] mat = np.array([[cos, -sin], [sin, cos]])
    for i in range(n):
        x = mat * x
    return