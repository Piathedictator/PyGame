#WP17
#17.1.1

import math
import random
import matplotlib.pyplot as plt

N=100
X = [3*math.pi*x/N for x in range (0, N+1)]
Y1 = [math.exp (-0.25*x) *math.sin(2*x) for x in X]
Y2 = [math.sin(-x) * math.cos(2*x) for x in X]

plt.plot(X, Y1, label ="exp(−0.25x)·sin(2x)")
plt.plot(X, Y2, label = "sin(−x)·cos(2x)")

plt.legend()
plt.xlim(0, 3*math.pi)
plt.grid()
plt.show()

#17.1.2

N = 40
X = [3 * math.pi * x/N for x in range (0, N+1)]
Y = [math.sin(x) * math.log10(x+0.1) for x in X]
err = [random.uniform(0.05, 0.10) for _ in X]

plt.errorbar(X, Y, yerr = err, capsize = 3, fmt = 'r+')

plt.plot(X, Y)
plt.xlim(0, 3 * math.pi)
plt.grid()
plt.show()

