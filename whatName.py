print("Hi!")
name = input("What's your name? : ")
print(f"Hi {name}!")
shower = input(f"How was your shower {name}? (good or bad): ").lower()
if shower == "good":
	print(f"I'm glad to hear that your shower was {shower}!")
elif shower == "bad":
	print(f"I'm sorry to hear that you shower was {shower}.")
else:
	print(f"Next time please pick from the displayed options!")
