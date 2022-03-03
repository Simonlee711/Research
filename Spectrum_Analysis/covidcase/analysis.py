# Simon Lee 
# AM 170A

from array import array
from random import gauss
from tkinter import N
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.fftpack import fft, ifft
from scipy import stats
import random


#from utils import period2freq, freq2period

def cos_func(times, amplitude, frequency):
    return amplitude * np.cos(frequency * times)

def Gauss(x, A, B):
    return A*np.exp(-1*B*x**2)
    
# Northern Hemisphere countries
f = open("/Users/simonlee/covidcase/north/canada.txt", "r")                                                     
lines = f.readlines()    
dates = []
canada_cases = []                                                                                                                                                                  
for line in lines:                                                                                  
    line = line.strip()                                                                             
    dates.append(line.split()[0])
    canada_cases.append(int(line.split()[4]))

f = open("/Users/simonlee/covidcase/north/india.txt", "r")                                                     
lines = f.readlines()    
india_cases = []                                                                                                                                                                   
for line in lines:                                                                                  
    line = line.strip()                                                                             
    india_cases.append(int(line.split()[1]))

f = open("/Users/simonlee/covidcase/north/russia.txt", "r")                                                     
lines = f.readlines()    
russia_cases = []                                                                                                                                                                   
for line in lines:                                                                                  
    line = line.strip()                                                                             
    russia_cases.append(int(line.split()[4]))

f = open("/Users/simonlee/covidcase/north/uk.txt", "r")                                                     
lines = f.readlines()    
uk_cases = []                                                                                                                                                                   
for line in lines:                                                                                  
    line = line.strip()                                                                             
    uk_cases.append(int(line.split()[1]))

f = open("/Users/simonlee/covidcase/north/usa.txt", "r")                                                     
lines = f.readlines()    
usa_cases = []                                                                                                                                                                   
for line in lines:                                                                                  
    line = line.strip()                                                                             
    usa_cases.append(int(line.split()[4]))

# weeks data comverter 
sum = 0
canada_week_cases = []
russia_week_cases = []
india_week_cases = []
uk_week_cases = []
usa_week_cases = []

sum = 0
for i in range(len(canada_cases)):
    sum += canada_cases[i]
    if (i+1) % 7 == 0:
        canada_week_cases.append(sum)
        sum = 0

sum = 0
for i in range(len(russia_cases)):
    sum += russia_cases[i]
    if (i+1) % 7 == 0:
        russia_week_cases.append(sum)
        sum = 0

sum = 0
for i in range(len(india_cases)):
    sum += india_cases[i]
    if (i+1) % 7 == 0:
        india_week_cases.append(sum)
        sum = 0

sum = 0
for i in range(len(uk_cases)):
    sum += uk_cases[i]
    if (i+1) % 7 == 0:
        uk_week_cases.append(sum)
        sum = 0

sum = 0
for i in range(len(usa_cases)):
    sum += usa_cases[i]
    if (i+1) % 7 == 0:
        usa_week_cases.append(sum)
        sum = 0

# Southern Hemisphere countries
f = open("/Users/simonlee/covidcase/south/argentina.txt", "r")                                                     
lines = f.readlines()    
argentina_cases = []                                                                                                                                                                   
for line in lines:                                                                                  
    line = line.strip()                                                                             
    argentina_cases.append(int(line.split()[4]))

f = open("/Users/simonlee/covidcase/south/brazil.txt", "r")                                                     
lines = f.readlines()    
brazil_cases = []                                                                                                                                                                   
for line in lines:                                                                                  
    line = line.strip()                                                                             
    brazil_cases.append(int(line.split()[4]))

f = open("/Users/simonlee/covidcase/south/indonesia.txt", "r")                                                     
lines = f.readlines()    
indonesia_cases = []                                                                                                                                                                   
for line in lines:                                                                                  
    line = line.strip()                                                                             
    indonesia_cases.append(int(line.split()[4]))

f = open("/Users/simonlee/covidcase/south/singapore.txt", "r")                                                     
lines = f.readlines()    
singapore_cases = []                                                                                                                                                                   
for line in lines:                                                                                  
    line = line.strip()                                                                             
    singapore_cases.append(int(line.split()[4]))

f = open("/Users/simonlee/covidcase/south/southafrica.txt", "r")                                                     
lines = f.readlines()    
southafrica_cases = []                                                                                                                                                                   
for line in lines:                                                                                  
    line = line.strip()                                                                             
    southafrica_cases.append(int(line.split()[5]))

