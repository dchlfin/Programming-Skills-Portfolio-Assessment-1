import random

def jokes():
    jokes = [
        "Why did the zombies get divorced? Their marriage was dead!",
        "Why did the lion go to therapy? He found out his wife was a cheetah!",
        "Did you hear about the couple of bed bugs? They got married in the spring!",
        "Which one of your kids will never grow up and move out! Your husband!",
        "Why is being married worse than going to work? At least at work, you might get a new boss!",
        "How are boys similar to wine? They take years and years and years to mature!",
        "Why is a good doctor able to stay calm? He has a lot of patients!",
        "What's the best way to criticize your boss? Very quietly, so she can’t hear you!",
        "Why did the marketer dump her boyfriend? Lack of engagement!",
        "What’s a pirate’s favorite meeting style? A webinarrrrr!",
        "What does Nemo have in common with my dad? Neither can be found!",
        "What did the cow say to the leather chair? 'Hi, Mom!'",
        "When does a joke become a dad joke? When it leaves and never comes back!",
        "Who makes the most money off of Father’s Day? Therapists!",
        "Why don’t cannibals eat clowns? Because they taste funny!",
        "Why don’t graveyards ever get overcrowded? Because people are dying to get in!",
        "Why don’t orphans get their driver’s license? Because they don’t know where home is!",
        "What’s the best part about dead batteries? Free of charge!",
        "Why did the old man fall into the well? Because he couldn’t see that well!",
        "Why don’t we play hide and seek in cemeteries? Because good luck finding someone who hasn’t already won!",
        "Why do blind people hate skydiving? It scares the heck out of their dog!",
        "What’s red and bad for your teeth? A brick!"
    ]
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


