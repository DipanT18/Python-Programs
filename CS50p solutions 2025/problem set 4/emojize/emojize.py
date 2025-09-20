import emoji

userInput=input("Input: ").strip()
print(f"Output: {emoji.emojize(userInput, language='alias')}")

