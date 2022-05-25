## coding: UTF-8
# cython test

# 出典 :小さなライオンblog
#        CythonによるPythonプログラムの高速化
#    https://www.makeitconvenient72.com/729/
#

import numpy as np
import math
import time
from cython_main import *


if __name__ == "__main__":
    t_start = time.time()
    main(1000000)
    pros_time = time.time() - t_start
    print("time",pros_time)

