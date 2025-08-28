import string

def encode_word(word):
    if len(word) < 2:
        return word
    first, last = word[0], word[-1]
    middle = word[1:-1]
    middle_numbers = []
    for char in middle:
        if char.isalpha():
            middle_numbers.append(str(ord(char.lower()) - ord('a') + 1))
        else:
            middle_numbers.append(char)
    middle_str = "'".join(middle_numbers)
    return last + middle_str + first

def encode_message(message):
    return ' '.join(encode_word(w) for w in message.split())

def main():
    print("Secret Agent Codeword Chat!")
    while True:
        user = input("You: ")
        if user.lower() in ['exit', 'quit']:
            print("Goodbye, agent!")
            break
        code = encode_message(user)
        print("Agent:", code)

if __name__ == "__main__":
    main()
