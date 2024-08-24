def find_all_paths(row, col, lab, direction, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return

    if lab[row][col] == '*':
        return
    if lab[row][col] == 'v':
        return

    path.append(direction)

    if lab[row][col] == 'e':
        print(''.join(path))
    else:
        lab[row][col] = 'v'

        find_all_paths(row - 1, col, lab, 'U', path)
        find_all_paths(row + 1, col, lab, 'D', path)
        find_all_paths(row, col - 1, lab, 'L', path)
        find_all_paths(row, col + 1, lab, 'R', path)
        lab[row][col] = '-'

    path.pop()



rows = int(input())
cols = int(input())

lab = []

for _ in range(rows):
    lab.append(list(input()))


find_all_paths(0, 0, lab, '', [])



# def find_count(board, row, col):
#     moves = [
#         [row - 2, col - 1],
#         [row - 2, col + 1],
#         [row - 1, col - 2],
#         [row - 1, col + 2],
#         [row + 1, col - 2],
#         [row + 1, col + 2],
#         [row + 2, col - 1],
#         [row + 2, col + 1]
#     ]
#     result = 0
#     for r, c in moves:
#         if 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == 'K':
#             result += 1
#
#     return result
#
#
# size = int(input())
#
# board = []
#
# for _ in range(size):
#     board.append(list(input()))
#
# remove_knight_counter = 0
# while True:
#     best_count = 0
#     knight_row = 0
#     knight_col = 0
#     for row in range(size):
#         for col in range(size):
#             if board[row][col] == '0':
#                 continue
#             count = find_count(board, row, col)
#             if count > best_count:
#                 best_count = count
#                 knight_row = row
#                 knight_col = col
#     if best_count == 0:
#         break
#     board[knight_row][knight_col] = '0'
#     remove_knight_counter += 1
#
# print(remove_knight_counter)
