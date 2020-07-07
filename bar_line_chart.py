import pyodbc as db
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

query = """ DECLARE @Thisday CHAR(8) = CONVERT(varchar(8), dateAdd(day,-1,getdate()), 112)
            DECLARE @lastday CHAR(8) = CONVERT(varchar(8), dateAdd(DAY,-2,getdate()), 112)
            DECLARE @thismonth CHAR(6) = CONVERT(varchar(6), dateAdd(MONTH,0,getdate()-30), 112)
            select top 10 RSMTR as RSMTR, 
            SUM(case when TRANSDATE = @Thisday then EXTINVMISC END)  as YesterdaySales,
            SUM(case when TRANSDATE = @lastday then EXTINVMISC END) as BeforeTwodaysSales,
            SUM(case when transtype=2 and left(transdate,6) = @thismonth then EXTINVMISC*(-1) END) as ReturnVal
            from OESalesDetails
            group by RSMTR
            order by  YesterdaySales desc,   BeforeTwodaysSales desc, ReturnVal DESC"""

data = pd.read_sql_query(query, connection)

RSMTR = data.RSMTR.tolist()
todaySales = data.YesterdaySales.tolist()
LastdaySales = data.BeforeTwodaysSales.tolist()
ReturnVal = data.ReturnVal.tolist()


# print(RSMTR)
# print(todaySales)
# print(LastdaySales)
# print(ReturnVal)


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
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.75
opacity = 0.9

bar1 = plt.bar(bar_index, todaySales, bar_width,
               alpha=opacity, color='orange', label='Frank')

ax.plot(RSMTR, ReturnVal, color='red', linewidth=3, marker='o')


def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() + bar.get_width() / 2, height,
                thousand_K_number_decorator(height),
                va='bottom', ha='center', color='red',
                fontsize=12, fontweight='bold')


autolabel(bar1)

# # Line data point
for a, b in zip(RSMTR, ReturnVal):
    plt.text(a, b, thousand_K_number_decorator(b),
             ha='center', va='bottom',
             fontsize=12, fontweight='bold', color='black')

plt.ylabel('Sales Amount and Return', fontsize=14, fontweight='bold')
plt.xlabel('RSMTR Name', fontsize=14, fontweight='bold')
plt.title('Sales Evaluation - Developed by :Name', fontsize=16, fontweight='bold')
plt.yticks(fontweight='bold')
plt.xticks(bar_index, RSMTR, fontweight='bold')

plt.legend(['30 Days Return', 'Yesterday Sales'], loc='upper center',
           bbox_to_anchor=(0.5, -0.2),
           fancybox=True, shadow=True, ncol=2)
plt.tight_layout()
# plt.show()

plt.savefig('assignment5.png')
