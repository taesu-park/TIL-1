import datetime

for i in range(50):
    targetDt = datetime.datetime(2019, 7, 13) - datetime.timedelta(weeks=i)
    targetDt = targetDt.strftime('%Y%m%d')