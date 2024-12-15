def find_longest_increasing_subsequence(goals):
    goals = list(map(int, goals.split(", ")))

    best_sequence = []
    current_sequence = [goals[0]]

    for i in range(1, len(goals)):
        if goals[i] >= goals[i - 1]:
            current_sequence.append(goals[i])
        else:
            if len(current_sequence) > len(best_sequence):
                best_sequence = current_sequence
            current_sequence = [goals[i]]

    if len(current_sequence) > len(best_sequence):
        best_sequence = current_sequence
    print(" ".join(map(str, best_sequence)))

input_goals = input()
find_longest_increasing_subsequence(input_goals)
