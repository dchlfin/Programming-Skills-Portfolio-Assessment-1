sides_1_2 = []

s1 = sides_1_2.append(int(input("Enter your first side: ")))
s2 = sides_1_2.append(int(input("Enter your second side: ")))
s3 = int(input("Enter your third and final side: "))

def triangle():
    if s3 <= sum(sides_1_2):
        print("We have a triangle!")
    else:
        print("Side lengths do not adhere to the triangle inequality theorem, which states that the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side.")
    
triangle()
