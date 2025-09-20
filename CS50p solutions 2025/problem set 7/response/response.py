import validators
print("Valid") if validators.email(input("What's your email adress: ")) else print("Invalid")
