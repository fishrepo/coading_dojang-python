files = input().split()

x = map(lambda x: '{0:03d}.{1}'.format(
    int(x.split('.')[0]), x.split('.')[1]), files)
x = list(x)
# list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]),x.split('.')[1]) ,files))
print(x)
