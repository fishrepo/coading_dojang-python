# x, y = map(int, input().split())
# matrix = []
# for i in range(x):
#     matrix.append(list(input()))

x, y = 3, 3
matrix = [['.', '*', '*'], ['*', '.', '.'], ['.', '*', '.']]


print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '*':
            print(matrix[i][j], end='')
            continue

        if matrix[i][j] == '.':

            count = 0

            star = [[''] if i-1 < 0 else matrix[i-1][0 if j-1 < 0 else j-1:j+2],
                    matrix[i][0 if j-1 < 0 else j-1:j+2],
                    [''] if i+1 >= len(matrix) else matrix[i+1][0 if j-1 < 0 else j-1:j+2]]

            for z in star:
                count += z.count('*')

            print(count, end='')

    print()
