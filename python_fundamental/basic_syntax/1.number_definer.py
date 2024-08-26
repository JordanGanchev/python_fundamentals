numbers = float(input())

if numbers == 0:
    print("zero")

elif numbers > 0:
    if numbers < 1:
        print("small positive")
    elif numbers > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(numbers) < 1:
        print("small negative")
    elif abs(numbers) > 1000000:
        print("large negative")
    else:
        print("negative")
