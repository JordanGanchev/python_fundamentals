def reverse_array(idx, element):
    if idx == len(element) // 2:
        return
    swap_idx = len(element) - 1 - idx
    element[idx], element[swap_idx] = element[swap_idx], element[idx]
    reverse_array(idx + 1, element)


element = input().split()

reverse_array(0, element)
print(' '.join(element))