# weeks data comverter 
sum = 0
argentina_week_cases = []
brazil_week_cases = []
indonesia_week_cases = []
singapore_week_cases = []
southafrica_week_cases = []

sum = 0
for i in range(len(argentina_cases)):
    sum += argentina_cases[i]
    if (i+1) % 7 == 0:
        argentina_week_cases.append(sum)
        sum = 0

sum = 0
for i in range(len(brazil_cases)):
    sum += brazil_cases[i]
    if (i+1) % 7 == 0:
        brazil_week_cases.append(sum)
        sum = 0

sum = 0
for i in range(len(indonesia_cases)):
    sum += indonesia_cases[i]
    if (i+1) % 7 == 0:
        indonesia_week_cases.append(sum)
        sum = 0

sum = 0
for i in range(len(singapore_cases)):
    sum += singapore_cases[i]
    if (i+1) % 7 == 0:
        singapore_week_cases.append(sum)
        sum = 0

sum = 0
for i in range(len(southafrica_cases)):
    sum += southafrica_cases[i]
    if (i+1) % 7 == 0:
        southafrica_week_cases.append(sum)
        sum = 0

array1 = np.linspace(1,705,705)
array2 = np.linspace(1,100,100)
array3 = np.linspace(1,20,20)

'''

# Northern Hemisphere Fast Fourier Transforms

X = fft(southafrica_week_cases)
N = len(X)
n = np.arange(N)
# get the sampling rate
sr = 1 / (60*60)
T = N/sr
freq = n/T 

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

t_h = 1/f_oneside / (60 * 60)
y = np.abs(X[:n_oneside])/n_oneside
low_values = y < 39999
y[low_values] = 0
filtered = y

# weeks graph
plt.stem(t_h, filtered,'r')
plt.xlabel("Period (Period = Weeks)")
plt.ylabel("Intensity (Counts = Cases)")
plt.title("PSD for South Africa")
plt.xlim(0,52)
plt.grid()
plt.savefig('Southafrica.png')
plt.show()

plt.title("FFT for South Africa (Frequency)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("FFT Amplitude")
plt.plot(f_oneside, np.abs(X[:n_oneside]), 'r')
plt.grid()
plt.savefig('Southafrica1.png')
plt.show()

X = fft(indonesia_week_cases)
N = len(X)
n = np.arange(N)
# get the sampling rate
sr = 1 / (60*60)
T = N/sr
freq = n/T 

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

t_h = 1/f_oneside / (60 * 60)
y = np.abs(X[:n_oneside])/n_oneside
low_values = y < 38000
y[low_values] = 0
filtered = y

# weeks graph
plt.stem(t_h, filtered, 'g')
plt.xlabel("Period (Period = Weeks)")
plt.ylabel("Intensity (Counts = Cases)")
plt.title("PSD for Indonesia")
plt.xlim(0,52)
plt.grid()
plt.savefig('Indonesia.png')
plt.show()

plt.plot(f_oneside, np.abs(X[:n_oneside]), 'g')
plt.title("FFT for Indonesia (Frequency)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("FFT Amplitude")
plt.grid()
plt.savefig('Indonesia1.png')
plt.show()


X = fft(brazil_week_cases)
N = len(X)
n = np.arange(N)
# get the sampling rate
sr = 1 / (60*60)
T = N/sr
freq = n/T 

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

t_h = 1/f_oneside / (60 * 60)
y = np.abs(X[:n_oneside])/n_oneside
low_values = y < 80000
y[low_values] = 0
filtered = y



# weeks graph
plt.stem(t_h, filtered, 'c')
plt.title("PSD for Brazil")
plt.xlabel("Period (Period = Weeks)")
plt.ylabel("Intensity (Counts = Cases)")
plt.grid()
plt.xlim(0,52)
plt.savefig('Brazil.png')
plt.show()


plt.plot(f_oneside, np.abs(X[:n_oneside]), color = 'c')
plt.title("FFT for Brazil (Frequency)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("FFT Amplitude")
plt.grid()
plt.savefig('Brazil1.png')
plt.show()


X = fft(argentina_week_cases)
N = len(X)
n = np.arange(N)
# get the sampling rate
sr = 1 / (60*60)
T = N/sr
freq = n/T 

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

t_h = 1/f_oneside / (60 * 60)
y = np.abs(X[:n_oneside])/n_oneside
low_values = y < 80000
y[low_values] = 0
filtered = y

# weeks graph
plt.stem(t_h, filtered)
plt.xlabel("Period (Period = Weeks)")
plt.ylabel("Intensity (Counts = Cases)")
plt.title("PSD for Argentina ")
plt.xlim(0,52)
plt.grid()
plt.savefig('Argentina.png')
plt.show()


plt.plot(f_oneside, np.abs(X[:n_oneside]), 'b')
plt.title("FFT for Argentina (Frequency)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("FFT Amplitude")
plt.grid()
plt.savefig('Argentina1.png')
plt.show()


# Northern Fourier Transforms

X = fft(usa_week_cases)
N = len(X)
n = np.arange(N)
# get the sampling rate
sr = 1 / (60*60)
T = N/sr
freq = n/T 

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

t_h = 1/f_oneside / (60 * 60)
y = np.abs(X[:n_oneside])/n_oneside
low_values = y < 500000
y[low_values] = 0
filtered = y

# weeks graph
plt.stem(t_h, filtered,'r')
plt.xlabel("Period (Period = Weeks)")
plt.ylabel("Intensity (Counts = Cases)")
plt.title("PSD for USA")
plt.xlim(0,52)
plt.grid()
plt.savefig('USA.png')
plt.show()

plt.plot(f_oneside, np.abs(X[:n_oneside]), 'r')
plt.title("FFT for USA (Frequency)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("FFT Amplitude")
plt.grid()
plt.savefig('USA1.png')
plt.show()


X = fft(india_week_cases)
N = len(X)
n = np.arange(N)
# get the sampling rate
sr = 1 / (60*60)
T = N/sr
freq = n/T 

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

t_h = 1/f_oneside / (60 * 60)
y = np.abs(X[:n_oneside])/n_oneside
low_values = y < 400000
y[low_values] = 0
filtered = y

# weeks graph
plt.stem(t_h, filtered, 'b')
plt.xlabel("Period (Period = Weeks)")
plt.ylabel("Intensity (Counts = Cases)")
plt.title("PSD for India")
plt.xlim(0,52)
plt.grid()
plt.savefig('India.png')
plt.show()

plt.plot(f_oneside, np.abs(X[:n_oneside]), 'b')
plt.title("FFT for India (Frequency)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("FFT Amplitude")
plt.grid()
plt.savefig('India1.png')
plt.show()


X = fft(russia_week_cases)
N = len(X)
n = np.arange(N)
# get the sampling rate
sr = 1 / (60*60)
T = N/sr
freq = n/T 

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

t_h = 1/f_oneside / (60 * 60)
y = np.abs(X[:n_oneside])/n_oneside
low_values = y < 32000
y[low_values] = 0
filtered = y

# weeks graph
plt.stem(t_h, filtered,'c')
plt.xlabel("Period (Period = Weeks)")
plt.ylabel("Intensity (Counts = Cases)")
plt.title("PSD for Russia ")
plt.xlim(0,52)
plt.grid()
plt.savefig('Russia.png')
plt.show()

plt.plot(f_oneside, np.abs(X[:n_oneside]), color = 'c')
plt.title("FFT for Russia (Frequency)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("FFT Amplitude")
plt.grid()
plt.savefig('Russia1.png')
plt.show()


X = fft(uk_week_cases)
N = len(X)
n = np.arange(N)
# get the sampling rate
sr = 1 / (60*60)
T = N/sr
freq = n/T 

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

t_h = 1/f_oneside / (60 * 60)
y = np.abs(X[:n_oneside])/n_oneside
low_values = y < 20000
y[low_values] = 0
filtered = y

# weeks graph
plt.stem(t_h, filtered, 'g')
plt.xlabel("Period (Period = Weeks)")
plt.ylabel("Intensity (Counts = Cases)")
plt.title("PSD for United Kingdom")
plt.xlim(0,52)
plt.grid()
plt.savefig('Uk.png')
plt.show()

plt.plot(f_oneside, np.abs(X[:n_oneside]), 'g')
plt.title("FFT for United Kingdom (Frequency)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("FFT Amplitude")
plt.grid()
plt.savefig('UK1.png')
plt.show()


# Cases Graphs 

plot2 = plt.figure(2)
plt.plot(array2, india_week_cases, label='India')
plt.plot(array2, russia_week_cases, 'c', label='Russia')
plt.plot(array2, uk_week_cases, label='United Kingdom')
plt.plot(array2, usa_week_cases, label='USA')
plt.axvline(x = 1,color = 'r', label = 'Spring')
plt.axvline(x = 13.85, color = 'y', label = 'Summer')
plt.axvline(x = 26.7, color = 'g', label = 'Fall')
plt.axvline(x = 39.55, color = 'b', label = 'Winter')
plt.axvline(x = 52.4, color = 'r')
plt.axvline(x = 65.25, color = 'y')
plt.axvline(x = 78.1, color = 'g')
plt.axvline(x = 90.95, color = 'b')
plt.axvline(x = 103.8, color = 'r')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.ylim((0,400000))
plt.legend(loc=2, prop={"size":6})
plt.title("Northern Hemisphere Seasonal Cases")
plt.grid()
plt.savefig('Graph1.png')

plot4 = plt.figure(4)
plt.plot(array2, india_week_cases, label='India')
plt.axvline(x = 1,color = 'r', label = 'Spring')
plt.axvline(x = 13.85, color = 'y', label = 'Summer')
plt.axvline(x = 26.7, color = 'g', label = 'Fall')
plt.axvline(x = 39.55, color = 'b', label = 'Winter')
plt.axvline(x = 52.4, color = 'r')
plt.axvline(x = 65.25, color = 'y')
plt.axvline(x = 78.1, color = 'g')
plt.axvline(x = 90.95, color = 'b')
plt.axvline(x = 103.8, color = 'r')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("India Seasonal Cases")
plt.grid()
plt.savefig('Graph3.png')
plt.show()

array4 = np.linspace(0,80,80)
for i in range(0, 20):
    india_week_cases.pop()

plt.plot(array4, india_week_cases, label='India')
plt.axvline(x = 1,color = 'r', label = 'Spring')
plt.axvline(x = 13.85, color = 'y', label = 'Summer')
plt.axvline(x = 26.7, color = 'g', label = 'Fall')
plt.axvline(x = 39.55, color = 'b', label = 'Winter')
plt.axvline(x = 52.4, color = 'r')
plt.axvline(x = 65.25, color = 'y')
plt.axvline(x = 78.1, color = 'g')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("India Seasonal Cases")
plt.grid()
plt.savefig('Graph3.1.png')
plt.show()
'''
plot5 = plt.figure(5)
plt.plot(array2, russia_week_cases, label='Russia', color = 'c')
plt.axvline(x = 1,color = 'r', label = 'Spring')
plt.axvline(x = 13.85, color = 'y', label = 'Summer')
plt.axvline(x = 26.7, color = 'g', label = 'Fall')
plt.axvline(x = 39.55, color = 'b', label = 'Winter')
plt.axvline(x = 52.4, color = 'r')
plt.axvline(x = 65.25, color = 'y')
plt.axvline(x = 78.1, color = 'g')
plt.axvline(x = 90.95, color = 'b')
plt.axvline(x = 103.8, color = 'r')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("Russia Seasonal Cases")
plt.grid()
plt.savefig('Graph4.png')
plt.show()

