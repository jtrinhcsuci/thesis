import numpy as np
import decimal
import matplotlib.pyplot as plt
import pandas as pd

import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

# User inputs
num_of_patients = 5
sample_size = 3000
mu1 = 10
sigma1 = 1
mu2 = 20
sigma2 = 2
probability_of_bin1 = 0.7

v_d_mean = 15

def bimodal_distribution(size, mu1, sigma1, mu2, sigma2):
    random_list = np.random.rand(1, size)
    

    val_greater_than_prob = (random_list > probability_of_bin1).sum()

    val_less_than_or_equal_prob = size - val_greater_than_prob

    X1 = np.random.normal(mu1, sigma1, val_greater_than_prob)
    X2 = np.random.normal(mu2, sigma2, val_less_than_or_equal_prob)
    
    X = np.concatenate([X1, X2])

    return X


# Patient ID

patient = np.empty(sample_size)
patient.fill(1)



#Generate Data Points


#Drug Concentration

# Drug Concentration in Central Compartment
A = np.random.randint(low=1, high=100, size=sample_size) / 1000 # the "/1000" converts from grams to miligrams

K_e = bimodal_distribution(sample_size, mu1, sigma1, mu2, sigma2)

# plt.hist(K_e, 10, histtype = 'bar', facecolor = 'blue')
# plt.ylabel("Values")
# plt.xlabel("Bin Number")
# plt.title("Histogram")
# plt.axis([np.min(K_e),np.max(K_e),0, sample_size])
# plt.show()


#Rate of infusion (mL/min)
R_inf = np.random.randint(low=1, high=100, size=sample_size) / 1000 # the "/1000" converts from liters to mililiters


# def differential_eq_solver():
i = np.random.randint(0, sample_size - 1)
def dAdt(t, A):
    return -1 * K_e * A[i] + R_inf[i]
A0 = np.zeros(sample_size)

t = np.linspace(0, 1, sample_size)
A = odeint(dAdt, y0=A0, t=t, tfirst = True)


# #Apparent Volume Distribution (Unimodal Distribution)
v_d = np.random.normal(0, 0.05 * v_d_mean, sample_size)

model_concentration = np.divide(A, v_d)

# mean = np.average(model_concentration)
# #v_d = np.random.uniform(low=0, high=1, size=sample_size) #?



epilson = np.random.normal(0, 0.05, size=sample_size) #?


true_concentration = model_concentration + epilson


time_of_infusion = .5 # 500 units over half an hour time width, units of in hours, make sure that it is consistent

time_of_infusion_array = np.full(sample_size, time_of_infusion)

amount_of_infusion = 500
amount_of_infusion_array = np.full(sample_size, amount_of_infusion)
df = pd.DataFrame({'Patient ID' :  patient, 'A' : A[6], 'Elimination Rate Constant' : K_e, 'Rate of Infusion' : R_inf, 'Apparent Volume of Distribution' : v_d, 'Concentration' : true_concentration[6], 'Amount of Infusion' : amount_of_infusion_array, 'Time of Infusion' : time_of_infusion_array})



df.to_csv("Data_Points.csv", index=False)