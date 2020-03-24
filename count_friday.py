import datetime

today = datetime.date.today()


month_start = datetime.date(today.year, 1, 1)
print('Months Start Day = ', month_start)

single_day = datetime.timedelta(days=1)
total_friday = 0
total_satur_day = 0
while month_start.month == today.month:
    if month_start.weekday() == 4:
        total_friday += 1
    if month_start.weekday() == 5:
        total_satur_day += 1

    month_start += single_day

print('Total Friday:', total_friday)
print('Total Sunday:', total_satur_day)
