path = map(int, input(':').split(';'))

path = list(path)

print(path)

path.sort(reverse=True)

print(path)

index = 0

for i in path:
    path[index] = '{0: >9,}'.format(i)
    index += 1

for i in path:
    print(i)