array4 = np.linspace(0,80,80)
for i in range(0, 20):
    russia_week_cases.pop()

plot5 = plt.figure(5)
plt.plot(array4, russia_week_cases, label='Russia', color = 'c')
plt.axvline(x = 1,color = 'r', label = 'Spring')
plt.axvline(x = 13.85, color = 'y', label = 'Summer')
plt.axvline(x = 26.7, color = 'g', label = 'Fall')
plt.axvline(x = 39.55, color = 'b', label = 'Winter')
plt.axvline(x = 52.4, color = 'r')
plt.axvline(x = 65.25, color = 'y')
plt.axvline(x = 78.1, color = 'g')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.xticks([0,40,80])
plt.legend(loc=2, prop={"size":9})
plt.title("Russia Seasonal Cases")
plt.grid()
plt.savefig('Graph4.1.png')
plt.show()

plot6 = plt.figure(6)
plt.plot(array2, uk_week_cases, label='United Kingdom',color = 'g')
plt.axvline(x = 1,color = 'r', label = 'Spring')
plt.axvline(x = 13.85, color = 'y', label = 'Summer')
plt.axvline(x = 26.7, color = 'g', label = 'Fall')
plt.axvline(x = 39.55, color = 'b', label = 'Winter')
plt.axvline(x = 52.4, color = 'r')
plt.axvline(x = 65.25, color = 'y')
plt.axvline(x = 78.1, color = 'g')
plt.axvline(x = 90.95, color = 'b')
plt.axvline(x = 103.8, color = 'r')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("United Kingdom Seasonal Cases")
plt.grid()
plt.savefig('Graph5.png')
plt.show()

