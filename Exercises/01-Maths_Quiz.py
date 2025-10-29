import random

def displayResults(points):
    print(f"Total Score: {points}/100")

    if points < 70:
        print("Rank F: Better luck next time!")
    elif points >= 70 and points < 80:
        print("Rank B: Nice!")
    elif points >= 80 and points < 90:
        print("Rank A: Good job!")
    elif points >= 90 and points <= 100:
        print("Rank A+: Congratulations! ")

def isCorrect(user_ans, ans):
    return (user_ans == ans)

def displayProblem(a, o, b, q):
    points = 10
    ans = 0
    if o == "+":
        ans = a + b
    else:
        ans = a - b
    while (points >= 0):
        # print(f"Points: {points}")
        user_ans = int(input(f"{q + 1}. {a} {o} {b} = "))
        if (isCorrect(user_ans, ans)):
            break
        points -= 5
    return points

def decideOperation():
    return random.choice(["+", "-"])

def randomInt(range_arr:list):
    a, b = [], []
    
    for i in range(10):
        a.append(random.choice(range_arr))
        b.append(random.choice(range_arr))
    return (a, b)

def createRange(n):
    num = []
    if n == 3:
        n = 4
    num = [i for i in range(10**n)]
    return num

def generateQuestions(diff):
    points = 0
    range_arr = createRange(diff)
    q_a, q_b = randomInt(range_arr)
    for i in range(10):
        points += displayProblem(q_a[i], decideOperation(), q_b[i], i)
    displayResults(points)

def displayMenu():
    print("""DIFFICULTY LEVEL
1. Easy
2. Moderate
3. Advanced""")
    
def game_loop():
    cond = "y"
    while (cond == "y"):
        displayMenu()
        diff = int(input("Enter preferred difficulty (i.e, 1, 2, 3): "))
        generateQuestions(diff)
        cond = input("Would you like to play again? (y/n): ").lower()
        if (cond == "n"): #recheck
            break

def main():
    game_loop()

if __name__ == "__main__":
    main()

