from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_value = bisect_right(a, right_value)
    left_value = bisect_left(a, left_value)

    return right_value - left_value


def solution(words, queries):
    answer = []

    # 1. 각각의 리스트를 길이에 따라 나눈다.
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    # 2. 리스트를 정렬한다.

    for i in range(10001):
        array[i].sort()
        reversed_array.sort()

    # 3. 이진탐색으로 시작되는 단어부터 마지막 단어의 위치를 찾고 위치의 차이를 계산

    for query in queries:
        if query[0] != '?':
            res = count_by_range(array[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))

        answer.append(res)

        return answer