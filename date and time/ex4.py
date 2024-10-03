# Print a date in a the following format

from datetime import datetime

given_date = datetime(2020, 2, 25)

date_str_time = given_date.strftime("%A %d %B %Y")
print(date_str_time)