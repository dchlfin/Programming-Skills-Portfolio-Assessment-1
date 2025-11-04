counter = 0
inp = "y"

while inp == "y":
    inp = input("Would you like to continue using the while loop? ")
    counter += 1
    if inp == "n":
        break
