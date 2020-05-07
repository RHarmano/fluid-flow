import numpy as np
import matplotlib.pyplot as plt

R = 1
x = np.linspace(-2*R,2*R,50,endpoint=True)
y = x
[X, Y] = np.meshgrid(x,y)
r = (X**2+Y**2)**0.5
R = 1#(3*X**2+Y**2)**0.5
cos = X/r
sin = Y/r
u = 1

vec = np.array([u*(cos**2*(1-(R**2/r**2))+sin**2*(1+(R**2/r**2))),u*cos*sin*((1-(R**2/r**2))-(1+(R**2/r**2)))])
U = vec[0]
V = vec[1]

for i in range(np.shape(X)[0]):
    for j in range(np.shape(X)[1]):
        if X[i,j]**2+Y[i,j]**2 <= R:
            U[i,j] = np.NaN
            V[i,j] = np.NaN

fig,ax = plt.subplots(figsize=(15,15))
ax.quiver(X/R,Y/R,U,V)
c1 = plt.Circle((0,0),R/R,alpha=0.25)
ax.add_artist(c1)
plt.xlabel(r'$\frac{x}{R}$',size=18,weight='bold')
plt.ylabel(r'$\frac{y}{R}$',size=18,weight='bold')
plt.title('Incompressible, Inviscid Flow Around a Cylinder',size=24,weight='bold')
plt.xlim([x.min(),x.max()])
plt.ylim([y.min(),y.max()])
plt.show()