array4 = np.linspace(0,80,80)
for i in range(0, 20):
    uk_week_cases.pop()

plot6 = plt.figure(6)
plt.plot(array4, uk_week_cases, label='United Kingdom',color = 'g')
plt.axvline(x = 1,color = 'r', label = 'Spring')
plt.axvline(x = 13.85, color = 'y', label = 'Summer')
plt.axvline(x = 26.7, color = 'g', label = 'Fall')
plt.axvline(x = 39.55, color = 'b', label = 'Winter')
plt.axvline(x = 52.4, color = 'r')
plt.axvline(x = 65.25, color = 'y')
plt.axvline(x = 78.1, color = 'g')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.xticks([0,40,80])
plt.legend(loc=2, prop={"size":9})
plt.title("United Kingdom Seasonal Cases")
plt.grid()
plt.savefig('Graph5.1.png')
plt.show()


plot7 = plt.figure(7)
plt.plot(array2, usa_week_cases, label='USA', color = 'r')
plt.axvline(x = 1,color = 'r', label = 'Spring')
plt.axvline(x = 13.85, color = 'y', label = 'Summer')
plt.axvline(x = 26.7, color = 'g', label = 'Fall')
plt.axvline(x = 39.55, color = 'b', label = 'Winter')
plt.axvline(x = 52.4, color = 'r')
plt.axvline(x = 65.25, color = 'y')
plt.axvline(x = 78.1, color = 'g')
plt.axvline(x = 90.95, color = 'b')
plt.axvline(x = 103.8, color = 'r')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("USA Seasonal Cases")
plt.grid()
plt.savefig('Graph6.png')

