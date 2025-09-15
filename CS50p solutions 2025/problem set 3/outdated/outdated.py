months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        userInput=input("Date: ").strip()
        if " " in userInput:
            if "," in userInput:
                month, day, year=userInput.split(" ")
                month=months.index(month)+1
                day=day.split(",")[0]
        if "/" in userInput:
            month, day, year=userInput.split("/")
        if int(day)>31:
            continue
        elif int(month)>12:
            continue
        else:
            break
    except (ValueError,Exception):
        continue

print(f"{int(year):04}-{int(month):02}-{int(day):02}")

