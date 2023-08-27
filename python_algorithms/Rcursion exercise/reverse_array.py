def reverse_array(index, element):
    if index ==len(element) // 2:
        return
    swap_index = len(element) - 1 -index
    element[index], element[swap_index] = element[swap_index], element[index]
    reverse_array(index + 1, element)

element = input().split()


reverse_array(0, element)

print(' '.join(element))