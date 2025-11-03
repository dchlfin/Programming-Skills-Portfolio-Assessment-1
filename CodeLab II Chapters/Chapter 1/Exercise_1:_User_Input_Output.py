def title():
    name = input("""Hello, user!\nWhat is your name? """)
    age = int(input("What is your age? "))
    print(f"""It is good to meet you, {name.capitalize()}\nThe length of your name is:\n{len(name)}\nYou will be {age + 1} in a year.""")
    
title()
