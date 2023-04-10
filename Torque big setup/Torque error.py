import math
import numpy as np
import pandas as pd
from uncertainties import ufloat
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt

# Data retrievel

sheet_id = "1_C5XpQi5iUlPSATJaOcr-rKgmDe35KfcF1B5BaD7Twg"
sheet_name = "22"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url)

angle_rad = df["Angle (rad)"]
force_N = df["Force act. ccw"]
force_N_other = df["Force act. cw"]
radius = 0.602

err_angle = 0.0349
err_force = 0.25
err_r = 0.001

#curve fit

def line(x, m, c):
    return m*x + c

(m1, c1), cov1 = curve_fit(line, angle_rad, force_N)

(m2, c2), cov2 = curve_fit(line, angle_rad, force_N_other)

x_bad = np.array([0.1745 + err_angle, 1.571 - err_angle])
y1_bad = np.array([2.5 + err_force, 11.5 - err_force])
y2_bad = np.array([2.5 + err_force, 13.5 - err_force])

(m1_bad, c1_bad), cov3 = curve_fit(line, x_bad, y1_bad)
(m2_bad, c1_bad), cov4 = curve_fit(line, x_bad, y2_bad)

#calculation

r = ufloat(radius, err_r)
um1 = ufloat(m1, abs(m1 - m1_bad))
um2 = ufloat(m2, abs(m2 - m2_bad))

um = (um1 + um2) / 2

D = r * um

print(f"D = {D}Nm")

#visualization

force_N_fit = angle_rad * m1 + c1
force_N_other_fit = angle_rad * m2 + c2

plt.scatter(angle_rad, force_N, color="red")
plt.plot(angle_rad, force_N_fit, color="red")
plt.scatter(angle_rad, force_N_other, color="blue")
plt.plot(angle_rad, force_N_other_fit, color="blue")

plt.show()


