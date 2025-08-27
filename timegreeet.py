import time
# Standardized Time Representation
timestamp = time.strftime("%H:%M:%S")
print("Current Time =", timestamp)
h = int(time.strftime("%H"))
m = int(time.strftime("%M"))
s = int(time.strftime("%S"))
# to show am or pm
st = "am" if h < 12 else "pm"
if 0 <= h < 12 and 0 <= m < 60 and 0 <= s < 60:
    print("Good Morning Mr.Dipan and Ms.Dristi")
elif 12 <= h < 18 and 0 <= m < 60 and 0 <= s < 60:
    print("Good Afternoon Mr.Dipan and Ms.Dristi")
elif 18 <= h < 21 and 0 <= m < 60 and 0 <= s < 60:
    print("Good Evening Mr.Dipan and Ms.Dristi")
elif 21 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
    print("Good Night Mr.Dipan and Ms.Dristi")