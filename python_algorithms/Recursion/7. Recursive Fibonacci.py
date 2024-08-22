# def calc_fin(n):
#     if n <= 1:
#         return 1
#     return calc_fin(n - 1) + calc_fin(n - 2)


def iterative_fib(number):
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(number - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result


n = int(input())
print(iterative_fib(n))
