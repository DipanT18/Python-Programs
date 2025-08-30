def encode_message(message):
    """Encode the message using Don Anna Bhai's cipher"""
    words = message.split(" ")
    encoded_words = []
    
    for word in words:
        if len(word) >= 3:
            # For words 3 characters or less:
            # Move first letter to end, then add prefix/suffix
            f = "zxt"
            l = "kjd"
            encoded_word = f + word[1:] + word[0] + l
            encoded_words.append(encoded_word)
        else:
            # For words longer than 3 characters: reverse them
            encoded_words.append(word[::-1])
    
    return " ".join(encoded_words)

def decode_message(message):
    """Decode the message using Don Anna Bhai's cipher"""
    words = message.split(" ")
    decoded_words = []
    
    for word in words:
        # Check if word has the encoding pattern (starts with "zxt" and ends with "kjd")
        if word.startswith("zxt") and word.endswith("kjd") and len(word) >= 9:
            # Remove prefix "zxt" and suffix "kjd"
            middle_part = word[3:-3]
            if middle_part:  # Make sure there's content to decode
                # Move last character to front
                decoded_word = middle_part[-1] + middle_part[:-1]
                decoded_words.append(decoded_word)
            else:
                decoded_words.append("")
        else:
            # For longer words that were reversed
            decoded_words.append(word[::-1])
    
    return " ".join(decoded_words)

def main():
    print("=== Don Anna Bhai's Secret Communication System ===")
    print("Because Don Anna Bhai is a most wanted smuggler and criminal mastermind,")
    print("all communications must be encrypted.\n")
    
    message = input("Enter your message for Don Anna Bhai: ")
    
    if not message.strip():
        print("Error: Please enter a valid message!")
        return
    
    coding_choice = input("Type 'Greasing' to encode or 'Drying' to decode: ").strip()
    
    if coding_choice.lower() == "greasing":
        # Encoding
        encoded = encode_message(message)
        print(f"\nEncoded message: {encoded}")
        
    elif coding_choice.lower() == "drying":
        # Decoding
        decoded = decode_message(message)
        print(f"\nDecoded message: {decoded}")
        
    else:
        print("Error: Please type exactly 'Greasing' or 'Drying'")

if __name__ == "__main__":
    main()
    