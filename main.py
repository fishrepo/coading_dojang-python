def countdown(n):
    stack = n+1

    def count():
        nonlocal stack
        stack -= 1
        return stack
    return count


n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')
