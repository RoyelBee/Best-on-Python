import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch


def convert(number):
    number = number / 1000
    number = int(number)
    number = format(number, ',')
    number = number + 'K'
    return number


data = [5000, 7000]
total = data[0] + data[1]
total = 'Total \n' + str(total)

colors = ['green', 'blue']

legend_element = [Patch(facecolor='green', label='A'),
                  Patch(facecolor='blue', label='B')]

# -------------------new code--------------------------

cash_label = convert(data[0])
credit_label = convert(data[1])

DataLabel = [cash_label, credit_label]
# -----------------------------------------------------

fig, ax = plt.subplots()
pack_all, label, percent_value = ax.pie(data, colors=colors, labels=DataLabel,
                                        autopct='%.1f%%', startangle=90,
                                        pctdistance=.7)
plt.setp(percent_value, fontsize=14, color='black', fontweight='bold')
ax.text(0, -.1, total, ha='center', fontsize=14, fontweight='bold')

centre_circle = plt.Circle((0, 0), 0.50, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')

ax.axis('equal')
plt.legend(handles=legend_element, loc='lower left', fontsize=11)
plt.tight_layout()
plt.show()
