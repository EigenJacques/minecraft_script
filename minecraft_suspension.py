#%%
import numpy as np
from matplotlib import pyplot as plt

#%%

L = 148-125
H = 4
rho = 0.1
T = np.linspace(0.2,3,10)

x = np.arange(-L/2,L/2,1)+0.5


for t in T:
    y = t/rho*np.cosh(rho*x/t) - t/rho
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot()
    ax.scatter(x,np.round(y/np.max(y)*H*2,0)/2, label=f't = {t}', marker="s", s=1000)
    ax.scatter(x,0.5+np.round(y/np.max(y)*H*2,0)/2, label=f't = {t}', marker="s", s=1000, c="w")
    ax.plot(x,y/np.max(y)*H*2/2-0.25, label=f't = {t}', c="r")
    ax.set_aspect("equal")
    ax.set_ylim(-0.5,4.5)
    ax.set_xticks(np.arange(-L/2,L/2+1,1)+0.5)
    ax.set_yticks(np.arange(0,H,0.5))
    ax.grid()
plt.legend()

# %%
