while True:
    ask = input("\nWould you like to encode or decode a message: (say quit to leave)\n\n> ")

    if ask.lower() == "quit":
        break

    elif ask.lower() == "encode" or ask.lower() == "decode":
        word = input(f'What message would you like me to {ask.lower()}?\n\n> ')
        new_word = []
        for letter in list(word):
            if letter == ' ':
                new_word.append(" ")
            else:
                asci_code = ord(letter)
                new_chr = chr(asci_code + 12) if ask.lower() == "encode" else chr(asci_code - 12)
                new_word.append(new_chr)

        print(f"Your {ask.lower()}d message is: ", end="")
        for letter in new_word:
            print(letter, end="")

        print("\nOrigional message:", word)


    else:
        print("I'm sorry that is not an option")
