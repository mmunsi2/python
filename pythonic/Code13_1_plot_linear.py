
#M.M. Patrick
import matplotlib.pyplot as plt
from random import randint
from scipy import stats
import numpy as np


y = list()
xi = list()
last = 1
bound = 100
for i in range(-2, 2):
  last *= randint(0, bound)
  y=y+list([last])
  xi=xi+list([i])


xi_points = []
xi_points = np.asarray(xi)
y_points = []
y_points = np.asarray(y)

#linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
line = slope*xi_points+intercept

#Poly fit
z = np.polyfit(xi_points, y_points, 2)
f = np.poly1d(z)
z = np.polyfit(xi_points, y_points, 3)
f3 = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(xi_points[0], xi_points[-1], 50)
y_new = f(x_new)
y3_new = f3(x_new)

print(y)
print(f)
plt.plot(xi,y,'b.')
plt.plot(xi,line)
plt.plot(x_new,y_new,x_new,y3_new)
plt.show()
