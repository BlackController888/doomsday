# Mobile Health Check
n = 18
y = "male"
z = "female"
a = input("Enter your full name: ")
b = int(input("Enter your age: "))
if n < b:
    print("You are an adult", a)
    print("your age determines your prescription")
else:
    print("a teenager")

c = input("Your gender: ")
if y == c:
    print(a, "you're Male")
else:
    print(a, "you're a Female")


height = 170
weight = 70
aa = float(input("Enter your height_m: "))
ab = float(input("Enter your weight_kg: "))
result = aa + ab
hwh = weight / height ** 2
if hwh > result:
    print(a)
    print("you have a normal weight")
    print("keep it up by exercising")
else:
    print("you need to be attended")
    print("you need some training")
    print("and a medical attention now!!!!")




