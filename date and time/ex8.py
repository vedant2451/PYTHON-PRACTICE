# Convert the following datetime into a string
from datetime import datetime

given_date = datetime(2020, 2, 25)
date_str_time = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(date_str_time)
