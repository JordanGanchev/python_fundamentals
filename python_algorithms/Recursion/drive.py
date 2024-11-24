def calc_fun(n, index):
    if index == len(n) - 1:
        return n[index]
    return n[index] + calc_fun(n, index + 1)


n = [int(x) for x in input().split()]

print(calc_fun(n, 0))
