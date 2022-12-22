with open('words.txt', 'r') as file:

    lines = file.readlines()

    print(lines)

    for word in lines:
        word = word.strip('\n')
        if word == word[::-1]:
            print(word)
