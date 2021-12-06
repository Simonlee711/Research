import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import time

# Define the right hand side term
def rhs(x,k,a):
    hook = np.zeros(x.shape)
    hook[1:-1] = x[:-2] + x[2:] - 2.*x[1:-1]
    nl = np.ones(x.shape)
    nl[1:-1] = nl[1:-1] + a*(x[2:] - x[:-2])
    return k*hook*nl

# Define leapfrog scheme, takes in current and previous state, returns next state
def leapfrog(xm,x,dt,k,a):
    return 2*x - xm + dt**2*rhs(x,k,a)

# main loop
if __name__ == "__main__":
    # Set up domain
    N = 32
    if(len(sys.argv)>1):
        N = int(sys.argv[1])
    eqPos = np.linspace(0,1,N)
    h = eqPos[1]-eqPos[0]
    # Set time domain and system properties
    c = 2.         # Wavespeed
    k = c**2/h**2  # Hook factor
    a = N/10     # Interaction strength
    Tf = 50*np.pi  # Final time
    M = int( np.ceil(Tf*np.sqrt(k)/0.5) )
    t = np.linspace(0,Tf,M)
    dt = t[1]-t[0]
    # Create FT matrix
    T = np.zeros([4,N-2])
    T[0,:] = 2*np.sin(np.pi*eqPos[1:-1])/(N+2)
    T[1,:] = 2*np.sin(2*np.pi*eqPos[1:-1])/(N+2)
    T[2,:] = 2*np.sin(3*np.pi*eqPos[1:-1])/(N+2)
    T[3,:] = 2*np.sin(4*np.pi*eqPos[1:-1])/(N+2)
    # Make room for the solution
    print("Using %d grid points and %d time steps" % (N,M))
    x = np.zeros([N,M])
    x[:,1] = dt*np.sin(np.pi*eqPos)
    # Room for modes
    p = np.zeros([4,M])
    p[:,0] = T.dot(x[1:-1,0])
    p[:,1] = T.dot(x[1:-1,1])
    # Start solving
    for m in range(1,M-1):
        x[:,m+1] = 2*x[:,m] - x[:,m-1] + dt**2*rhs(x[:,m],k,a)
        p[:,m+1] = T.dot(x[1:-1,m+1])

    # Plot animated solution
    fig,ax = plt.subplots()
    lineV,lineH = ax.plot(eqPos, x[:,0], '-ob', eqPos+x[:,0], 1.05*x.max()*np.ones(eqPos.shape), '-ob')
    ax.set_ylim([1.1*x.min(),1.1*x.max()])
    def update(i):
        lineV.set_ydata(x[:,i])
        lineH.set_xdata(eqPos+x[:,i])
        plt.title("Time = %f" % t[i])
    ani = animation.FuncAnimation(fig,update,interval=15,frames=M)
    plt.show()
    fig,ax = plt.subplots()
    plt.plot(t,p[0,:],'-k',t,p[1,:],'-r',t,p[2,:],'-g',t,p[3,:],'-b')
    plt.show()
