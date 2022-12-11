divisor_number = 0
number = ''
for i in range(100, 1, -1):
    divisor_number = 0
    for b in range(1, 101, 1):
        if i % b == 0:
            divisor_number += 1
        if b == 100 and divisor_number == 2:
            number += str(i)
            number += " "
        if divisor_number > 2:
            break
print(number)