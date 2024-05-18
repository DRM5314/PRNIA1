
def askNumber():
    while True:
        try:
            inputNumber = input("Enter Number: ")
            number = int(inputNumber)
            if number < 0:
                continue
            return number
        except ValueError:
            print("Entry no valid!!!, number please!")
def askNumberInclude0():
    while True:
        try:
            inputNumber = input("Enter Number: ")
            number = int(inputNumber)
            if number < 0:
                continue
            return number
        except ValueError:
            print("Entry no valid!!!, number please!")