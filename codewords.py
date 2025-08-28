import string

def encode_word(word):
    if len(word) < 2:
        return word
    first, last = word[0], word[-1]
    middle = word[1:-1]
    middle_numbers = ''
    for char in middle:
        if char.isalpha():
            middle_numbers += str(ord(char.lower()) - ord('a') + 1)
        else:
            middle_numbers += char  # keep non-letters as is
    return first + middle_numbers + last

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
