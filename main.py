import time

h = int(input("Enter time in hours: "))
m = int(input("Enter time in minutes: "))
s = int(input("Enter time in seconds: "))
st = input("What is the time situation (am/pm): ").strip().lower()

if 0 <= h < 12 and 0 <= m < 60 and 0 <= s < 60 and st == "am":
    print("Good Morning Mr.Dipan and Ms.Dristi")
elif 12 <= h < 18 and 0 <= m < 60 and 0 <= s < 60 and st == "pm":
    print("Good Afternoon Mr.Dipan and Ms.Dristi")
elif 18 <= h < 21 and 0 <= m < 60 and 0 <= s < 60 and st == "pm":
    print("Good Evening Mr.Dipan and Ms.Dristi")
elif 21 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
    print("Good Night Mr.Dipan and Ms.Dristi")
else:
    print("Invalid time entered.")

