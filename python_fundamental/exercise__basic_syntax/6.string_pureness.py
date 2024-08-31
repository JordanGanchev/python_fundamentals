n = int(input())

for _ in range(n):
    char = input()

    for i in char:
        if i == "." or i == '_' or i == ',':
            print(f"{char} is not pure!")
            break
    else:
        print(f"{char} is pure.")
