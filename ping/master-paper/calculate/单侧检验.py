import numpy as np
def check(p):
    tmp = (1.645+1.282)/np.log((1+p)/(1-p))
    return 4*np.power(tmp, 2) + 3

print("p=0.7, n=" + str(check(0.7)))
print("p=0.575, n=" + str(check(0.575)))