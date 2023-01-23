import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1000)

# Objective function
z = 2.5*x
plt.plot(x,z)
plt.xlim((0,800))
plt.show()

# First constraint
time = 0.75*x
plt.plot(x,time)
plt.xlim((0,800))
plt.show()
# Second constraint
eggs = 0.2*x
plt.plot(x, eggs)
plt.xlim((0,800))
plt.show()

# With two decision variables
# z = 2.5x + 4*y
# 0.75*x + 0.9*y <= 480
# 0.2*x + 0.23*y <= 120

y1 = (480 - 0.75*x)/0.9
y2 = (150 - 0.2*x)/0.35

plt.plot(x, y1, label='time')
plt.plot(x, y2, label = 'eggs')
plt.ylim((0,500))
plt.xlim((0,800))
plt.legend()
plt.show()