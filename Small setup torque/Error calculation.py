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

m = 0.0581
r1 = ufloat(0.06, 0.003)
r2 = ufloat(0.108, 0.003)
r3 = ufloat(0.146, 0.003)
r4 = ufloat(0.187, 0.003)

#Averaging times

t1_array = df["Period (s) (Weight 5)  (6.0 cm)"]
t2_array = df["Period (s) (Weight 5)  (10.8 cm)"]
t3_array = df["Period (s) (Weight 5)  (14.6 cm)"]
t4_array = df["Period (s) (Weight 5)  (18.7 cm)"]

t1 = ufloat(0, 0)
t2 = ufloat(0, 0)
t3 = ufloat(0, 0)
t4 = ufloat(0, 0)

for i in range(4):
    t1 = t1 + ufloat(t1_array[i], 0.001)
    t2 = t2 + ufloat(t2_array[i], 0.001)
    t3 = t3 + ufloat(t3_array[i], 0.001)
    t4 = t4 + ufloat(t4_array[i], 0.001)

t1 = (t1/4)**2
t2 = (t2/4)**2
t3 = (t3/4)**2
t4 = (t4/4)**2

#y = mr^2

y1 = 2*m*r1**2
y2 = 2*m*r2**2
y3 = 2*m*r3**2
y4 = 2*m*r4**2

