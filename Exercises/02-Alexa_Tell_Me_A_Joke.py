import random

def jokes():
    with open('randomJokes.txt', 'r') as j_line:
        jokes = [line.strip() for line in j_line if line.strip()]

    return jokes
    
def setup(jokes):
    value = random.choice(jokes)
    qm = value.find('?')
    if qm != -1:
        kw = value.lower()
        if "what" in kw:
            stp = input(f"Alexa: {value[:1 + qm].strip()}\nYou: (Ask 'What?') ") 
        elif "which" in kw:
            stp = input(f"Alexa: {value[:1 + qm].strip()}\nYou: (Ask 'Which?') ")
        elif "did you hear" in kw:
            stp = input(f"Alexa: {value[:1 + qm].strip()}\nYou: (Ask 'No, why?') ")
        elif "when" in kw:
            stp = input(f"Alexa: {value[:1 + qm].strip()}\nYou: (Ask 'When?') ")
        elif "why" in kw:
            stp = input(f"Alexa: {value[:1 + qm].strip()}\nYou: (Ask 'Why?') ")
        elif "how" in kw:
            stp = input(f"Alexa: {value[:1 + qm].strip()}\nYou: (Ask 'How?') ")
        elif "who":
            stp = input(f"Alexa: {value[:1 + qm].strip()}\nYou: (Ask 'Who?') ")
        else: 
            stp = input(f"Alexa: {value[:1 + qm].strip()}\nYou: (Ask)")
        if stp:
            print(f"Alexa: {value[qm + 1:].strip()}\n")
    else: 
        print(value.strip())

def validate(ans):
    kw = 'joke'
    while kw not in ans:
        ans = input("Alexa: Sorry, I didn't quite understand that. Could you repeat that?: ")
    else:
        setup(jokes())
    
def joke_loop():
    cond = 'y'
    ans = input("Alexa: Hello, do you want to hear a joke?\nAlexa: Repeat after me, \"Alexa, tell me a joke.\": ").lower()
    validate(ans)
    while (cond == 'y'):
        cond = input("Alexa: Would you like to hear another joke? (y/n): ").lower()
        if (cond == 'n'):
            break
        setup(jokes())

def main():
    joke_loop()
    
if __name__ == '__main__':
    main()


