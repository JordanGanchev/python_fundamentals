number_order = int(input())

total_sum = 0.00
for _ in range(number_order):
    price_capsule = float(input())
    if 0.01 > price_capsule > 100.00:
        continue
    days = int(input())
    if 1 > days > 31:
        continue
    capsul_on_day = int(input())
    if 1 > capsul_on_day > 2000:
        continue

    day_sum = price_capsule * days * capsul_on_day
    if day_sum > 0:
        print(f"The price for the coffee is: ${day_sum:.2f}")
    total_sum += day_sum

if total_sum > 0:
    print(f"Total: ${total_sum:.2f}")