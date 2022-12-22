with open('words.txt', 'r') as file:

    lines = file.readline()

    words = lines.split(' ')

    for word in words:
        if word.count('c') >= 1:

            word = word.strip('.,')

            print(word)
