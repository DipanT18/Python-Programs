list = [
    {"n": "apple", "c": "130", },
    {"n":   "avocado", "c": "50", },
    {"n":   "banana", "c": "110", },
    {"n":   "cantaloupe", "c": "50", },
    {"n":   "grapefruit", "c": "60", },
    {"n": "grapes", "c": "90", },
    {"n":   "honeydew melon", "c": "50", },
    {"n":   "kiwifruit", "c": "90", },
    {"n":   "lemon", "c": "15", },
    {"n":   "lime", "c": "20", },
    {"n":   "nectarine", "c": "60", },
    {"n":  "orange", "c": "80", },
    {"n":  "peach", "c": "60", },
    {"n":  "pear", "c": "100", },
    {"n":  "pineapple", "c": "50", },
    {"n":  "plums", "c": "70", },
    {"n":  "strawberries", "c": "50", },
    {"n":   "tangerine", "c": "50", },
    {"n":   "watermelon", "c": "80"}, {"n":   "sweet cherries", "c": "100"},
]

x = input("Item: ").strip().lower()

for i in list:
    if i["n"] == x:
        print(f"Calories: {i["c"]}")