plt.show()

array4 = np.linspace(0,80,80)
for i in range(0, 20):
    usa_week_cases.pop()

plot7 = plt.figure(7)
plt.plot(array4, usa_week_cases, label='USA', color = 'r')
plt.axvline(x = 1,color = 'r', label = 'Spring')
plt.axvline(x = 13.85, color = 'y', label = 'Summer')
plt.axvline(x = 26.7, color = 'g', label = 'Fall')
plt.axvline(x = 39.55, color = 'b', label = 'Winter')
plt.axvline(x = 52.4, color = 'r')
plt.axvline(x = 65.25, color = 'y')
plt.axvline(x = 78.1, color = 'g')
plt.xlabel("Weeks")
plt.xticks([0,40,80])
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("USA Seasonal Cases")
plt.grid()
plt.savefig('Graph6.1.png')
plt.show()

##### Southern Hemisphere Graphs #######
'''
plot8 = plt.figure(8)
plt.plot(array2, argentina_week_cases, label='Argentina')
plt.plot(array2, brazil_week_cases,'c', label='Brazil')
plt.plot(array2, indonesia_week_cases, label='Indonesia')
plt.plot(array2, southafrica_week_cases, label='South Africa')
plt.axvline(x = 1,color = 'g', label = 'Fall')
plt.axvline(x = 13.85, color = 'b', label = 'Winter')
plt.axvline(x = 26.7, color = 'r', label = 'Spring')
plt.axvline(x = 39.55, color = 'y', label = 'Summer')
plt.axvline(x = 52.4, color = 'g')
plt.axvline(x = 65.25, color = 'b')
plt.axvline(x = 78.1, color = 'r')
plt.axvline(x = 90.95, color = 'y')
plt.axvline(x = 103.8, color = 'g')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.ylim((0,400000))
plt.legend(loc=2, prop={"size":9})
plt.title("Southern Hemisphere Seasonal Cases")
plt.grid()
plt.savefig('Graph7.png')
'''

plot9 = plt.figure(9)

plt.plot(array2, argentina_week_cases, label='Argentina')
plt.axvline(x = 1,color = 'g', label = 'Fall')
plt.axvline(x = 13.85, color = 'b', label = 'Winter')
plt.axvline(x = 26.7, color = 'r', label = 'Spring')
plt.axvline(x = 39.55, color = 'y', label = 'Summer')
plt.axvline(x = 52.4, color = 'g')
plt.axvline(x = 65.25, color = 'b')
plt.axvline(x = 78.1, color = 'r')
plt.axvline(x = 90.95, color = 'y')
plt.axvline(x = 103.8, color = 'g')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("Argentina Seasonal Cases")
plt.grid()
plt.savefig('Graph8.png')
plt.show()

