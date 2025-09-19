#This program is to convert a given string into its shorthand form by replacing certain words with their corresponding symbols.

a=300
b=200
print(a) if a>b else print ("=") if a==b else print(b)


#Second one
def convert_to_shorthand(input_string):
    shorthand_dict = {
        "and": "&",
        "to": "2",
        "you": "U",
        "for": "4",
        "be": "B",
        "at": "@",
        "one": "1"
    }
    
    words = input_string.split()
    shorthand_words = [shorthand_dict.get(word, word) for word in words]
    shorthand_string = ' '.join(shorthand_words)
    
    return shorthand_string
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result = convert_to_shorthand(input_string)
    print("Shorthand form:", result)