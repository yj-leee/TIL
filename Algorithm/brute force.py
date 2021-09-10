## brute force 알고리즘
"""

카드 두 뭉치가 있습니다.

왼쪽 뭉치에서 카드를 하나 뽑고 오른쪽 뭉치에서 카드를 하나 뽑아서, 두 수의 곱이 가장 크게 만들고 싶은데요. 어떻게 하면 가장 큰 곱을 구할 수 있을까요?

함수 max_product는 리스트 left_cards와 리스트 right_cards를 파라미터로 받습니다.

left_cards는 왼쪽 카드 뭉치의 숫자들, right_cards는 오른쪽 카드 뭉치 숫자들이 담겨 있고, max_product는 left_cards에서 카드 하나와 right_cards에서 카드 하나를 뽑아서 곱했을 때 그 값이 최대가 되는 값을 리턴합니다.
"""


def max_product(left_cards, right_cards):
    max = 0
    for left_card in left_cards:
        for right_card in right_cards:
            temp = left_card * right_card
            if max < temp:
                max = temp
            else:
                max = max
    return max


print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
