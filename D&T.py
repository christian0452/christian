import datetime
import pytz

# Create a datetime object with the current date and time in UTC timezone
utc_date = datetime.datetime.now(pytz.utc)

# Convert the UTC datetime to a specific timezone (e.g. US/Pacific)
pacific_tz = pytz.timezone('US/Pacific')
pacific_date = utc_date.astimezone(pacific_tz)
# Print both the UTC datetime and the timezone-adjusted datetime
print("UTC datetime:", utc_date)
print("Pacific datetime:", pacific_date)