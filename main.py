keys = input('keys :').split(' ')
values = map(int, input('values :').split(' '))
values = list(values)

y = dict()
y.update(zip(keys, values))

y = {key: value for key, value in y.items() if value != 30 and key != 'delta'}
print(y)
