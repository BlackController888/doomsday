import datetime
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print("datetime: ", day, "-", month, "-", year)

Machine_Admin = "Paloma"
Admin = "Atteh Bernard Kwey"
Password = "palomakwey1997"
Password_hint = "Hers, and yours BACK IN TIME"

def introduction(name):
    print("Loading.." + name)
# The introduction is to inform the user, that the machine is now loading!!
introduction("system")

# The system is to print out its name...

print("This is " + Machine_Admin)

# The machine needs to recognize the user..

user = input("Enter Admins Name:")
if user == Admin:
    print("HELLO CREATOR")
else:
    print(user + " Please..you cannot proceed")
    print("Wrong Admins NAME...!!! ")

# if Admins name is wrong there should be a BREAKPOINT TO END THE PROCESS..

    breakpoint()
    breakpoint()

# The machine now needs to confirm the user name by inputting password
# ... to gain Full Control

Enter_P = input("Enter password to gain control:")
if Enter_P is not Password:
    print("Wrong Password")
    print("PASSWORD HINT")
    print(Password_hint)
    input("Re-type Password:")
else:
    if Password is not Enter_P:
        print("Sorry you're Out..." + Machine_Admin)
        print(exit())






