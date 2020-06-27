from matplotlib import pyplot as plt
import numpy as np
import math  # needed for definition of pi

# x = ['A', 'B', 'C', 'D', 'E']
# y = [24, 40, 30, 50, 45]
#
# plt.plot(x, y, 'go..')
#
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.title('Line chart')
# plt.show()

# # For multiple lines ---------------------
x = ['A', 'B', 'C', 'D', 'E']
y = [24, 40, 30, 50, 45]
y1 = [10, 20, 28, 14, 35]

colors = 'red'
fig, ax = plt.subplots()
line1 = ax.plot(x, y, color='red')
line2 = ax.plot(x, y1, color='blue')

ax.legend(labels=('Math', 'English'), loc='best')  # legend placed at lower right
plt.xlabel("Name",  color='black', fontsize=14, fontweight='bold')
plt.ylabel("Marks", color='black', fontsize=14, fontweight='bold')
plt.title('Line chart', fontweight='bold', color='#3e0a75',  fontsize=18)
plt.show()
# plt.savefig('linechart.png')

