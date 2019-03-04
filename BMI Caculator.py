# BMI Calculator
name1 = "bernard"
height_m1 = 2.5
weight_kg1 = 180

name2 = "bernard's sister"
height_m2 = 3.4
weight_kg2 = 160

name3 = "sammy"
height_m3 = 169
weight_kg3 = 67

def bmi_calculate(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi :")
    print(bmi)
    if bmi < 24:
        return name + " is not overweight"
    else:
        return name + " overweight"

result1 = bmi_calculate(name1, height_m1, weight_kg1)
result2 = bmi_calculate(name2, height_m2, weight_kg2)
result3 = bmi_calculate(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)

