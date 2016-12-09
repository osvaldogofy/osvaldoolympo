import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,5,100)
y=(2*x**2)-(8*x)-11
plt.figure("g(x)=Parabola")
plt.plot(x,y,linewidth=6,color='g',label='Grafica de g(x)')
plt.legend()
plt.title("g(x)=2x^2-8x-11")
plt.xlabel('x=[-1,5]')
plt.ylabel('Resultados de g(x)')
plt.grid(True)
plt.show()
