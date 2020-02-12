%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,121)
plt.plot(x,np.cos(x+1))
plt.plot(x,np.cos(x +8))
