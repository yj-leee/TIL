# n, target = map(int, input().split())
# array = list(map(int, input().split()))
n = 7
target = 2
array = [1, 1, 2, 2, 2, 2, 3]


def first_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (array[mid] == target) and (mid == 0 or target > array[mid - 1]):
        return mid
    elif array[mid] >= target:
        return first_search(array, target, start, mid - 1)
    else:
        return first_search(array, target, mid + 1, end)


def last_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (array[mid] == target) and (
        (mid == len(array) - 1) or (target < array[mid + 1])
    ):
        return mid
    elif array[mid] > target:
        return first_search(array, target, start, mid - 1)
    else:
        return first_search(array, target, mid + 1, end)


def count_by_value(array, x):
    n = len(array) - 1

    first_index = first_search(array, x, 0, n)

    if first_index == None:
        return 0

    last_index = last_search(array, x, 0, n)

    return last_index - first_index + 1


count = count_by_value(array, target)

if count == 0:
    print(-1)
else:
    print(count)
