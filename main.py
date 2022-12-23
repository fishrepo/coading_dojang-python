korean, english, mathematics, science = map(int, input().split())


def get_min_max_score(*args):
    return min(args), max(args)


# 딕셔너리를 언패킹 하여 인수로 가져오면 키:값 형태이므로 for 문을 사용하여 합을 구했다.
def get_average(**kwargs):

    x = 0  # 초기화 안하면 오류생김
    for kw, arg in kwargs.items():
        x += arg

    return x/len(kwargs)


min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(
    korean=korean, english=english, mathematics=mathematics, science=science)

print('낮은점수:{0: .2f}, 높은 점수 :{1: .2f}, 평균점수 : {2:.2f}'.format(
    min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은점수:{0: .2f}, 높은 점수 :{1: .2f}, 평균점수 : {2:.2f}'.format(
    min_score, max_score, average_score))
