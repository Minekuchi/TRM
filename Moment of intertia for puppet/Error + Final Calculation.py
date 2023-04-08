import math
import numpy as np
import pandas as pd
from uncertainties import ufloat
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt

# Data retrievel

sheet_id = "1_C5XpQi5iUlPSATJaOcr-rKgmDe35KfcF1B5BaD7Twg"
sheet_name = "PuppetPY"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url)

#Times squared with weight
t1w = ufloat(1.2106, 0.0011)
t2w = ufloat(2.6374, 0.0016)
t3w = ufloat(4.5924, 0.0021)
t4w = ufloat(7.6743, 0.0028)

#Times with puppet

t_str_array = df["Puppet (Standing still)"]
t_out_array = df["Puppet (Arms at sides)"]

t_str = ufloat(0, 0)
t_out = ufloat(0, 0)

for i in range(4):
    t_str = t_str + ufloat(t_str_array[i], 0.001)
    t_out = t_out + ufloat(t_out_array[i], 0.001)

t_str = (t_str / 4)**2
t_out = (t_out / 4)**2

#Moment of inertia with weights

mass = ufloat(0.0581, 0.0001)
R = ufloat(0.03, 0.0006)
r1 = ufloat(0.06, 0.003)
r2 = ufloat(0.108, 0.003)
r3 = ufloat(0.146, 0.003)
r4 = ufloat(0.187, 0.003)

J1 = mass * (R**2 + 2*r1**2)
J2 = mass * (R**2 + 2*r2**2)
J3 = mass * (R**2 + 2*r3**2)
J4 = mass * (R**2 + 2*r4**2)

#Final Calculation

J_str1 = J1 + (0.0233 / (4*3.1416**2)) * (t_str - t1w)
J_str2 = J2 + (0.0233 / (4*3.1416**2)) * (t_str - t2w)
J_str3 = J3 + (0.0233 / (4*3.1416**2)) * (t_str - t3w)
J_str4 = J4 + (0.0233 / (4*3.1416**2)) * (t_str - t4w)

J_str = (J_str1 + J_str2 + J_str3 + J_str4)/4


J_out1 = J1 + (0.0233 / (4*3.1416**2)) * (t_out - t1w)
J_out2 = J2 + (0.0233 / (4*3.1416**2)) * (t_out - t2w)
J_out3 = J3 + (0.0233 / (4*3.1416**2)) * (t_out - t3w)
J_out4 = J4 + (0.0233 / (4*3.1416**2)) * (t_out - t4w)

J_out = (J_out1 + J_out2 + J_out3 + J_out4)/4

J_ratio = J_out / J_str

print(f"J_str = {J_str}")
print(f"J_out = {J_out}")
print(f"J_ratio = {J_ratio}")
      
