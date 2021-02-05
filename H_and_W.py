def height_conversion(conv1):
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


def weight_conversion(conv1):
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
