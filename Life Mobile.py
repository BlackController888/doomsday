# An App that will question and suggestion health...
# Date and Time have been set to monitor the time and day of diet...

import datetime
now = datetime.datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# The name would be the user
Name = input("Enter your name: ")
print(Name.title())


print("Enter your Profiles!!")
enter = input(str("Enter your Day of birth: "))
enter1 = input(str("Enter your birth Month: "))
enter2 = input(str("Enter your year of birth: "))
print(enter, "-", enter1, "-", enter2, ".", "\n these is your time of birth...")

# setting up a code that will request the time to Eat, drink, everyday...
am = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pm = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


print("use digits example: if 8am, if 5pm, if 2pm  add AM OR PM but type an integer")
eating_time = input(str("What time do you Eat in the morning: "))










