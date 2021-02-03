import numpy as np
from numpy import genfromtxt    
data = genfromtxt('/home/samueln/Programming/KTH/maf/datasets/power/household_power_consumption.csv', delimiter=';', skip_header=1, dtype=str)

#res = data[:,0:2]
#print(res)
#noise = np.hstack((gap_noise, voltage_noise, sm_noise, time_noise))

#export = data[:, 2:]
print(data)
#np.save("data.npy", export)