# reprogramming Matlab codes to Python from Electrical Engineering degree for fun
#try:
#    import numpy as np
#    print("NumPy is installed. Version:", np.__version__)
#except ImportError:
#    print("NumPy is not installed.")
import numpy as np

h=0.01
a=5
b=15
t0=a
y0=np.exp(t0)-t0-1


n=(b-a)/h
t=np.zeros(n,1)







