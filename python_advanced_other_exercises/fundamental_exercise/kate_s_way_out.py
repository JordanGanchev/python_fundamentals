import sys
from io import StringIO

test_input1 = '''4
######
##  k#
## ###
## ###
'''
test_input2 = '''5
######
##  k#
## ###
######
## ###
'''
sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)


def progress_check(line, row, col):
    move = [
        [row, col + 1],
        [row + 1, col],
        [row, col - 1],
        [row - 1, col]
    ]

    for r, c in move:
        if 0 <= r < len(line) and 0 <= c < len(line) and line[r][c] == ' ':
            line[r][c] = 'k'


n = int(input())
line = []
for i in range(n):
    line.append(list(input()))
count = 0
while True:
    for row in range(n):
        for col in range(len(line[0])):
            if line[row][col] == 'k':
                progress = progress_check(line, row, col)
                # if 0 <= row < len(line) and 0 <= col < len(line) and line[row][col]:
                #     print(f'Kate got out in {count} moves')
                #
                # else:
                #     print('Kate cannot get out')

                count += 1


