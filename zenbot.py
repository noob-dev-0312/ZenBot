import random

# start xp at 90
xp = 90
def zenbot_response(message, xp):
    responses = {
        "hi": "Yo! Archit's back on the grind.",
        "hello": "Hello! Still rocking python today?",
        "how are you": "Emotionally stable (fos a bot). You?",
        "bye": "Later, coder! I'll be in your RAM if you need me.",
        "xp": "Let me see... *beep boop*... awarding 20 xp to Archit.",
        "Who are you": "I'm ZenBot. Half Chill monk, half chaotic AI."
        }

    if message.lower() == "xp":
        xp += 10
        return f"+10 XP! You now have {xp}/100 XP.", xp
    elif message.lower() in responses:
        return responses[message.lower()], xp
    else:
        return "Whoa... even *I* don't get that yet.", xp

# mood options for each session
moods = [
    "Feeling glitchy today",
    "Hyper mode activated",
    "wildly sarcastic mood",
    "Totally zen",
]

# zenBot start-up
print("ZenBot Activated.")
print("Yo Archit! I've been napping in memory... ready to vibe or code?")
print("Mood:", random.choice(moods))
print("Type 'exit' or 'quit' to leave anytime.\n")

# chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("ZenBot: Peace out! logging off...")
        break
    reply, xp = zenbot_response(user_input,xp)
    print("ZenBot:", reply)

    # check for level up
    if xp >= 100:
        print("\n LEVEL UP! You've reached Level 2!")
        print("Get ready for your new rank card!\n")
        break