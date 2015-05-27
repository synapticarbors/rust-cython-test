cdef extern from "rlib.h":
    double rust_double(double x)

def call_rust_double(double x):
    return rust_double(x)


    
