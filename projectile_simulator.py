import matplotlib.pyplot as plt
import math
import numpy as np
u = float(input("Enter intial velocity: "))
theta = float(input("Enter angle: "))

g = 9.80665 


p_i = math.pi
f_theta = theta * math.pi/180
range_1 = u**2 * math.sin(2*theta*p_i/180)/g
total_time = 2*u*math.sin(f_theta)/g
def range_calci(t):
    
    x_dist = u * math.cos(f_theta) * t
    y = x_dist*math.tan(f_theta) - (g/2)*(x_dist**2)/(u*math.cos(f_theta))**2
    return x_dist,y

times = list(np.linspace(0,total_time,1000))
dist = 0
height = 0
X = []
Y =[]
for t in times:
    dist,height  = range_calci(t)
    X.append(dist)
    Y.append(height)
    
plt.plot(X,Y)
plt.show()

print(f'Time of flight: {times[-1]}')
print(f'Range: {X[-1]}')
print(f'Max height achieved: {max(Y)}')
