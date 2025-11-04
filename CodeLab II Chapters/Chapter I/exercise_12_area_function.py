def areaTriangle(b, h):
    area_t = 1/2 * b * h
    print(f"The area of a triangle with a base of {b} and height of {h} is {area_t}.")

def areaCircle(r = 0, d = 0):
    pi = 3.14

    if r > 0:
        r2 = r * r
        area_r = round(pi * r2, 2)
        print(f"The area of a circle with a radius of {r} is {area_r}")
        
    elif d > 0:
        d_r = d / 2
        d_r2 = d_r * d_r
        
        area_d = round(pi * d_r2, 2)
        print(f"The area of a circle with a diameter of {d} is {area_d}.")
    
def areaSquare(s):
    area_s = s * s
    print(f"The area of a square with a side of {s} is {area_s}.")

def operationSelection():
    while True:
        a = int(input("\nSelect operation: (e.g. 1, 2, 3) "))
        if a in range(1, 4):
            if a == 1:
                s = int(input("Enter a side: "))
                areaSquare(s)
            elif a == 2:
                rd = input("Enter radius or diameter: (r/d) ").lower()
                while rd != 'r' and rd != 'd':
                    rd = input("Invalid measurement. Radius or diameter?").lower()

                if rd =='r':
                    r = int(input("Enter radius: "))
                    areaCircle(r, 0)
                elif rd == 'd':
                    d = int(input("Enter diameter: "))
                    areaCircle(0, d)
                
            else:
                b = int(input("Enter the base: "))
                h = int(input("Enter the height: "))
                areaTriangle(b, h)
            break
        else:
            print("Invalid operation. Please try again.")

def displayMenu():
    print("""
1: Calculate the area of a square
2: Calculate the area of a circle
3: Calculate the area of a triangle""")

def main():
    displayMenu()
    operationSelection()

if __name__ == "__main__":
    main()
