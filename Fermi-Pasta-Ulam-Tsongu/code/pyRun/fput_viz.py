'''
Python module to run the Fermi-Pasta-Ulam-Tsingou simulation

Overall this code is kinda dirty and I am sure there is a far more efficeint way to plot these but we plot them anyway.
'''
__author__ = 'Simon Lee: siaulee@ucsc.edu'

import os
import numpy as np
import matplotlib.pyplot as plt
import math

path = '/Users/simonlee/leesimon-am129-fall21/Project/'

def rebuild():
    os.chdir(path + "code/fortran")
    os.system('make clean')
    os.chdir(path)

def build():
    os.chdir(path + "code/fortran")
    os.system('make')
    os.chdir(path)

def generate_input(N,a):
    
    exists = os.path.exists(path + "code/fortran/FPUT.init")
    backup = (path + "code/fortran/FPUT.init")
    if exists:
        os.chdir(path + "code/fortran")
        os.rename('FPUT.init','FPUT.init.bak') 
    # write into a file
    init_file = open(backup,"w+")
    # write 3 lines into init file
    
    init_file.write('num_masses '+ str(N) + '\n')
    init_file.write('alpha ' + str(a) + '\n')
    init_file.write('run_name FPUT_'+ str(N) + '_' + str(a))
    init_file.close()

def run_FPUT(N,a):
    build()
    generate_input(N,a)
    os.chdir(path + "code/fortran")
    os.system('./fput')
    os.chdir(path)

def clean():
    os.chdir(path + "code/fortran/data")
    os.system('rm *.dat')
    os.chdir(path)

def run_all():
    # linear osicllators
    run_FPUT(1, 0.0)

    run_FPUT(8, 0.0)
    run_FPUT(8, (8.0/10.0))
    run_FPUT(8, (-8.0/10.0))
    
    run_FPUT(16, 0.0)
    run_FPUT(16, (16.0/10.0))
    run_FPUT(16, (-16.0/10.0))

    run_FPUT(32, 0.0)
    run_FPUT(32, (32.0/10.0))
    run_FPUT(32, (-32.0/10.0))

def plot_fput_1():
    # Set range and space to store data
    plot1 = np.zeros(4)
    fname = path + 'code/fortran/data/FPUT_1_0.0.Tf.dat'
    data = np.loadtxt(fname)
    plot1 = data[:,1]
    time = np.array([ (10*math.pi)/4, (10*math.pi)/2, (3*10*math.pi)/4, (10*math.pi) ])
    
    # Generate a plot of the eigenvalues as a function of the parameter q
    plt.plot(time,plot1,'-k')
    plt.grid()
    plt.ylabel('Values')
    plt.xlabel('Final Time')
    plt.title("Final Time graph: N = 1");
    plt.savefig(path+'report/figures/n1mass.png')
    plt.show()
    


def plot_fput_linear(fname, fname2, fname3, fname4, fname5, fname6, N1, N2, N3):
    '''
    We plot the equations

    For N = 8, alpha = 0.0, N1 = 692
    For N = 16, alpha = 0.0, N2 = 1194
    For N = 32, alpha = 0.0, N3 = 2200  
    '''

    # time array for first column graphs
    time = np.array([ (10*math.pi)/4, (10*math.pi)/2, (3*10*math.pi)/4, (10*math.pi) ], ) # time array
    
    # second array for x-axis of second column graphs
    x_axis_1 = np.arange(1, N1+1)
    x_axis_2 = np.arange(1, N2+1)
    x_axis_3 = np.arange(1, N3+1)

  
    # intialize 3 size 4xN arrays 
    plot1 = np.zeros((4, 8))
    plot2 = np.zeros((4, 16))
    plot3 = np.zeros((4, 32))
    
    # load data in properly for these arrays
    data = np.loadtxt(path + fname)
    plot1 = data[:,1:9]
    data2 = np.loadtxt(path + fname2)
    plot2 = data2[:,1:17]
    data3 = np.loadtxt(path + fname3)
    plot3 = data3[:,1:33]
    
    # initialize 3 i = N/2 arrays 
    plot4 = np.zeros(N1)
    plot5 = np.zeros(N2)
    plot6 = np.zeros(N3)

    # load in data for i = N/2 weight
    data = np.loadtxt(path + fname4)
    plot4 = data[:]
    data = np.loadtxt(path + fname5)
    plot5 = data[:]
    data = np.loadtxt(path + fname6)
    plot6 = data[:]


    # Generate a plot of the eigenvalues as a function of the parameter q
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
    fig.suptitle((r'Fermi-Pasta-Ulam-Tsongu - Linear Oscillation: $\alpha = 0.0$'))
    ax1.plot(time, plot1)
    ax2.plot(x_axis_1, plot4,'-k')
    ax3.plot(time, plot2)
    ax4.plot(x_axis_2, plot5,'--b') 
    ax5.plot(time, plot3) 
    ax6.plot(x_axis_3, plot6,'-.r') 
    plt.ylabel('mass position')
    plt.xlabel('time')
    plt.savefig(path+ 'report/figures/FPUT1.png')
    plt.show()