array4 = np.linspace(0,80,80)
for i in range(0, 20):
    argentina_week_cases.pop()

plt.plot(array4, argentina_week_cases, label='Argentina')
plt.axvline(x = 1,color = 'g', label = 'Fall')
plt.axvline(x = 13.85, color = 'b', label = 'Winter')
plt.axvline(x = 26.7, color = 'r', label = 'Spring')
plt.axvline(x = 39.55, color = 'y', label = 'Summer')
plt.axvline(x = 52.4, color = 'g')
plt.axvline(x = 65.25, color = 'b')
plt.axvline(x = 78.1, color = 'r')
plt.xticks([0,40,80])
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("Argentina Seasonal Cases")
plt.grid()
plt.savefig('Graph8.1.png')
plt.show()

plot10 = plt.figure(10)
plt.plot(array2, brazil_week_cases, label='Brazil', color = 'c')
plt.axvline(x = 1,color = 'g', label = 'Fall')
plt.axvline(x = 13.85, color = 'b', label = 'Winter')
plt.axvline(x = 26.7, color = 'r', label = 'Spring')
plt.axvline(x = 39.55, color = 'y', label = 'Summer')
plt.axvline(x = 52.4, color = 'g')
plt.axvline(x = 65.25, color = 'b')
plt.axvline(x = 78.1, color = 'r')
plt.axvline(x = 90.95, color = 'y')
plt.axvline(x = 103.8, color = 'g')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("Brazil Seasonal Cases")
plt.grid()
plt.savefig('Graph9.png')
plt.show()

array4 = np.linspace(0,80,80)
for i in range(0, 20):
    brazil_week_cases.pop()

plot10 = plt.figure(10)
plt.plot(array4, brazil_week_cases, label='Brazil', color = 'c')
plt.axvline(x = 1,color = 'g', label = 'Fall')
plt.axvline(x = 13.85, color = 'b', label = 'Winter')
plt.axvline(x = 26.7, color = 'r', label = 'Spring')
plt.axvline(x = 39.55, color = 'y', label = 'Summer')
plt.axvline(x = 52.4, color = 'g')
plt.axvline(x = 65.25, color = 'b')
plt.axvline(x = 78.1, color = 'r')
plt.xlabel("Weeks")
plt.xticks([0,40,80])
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("Brazil Seasonal Cases")
plt.grid()
plt.savefig('Graph9.1.png')
plt.show()

plot11 = plt.figure(11)
plt.plot(array2, indonesia_week_cases, label='Indonesia',color = 'g')
plt.axvline(x = 1,color = 'g', label = 'Fall')
plt.axvline(x = 13.85, color = 'b', label = 'Winter')
plt.axvline(x = 26.7, color = 'r', label = 'Spring')
plt.axvline(x = 39.55, color = 'y', label = 'Summer')
plt.axvline(x = 52.4, color = 'g')
plt.axvline(x = 65.25, color = 'b')
plt.axvline(x = 78.1, color = 'r')
plt.axvline(x = 90.95, color = 'y')
plt.axvline(x = 103.8, color = 'g')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("Indonesia Seasonal Cases")
plt.grid()
plt.savefig('Graph10.png')

plot12 = plt.figure(12)
plt.plot(array2, southafrica_week_cases, label='South Africa', color = 'r')
plt.axvline(x = 1,color = 'g', label = 'Fall')
plt.axvline(x = 13.85, color = 'b', label = 'Winter')
plt.axvline(x = 26.7, color = 'r', label = 'Spring')
plt.axvline(x = 39.55, color = 'y', label = 'Summer')
plt.axvline(x = 52.4, color = 'g')
plt.axvline(x = 65.25, color = 'b')
plt.axvline(x = 78.1, color = 'r')
plt.axvline(x = 90.95, color = 'y')
plt.axvline(x = 103.8, color = 'g')
plt.xlabel("Weeks")
plt.ylabel("Total Cases")
plt.legend(loc=2, prop={"size":9})
plt.title("South Africa Seasonal Cases")
plt.grid()
plt.savefig('Graph11.png')
plt.show()

