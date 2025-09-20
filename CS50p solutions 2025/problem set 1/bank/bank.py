x=input("Greeting: ").lower().strip().partition(" ")[0]

if x[:5]=="hello":
    print("$0")
elif x[0]=="h":
    print("$20")
else:
    print("$100")
