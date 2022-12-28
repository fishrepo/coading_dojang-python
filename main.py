
def is_multiple(func):
    def wrapper(a, b):
        r = func(a, b)
        x = 3
        if r % x == 0:
            print('{0}의 반환값은 {1}의 배수 입니다.'.format(func.__name__, x))
        else:
            print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
        return r
    return wrapper


@is_multiple
def add(a, b):
    return a+b


print(add(10, 20))
print(add(2, 5))
