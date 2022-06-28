from distutils.core import setup
from Cython.Build import cythonize

import numpy

setup(
    name = 'test',
    ext_modules = cythonize('cython_main.pyx'),
    # define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
    include_dirs = [numpy.get_include()]
)

