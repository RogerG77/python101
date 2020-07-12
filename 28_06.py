import matplotlib
import matplotlib.pyplot as plt
import math
import numpy

def funktion1(x):
    return math.sin(x)

x1 = []
y1 = []
'''
for i in numpy.arange(-math.pi, math.pi, 0.1):
    x1.append(i)
    y1.append(funktion1(i))
'''
tage = [1, 2, 3, 4, 5]
temp = [23.1, 24.4, 25.5, 26.1, 24.6]


print("x:", x1)
print("y:", y1)
figure = plt.figure()
ax = plt.axes()
ax.plot(tage, temp)
figure.show()
