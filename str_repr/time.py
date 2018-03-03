import datetime

today = datetime.datetime.now()

# Prints readable format for date-time object
print(str(today))

# Prints the official format of date-time object
print(repr(today))

# output
# -------
# 2018-03-03 13:49:16.841707
# datetime.datetime(2018, 3, 3, 13, 49, 16, 841707)
