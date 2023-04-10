import math
import numpy as np
import pandas as pd
from uncertainties import ufloat
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt

# Data retrievel

sheet_id = "1_C5XpQi5iUlPSATJaOcr-rKgmDe35KfcF1B5BaD7Twg"
sheet_name = "33"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url)

#Time squared only plate
t_noerror = 2 * df["Times (half Period) 1"]
err_t = 0.1
t = ufloat(0, 0)
for i in range(13):
    t = t + ufloat(t_noerror[i], err_t)
t = (t / 13)**2

#Times with joe squared

t_str_array = 2 * df["Times (with joe)"]
t_out_array = 2 * df["Times (with joe) (arms out)"]

t_str = ufloat(0, 0)
t_out = ufloat(0, 0)

for i in range(13):
    t_str = t_str + ufloat(t_str_array[i], 0.001)
    t_out = t_out + ufloat(t_out_array[i], 0.001)

t_str = (t_str / 13)**2
t_out = (t_out / 13)**2

#Moment of inertia with weights, Torque

h = ufloat(0.02, 0.0005)
R = ufloat(0.602, 0.001)
rho = ufloat(2700, 0)
J = (rho * h * R**4 * 3.1416) / 2

D = (4 * 3.1416**2 * J) / (t * 10)

#Final Calculation

J_str = ((D * t_str) / (4 * 3.1416**2)) - J - (61 * 0.2**2)

J_out = ((D * t_out) / (4 * 3.1416**2)) - J - (61 * 0.2**2)

J_ratio = J_out / J_str

print(f"J_str = {J_str}")
print(f"J_out = {J_out}")
print(f"J_ratio = {J_ratio}")
