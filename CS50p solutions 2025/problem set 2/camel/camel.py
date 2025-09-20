x = input("camelCase ").strip()

buffer = ""
for char in x:
    if ord(char) <= 90 and ord(char) >= 65:
        buffer += "_"
        buffer += char.lower()
    else:
        buffer+=char
print(buffer,end="")
