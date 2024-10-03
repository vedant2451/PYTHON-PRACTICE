# Find the day of the week of a given date
from datetime import datetime

given_date = datetime(2020, 7, 26)
date_str_time = given_date.strftime("%A ")
print(date_str_time)