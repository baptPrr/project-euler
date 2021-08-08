import numpy as np

def pythagore(adj,base):
    hypo = np.sqrt(float(base**2 + adj**2))
    return hypo
    

print(pythagore(8000000000000,5000100))