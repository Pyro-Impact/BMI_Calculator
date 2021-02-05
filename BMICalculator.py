from BMICalc.H_and_W import height_conversion, weight_conversion

print("Welcome to the BMI Calculator. \n ")

name_1 = str(input("What is your name? "))
conv1 = str(input("Pounds/Inches or Kilograms/Meters?"
                  "\nType 1 for the first option, and anything else for the second option: "))


def bmi_calculator(name, height, weight):
    bmi = float(703 * weight / (height ** 2))
    print("Your BMI is: ")
    print(str(round(bmi, 1)))
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


print(bmi_calculator(name_1, height_conversion(conv1), weight_conversion(conv1)))
