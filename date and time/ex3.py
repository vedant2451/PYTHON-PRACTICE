# Subtract a week (7 days)  from a given date in Python
from datetime import datetime, timedelta
given_date = datetime(2020, 2, 25)
print("Given date : ",given_date)

new_date = given_date - timedelta(weeks = 1)
print("Past Date : ",new_date)