def prime_number_generator(start, stop):
    for n in range(start, stop):
        # 소수여부 확인용 변수 생성
        is_prime = True
        # start 부터 stop의 모든 수에 대해 소수여부 확인
        for i in range(2, n):
            # 만약 소수가 아니면 소수여부 False 처리
            if n % i == 0:
                is_prime = False
        # 소수여부 확인된 값만 전달
        if is_prime:
            yield n


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
