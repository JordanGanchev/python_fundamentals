row = int(input())
col = int(input())

matrix = []

for _ in range(row):
    list_met = []
    for num in range(col):
        list_met.append(num)
    matrix.append(list_met)


print(matrix)
