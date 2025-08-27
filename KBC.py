def ask_questions(questions, answers):
    for i, (q, opts) in enumerate(questions):
        print(f"\nQ{i+1}: {q}")
        for idx, opt in enumerate(opts, 1):
            print(f"  {idx}. {opt}")
        user_ans = input("Select your answer (1-4): ").strip()
        if user_ans == answers[i]:
            print("Correct!\n")
        else:
            print("Wrong answer! Quiz exited.")
            return False
    print("Congratulations! You answered all questions correctly.")
    return True

def select_category():
    categories = [
        ("Science", science_questions),
        ("History", history_questions),
        ("Geography", geography_questions),
        ("Geopolitics", geopolitics_questions)
    ]
    for idx, (name, func) in enumerate(categories, 1):
        print(f"\nStarting the questions of {name}")
        result = func()
        if not result:
            print("Game Over.")
            return
    print("Amazing! You completed all categories!")

def science_questions():
    questions = [
        ("What is the chemical symbol for water?", ["H2O", "CO2", "O2", "NaCl"]),
        ("What planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"]),
        ("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Ribosome", "Chloroplast"]),
        ("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"])
    ]
    answers = ["1", "2", "2", "3"]
    return ask_questions(questions, answers)

def history_questions():
    questions = [
        ("Who was the first President of the United States?", ["Abraham Lincoln", "George Washington", "John Adams", "Thomas Jefferson"]),
        ("In which year did World War II end?", ["1942", "1945", "1939", "1950"]),
        ("Who wrote the Harry Potter series?", ["J.K. Rowling", "Stephen King", "Agatha Christie", "Mark Twain"]),
        ("Who was known as the Iron Man of India?", ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Mahatma Gandhi", "Subhas Chandra Bose"])
    ]
    answers = ["2", "2", "1", "2"]
    return ask_questions(questions, answers)

def geography_questions():
    questions = [
        ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"]),
        ("Which river is the longest in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"]),
        ("What is the largest desert on Earth?", ["Sahara", "Gobi", "Kalahari", "Arabian"]),
        ("Mount Everest is located in which country?", ["India", "Nepal", "China", "Bhutan"])
    ]
    answers = ["3", "2", "1", "2"]
    return ask_questions(questions, answers)

def geopolitics_questions():
    questions = [
        ("Which country is known as the superpower of the world?", ["Russia", "China", "United States", "India"]),
        ("Which country is known as the fastest growing economy?", ["India", "China", "Brazil", "Germany"]),
        ("What is the name of the mission made by India to attack Pakistan?", ["Operation Sindoor", "Operation Vijay", "Operation Meghdoot", "Operation Cactus"]),
        ("Which organization is responsible for global peacekeeping?", ["UN", "NATO", "EU", "ASEAN"])
    ]
    answers = ["3", "2", "1", "1"]
    return ask_questions(questions, answers)

def KBC():
    print("Welcome to Kaun Banega Crorepati!")

KBC()
start = input("Do you want to start the quiz? (yes/no): ").strip().lower()
if start == "yes":
    select_category()
elif start == "no":
    print("Thank you for your time!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")

