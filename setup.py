from setuptools import setup
from Cython.Build import cythonize


setup(
    name='my euclid',
    ext_modules=cythonize('euclid.pyx'),
    zip_safe=False)
