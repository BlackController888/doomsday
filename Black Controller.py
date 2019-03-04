# strong password for companies and phones
import datetime

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
print("date:", day, "/", month, "/", year)
hour = now.hour
minute = now.minute
second = now.second
seconds = now.microsecond
print("clock:", hour, ":", minute, ":", second, ":", seconds)

enter = input("enter Name:")
enter1 = input("enter your Secret Password: ")
enter2 = input("re-enter your password: ")
if enter1 == enter2:
    print("CONFIRMED!!")
else:
    print("Incorrect Pass...")
    print("retry your password")
    ent = input("re-enter your password correctly: ")
enter3 = input("enter your recovery password: ")
print("Successfully Done...")
while len(enter1) == 500:
        enter1 = len(enter1)
if len(enter1) > 12:
        print(" Strong password ", enter)
else:
    if len(enter1) < 12:
        print("Your Password is very weak")



