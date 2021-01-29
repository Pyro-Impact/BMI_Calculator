print("Welcome to the BMI Calculator. \n ")

name_1 = str(input("What is your name?"))

conv1 = input("Pounds/Inches or Kilograms/Meters?"
              "Type 1 for the first option, and 2 for the second option.")

if conv1 == "1":
    weight1 = float(input("What is your weight in pounds?"))
    height1 = float(input("What is your height in inches?"))
    weight2 = 2
    height2 = 2
else:
    weight2 = input("What is your weight in kilograms?")
    height2 = input("What is your height in meters?")
    weight2 = float(weight2) * 2.205
    height2 = float(height2) * 39.37
    weight1 = 2
    height1 = 2


def bmi_calculator(name, weight, height):
    bmi = float(703 * weight / (height ** 2))
    print("Your BMI is: ")
    print(str(round(bmi, 3)))
    if bmi < 18.5:
        return name + " is underweight."
    elif 18.5 <= bmi <= 24.9:
        return name + " has a healthy weight."
    elif 25 <= bmi <= 29.9:
        return name + " is overweight."
    elif 30 <= bmi < 40:
        return name + " is obese."
    elif bmi >= 40:
        return name + " is a class 3 obese."


if conv1 == "1":
    print(bmi_calculator(name_1, weight1, height1))
else:
    print(bmi_calculator(name_1, weight2, height2))
