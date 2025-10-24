import random

def jokes():
    jokes = [
        "Why did the chicken cross the road? To get to the other side.",
        "What happens if you boil a clown? You get a laughing stock.",
        "What did one penny say to another penny? We make cents.", 
        "Why don't penguins like talking to strangers at parties? They find it hard to break the ice.",
        "What do you call someone who dresses up like a noodle? An impasta!",
        "When is the best time to go to the dentist? Tooth-hurty!",
        "Why did the tree go to the dentist? It needed a root canal.",
        "Why did the melon jump into the lake? It wanted to be a water-melon.",
        "What did one eye say to the other eye? Don't look now, but something between us smells.",
        "What did the duck say when it bought lipstick? “Put it on my bill.”"
    ]
    return jokes
    
def setup(jokes):
    value = random.choice(jokes)
    qm = value.find("?")
    if qm != -1:
        stp = input(f"Alexa: {value[:1 + qm].strip()}\nYou: (Ask 'why?') ")
        if stp:
            punch = f"Alexa: {value[qm + 1:].strip()}\n"
            print(punch)     
    else: 
        print(value.strip())

def validate(ans):
    kw = "joke"
    while kw not in ans:
        ans = input("Alexa: Sorry, I didn't quite understand that. Could you repeat that?: ")
    else:
        # displayJoke(jokes())
        setup(jokes())
    
def joke_loop():
    cond = "y"
    ans = input("Alexa: Hello, do you want to hear a joke?\nAlexa: Repeat after me, \"Alexa, tell me a joke.\": ").lower()
    validate(ans)
    while (cond == "y"):
        cond = input("Alexa: Would you like to hear another joke? (y/n): ").lower()
        if (cond == "n"):
            break
        setup(jokes())

def main():
    joke_loop()
    
if __name__ == "__main__":
    main()
