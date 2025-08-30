import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

def format_sentence_with_proper_nouns(sentence):
    """
    Format a sentence by:
    1. Capitalizing the first letter
    2. Making the rest lowercase
    3. Capitalizing proper nouns (names, places, organizations, etc.)
    4. Adding period if missing
    """
    
    # Process the sentence with spaCy
    doc = nlp(sentence.lower())  # Start with lowercase for consistent processing
    
    # Create a list to store formatted words
    formatted_words = []
    
    for token in doc:
        word = token.text
        
        # Check if the token is a named entity (proper noun)
        if token.ent_type_:  # If it's part of a named entity
            # Capitalize the first letter of the word
            formatted_word = word.capitalize()
        else:
            # Keep the word as is (lowercase)
            formatted_word = word
            
        formatted_words.append(formatted_word)
    
    # Join the words back into a sentence
    result = " ".join(formatted_words)
    
    # Capitalize the first letter of the sentence
    if result:
        result = result[0].upper() + result[1:]
    
    # Add period if missing
    if result and result[-1] not in ".!?":
        result += "."
    
    return result

def format_sentence_advanced(sentence):
    """
    Advanced version that preserves spacing and handles punctuation better
    """
    # Process with spaCy
    doc = nlp(sentence.lower())
    
    # Create a character-by-character result
    result = list(sentence.lower())
    
    # Capitalize proper nouns
    for ent in doc.ents:
        # Get the start and end character positions of the entity
        start_char = ent.start_char
        end_char = ent.end_char
        
        # Capitalize each word in the entity
        entity_text = sentence[start_char:end_char].lower()
        words = entity_text.split()
        capitalized_words = [word.capitalize() for word in words]
        capitalized_entity = " ".join(capitalized_words)
        
        # Replace in result
        for i, char in enumerate(capitalized_entity):
            if start_char + i < len(result):
                result[start_char + i] = char
    
    # Join back to string
    result = "".join(result)
    
    # Capitalize first letter
    if result:
        result = result[0].upper() + result[1:]
    
    # Add period if missing
    if result and result[-1] not in ".!?":
        result += "."
    
    return result

def main():
    print("=== Sentence Formatter with Proper Noun Detection ===")
    print("This program will format your sentence and capitalize proper nouns.\n")
    
    while True:
        sentence = input("Enter a sentence (or 'quit' to exit): ").strip()
        
        if sentence.lower() == 'quit':
            print("Goodbye!")
            break
            
        if not sentence:
            print("Please enter a valid sentence!\n")
            continue
        
        # Format the sentence
        formatted = format_sentence_advanced(sentence)
        
        print(f"Original:  {sentence}")
        print(f"Formatted: {formatted}")
        
        # Show what entities were detected
        doc = nlp(sentence.lower())
        if doc.ents:
            print("Detected proper nouns:")
            for ent in doc.ents:
                print(f"  - '{ent.text}' ({ent.label_}: {spacy.explain(ent.label_)})")
        else:
            print("No proper nouns detected.")
        
        print("-" * 60)

def test_examples():
    """Test the function with various examples"""
    test_sentences = [
        "hello my name is john and i live in new york",
        "apple inc is located in california",
        "i visited paris last summer with mary",
        "barack obama was president of united states",
        "google and microsoft are tech companies",
        "LONDON IS THE CAPITAL OF ENGLAND"
    ]
    
    print("=== Testing Examples ===")
    for sentence in test_sentences:
        formatted = format_sentence_advanced(sentence)
        print(f"Input:  {sentence}")
        print(f"Output: {formatted}")
        print()

if __name__ == "__main__":
    # Run the main program
    main()
    
    # Uncomment to see test examples
    # test_examples()


'''If you don't want to change the case of the first letter in names, you can use the following code:'''
# sent=str(input("Enter a sentence: "))
# if sent[0].islower():
#     sent=sent.capitalize()
# else:
#     sent=sent[0].upper()+sent[1:]
# if sent[1:].isupper():
#     sent=sent[1:].lower()
# if sent[-1]!=".":
#     sent+="."
# print(sent)
'''Uncomment the following lines to enable the original functionality'''