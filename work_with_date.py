# #
# #
# # ## --------------------------------------------
# # # # ---------  Months Start Date --------------
# # # # -------------------------------------------
#
import datetime
from dateutil.relativedelta import relativedelta
import re
from datetime import date
from pandas.tseries import offsets
import pandas as pd

# # # --------------------------------------------------
# # # Current Date and Months Start Date
# # # --------------------------------------------------
todayDate = datetime.date.today()
resultDate = todayDate.replace(day=1)

if ((todayDate - resultDate).days > 25):
    resultDate = resultDate + relativedelta(months=0)

month_start_date = int(re.sub("\-",'', str(resultDate)))
current_date = int(re.sub("\-",'', str(todayDate)))


print('Month Start Date = ', month_start_date)
print('Current Date = ', current_date)

# # # ---------------------------------------------------------------
# # # Current Months Number of Off Day, Half day and Full Working Day
# # # ---------------------------------------------------------------
#
#
# # Read the dataset
# data = pd.read_excel('./working_date.xlsx')
# print(data.columns)
#
# # Sorting data set
# total_offday_in_month = data[
#         (data.maindate.between(month_start_date, current_date, inclusive=True))
#         & (data.working_status== 0)
#         ]
# print('Total Off Day In this Month = ', total_offday_in_month.maindate.count())
#
# # # Total Saturday in a month
# total_halfday_in_month = data[
#     (data.maindate.between(month_start_date, current_date, inclusive=True))
#      & (data.working_status== 1)
#     ]
# total_halfday_in_month = int(total_halfday_in_month.maindate.count())
# print('Total Half Day In this Month = ', total_halfday_in_month)
#
# # # Total Full Day in a month
# total_Fullday_in_month = data[
#     (data.maindate.between(month_start_date, current_date, inclusive=True))
#      & (data.working_status== 2)
#      ]
# total_Fullday_in_month= int(total_Fullday_in_month.maindate.count())
# print('Total Full Day In this Month = ', total_Fullday_in_month)
#
#
# # # --------------------------------------------------
# # # Months last day
# # # --------------------------------------------------
# import datetime
# import re
# date = datetime.date.today()
# def last_day_of_month(any_day):
#     next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
#     return next_month - datetime.timedelta(days=next_month.day)
#
# months_last_day = last_day_of_month(datetime.date(date.year, date.month, 1))
# months_last_day =  int(re.sub("\-",'', str(months_last_day)))
#
# print("Month's Last Day = ", months_last_day)
#
# # # --------------------------------------------------
# # # Yars First Day
# ## ---------------------------------------------------
# date = datetime.date.today()
# years_first_day = int(str(date.year)+'0101')
# print('Years Start Date = ', years_first_day)
#
# total_personel =  45
# avg_working_hour = (int(total_Fullday_in_month) * 8 * total_personel) + (int(total_halfday_in_month) * 4 * total_personel)
# print('avg working hour = ', avg_working_hour)
#

# # ---------------------------------------------------------
# # Work with govt holiday
# # ----------------------------------------------------------
# import pandas as pd
# import Datetime
# todayDate = datetime.date.today()
# data = pd.read_excel('working_date.xlsx', index=False)
# govt_date = data[() & data.remarks==3].count()
#
# print(govt_date.working_status)