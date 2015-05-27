from setuptools import setup, Extension, find_packages

from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext = Extension('cytest', 
          sources=['cytest.pyx'],
          libraries=['rustcython_test',],
          library_dirs=['target/release',],
          include_dirs=['.',]
)

extensions = [ext,]

setup(
    name = "cytest",
    ext_modules = cythonize(extensions),
    cmdclass={'build_ext': build_ext},
)

