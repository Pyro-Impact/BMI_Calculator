class HeightandWeight:
    def __init__(self, conv1):
        self.conv1 = conv1

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
