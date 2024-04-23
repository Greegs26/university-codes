# reprogramming Matlab codes to Python from Electrical Engineering degree for fun
h=0.01
a=5
b=15
t0=a
#y0=exp(t0)-t0-1


n=(b-a)/h
#t=zeros(n,1)

try:
    import numpy as np
    print("NumPy is installed. Version:", np.__version__)
except ImportError:
    print("NumPy is not installed.")






