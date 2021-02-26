from Shift15.Restart_Function import confirm_restart

print("Welcome to the BMI Calculator. \n ")
name_1 = str(input("What is your name? "))
conv1 = str(input("Pounds/Inches or Kilograms/Meters?"
                  "\nType 1 for the first option, and anything else for the second option: "))


class HeightandWeight:
    def __init__(self, conversion):
        self.conv1 = conversion

    def height_conversion(self):
        while True:
            try:
                if self.conv1 == "1":
                    height = float(input("What is your height in inches? "))
                    break
                else:
                    height = float(input("What is your height in meters? "))
                    height *= 39.37
                    break
            except ValueError:
                print("Please try again.")
        return height

    def weight_conversion(self):
        while True:
            try:
                if self.conv1 == "1":
                    weight = float(input("What is your weight in pounds? "))
                    break
                else:
                    weight = input("What is your weight in kilograms? ")
                    weight = float(weight) * 2.205
                    break
            except ValueError:
                print("Please try again.")
        return weight


class FinalConversion:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def bmi_calculator(self):
        bmi = float(703 * self.weight / (self.height ** 2))
        print("Your BMI is: ")
        print(str(round(bmi, 1)))
        if bmi < 18.5:
            return self.name + " is underweight."
        elif 18.5 <= bmi <= 24.9:
            return self.name + " has a healthy weight."
        elif 25 <= bmi <= 29.9:
            return self.name + " is overweight."
        elif 30 <= bmi < 40:
            return self.name + " is obese."
        elif bmi >= 40:
            return self.name + " is a class 3 obese."


while True:
    HaW = HeightandWeight(conv1)
    FC = FinalConversion(name_1, HaW.weight_conversion(), HaW.height_conversion())
    print(FC.bmi_calculator())

    if confirm_restart() == "yes":
        continue
    else:
        break
