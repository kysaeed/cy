## coding: UTF-8
# cython test

# 出典:
#  小さなライオンblog
#        CythonによるPythonプログラムの高速化
#    https://www.makeitconvenient72.com/729/
#
#  Cython+Numpyでいいとこどり
#    https://qiita.com/neruoneru/items/6c0fc0496620d2968b57
#

import numpy as np
import math
import time
import cython_main
import py_main


if __name__ == "__main__":
    print('py')    
    t_start = time.time()
    py_main.func(1000000)
    pros_time = time.time() - t_start
    print("time",pros_time)
    
    print('C')    
    t_start = time.time()
    # print(cython_main)
    cython_main.func(1000000)
    pros_time = time.time() - t_start
    print("time",pros_time)


