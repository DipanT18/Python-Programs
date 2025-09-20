def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    x = 0
    if len(s) > 6 or len(s)<2:
        return False
    if ord(s[0]) <= 90 and ord(s[0]) >= 65 and ord(s[1]) <= 90 and ord(s[1]) >= 65:
        for char in s:
            x += 1
            if char == "." or char == " ":
                return False
            if char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0":
                if char == "0":
                    return False
                while x<len(s)-1:
                    if s[x] == "." or s[x] == " ":
                        return False
                    if ord(s[x]) <= 90 and ord(s[x]) >= 65 and ord(s[x]) <= 90 and ord(s[x]) >= 65:
                        return False
                    x+=1
                break
    else:
        return False

    return True

if __name__ == "__main__":
    main()
