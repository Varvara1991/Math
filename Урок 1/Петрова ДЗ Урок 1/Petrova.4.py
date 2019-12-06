import numpy as np
import matplotlib.pyplot as plt
import pylab

x = np.linspace(0,10,500)
plt.plot(x,np.cos(x),x,np.cos(5*x))
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title('Графики', fontsize=17)
pylab.legend(('y(k,x)=cos(x)', 'y(k,x)=cos(5x)'), loc = 'upper right')
#print(x)

plt.show()



