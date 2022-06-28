
import numpy as np
cimport numpy as cnp # コンパイル（コツ1）
cimport cython       # コンパイル（コツ1）
from cython import boundscheck, wraparound  # 配列チェック機能（コツ7）

ctypedef cnp.float64_t DTYPE_t  # numpyの詳細な型指定（コツ3）

cpdef double func(int n):
    cdef DTYPE_t theta = np.pi/2

    cdef DTYPE_t cos = np.cos(theta)
    cdef DTYPE_t sin = np.sin(theta)

    cdef int i                           # 変数の型指定（コツ2）
    cdef double sum                      # 変数の型指定（コツ2）
    cdef cnp.ndarray[DTYPE_t, ndim=1] A  # numpyの詳細な型指定（コツ3）
    cdef cnp.ndarray[DTYPE_t, ndim=2] mat = np.array([[cos, -sin], [sin, cos]])

    with  boundscheck(False), wraparound(False):  # 配列チェック機能を無効化（コツ7）
        A = np.array([[1.0, 2.0], [1.0, 2.0]])
        for i in range(n):
            A *= mat
        sum = 0
    return sum