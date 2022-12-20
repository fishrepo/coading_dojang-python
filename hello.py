# x, y = map(int, input().split())
# matrix = []
# for i in range(x):
#     matrix.append(list(input()))

x, y = 3, 3
matrix = [['.', '*', '*'], ['*', '.', '.'], ['.', '*', '.']]


print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '.':
            count = 0

            if i-1 >= 0 and matrix[i-1][j-1] == '*':
                count += 1

            if i-1 >= 0 and matrix[i-1][j] == '*':
                count += 1

            if i-1 >= 0 and j+1 < len(matrix[i]) and matrix[i-1][j+1] == '*':
                count += 1

            if j-1 >= 0 and matrix[i][j-1] == '*':
                count += 1

            if j+1 < len(matrix[i]) and matrix[i][j+1] == '*':
                count += 1

            if i+1 < len(matrix) and j-1 >= 0 and matrix[i+1][j-1] == '*':
                count += 1

            if i+1 < len(matrix) and matrix[i+1][j] == '*':
                count += 1

            if i+1 < len(matrix) and j+1 < len(matrix[i]) and matrix[i+1][j+1] == '*':
                count += 1
            print(count, end='')
        else:
            print(matrix[i][j], end='')
    print()
