print("Welcome to the BMI Calculator. \n ")

name_1 = str(input("What is your name? "))
conv1 = str(input("Pounds/Inches or Kilograms/Meters?"
                  "\nType 1 for the first option, and anything else for the second option: "))


def height_conversion():
    while True:
        try:
            if conv1 == "1":
                height = float(input("What is your height in inches? "))
                break
            else:
                height = float(input("What is your height in meters? "))
                height *= 39.37
                break
        except ValueError:
            print("Please try again.")
    return height


def weight_conversion():
    while True:
        try:
            if conv1 == "1":
                weight = float(input("What is your weight in pounds? "))
                break
            else:
                weight = input("What is your weight in kilograms? ")
                weight = float(weight) * 2.205
                break
        except ValueError:
            print("Please try again.")
    return weight


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


print(bmi_calculator(name_1, height_conversion(), weight_conversion()))
