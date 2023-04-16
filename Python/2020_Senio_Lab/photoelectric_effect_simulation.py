import numpy as np
import matplotlib.pyplot as plt


"""
KE = hf - W 

f = c/lambda

def current_vs_voltage():
    f = c/wl
    
    V = h * f/e - W/e
    
    #I = 

    return V

def current_vs_intensity():
    
    eV = h * f - W
    
    return eV

"""

#Constants
c = 3e17
h = 4.136e-15

# Materials dictionary to be used later
materials = {"Copper": {
        "work_function": 4.65
    },
    "Sodium": {
        "work_function": 2.75
    },
    "Aluminium": {
        "work_function": 4.28
    },
    "Zinc":{
        "work_function": 4.47
    },
    "Platinum":{
        "work_function": 5.65
    },
    "Calcium":{
        "work_function": 3.20
    }
}


def energy_vs_frequency():
    
    wl = np.arange(100,850,10)
    
    frequency = np.zeros(len(wl))
    eV = np.empty(len(wl))
    
    work_function = float(materials[input("Please choose a material (Copper, Sodium, Aluminium, Zinc, Platinum, Calcium): ")]['work_function'])
    
    for i in range(len(wl)):
        frequency[i] = c/wl[i]
        eV[i] = h * frequency[i] - work_function
           
        if eV[i] <= 0:
            eV[i] = 0
        
        
    return eV, frequency, wl


eV,freq,wl = energy_vs_frequency()




#Plotting
plt.figure(1)
plt.plot(wl,eV,'.') 
plt.xlabel("Wavelength (nm)")
plt.ylabel("Energy (eV)")
plt.grid()
    
plt.figure(2)
plt.plot(freq,eV,'.')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Energy (eV)")
plt.grid()

#Curve Fit
def func(x,m,b):
    return m*x + b

pos = np.where(eV > 0)
popt, pcov = curve_fit(func,freq[pos],eV[pos]) 

# slope: h(Plancks) y-int: Work function
h,W = popt

# Threshold wavelength at which photons become excited 
freq_th = -W/h
wl_th = c/freq_th 


plt.figure(2)
plt.plot(freq[pos],func(freq[pos],*popt), 'k--', label= f'Line of best fit, h = {h:.3e} eV, $\lambda$$_{{th}}$={wl_th:.2f} nm')
plt.legend()
plt.show()


