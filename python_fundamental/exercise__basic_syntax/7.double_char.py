word = input()

while word != 'End':

    if word == "SoftUni":
        word = input()
        continue
    new_word = ''
    for i in word:
        new_word += i + i
    print(new_word)

    word = input()
    new_word = ''

