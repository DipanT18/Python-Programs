message = input("Enter your message for don anna bhai: ")
'''Because Don Anna Bhai is a most wanted smuggler and criminal mastermind, all communications must be encrypted.'''
words = message.split(" ")
coding = input("Type 'Greasing' to encode or 'Drying' to decode: ")
coding = True if coding == "Greasing" else False

nwords = []
if coding:
    for word in words:
        if len(word) <= 3:
            f = "zxt"
            l = "kjd"
            # Move first letter to end, then add prefix/suffix
            message_new = f + word[1:] + word[0] + l
            nwords.append(message_new)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    for word in words:
        if len(word) <= 3:
            # Remove prefix and suffix
            core = word[3:-3]
            # Move last character to front
            if core:
                message_new = core[-1] + core[:-1]
            else:
                message_new = ''
            nwords.append(message_new)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
