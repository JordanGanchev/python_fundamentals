def find_combinations(target, matrix=[], current=[], start=1):

    if target == 0:
        matrix.append(current)
    for i in range(start, target + 1):
        find_combinations(target - i, matrix, current + [i], i)
    return matrix

n = int(input())

result = find_combinations(n)
result2 = []
for num in reversed(result):
    revers_result = []
    for i in reversed(num):
        revers_result.append(i)
    result2.append(revers_result)

result_end = sorted(result2, key=lambda x: max(x), reverse=True)

for i in result_end:
    print(*i, sep=" + ")

 # 40%