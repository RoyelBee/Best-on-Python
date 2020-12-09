import pyodbc as db
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

query = """ DECLARE @Thisday CHAR(8) = CONVERT(varchar(8), dateAdd(day,0,getdate()), 112)
            DECLARE @lastday CHAR(8) = CONVERT(varchar(8), dateAdd(DAY,-1,getdate()), 112)
            DECLARE @thismonth CHAR(6) = CONVERT(varchar(6), dateAdd(MONTH,0,getdate()), 112)
            
            select top 5 RSMTR, 
            SUM(case when TRANSDATE = @Thisday then EXTINVMISC END)  as todaySales,
            SUM(case when TRANSDATE = @lastday then EXTINVMISC END) as LastdaySales,
            SUM(case when transtype=2 and left(transdate,6) = @thismonth then EXTINVMISC*(-1) END) as ReturnVal
            from OESalesDetails
            group by RSMTR
            order by  todaySales desc, LastdaySales desc, ReturnVal DESC"""

data = pd.read_sql_query(query, connection)

RSMTR = data.RSMTR.tolist()
todaySales = data.todaySales.tolist()
LastdaySales = data.LastdaySales.tolist()
ReturnVal = data.ReturnVal.tolist()

print(RSMTR)
print(todaySales)
print(LastdaySales)
print(ReturnVal)

def number_decorator(number):
    number = round(number, 1)
    number = format(number, ',')
    number = number + 'K'
    return number

def thousand_K_number_decorator(number):
    number = int(number / 1000)
    number = format(number, ',')
    number = number + 'K'
    return number


bar_index = np.arange(len(RSMTR))

# create plot
fig, ax = plt.subplots()

bar_width = 0.3
opacity = 0.9

bar1 = plt.bar(bar_index, todaySales, bar_width,
               alpha=opacity, color='b', label='Frank')

bar2 = plt.bar(bar_index + bar_width, LastdaySales, bar_width,
               alpha=opacity, color='r', label='Guido')

ax.plot(RSMTR, ReturnVal, color='red', linewidth=3)


def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() + .1, 0.8 * height,
                number_decorator(height),
                va='bottom', rotation=90,
                fontsize=12, fontweight='bold')


def autolabel(bar2):
    for bar in bar2:
        height = int(bar.get_height())
        ax.text(bar.get_x() + .1, 0.8 * height,
                number_decorator(height),
                va='bottom', rotation=90,
                fontsize=12, fontweight='bold')

for a, b in zip(RSMTR, ReturnVal):
    plt.text(a, b, str(b) + 'K',
             ha='center', va='bottom',
             fontsize=9, fontweight='bold')

autolabel(bar1)
autolabel(bar2)

plt.ylabel('Amount')
plt.xlabel('Name')
plt.title('Sales Evaluation')
plt.xticks(bar_index + bar_width / 2, RSMTR)
plt.legend(['day1', 'day2'])

# plt.tight_layout()
plt.show()
