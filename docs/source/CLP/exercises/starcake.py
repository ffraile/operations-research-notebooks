import numpy as np
from matplotlib import pyplot as plt
# Increase the default font size
plt.rcParams.update({'font.size': 15})


# With one decision variable
# z = 2.5x
# x represents kgs of pancake dough
x = np.arange(1000)

# Objective function
z = 2.5*x
plt.plot(x,z)
plt.xlim((0,800))
# add axis labels
plt.xlabel('x (pancake dough kgs)')
plt.title('z (turnover in €)')
plt.show()

# First constraint
# Time availability, 0.75 minutes per kg of dough, max 480 minutes
time = 0.75*x
plt.plot(x,time)
plt.xlim((0,800))

# Add a horizontal line at y=480
plt.axhline(y=480, color='r', linestyle='-')
# Add a vertical line at x=640
plt.axvline(x=640, color='r', linestyle='-')
# Add axis labels
plt.xlabel('x (pancake dough kgs)')
plt.ylabel('time (minutes)')
plt.show()

# Let us plot the turnover and the time constraints together
plt.plot(x,z, label='turnover')
plt.axvline(x=640, color='r', linestyle='-'
            , label='time constraint')
plt.axhline(y=1600, color='g', linestyle='-',
            label='max turnover')

plt.xlim((0,800))
plt.xlabel('x (pancake dough kgs)')
plt.title('z (turnover in €)')
plt.show()

# Second constraint
# Eggs availability, 200 grams (0.2 kg) of eggs per kg of dough, max 120 eggs
eggs = 0.2*x
plt.plot(x, eggs)
plt.axhline(y=120, color='r', linestyle='-')
plt.axvline(x=600, color='r', linestyle='-')
plt.xlabel('x (pancake dough kgs)')
plt.ylabel('eggs (kgs)')
plt.xlim((0,800))
plt.show()

# Now, let us plot the turnover and both constraints limit together
plt.plot(x,z, label='turnover')
plt.axvline(x=640, color='r', linestyle='-'
            , label='time constraint')
plt.axvline(x=600, color='r', linestyle='-'
            , label='eggs constraint')
plt.axhline(y=1500, color='g', linestyle='-',
            label='max turnover')
plt.xlabel('x (pancake dough kgs)')
plt.ylabel('z (turnover in €)')
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
plt.xlabel('x (pancake dough in kgs)')
plt.ylabel('y (pancake premium dough in kgs)')
plt.xlim((0,800))
plt.legend()
plt.show()