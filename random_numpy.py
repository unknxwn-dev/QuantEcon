import numpy as np 

a = np.linspace(-np.pi, np.pi, 100) # Even grid with 100 elements 

b = np.cos(a)

c = np.sin(a)

# Inner product of b and c 
print(b @ c) 

np.float64(2.706168622523819e-16)