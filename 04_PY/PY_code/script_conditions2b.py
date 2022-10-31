nmr = 100

while True:
    number = int(input("Please enter a number:"))

    if number == nmr:
        print(number, "is a great number, you are finished.")
        break
    elif number < 100:
        print(number, "is a smaller number, try again")
    else:
        print(number, "is a bigger number, try again.")



