import math
import numpy as np
import pandas as pd
from uncertainties import ufloat
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt

#angle_deg values are now actually in rad

# Data retrievel

sheet_id = "1_C5XpQi5iUlPSATJaOcr-rKgmDe35KfcF1B5BaD7Twg"
sheet_name = "PuppetPY"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url)

force_N = df[" Force (N)"]
force_N_other = df["Force other (N)"]
angle_deg = df["Angle (deg)"]

uforce_N = unumpy.uarray(df[" Force (N)"], 0.05)
uforce_N_other = unumpy.uarray(df["Force other (N)"], 0.05)
uangle_deg = unumpy.uarray(df["Angle (deg)"], 2)

#Averaging measurements

force_new = (force_N + force_N_other) / 2
uforce_new = (uforce_N + uforce_N_other) / 2
r = 0.193
err_r = 0.005
D_bruh = force_new * r / angle_deg

x_data = force_new
y_data = angle_deg

def line(x, m, c):
    return m*x + c

(m, c), cov = curve_fit(line, x_data, y_data)
#print(cov)

(m_bad, c_bad), covbad= curve_fit(line, [0.2 + 0.035, 0.5 - 0.035], [(43), (182)])

#print(r/m)
#print(r/m_bad)

um = ufloat(m, m_bad - m)
ur = ufloat(r, 0.005)
uD = ur/um
#print(uD) #Nm to Nmm
#print(c)
y_data_new = line(x_data, m, c)

plt.title("angle vs F")
#plt.plot(x_data, y_data_new, color="red")




#plt.show()


#Calculating D by averaging over Fr/angle
D_av = ufloat(0, 0)
for i in range(4):
    D_av = D_av + (uforce_new[i] * ur / uangle_deg[i])

D_av = D_av/4

print(D_av)

#Measurements for individual direction

(m1, c1), cov1 = curve_fit(line, force_N, angle_deg)
(m2, c2), cov = curve_fit(line, force_N_other, angle_deg)

y1 = line(force_N, m1, c1)
y2 = line(force_N_other, m2, c2)

plt.scatter(force_N, angle_deg, color="black")
plt.plot(force_N, y1, color="orange")
m1_bad = (0.55 - 0.1)/2.3562
m2_bad = (0.55 - 0.2)/2.3562

plt.scatter(force_N_other, angle_deg, color="blue")
plt.plot(force_N_other, y2, color="red")

um1 = ufloat(m1, m1 - m1_bad)
um2 = ufloat(m2, m2 - m2_bad)

print(ur/um1)
print(ur/um2)
#plt.show()
