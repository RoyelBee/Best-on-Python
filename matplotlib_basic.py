from matplotlib import pyplot as plt

# x = ['A', 'B', 'C', 'D', 'E']
# y = [24, 40, 30, 50, 45]
#
# plt.plot(x, y, color='red')
#
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.title('Line chart')
# plt.show()

# # For multiple lines ---------------------
# x = ['A', 'B', 'C', 'D', 'E']
# y = [24, 40, 30, 50, 45]
# z = [10, 20, 28, 14, 35]
#
#
# fig, ax = plt.subplots()
# line1 = ax.plot(x, y, color='red')
# line2 = ax.plot(x, z, color='blue')
#
# ax.legend(labels=('Math', 'English'), loc='best')  # legend placed at lower right
# plt.xlabel("Name",  color='black', fontsize=14, fontweight='bold')
# plt.ylabel("Marks", color='black', fontsize=14, fontweight='bold')
# plt.title('Line chart', fontweight='bold', color='#3e0a75',  fontsize=18)
#
# plt.show()
# plt.tight_layout()
# plt.savefig('linechart.png')


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

# # --------------------------------------------------
# #  ------ Final Format -----------------------------

x = ['Habib', 'Raihan', 'Rocky', 'Kabir']
y = [30000, 100000, 40000, 20000]
z = [50000, 10000, 60000, 100000]

fig, ax = plt.subplots(figsize=(6.4, 4.8))
ax.plot(x, y, color='red', linewidth=2)
ax.plot(x, z, color='blue', linewidth=2)

for a, b in zip(x, y):
    plt.text(a, b, str(int(b / 1000)) + 'K',
             ha='center', va='bottom',
             fontsize=9, fontweight='bold')

for a, b in zip(x, z):
    plt.text(a, b, str(b) + ' K',
             ha='center', va='bottom',
             fontsize=9, fontweight='bold', rotation=45)

ax.legend(labels=('sales', 'return'))

# Placed legend in the bottom
# ax.legend(labels=('sales', 'return'), loc='upper center',
#           bbox_to_anchor=(0.5, -0.3),
#           fancybox=True, shadow=True, ncol=2)

plt.xticks(rotation=90, fontweight='bold')
# plt.yticks(np.arange(0, 500000, 10000), fontweight='bold')
plt.yticks(np.arange(0, max(z) * 1.5, (max(z) * 1.5) / 10), fontweight='bold')

plt.xlabel("Sales person", color='black', fontsize=14, fontweight='bold')
plt.ylabel("Amount", color='black', fontsize=14, fontweight='bold')
plt.title('Sales performance', fontweight='bold', color='#3e0a75', fontsize=18)
plt.tight_layout()
plt.show()
