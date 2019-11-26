import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def plot_3D(xs, ys, zs, labels=('x','y','z')):
    plt.figure(figsize=(10,10))
    ax = plt.axes(projection='3d')

    ax.contour3D(xs,ys,zs,300)
    
    x,y,z = labels
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)

def plot_xzp(wonderland_zustand):
    plt.plot([(x,z,p) for x,_,z,p in wonderland_zustand])
    plt.show()