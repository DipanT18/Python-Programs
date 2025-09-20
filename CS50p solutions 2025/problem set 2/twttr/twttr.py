x=input("Input: ").strip()

buff=""
for i in x:
    if i!="a" and i!="e" and i!="i" and i!="o" and i!="u" and i!="A" and i!="E" and i!="I" and i!="O" and i!="U":
        buff+=i
print(f"Output: {buff}")

