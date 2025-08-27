def ask_name():
    return input("Dear student, enter your name: ")

def get_marks():
    m1 = float(input("Marks in Mathematics: "))
    m2 = float(input("Marks in Physics: "))
    m3 = float(input("Marks in Chemistry: "))
    return m1, m2, m3

def calculate_mean(m1, m2, m3):
    return (m1 + m2 + m3) / 3
def calculate_percentage(mean):
    return (mean/300)*100

def calculate_grade(mean):
    if mean >= 90:
        return "A"
    elif mean >= 80:
        return "B"
    elif mean >= 70:
        return "C"
    elif mean >= 60:
        return "D"
    elif mean >= 40:
        return "Just Pass"
    else:
        return "Fail"

for i in range(1, 11):
    print(f"\nStudent {i}:")
    name = ask_name()
    m1, m2, m3 = get_marks()
    mean = calculate_mean(m1, m2, m3)
    percentage = calculate_percentage(mean)
    grade = calculate_grade(mean)
    print(f"Hey! {name}, your percentage is {percentage:.2f}%. You've got a {grade} grade!")
    if grade == "Just Pass":
        print("You need to work harder next time.")
    elif grade == "Fail":
        print("Please try again next year.")






{
        "phone charger": 100,
        "power bank": 150,
        "t-Shirt": 220,
        "Cargo pants": 325,
        "Economics Book": 830,
        "Iphone 13 pro": 935,
        "Samsung S23 Ultra": 1040,
        "beard trimmer": 145,
        "camera": 650,
        "Titan watch": 555
    }