def plot_fput_nonlinear(fname, fname2, fname3, fname4, fname5, fname6, N1, N2, N3):
    '''
    For N = 8, alpha = 0.8, N1 = 1383
    For N = 16, alpha = 1.6, N2 = 2388
    For N = 32, alpha = 3.2, N3 = 4399 
    '''

    # Set x-axis for column 1 graph
    time = np.array([ (10*math.pi)/4, (10*math.pi)/2, (3*10*math.pi)/4, (10*math.pi) ], ) # time array
    
    # Set x-axis for column 2 graph
    x_axis_1 = np.arange(1, N1+1)
    x_axis_2 = np.arange(1, N2+1)
    x_axis_3 = np.arange(1, N3+1)

    # intialize 3 size 4xN arrays 
    plot1 = np.zeros((4, 8))
    plot2 = np.zeros((4, 16))
    plot3 = np.zeros((4, 32))

    # load in data for 4xN arrays
    data = np.loadtxt(path + fname)
    plot1 = data[:,1:9]
    data2 = np.loadtxt(path + fname2)
    plot2 = data2[:,1:17]
    data3 = np.loadtxt(path + fname3)
    plot3 = data3[:,1:33]
    
    # intialize 3 arrays for the i = N/2 graph
    plot4 = np.zeros(N1)
    plot5 = np.zeros(N2)
    plot6 = np.zeros(N3)

    # load in data for i = N/2 weight
    data = np.loadtxt(path + fname4)
    plot4 = data[:]
    data = np.loadtxt(path + fname5)
    plot5 = data[:]
    data = np.loadtxt(path + fname6)
    plot6 = data[:]


    # Generate a plot of the eigenvalues as a function of the parameter q
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
    fig.suptitle((r'Fermi-Pasta-Ulam-Tsongu - Non Linear Oscillation: $\alpha = \mathbb{R}$'))
    ax1.plot(time, plot1)
    ax2.plot(x_axis_1, plot4,'-k')
    ax3.plot(time, plot2)
    ax4.plot(x_axis_2, plot5,'--b') 
    ax5.plot(time, plot3) 
    ax6.plot(x_axis_3, plot6,'-.r') 
    plt.ylabel('mass position')
    plt.xlabel('time')
    plt.savefig('report/figures/FPUT2.png')
    plt.show()


def plot_fput_nonlinear_neg(fname, fname2, fname3, fname4, fname5, fname6, N1, N2, N3):
    '''
    For N = 8, alpha = -0.8, N1 = 1383
    For N = 16, alpha = -1.6, N2 = 2388
    For N = 32, alpha = -3.2, N3 = 4399 
    '''

    # Set x-axis for column 1 graph
    time = np.array([ (10*math.pi)/4, (10*math.pi)/2, (3*10*math.pi)/4, (10*math.pi) ], ) # time array
    
    # Set x-axis for column 2 graph
    x_axis_1 = np.arange(1, N1+1)
    x_axis_2 = np.arange(1, N2+1)
    x_axis_3 = np.arange(1, N3+1)

    # intialize 3 size 4xN arrays 
    plot1 = np.zeros((4, 8))
    plot2 = np.zeros((4, 16))
    plot3 = np.zeros((4, 32))

    # load in data for 4xN arrays
    data = np.loadtxt(path + fname)
    plot1 = data[:,1:9]
    data2 = np.loadtxt(path + fname2)
    plot2 = data2[:,1:17]
    data3 = np.loadtxt(path + fname3)
    plot3 = data3[:,1:33]
    
    # intialize 3 arrays for the i = N/2 graph
    plot4 = np.zeros(N1)
    plot5 = np.zeros(N2)
    plot6 = np.zeros(N3)

    # load in data for i = N/2 weight
    data = np.loadtxt(path + fname4)
    plot4 = data[:]
    data = np.loadtxt(path + fname5)
    plot5 = data[:]
    data = np.loadtxt(path + fname6)
    plot6 = data[:]


    # Generate a plot of the eigenvalues as a function of the parameter q
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
    fig.suptitle((r'Fermi-Pasta-Ulam-Tsongu - Non Linear Oscillation: $\alpha = - \mathbb{R}$'))
    ax1.plot(time, plot1)
    ax2.plot(x_axis_1, plot4,'-k')
    ax3.plot(time, plot2)
    ax4.plot(x_axis_2, plot5,'--b') 
    ax5.plot(time, plot3) 
    ax6.plot(x_axis_3, plot6,'-.r') 
    plt.ylabel('mass position')
    plt.xlabel('time')
    plt.savefig('report/figures/FPUT3.png')
    plt.show()


if __name__=="__main__":
    clean()
    build()
    run_all()
    rebuild()
    plot_fput_1()
    plot_fput_linear('code/fortran/data/FPUT_8_0.0.Tf.dat','code/fortran/data/FPUT_16_0.0.Tf.dat','code/fortran/data/FPUT_32_0.0.Tf.dat',\
        'code/fortran/data/FPUT_8_0.0.Ndiv2.dat', 'code/fortran/data/FPUT_16_0.0.Ndiv2.dat', 'code/fortran/data/FPUT_32_0.0.Ndiv2.dat',\
            692,1194,2200)
    plot_fput_nonlinear('code/fortran/data/FPUT_8_0.8.Tf.dat','code/fortran/data/FPUT_16_1.6.Tf.dat','code/fortran/data/FPUT_32_3.2.Tf.dat',\
        'code/fortran/data/FPUT_8_0.8.Ndiv2.dat', 'code/fortran/data/FPUT_16_1.6.Ndiv2.dat', 'code/fortran/data/FPUT_32_3.2.Ndiv2.dat',\
            1383,2388,4399)
    plot_fput_nonlinear_neg('code/fortran/data/FPUT_8_-0.8.Tf.dat','code/fortran/data/FPUT_16_-1.6.Tf.dat','code/fortran/data/FPUT_32_-3.2.Tf.dat',\
        'code/fortran/data/FPUT_8_-0.8.Ndiv2.dat', 'code/fortran/data/FPUT_16_-1.6.Ndiv2.dat', 'code/fortran/data/FPUT_32_-3.2.Ndiv2.dat',\
            1383,2388,4399)
