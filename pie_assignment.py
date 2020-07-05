import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def numberInThousands(number):
    number = number / 1000
    number = int(number)
    number = format(number, ',')
    number = number + 'K'
    return number


def numberInComma(number):
    number = int(number)
    number = format(number, ',')
    return number


conn = db.connect('DRIVER={SQL Server};'
                  'SERVER=137.116.139.217;'
                  'DATABASE=ARCHIVESKF;'
                  'UID=sa;PWD=erp@123')

outstanding_df = pd.read_sql_query(""" select
                    SUM(CASE WHEN TERMS='CASH' THEN OUT_NET END) AS TotalOutStandingOnCash,
                    SUM(CASE WHEN TERMS not like '%CASH%' THEN OUT_NET END) AS TotalOutStandingOnCredit
                    from  [ARCOUT].dbo.[CUST_OUT]
                    where [INVDATE] <= convert(varchar(8),DATEADD(D,0,GETDATE()),112)
                     """, conn)

cash = int(outstanding_df['TotalOutStandingOnCash'])
credit = int(outstanding_df['TotalOutStandingOnCredit'])
data = [cash, credit]

data = [300, 400, 700, 200, 150]
colors = ['#f9ff00', '#ff8600', '#ffba00', '#927426', '#268c92']
legend_element = [Patch(facecolor='#f9ff00', label='A'),
                  Patch(facecolor='#ff8600', label='B'),
                  Patch(facecolor='#ffba00', label='C'),
                  Patch(facecolor='#927426', label='D'),
                  Patch(facecolor='#268c92', label='E')
                  ]
data_label = [data[0], data[1], data[2], data[3], data[4]]

fig1, ax = plt.subplots()
pack_all, label, percent_v = ax.pie(data, labels=data_label, colors=colors, autopct='%.1f%%', textprops={
    'color': "Black"}, startangle=90, pctdistance=.8)
plt.setp(percent_v, fontsize=12, color='blue', fontweight='bold')

plt.title('Product wise Sales', fontsize=16, fontweight='bold', color='#3e0a75')
ax.axis('equal')
plt.legend(handles=legend_element, loc='lower left', fontsize=11)
plt.tight_layout()
# plt.show()

plt.savefig('assignment6.png')
