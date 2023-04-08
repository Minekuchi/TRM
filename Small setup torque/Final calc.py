import math
import numpy as np
import pandas as pd
from uncertainties import ufloat
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt


# Data retrievel

sheet_id = "1_C5XpQi5iUlPSATJaOcr-rKgmDe35KfcF1B5BaD7Twg"
sheet_name = "Puppet"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url)


#Placement of masses

mass = 0.0581
r1 = 0.06
r2 = 0.108
r3 = 0.146
r4 = 0.187


#Times squared

t1 = 1.2106
t2 = 2.6374
t3 = 4.5924
t4 = 7.6743


#Plot 2mr^2 over t^2

x_data = np.array([t1, t2, t3, t4])

y_data = np.array([r1, r2, r3, r4])
y_data = 2 * mass * y_data**2


#Curve fit

def line(x, m, c):
    return m*x + c

(m, c), cov = curve_fit(line, x_data, y_data)


#Error margins taken from seperate calculations
x_bad = np.array([1.2106 + 0.0011, 7.6743 - 0.0028])
y_bad = np.array([(4.1832 - 0.4183)*0.0001, (40.6340 + 1.3038)*0.0001])

(mbad, cbad), cov = curve_fit(line, x_bad, y_bad)



D = m * 4 * 3.1416**2
err_D = abs(D - (mbad * 4 * 3.1416**2))
uD = ufloat(D, err_D)
print(f"D = :{uD}")




